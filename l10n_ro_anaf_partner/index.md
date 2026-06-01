# Romania - Monitorizare Modificări Date ANAF Parteneri (FR-23) (localizat la `l10n_ro_anaf_partner/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_partner`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_partner
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_partner`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Acest modul extinde `l10n_ro_fiscal_validation` (OCA) cu monitorizarea modificărilor datelor ANAF ale partenerilor. La fiecare actualizare ANAF, modulul înregistrează automat orice schimbare detectată (denumire, adresă, CAEN, TVA, statut plătitor TVA), marchează partenerii inactivi fiscal și emite alerte (activități și note în chatter) atunci când un partener devine inactiv sau își schimbă regimul de TVA, prevenind astfel facturarea către parteneri radiați.

#### 2. Funcționalități Cheie

- **Change log:** înregistrarea automată a oricărei modificări detectate la actualizarea ANAF (denumire, adresă, CAEN, TVA, scpTVA).
- **Marcare inactiv ANAF:** câmpul `l10n_ro_is_inactive_anaf` calculat din istoricul `statusInactivi` OCA, cu badge pe fișa partenerului.
- **Alertă inactivare:** activitate Odoo plus notă în chatter la prima detectare a statusului inactiv.
- **Alertă schimbare regim TVA:** notă automată în chatter când `scpTVA` se modifică.
- **Avertizare factură:** notă în chatter la postarea unei facturi pe un partener inactiv ANAF.
- **Ultima verificare ANAF:** câmpul `l10n_ro_anaf_last_check` actualizat la fiecare rulare cron.
- **Meniu Log Modificări:** vizualizare globală a tuturor modificărilor ANAF, filtrabilă pe tip/partener/dată.

#### 3. Dependențe

- `l10n_ro_fiscal_validation`
- `account`

Dependență externă Python: `requests`.

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.change.log`: jurnalul de modificări ale datelor ANAF per partener.
- `res.partner` (extins): câmpurile `l10n_ro_is_inactive_anaf`, `l10n_ro_anaf_last_check` și logica de alertare.

**Vizualizări / Securitate**

- `views/l10n_ro_anaf_change_log_views.xml`: lista și formularul jurnalului de modificări, plus meniul Log Modificări.
- `views/res_partner_views.xml`: badge-ul de inactiv ANAF și informațiile pe fișa partenerului.
- `security/ir.model.access.csv`: drepturile de acces.

**Acțiuni Automate / Acțiuni Server**

- Verificarea ANAF rulează în cadrul cron-ului de actualizare moștenit din `l10n_ro_fiscal_validation`; la fiecare rulare se actualizează `l10n_ro_anaf_last_check` și se generează intrările în change log și alertele aferente.

#### 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_anaf_d394]]`
