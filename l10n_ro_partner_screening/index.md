# Romania - Verificarea partenerilor (localizat la `l10n_ro_partner_screening/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_screening`
- **Versiune:** `19.0.1.3.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_partner_screening
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_screening`
- **Ultima Ingestie:** `2026-11-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul de conformitate fiscală și AML (Anti-Money Laundering) pentru partenerii din Odoo, adaptat cerințelor legislative românești. Ajută companiile să respecte obligațiile legale privind paradisurile fiscale, sancțiunile internaționale și impozitul la sursă pentru nerezidenți, marcând automat riscurile pe fișa partenerului, pe facturi și, opțional, la postarea plăților. Modulul doar semnalează riscurile; deciziile de tranzacționare rămân ale contabilului sau ale ofițerului de conformitate.

#### 2. Funcționalități Cheie

- **Paradisuri fiscale (HG 1/2024):** țările din lista jurisdicțiilor necooperante sunt marcate la instalare; câmpul „Paradis Fiscal” al partenerului este derivat din țară, cu avertisment pe formularul partenerului și pe facturi. Lista se ajustează manual pe țară (**Paradis Fiscal RO (HG 1/2024)**), dacă legislația se modifică.
- **Liste de sancțiuni OFAC și UE:** bază de date locală a entităților sancționate (`l10n.ro.sanction.entry`), cu import din OFAC SDN List (Trezoreria SUA) și EU Consolidated Sanctions List, plus intrări manuale (**Contabilitate → Configurare → Contabilitate → Liste Sancțiuni**, vizibil managerilor de contabilitate; se deschide filtrat implicit pe „UE”). Importul automat săptămânal este livrat **dezactivat** și se activează doar dacă serverul are acces la internet; o actualizare imediată se face din **Acțiuni → Actualizează listele acum (OFAC / UE)**.
- **Screening pe fișa partenerului:** butonul **Screening** face potrivire fuzzy pe tokeni normalizați (fără diacritice, majuscule sau formă juridică) față de listele locale; bannerul roșu apare pe partener și pe factură dacă entitatea e sancționată, cu notă de sancțiune editabilă. Fără potrivire, utilizatorul primește o notificare verde.
- **Screening automat la creare/modificare:** la schimbarea numelui sau a țării rulează un screening „soft” (doar dacă există liste încărcate) care setează indicatorul **Posibilă potrivire sancțiuni** și postează un mesaj în chatter, fără a confirma statusul — decizia rămâne a operatorului (butonul **Screening** sau bifa **Entitate Sancționată**). **Acțiuni → Re-screenează partenerii** reevaluează partenerii existenți.
- **Impozit la Sursă (WHT):** câmpul „Impozit la Sursă (WHT)” se bifează automat pentru parteneri non-RO (se poate debifa, de exemplu dacă există convenție de evitare a dublei impuneri), cu avertisment informativ pe factură cu trimitere la D205/D207.
- **Avertismente pe factură:** roșu pentru partener sancționat, galben pentru paradis fiscal (verificarea deductibilității, art. 24 alin. 16 Cod fiscal), albastru pentru nerezident cu WHT.
- **Blocaj opt-in la plăți (FR-08):** în **Setări → Screening Parteneri (RO)**, opțiunile **Blocare plăți sancționate** și **Blocare plăți paradis fiscal** (per companie) opresc postarea plăților ieșite către parteneri cu risc; implicit rămâne doar bannerul informativ.
- **Status screening unificat:** câmpul calculat `l10n_ro_screening_status`, cu prioritate sancționat > paradis fiscal > WHT > OK, afișat ca badge colorat în lista de parteneri (coloană opțională) și în header-ul formularului.

#### 3. Dependențe

- `base`
- `account`
- Dependență Python (nedeclarată în manifest): `requests`, pentru descărcarea listelor OFAC/UE

#### 4. Componente Cheie

**Modele**

- `l10n.ro.sanction.entry`: stochează local entitățile sancționate (OFAC/UE/Manual), cu nume normalizat (index trigram) pentru potrivire pe tokeni, descărcarea și parsarea listelor sursă și re-screeningul în masă al partenerilor.
- `res.partner` (extins): câmpurile de paradis fiscal, sancțiuni, posibilă potrivire, WHT și statusul de screening calculat; `create`/`write` declanșează screening „soft”; `action_l10n_ro_check_sanctions` pentru verificare manuală.
- `res.country` (extins): marcajul de paradis fiscal conform HG 1/2024.
- `res.company` / `res.config.settings` (extinse): setările per companie pentru blocarea plăților către parteneri sancționați sau din paradisuri fiscale.
- `account.move` (extins): avertismentele de screening (sancțiuni, paradis fiscal, WHT) pe facturi.
- `account.payment` (extins): `action_post` blochează opt-in plățile ieșite către parteneri cu risc.

**Vizualizări**

- `view_partner_form_l10n_ro_screening`, `view_partner_list_l10n_ro_screening`: bannere de avertisment, butonul **Screening** și badge-ul de status pe fișa/lista de parteneri.
- `view_l10n_ro_sanction_entry_list`, `view_l10n_ro_sanction_entry_form`, `view_l10n_ro_sanction_entry_search`: gestiunea listei locale de sancțiuni, cu acțiunea `action_l10n_ro_sanction_entry` și meniul `menu_l10n_ro_sanctions`.
- `view_country_form_l10n_ro_screening`: câmpul de paradis fiscal pe fișa țării.
- `view_move_form_l10n_ro_screening`: bannerele de avertisment pe formularul facturii.
- `res_config_settings_view_form_partner_screening`: setările de blocaj plăți per companie.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_sanctions_refresh` („RO Screening: Actualizare liste sancțiuni OFAC / UE”): la 7 zile, **dezactivat implicit**; rulează `_l10n_ro_refresh_all_sanctions()`, care actualizează listele OFAC SDN și UE și re-screenează partenerii.
- `action_server_refresh_sanctions`: acțiune manuală din lista de sancțiuni — „Actualizează listele acum (OFAC / UE)”.
- `action_server_rescreen_partners`: acțiune manuală din lista de sancțiuni — „Re-screenează partenerii”.

#### 5. Conexiuni

- [l10n_ro_anaf_d205](../l10n_ro_anaf_d205/index.md): impozitul la sursă semnalat aici (WHT) se declară prin D205; legătura este informativă (avertismentul de pe factură), fără dependență de cod.
- [l10n_ro_anaf_d207](../l10n_ro_anaf_d207/index.md): declarația aferentă veniturilor nerezidenților (D207), la care trimite același avertisment WHT; fără dependență de cod.
