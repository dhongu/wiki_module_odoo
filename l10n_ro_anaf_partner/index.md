# Romania - Monitorizare Modificări Date ANAF Parteneri (FR-23) (localizat la `l10n_ro_anaf_partner/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_partner`
- **Versiune:** `19.0.2.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_partner
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_partner`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul monitorizează modificările datelor ANAF ale partenerilor, cu **client de sincronizare propriu** (fără dependențe de module OCA de fiscalitate). Interoghează direct serviciul sincron ANAF de verificare TVA, actualizează denumirea, adresa, codul CAEN, statutul de plătitor TVA și starea de înregistrare a fiecărui partener companie din România, înregistrează automat orice modificare detectată într-un jurnal (change log) și emite alerte (activități și note în chatter) atunci când un partener devine inactiv fiscal, este radiat/dizolvat sau își schimbă regimul de TVA — prevenind astfel emiterea de facturi către parteneri cu probleme fiscale.

#### 2. Funcționalități Cheie

- **Sincronizare ANAF proprie:** client direct pentru serviciul sincron de verificare TVA (loturi de max. 100 CUI-uri, o cerere pe secundă), fără dependențe OCA.
- **Change log:** înregistrarea automată a oricărei modificări detectate la actualizarea ANAF (denumire, adresă, CAEN, TVA, scpTVA, stare de înregistrare).
- **Marcare inactiv ANAF:** câmpul `l10n_ro_is_inactive_anaf` calculat din `statusInactivi`, cu badge/alertă vizibilă pe fișa partenerului.
- **Detectare radiere/dizolvare:** câmpul `l10n_ro_is_struck_off_anaf`, semnal separat de registrul inactivilor (pe baza `dataRadiere` sau a textului `stare_inregistrare`), configurabil prin cuvinte-cheie.
- **Alertă inactivare:** activitate Odoo plus notă în chatter la prima detectare a statusului inactiv.
- **Alertă radiere/dizolvare:** activitate Odoo plus notă în chatter la prima detectare a stării de radiat/dizolvat.
- **Alertă schimbare regim TVA:** notă automată în chatter când `scpTVA` se modifică.
- **Avertizare/blocare la postarea facturii:** notă informativă în chatter la postarea unei facturi emise (`out_invoice`) pe un partener inactiv sau radiat la ANAF; blocare hard opțională din Setări (`l10n_ro_anaf_block_inactive`, `l10n_ro_anaf_block_struck_off`).
- **Re-verificare VIES periodică:** cron opțional (dezactivat implicit) care reia verificarea VIES pentru partenerii UE și semnalează în chatter numerele devenite invalide.
- **Sincronizare manuală:** buton „Sync with ANAF" pe fila ANAF a partenerului.
- **Ultima verificare ANAF:** câmpul `l10n_ro_anaf_last_check` actualizat la fiecare rulare cron.
- **Meniu Log Modificări:** vizualizare globală a tuturor modificărilor ANAF, filtrabilă pe tip/partener/dată.

#### 3. Dependențe

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- `account`

Dependență externă Python: `requests`.

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.change.log`: jurnalul de modificări ale datelor ANAF per partener (câmp, valoare veche/nouă, tip modificare).
- `res.partner` (extins): câmpurile `l10n_ro_vat_subjected`, `l10n_ro_vat_number`, `l10n_ro_caen_code`, `l10n_ro_is_inactive_anaf`, `l10n_ro_anaf_registration_state`, `l10n_ro_anaf_radiation_date`, `l10n_ro_is_struck_off_anaf`, `l10n_ro_anaf_last_check`; logica de sincronizare ANAF, detecție modificări și alertare.
- `account.move` (extins): gardă de postare opțională (`_l10n_ro_posting_guard_errors`) și avertizare soft în chatter pentru facturile emise (`out_invoice`) către parteneri inactivi/radiați ANAF.
- `res.company` (extins): câmpurile `l10n_ro_anaf_block_inactive` și `l10n_ro_anaf_block_struck_off`.
- `res.config.settings` (extins): câmpuri related pentru cele două setări de blocare.

**Vizualizări**

- `views/l10n_ro_anaf_change_log_views.xml`: lista și căutarea jurnalului de modificări, plus meniul „ANAF Change Log" (sub Rapoarte financiare), cu filtru implicit pe stările neconforme (inactiv + radiat).
- `views/res_partner_views.xml`: alerte vizuale (inactiv/radiat) în antetul fișei, fila „ANAF" cu buton de sincronizare manuală și istoricul modificărilor, plus filtre „ANAF Inactive"/„Struck Off at ANAF" în lista de parteneri.
- `views/res_config_settings_views.xml`: secțiunea „ANAF Partner Monitoring (RO)" din Setări contabilitate, cu comutatoarele de blocare la postare.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_l10n_ro_anaf_sync_partners` (`RO: Sync partner data with ANAF`): rulează zilnic, sincronizează toți partenerii companie din România cu CUI, actualizează datele și generează intrările în change log și alertele aferente.
- `ir_cron_l10n_ro_recheck_vies` (`RO: Recheck partners VIES`): rulează lunar, dezactivat implicit; re-verifică validitatea TVA intracomunitar (VIES) pentru partenerii UE și notează în chatter numerele devenite invalide.

#### 5. Conexiuni

Nu au fost identificate în cod alte module care să consume câmpurile sau modelele definite aici (`l10n_ro_is_inactive_anaf`, `l10n_ro_is_struck_off_anaf`, `l10n.ro.anaf.change.log`) în afara dependenței directe [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md), de la care preiau meniul de rapoarte financiare și infrastructura comună ANAF.
