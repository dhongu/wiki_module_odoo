# Romania - Taxa verde în e-Factura

- **Nume Tehnic:** `l10n_ro_green_tax_analytic_edi`
- **Versiune:** `20.0.0.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_green_tax_analytic_edi
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_green_tax_analytic_edi`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul-punte care duce nota de taxă verde din `l10n_ro_green_tax_analytic` în XML-ul UBL trimis în e-Factura (SPV / ANAF). Fără el, exportul UBL standard omite nota, iar XML-ul ajunge în SPV fără nicio mențiune despre taxa verde.

#### 2. Funcționalități Cheie

- Textul notei devine **notă pe linie (BT-127, `cbc:Note`)** a liniei de produs corespunzătoare; apare în factura tipărită din SPV, sub tabelul liniilor, ca „Nota liniei facturii nr. N”.
- Liniile fără taxă verde nu au notă.
- Totalurile, TVA-ul și numerele liniilor rămân neschimbate: nu se adaugă nicio linie, taxă sau sumă.
- Se instalează singur când sunt instalate `l10n_ro_green_tax_analytic` și `account_edi_ubl_cii`; nu cere configurare, textul fiind cel setat pe companie.

#### 3. Dependențe

- [l10n_ro_green_tax_analytic](../l10n_ro_green_tax_analytic/index.md)
- `account_edi_ubl_cii`

#### 4. Componente Cheie

**Modele**

- `account.edi.xml.ubl_20`: extins pentru a adăuga nota liniei (BT-127) în XML.

**Vizualizări**

- Nu are.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_green_tax_analytic](../l10n_ro_green_tax_analytic/index.md): sursa notei de taxă verde.
