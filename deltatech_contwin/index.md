# ContWin Interface

- **Nume Tehnic:** `deltatech_contwin`
- **Versiune:** `20.0.1.0.17`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_contwin
- **Cale Locală:** `odoo-addons/bitshop/deltatech_contwin`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite ținerea contabilității în ContWin, programul românesc de contabilitate, în timp ce facturarea, achizițiile și stocurile rulează în Odoo. Pentru o perioadă aleasă, exportă documentele postate ale unei companii în formatul text pe care îl importă ContWin și, la nevoie, ca tabele pregătite pentru SAF-T, toate împachetate într-un singur fișier ZIP.

#### 2. Funcționalități Cheie

- **Achiziții și vânzări:** facturi de furnizor și client, note de credit și recepții, cu conturi, sume în RON și în valută, curs, scadență, tip și cotă de TVA.
- **Plăți și încasări:** înregistrările de bancă și casă din perioadă, câte un fișier pe jurnal, cu contul jurnalului sau al plății.
- **Transferuri între depozite:** pentru un depozit ales, intrările și ieșirile de stoc către alte locații.
- **Tabele SAF-T:** unități de măsură, produse, linii de facturi de intrare și de ieșire cu tipul și codul de taxă SAF-T și numerele de înregistrare ale partenerilor, pentru fișierul D406.
- **Detalii TVA România:** TVA la încasare recunoscut din poziția fiscală a facturii; CNP-ul persoanelor fizice este validat înainte de export.
- **Filtre și o singură companie:** jurnale, unitate operațională (jurnalele unei sucursale) și depozit; sunt incluse doar documentele companiei alese, iar jurnalele altei companii sunt refuzate.
- **Cale de meniu și moduri:** *Contabilitate > Contabilitate > ContWin > Export ContWin* (manageri de contabilitate); modul *Contwin*, *SAFT* sau *All* produce fișiere precum `IN_…`/`IE_…` (facturi), `INT_…`/`IET_…` (transferuri), `TOT_…` și câte un fișier pe jurnal de bancă/casă, respectiv `UM_SAFT_…`, `PRODUCTS_SAFT_…`, `IN_SAFT_…`, `IE_SAFT_…`, `TOT_SAFT_…`.
- **De știut:** `IN_…` conține doar facturile de furnizor cu cont din clasa 3; în fișierele de bancă orice alt cont decât banca și partenerul se exportă ca `5125` (inclusiv comisionul), iar în cele de casă ca cont de casă, deci diferențele se corectează manual în ContWin; codul de TVA este A (cota standard), B (redusă) sau C (restul).
- **Configurare:** planul de conturi `l10n_ro` instalat, parteneri cu CUI sau CNP, unitate operațională pe jurnalele sucursalelor, poziția fiscală pentru TVA la încasare (găsită după numele „incasare") și, pentru SAF-T, localizarea SAF-T românească pentru tipurile și codurile de taxe.

#### 3. Dependențe

- `base`
- `account`
- `stock`
- `stock_account`
- [deltatech_contact](../deltatech_contact/index.md)
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `export.contwin` (wizard, `wizard/export_contwin.py`): colectează perioada, compania, modul și filtrele, procesează documentele și generează ZIP-ul cu fișierele ContWin și SAF-T.
- `account.journal` (extins): câmpuri suplimentare ale jurnalului folosite la filtrarea exportului (ex. unitate operațională).

**Vizualizări**

- `view_export_contwin_form`: formularul wizardului de export.
- `contwin_menu.xml`: meniul *Export ContWin*, cu acțiunea `action_export_contwin`.

**Acțiuni Automate / Acțiuni Server**

Nu definește `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_saga](../deltatech_saga/index.md): modul înrudit de export contabil către SAGA, din aceeași familie de interfețe de export Terrabit.
