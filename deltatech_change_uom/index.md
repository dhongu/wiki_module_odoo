# Schimbare unitate de măsură (Change Unit of measure)

- **Nume Tehnic:** `deltatech_change_uom`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_change_uom
- **Cale Locală:** `odoo-addons/deltatech/deltatech_change_uom`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite corectarea unității de măsură a unui produs care a fost creat greșit și este deja folosit în documente, caz în care Odoo standard refuză schimbarea (facturi postate sau comenzi într-o altă unitate). Printr-o acțiune dedicată pe fișa produsului, unitatea veche este înlocuită cu cea nouă pe produs și pe toate documentele lui, fără a crea un produs nou și fără a rupe istoricul în două. Modulul corectează eticheta unității, nu convertește cantitățile.

#### 2. Funcționalități Cheie

- Acțiunea **Schimbă UM** în meniul **Acțiune** al formularului de produs (doar pe fișa produsului, nu pe variante), vizibilă membrilor grupului **Permite schimbarea unității de măsură**; administratorii de sistem primesc grupul automat.
- Asistent cu două câmpuri: **Unitate de măsură** (noua unitate a produsului, din orice arbore de unități) și **Unitate implicită de achiziție** (limitată la unitățile convertibile la unitatea nouă; se golește automat dacă devine incompatibilă).
- Înlocuirea unității pe produs și variantele lui, pe liniile comenzilor de vânzare și de achiziție, pe liniile facturilor (inclusiv cele postate), pe mișcările de stoc și liniile lor detaliate și pe liniile de furnizor.
- Documentele din vechea unitate implicită de achiziție trec în noua unitate de achiziție, astfel încât comanda, recepția și factura de furnizor rămân în aceeași unitate.
- Cantitățile, prețurile și valorile rămân neschimbate (fără conversie); nu se generează note contabile.
- Limitări: liniile într-o a treia unitate, listele de materiale și regulile din listele de prețuri nu sunt atinse; documentele deja transmise (e-Factura, SAF-T) rămân la unitatea de la momentul transmiterii.
- Pașii detaliați, verificările și erorile frecvente sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `product`
- `account`
- `stock`
- `sale`
- `purchase`
- [deltatech_uom_domain](../deltatech_uom_domain/index.md)

#### 4. Componente Cheie

**Modele**

- `product.change.uom`: asistent (model tranzitoriu) care primește unitatea nouă și unitatea implicită de achiziție și aplică înlocuirea prin `do_change` (UPDATE direct SQL, cu verificarea grupului și a convertibilității unității de achiziție). Moștenește `deltatech.uom.domain.mixin`.

**Vizualizări**

- `view_product_change_uom_form`: formularul asistentului, cu butoanele Aplică / Anulează.
- `action_product_change_uom`: acțiune legată de `product.template` (formular), restricționată la grupul `group_change_uom`.

**Acțiuni Automate / Acțiuni Server**

- Niciuna. Grupul `group_change_uom` este implicat de `base.group_system`.

#### 5. Conexiuni

- [deltatech_uom_domain](../deltatech_uom_domain/index.md): aduce pe produs câmpul **Unitate implicită de achiziție** și listele de unități compatibile, folosite de asistent.
