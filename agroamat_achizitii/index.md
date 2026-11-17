# Agroamat: achiziții

- **Nume Tehnic:** `agroamat_achizitii`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-ro/agroamat/tree/19.0/agroamat_achizitii
- **Cale Locală:** `proiecte/agroamat/agroamat_achizitii`
- **Ultima Ingestie:** `2026-11-17`

#### 1. Sumar

Modulul completează comenzile de achiziție ale clientului Agroamat cu informațiile de care are nevoie echipa la recepția mărfii și la facturare: data și scadența facturii furnizorului, codurile de furnizor ale produselor și o semnalare a produselor care sunt deja cerute de clienți pe oferte validate, pentru a fi aduse cu prioritate.

#### 2. Funcționalități Cheie

- Pe comanda de achiziție se completează „Data facturii” și „Data scadenței facturii”; la crearea facturii din comandă (butonul „Creare factură”) acestea se preiau ca dată a facturii, dată contabilă și scadență.
- Butonul „Produse” din comandă deschide lista șabloanelor de produs comandate.
- Completarea codurilor de furnizor din comandă: codul alternativ al produsului este trecut în informațiile de furnizor (`product.supplierinfo`) și înlocuiește codul din descrierea liniei; dacă produsul nu are coduri alternative, se afișează o eroare.
- Semnalarea liniilor cu produse cerute pe oferte validate (comenzi de vânzare în starea „trimisă”): pe fiecare linie se calculează dacă produsul e cerut, cantitatea totală cerută și numerele ofertelor; există și metode care returnează produsele aflate pe oferte validate, pentru colorarea opțiunilor din lista de produse.
- Pe lista comenzilor, comenzile în starea „ciornă” sunt evidențiate; în formular, tipul de operațiune (recepție) poate fi ales doar dintre cele de tip intrare, când sunt active locațiile multiple.
- Corecție recentă (19.0.1.0.1, 13.11.2026): „Creare factură” transmite mai departe argumentele (`attachment_ids`), astfel că nu mai apare `TypeError` când `l10n_ro_message_spv_purchase` trimite atașamente.

#### 3. Dependențe

- `migration`
- `purchase_stock`
- `sale`
- [deltatech_purchase_create_bill_button](../deltatech_purchase_create_bill_button/index.md)

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): câmpurile `invoice_date`, `invoice_due_date`; metodele `action_view_products`, `get_supplier_codes`, `action_create_invoice` (transmite datele către factură prin context).
- `purchase.order.line` (extins): câmpurile calculate `x_in_oferta_validata`, `x_cant_oferta_validata`, `x_oferte_validate`; metodele `produse_pe_oferte_validate` și `sunt_pe_oferte_validate`.

**Vizualizări**

- `purchase_order_tree_agroamat`: evidențiază comenzile în ciornă în listă.
- `purchase_order_form_agroamat`: buton „Produse”, câmpurile cu datele facturii și tipul de operațiune de recepție.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_purchase_create_bill_button](../deltatech_purchase_create_bill_button/index.md): butonul „Creare factură” din comanda de achiziție, a cărui acțiune este extinsă aici.
- `l10n_ro_message_spv_purchase`: trimite `attachment_ids` către `action_create_invoice` (compatibilitate asigurată în 19.0.1.0.1).
- `terrabit_agroamat`: modulul din care a fost extras acesta (19.0.1.0.0).
