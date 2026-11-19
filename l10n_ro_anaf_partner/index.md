# Romania - Monitorizare modificări date ANAF parteneri (localizat la `l10n_ro_anaf_partner/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_partner`
- **Versiune:** `19.0.2.7.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_partner
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_anaf_partner
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul monitorizează modificările datelor ANAF ale partenerilor, cu **client de sincronizare propriu** (fără dependențe de module OCA de fiscalitate). Interoghează direct serviciul sincron ANAF de verificare TVA, actualizează denumirea, adresa, codul CAEN, statutul de plătitor TVA, regimul de TVA la încasare și starea de înregistrare a fiecărui partener din România, înregistrează automat orice modificare detectată într-un jurnal (change log) și emite alerte (activități și note în chatter) atunci când un partener devine inactiv fiscal, este radiat/dizolvat sau își schimbă regimul de TVA — prevenind astfel emiterea de facturi către parteneri cu probleme fiscale și deducerea greșită a TVA de la furnizori.

#### 2. Funcționalități Cheie

- **Sincronizare ANAF proprie:** client direct pentru serviciul sincron de verificare TVA (loturi de max. 100 CUI-uri, o cerere pe secundă), fără dependențe OCA; funcționează pentru partenerii din România cu CUI completat (fără prefix „RO"), inclusiv PFA și alte entități fără statut de companie. Persoanele de contact și partenerii fără CUI nu sunt procesați.
- **TVA la încasare (RTVAI):** bifa `l10n_ro_vat_on_payment` și datele de început/sfârșit, preluate din blocul `inregistrare_RTVAI`; același câmp ca în modulul OCA `l10n_ro_vat_on_payment`, deci cele două pot coexista.
- **Perioade de TVA:** istoricul înregistrării în scop de TVA și perioadele RTVAI, păstrate de la o sincronizare la alta, pentru regimul furnizorului la data facturii (folosit de declarația D394).
- **Avertizări pe factura de furnizor:** banner de avertizare când furnizorul aplică TVA la încasare (TVA deductibilă doar după plată) sau când nu era înregistrat în scop de TVA la data facturii, dar factura conține TVA.
- **Change log:** înregistrarea automată a oricărei modificări detectate la actualizarea ANAF (denumire, adresă, localitate, cod poștal, CAEN, TVA, scpTVA, TVA la încasare, stare de înregistrare).
- **Marcare inactiv ANAF:** câmpul `l10n_ro_is_inactive_anaf` calculat din `statusInactivi`, cu badge/alertă vizibilă pe fișa partenerului.
- **Detectare radiere/dizolvare:** câmpul `l10n_ro_is_struck_off_anaf`, semnal separat de registrul inactivilor (pe baza `dataRadiere` sau a textului `stare_inregistrare`), configurabil prin cuvinte-cheie (`l10n_ro_anaf_partner.struck_off_keywords`, implicit `RADIERE,RADIAT,DIZOLVARE`); `TRANSFER` e exclus intenționat. Un partener poate fi radiat fără să fie listat ca inactiv.
- **Excludere companiile proprii din sincronizare:** partenerul propriei companii și contactele lui copil (`l10n_ro_is_own_company_partner`) nu sunt suprascriși de ANAF; excluderea se aplică la cron, la sincronizarea manuală și la re-verificarea VIES, iar butonul „Sync with ANAF" e ascuns și înlocuit cu o notă explicativă.
- **Normalizare sector București pentru e-Factura:** localitatea întoarsă de ANAF (ex. „Sector 3 Mun. București") e convertită la forma cerută de CIUS-RO (`SECTOR1`…`SECTOR6`), derivată din text sau din prefixul codului poștal; dacă nu poate fi dedus, valoarea rămâne neatinsă.
- **Alerte:** activitate Odoo plus notă în chatter la prima detectare a stării inactiv sau radiat/dizolvat; notă automată în chatter când se schimbă `scpTVA` sau regimul de TVA la încasare.
- **Avertizare/blocare la postarea facturii:** notă informativă în chatter, restrânsă la facturile emise (`out_invoice`), la postarea pe un partener inactiv sau radiat; blocare hard opțională și independentă pentru fiecare stare, din Setări → Contabilitate → „ANAF Partner Monitoring (RO)" (`l10n_ro_anaf_block_inactive`, `l10n_ro_anaf_block_struck_off`), ambele oprite implicit.
- **Re-verificare VIES periodică:** cron lunar opțional (dezactivat implicit) care reia verificarea VIES pentru partenerii UE și semnalează în chatter numerele devenite invalide.
- **Sincronizare manuală și ultima verificare:** buton „Sync with ANAF" pe fila ANAF a partenerului; câmpul `l10n_ro_anaf_last_check` se actualizează la fiecare rulare cron.
- **Meniu Log Modificări:** vizualizare globală a modificărilor ANAF, filtrabilă pe tip/partener/dată, cu filtru implicit pe stările neconforme; citirea jurnalului e permisă oricărui utilizator intern, scrierea rămâne restricționată la contabilitate.
- **Configurare:** cron-ul „RO: Sync partner data with ANAF" e activ implicit, zilnic (Setări → Tehnic → Automatizări); parametri de sistem opționali `l10n_ro_anaf_partner.anaf_url`, `l10n_ro_anaf_partner.anaf_batch_size` (implicit 100) și `l10n_ro_anaf_partner.struck_off_keywords`. Dacă este instalat și modulul OCA `l10n_ro_fiscal_validation`, cron-ul lui sincronizează aceiași parteneri fără jurnal: se dezactivează sau se dezinstalează.

#### 3. Dependențe

- `account`
- `l10n_ro_move_guard`

Dependență externă Python: `requests`.

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.change.log`: jurnalul de modificări ale datelor ANAF per partener (câmp, valoare veche/nouă, tip modificare).
- `l10n.ro.anaf.vat.period`: perioadele de TVA ale unui partener (înregistrare în scop de TVA și TVA la încasare), cu dată de început/sfârșit și mesajul ANAF; unică pe (partener, tip, dată de început).
- `res.partner` (extins): câmpurile `l10n_ro_vat_subjected`, `l10n_ro_vat_number`, `l10n_ro_caen_code`, `l10n_ro_vat_on_payment` (cu date de început/sfârșit), `l10n_ro_is_inactive_anaf`, `l10n_ro_anaf_registration_state`, `l10n_ro_anaf_radiation_date`, `l10n_ro_is_struck_off_anaf`, `l10n_ro_anaf_last_check`, `l10n_ro_is_own_company_partner`; logica de sincronizare ANAF, excludere companii proprii, normalizare localitate București, detecție modificări și alertare.
- `account.move` (extins): gardă de postare opțională (`_l10n_ro_posting_guard_errors`), restrânsă la `out_invoice` prin `_l10n_ro_anaf_is_guarded()`, avertizare soft în chatter și câmpurile `l10n_ro_anaf_warn_vat_on_payment` / `l10n_ro_anaf_warn_non_vat_payer` pentru facturile de furnizor.
- `res.company` (extins): câmpurile `l10n_ro_anaf_block_inactive` și `l10n_ro_anaf_block_struck_off`.
- `res.config.settings` (extins): câmpuri related pentru cele două setări de blocare.

**Vizualizări**

- `view_l10n_ro_anaf_change_log_list` / `view_l10n_ro_anaf_change_log_search`: lista și căutarea jurnalului de modificări; acțiunea `action_l10n_ro_anaf_change_log` („ANAF Change Log").
- `view_partner_form_l10n_ro_anaf` / `view_partner_form_l10n_ro_anaf_page`: alerte vizuale (inactiv/radiat) în antetul fișei și fila „ANAF" cu buton de sincronizare manuală, regim TVA la încasare, perioade de TVA și istoricul modificărilor.
- `view_res_partner_filter_l10n_ro_anaf`: filtre „ANAF Inactive", „Struck Off at ANAF" și TVA la încasare în lista de parteneri.
- `view_move_form_l10n_ro_anaf_vendor`: bannere de avertizare pe factura de furnizor (TVA la încasare / furnizor neplătitor de TVA la data facturii).
- `res_config_settings_view_form_anaf_partner`: secțiunea „ANAF Partner Monitoring (RO)" din Setări contabilitate, cu comutatoarele de blocare la postare.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_l10n_ro_anaf_sync_partners` (`RO: Sync partner data with ANAF`): rulează zilnic, activ implicit; sincronizează partenerii din România cu CUI (cu excepția partenerilor propriilor companii), actualizează datele și generează intrările în change log și alertele aferente.
- `ir_cron_l10n_ro_recheck_vies` (`RO: Recheck partners VIES (intra-community VAT)`): rulează lunar, dezactivat implicit; re-verifică validitatea TVA intracomunitar (VIES) pentru partenerii UE și notează în chatter numerele devenite invalide.

#### 5. Conexiuni

- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): perioadele de TVA păstrate aici stabilesc regimul furnizorului la data facturii, folosit de declarația D394 (conform documentației modulului).
- `l10n_ro_move_guard`: oferă garda comună de postare folosită pentru blocarea opțională pe parteneri inactivi/radiați.
- `l10n_ro_vat_on_payment` (OCA): partajează câmpul `l10n_ro_vat_on_payment`, deci cele două module pot coexista.
- `l10n_ro_fiscal_validation` (OCA): cron-ul lui sincronizează aceiași parteneri; la actualizarea de la versiuni anterioare lui 19.0.2.0.0 este dezactivat automat.
