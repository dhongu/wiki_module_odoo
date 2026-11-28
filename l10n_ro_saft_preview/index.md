# Romania - Previzualizare SAF-T D406 (localizat la `l10n_ro_saft_preview/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_preview`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_saft_preview
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_preview`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul afișează declarația SAF-T D406 într-un ecran cu tab-uri înainte de depunere, ca să poți verifica conținutul, nu doar structura pe care o validează DUKIntegrator. Ecranul se construiește din XML-ul generat de export, deci ce vezi este exact ce depui, iar codurile de taxă greșite se corectează direct pe linia contabilă.

#### 2. Funcționalități Cheie

- **Previzualizarea este chiar fișierul:** se construiește din XML-ul exportului D406.
- **Tab-uri pe secțiunile declarației:** Informații generale, Avertismente, Plan de conturi, Clienți, Furnizori, Registru jurnal, Documente, TaxTable, Produse, Stocuri și Active.
- **Filtre și export Excel:** fiecare secțiune se deschide ca listă, cu căutare, grupare, totaluri și exportul standard Odoo în Excel.
- **Corecția codurilor din ecran:** pe registrul jurnal alegi tipul și codul de taxă SAF-T al unei linii fără taxe; corecția se salvează pe linia contabilă și rămâne la regenerare.
- **Toate tipurile D406:** lunar/trimestrial, active (anual) și stocuri (la cerere, cu modulul de stocuri SAF-T instalat).
- **Fără dublarea datelor:** o singură previzualizare pe companie, tip și perioadă; după 30 de zile rândurile se golesc automat, iar antetul și fișierul XML rămân.
- Fluxul de lucru este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_saft_export_fix](../l10n_ro_saft_export_fix/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro.saft.preview`: previzualizarea unei declarații, pe companie, tip și perioadă.
- `l10n_ro.saft.preview.line.mixin`: baza comună a liniilor de previzualizare.
- `l10n_ro.saft.preview.message`, `.account`, `.partner`, `.tax`, `.journal.line`, `.document`, `.product`, `.stock`, `.asset`: liniile fiecărei secțiuni (avertismente, plan de conturi, parteneri, taxe, registru jurnal, documente, produse, stocuri, active).

**Vizualizări**

- `l10n_ro_saft_preview_view_form` / `_view_list` / `_view_search`: formularul cu tab-uri, lista și căutarea previzualizărilor.
- `l10n_ro_saft_preview_<secțiune>_view_list` / `_view_search`: listele și căutările pentru fiecare secțiune.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_l10n_ro_saft_preview_purge`: zilnic, golește rândurile previzualizărilor mai vechi de 30 de zile.

#### 5. Conexiuni

- [l10n_ro_saft_validator](../l10n_ro_saft_validator/index.md): validarea D406, complementară previzualizării.
