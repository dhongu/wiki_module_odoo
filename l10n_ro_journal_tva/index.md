# Jurnale TVA Vânzări/Cumpărări (localizat la `l10n_ro_journal_tva/index.md`)

- **Nume Tehnic:** `l10n_ro_journal_tva`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_journal_tva
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_journal_tva`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Modulul generează Jurnalul de TVA Vânzări și Jurnalul de TVA Cumpărări conform OMFP 1802/2014. Pornind de la facturile postate (inclusiv stornouri), construiește jurnale lunare cu detaliere pe cote și categorii de TVA, totaluri pe header și posibilitate de confirmare și arhivare, plus export XLSX într-un format tabelar complet.

#### 2. Funcționalități Cheie

- Selecție tip jurnal (Vânzări / Cumpărări) și perioadă.
- Populare automată din facturile postate, inclusiv stornouri.
- Detaliu pe cote și categorii TVA: 21%, 11%, taxare inversă, intracomunitare, scutit, neimpozabil.
- Totaluri sumarizate la nivel de header.
- Confirmare și arhivare lunară a jurnalului.
- Export XLSX cu format tabelar complet (xlsxwriter).

#### 3. Dependențe

- `account`
- `mail`

#### 4. Componente Cheie

**Modele**

- Model dedicat de jurnal TVA care stochează antetul (tip, perioadă, totaluri) și liniile detaliate pe cote și categorii.

**Vizualizări / Date**

- `views/l10n_ro_journal_tva_views.xml`: Interfața de creare, populare și confirmare a jurnalelor de TVA.
- `security/ir.model.access.csv`: Drepturile de acces pentru modelele de jurnal TVA.

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate; popularea se declanșează la cerere.*

#### 5. Conexiuni

- `[[l10n_ro_journal_reports]]`
