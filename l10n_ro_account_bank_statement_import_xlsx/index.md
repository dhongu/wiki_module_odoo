# Import Extrase Bancare în Format xlsx (localizat la `l10n_ro_account_bank_statement_import_xlsx/index.md`)

- **Nume Tehnic:** `l10n_ro_account_bank_statement_import_xlsx`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-ro/bitshop_ent/tree/19.0/l10n_ro_account_bank_statement_import_xlsx
- **Cale Locală:** `odoo-addons/bitshop_ent/l10n_ro_account_bank_statement_import_xlsx`
- **Ultima Ingestie:** `2026-06-09`

#### 1. Sumar

Acest modul extinde funcționalitatea de import al extraselor bancare pentru a accepta fișiere XLSX. Se bazează pe mecanismul standard de import din Odoo, permițând utilizatorilor să mapeze coloanele dintr-un fișier Excel pe câmpurile liniilor de extras bancar. Astfel, contabilii pot prelua direct extrasele primite de la bancă în format Excel, fără conversii manuale, simplificând reconcilierea operațiunilor bancare.

#### 2. Funcționalități Cheie

- **Suport XLSX**: Adaugă formatul XLSX în lista formatelor de import disponibile pentru jurnalele bancare.
- **Mapare flexibilă**: Folosește asistentul de import din Odoo, permițând utilizatorilor să gestioneze diverse structuri de fișiere.
- **Îmbunătățiri moștenite**: Beneficiază de detectarea automată a partenerului (după nume sau după referința comenzii de vânzare) atunci când este folosit împreună cu modulul `deltatech_account_bank_statement_import`.

#### 3. Dependențe

- `account_bank_statement_import`
- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)

#### 4. Componente Cheie

Documentația este derivată din `readme/DESCRIPTION.md`, care descrie funcționalitatea la nivel de utilizator. Aceasta nu solicită o analiză detaliată a componentelor tehnice, deci secțiunea nu a fost populată prin analiza codului.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): furnizează detectarea automată a partenerului (după nume sau referința comenzii de vânzare), de care beneficiază importul XLSX.
