# Romania - Potrivire articol la import e-Factura

- **Nume Tehnic:** `l10n_ro_efactura_product_match`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_efactura_product_match
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_product_match`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

La importul facturilor de cumpărare din SPV, Odoo standard nu caută codul propriu de articol (BT-156, `BuyersItemIdentification`) dacă furnizorul trimite și codul lui; linia rămâne fără articol, fără nicio eroare. Modulul adaugă această căutare și leagă corect liniile de nomenclatorul de articole.

#### 2. Funcționalități Cheie

- O treaptă nouă în planul de căutare a articolului, cu prioritatea 16: după codul intern (`default_code`) și înaintea denumirii. Ordinea: cod furnizor (`supplierinfo`), cod de bare (BT-157), cod intern, codul propriu din BT-156, denumire, predicție din facturi anterioare.
- Rulează doar dacă treptele anterioare au eșuat și BT-156 diferă de codul deja căutat; comportamentul existent rămâne neschimbat.
- Fără meniuri, câmpuri sau setări: acționează la fiecare import. Pentru potrivire, completați Referința internă pe articole și, pentru furnizorii care nu retrimit codul, codul furnizorului în fila Achiziții.
- Facturile importate înainte de instalare nu se corectează retroactiv; o linie fără articol nu blochează validarea.
- Verificarea pas-cu-pas este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `product.product` (extins): treapta de căutare după codul propriu din factura electronică.

**Vizualizări**

- Nu are.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `account_edi_ubl_cii`: logica standard de import UBL, extinsă cu noua treaptă de căutare.
