# Purchase UBL Import (localizat la `deltatech_purchase_ubl/index.md`)

- **Nume Tehnic:** `deltatech_purchase_ubl`
- **Versiune:** `20.0.1.5.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_purchase_ubl
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_ubl`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul importă facturi de la furnizori în format UBL XML și le folosește pentru a actualiza fluxurile de achiziție din Odoo. Pe baza fișierului XML, identifică furnizorul și comanda de achiziție, potrivește produsele, actualizează prețurile furnizorului, poate valida recepția și poate crea factura de la furnizor. Reduce munca manuală și erorile la prelucrarea documentelor electronice de achiziție.

#### 2. Funcționalități Cheie

- **Rezolvare automată a furnizorului și a comenzii**: wizardul păstrează comanda selectată și poate identifica furnizorul și comanda din XML (`OrderReference`, CUI-ul furnizorului, numele).
- **Potrivire automată a produselor**: după cod de bare (GS1/EAN), cod de furnizor, referință internă sau nume exact.
- **Integrare cu comanda**: liniile existente se actualizează (cantitate, preț, discount), iar liniile cu produse care nu sunt încă pe comandă se adaugă; wizardul avertizează înainte de import când comanda are deja linii. Fără comandă, se pot actualiza totuși prețurile furnizorului.
- **Prețuri și discounturi**: prețurile se scriu în `product.supplierinfo`; discounturile de linie din `AllowanceCharge` (`ChargeIndicator=false`) devin discount procentual.
- **Verificarea totalului**: compară totalul comenzii cu cel din XML (`PayableAmount` / `TaxInclusiveAmount`, cu rezervă pe valoarea fără taxe) și avertizează la diferențe.
- **Stoc și contabilitate**: opțional validează recepția asociată și creează factura de la furnizor din comandă.
- **Produse lipsă**: opțiune de creare automată din datele UBL; apelanții automați pot trimite `purchase_ubl_no_new_products` în context ca liniile nepotrivite să rămână nepotrivite.
- **Previzualizare cu potrivire pe culori**: câte un rând per linie de factură (verde = cod furnizor sau cod de bare, galben = doar nume, roșu = fără potrivire); orice rând poate fi realocat altui produs înainte de confirmare.
- **Rulări automate vizibile**: un import fără interfață cu total diferit sau linii nepotrivite lasă un jurnal colorat și programează o activitate „SPV import needs review” pe comandă, atribuită cumpărătorului.
- Suportă namespace-urile UBL Invoice standard și codurile uzuale de unități de măsură (C62, KGM, LTR etc.). Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `purchase_stock`
- [deltatech_account_ubl_import](../deltatech_account_ubl_import/index.md)

#### 4. Componente Cheie

**Modele**

- `purchase.ubl.import.wizard`: wizardul de import UBL, cu parsarea XML și detecția formatului.
- `purchase.ubl.import.wizard.line`: rândurile de previzualizare cu produsul potrivit.
- `purchase.invoice.import.mixin`: logica comună de potrivire produse, prețuri, recepție și facturare, reutilizabilă de alte importuri de facturi.
- `purchase.order`: extins pentru butonul de import și atașamentele XML.

**Vizualizări**

- `view_purchase_ubl_import_wizard`: formularul wizardului, cu previzualizare.
- `purchase_order_form_view_inherit_ubl_button`: butonul de import pe comanda de achiziție.

**Acțiuni Automate / Acțiuni Server**

- `action_purchase_ubl_import_wizard`: acțiunea de deschidere a wizardului.

#### 5. Conexiuni

- [deltatech_purchase_ubl_ai](../deltatech_purchase_ubl_ai/index.md): variantă de import a facturilor de achiziție cu AI, înrudită funcțional.
- `account`: factura de la furnizor creată opțional din comandă.
