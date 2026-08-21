# Import Extrase Bancare în Format xlsx (localizat la `l10n_ro_account_bank_statement_import_xlsx/index.md`)

- **Nume Tehnic:** `l10n_ro_account_bank_statement_import_xlsx`
- **Versiune:** `19.0.2.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_bank_statement_import_xlsx
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_bank_statement_import_xlsx`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul extinde funcționalitatea de import al extraselor bancare pentru a accepta fișiere XLSX. Se bazează pe mecanismul standard de import din Odoo, permițând utilizatorilor să mapeze coloanele dintr-un fișier Excel pe câmpurile liniilor de extras bancar. Astfel, contabilii pot prelua direct extrasele primite de la bancă în format Excel, fără conversii manuale, simplificând reconcilierea operațiunilor bancare.

#### 2. Funcționalități Cheie

- **Suport XLSX**: Adaugă formatul XLSX în lista formatelor de import disponibile pentru jurnalele bancare.
- **Mapare flexibilă**: Folosește asistentul de import din Odoo, permițând utilizatorilor să gestioneze diverse structuri de fișiere.
- **Potrivire parteneri specifică României**: Identifică automat partenerul după nume sau după referința comenzii de vânzare regăsită în coloana de referință a plății.

#### 3. Dependențe

- `l10n_ro`
- `account_bank_statement_import_csv`

#### 4. Componente Cheie

**Modele**

- `base_import.import` (extindere, TransientModel): la `_parse_import_data`, îmbogățește datele importate din fișierul XLSX — completează coloana `partner_id/.id` căutând partenerul după nume (`partner_name`, potrivire `=ilike`) sau, dacă lipsește, după referința comenzii de vânzare regăsită în `payment_ref` (căutare exactă în `sale.order`, cu preluarea partenerului comercial de facturare).
- `account.journal` (extindere): adaugă `XLSX` în lista formatelor de import disponibile (`_get_bank_statements_available_import_formats`) și suprascrie `_import_bank_statement` pentru a gestiona fișierele XLSX — validează că nu se amestecă XLSX cu alte formate și că se selectează un singur fișier XLSX odată. Dacă un parser dedicat (ex. borderou GLS, detaliere Euplatesc) recunoaște fișierul, deleagă la fluxul standard de import; altfel, deschide asistentul de mapare (`base_import.import`) prin acțiunea client `import_bank_stmt`.

**Vizualizări**

Modulul nu adaugă vizualizări proprii; se bazează pe asistentul standard de import (`base_import.import`) din Odoo.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

Nu au fost identificate module conexe (dincolo de dependențe) cu pagină wiki proprie.
