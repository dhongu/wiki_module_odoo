# Romania - Integrare REGES-Online (FR-45) (localizat la `l10n_ro_reges/index.md`)

- **Nume Tehnic:** `l10n_ro_reges`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_reges
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reges`
- **Ultima Ingestie:** 2026-10-16
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md) (cu [OBTINERE_ACCES.md](OBTINERE_ACCES.md))

#### 1. Sumar

Modulul integrează Odoo cu **REGES-Online** (Registrul Electronic General al Salariaților), sistemul Inspecției Muncii care înlocuiește REVISAL. Permite tuturor angajatorilor din România să transmită automat angajați și contracte individuale de muncă direct din Odoo, fără dublă înregistrare în sisteme separate. Conform Legii 53/2003 (Codul Muncii) și HG 905/2017, transmiterea electronică a angajaților, contractelor, modificărilor, suspendărilor și încetărilor este obligatorie, iar nerespectarea termenelor atrage amendă de 5.000–8.000 RON per salariat neraportat.

#### 2. Funcționalități Cheie

- Autentificare OpenID Connect cu refresh automat al token-ului JWT.
- Transmitere angajați: înregistrare, modificare, radiere (`InregistrareSalariat`, `ModificareSalariat`, `RadiereSalariat`).
- Transmitere contracte: adăugare, modificare, suspendare, încetare, radiere (`AdaugareContract`, `ModificareContract`, `SuspendareContract`, `IncetareContract`, `RadiereContract`).
- Polling asincron al cozii de rezultate REGES (`/api/Status/PollMessage`).
- Auto-tracking al modificărilor pe câmpurile urmărite ale angajatului și contractului, cu retrimitere automată la `write()` dacă starea REGES e activă.
- Temei legal de încetare cu cele 13 coduri oficiale din nomenclatorul REGES (`TemeiIncetare`): art. 31 alin. (3), art. 55 lit. b), art. 56 alin. (1) lit. a), c), i), art. 61 lit. a), c), d), art. 65 (`Art65Alin1`), art. 68, art. 81 alin. (1), (7), (8). Codurile generice `Art56` și `Art65` nu existau în REGES; la migrare `Art65` devine `Art65Alin1`, iar `Art56` se golește, cu notă pe contract care cere alegerea literei înainte de transmitere. Lista (`TERMINATION_BASES`) e folosită și de decizia de încetare din `l10n_ro_hr_documents`.
- Actul de identitate pe angajat (Informații private, grupul Cetățenie): tip, serie, număr, emitent, dată eliberare; datele sunt preluate în deciziile din `l10n_ro_hr_documents` și în adeverințele din `l10n_ro_payroll_certificates`.
- Numărul CIM pe contract, transmis la REGES ca `numarContract` (anterior se trimitea numele versiunii); modificarea lui pe un contract activ pleacă drept `ModificareContract`.
- Jurnal de transmisii cu posibilitate de retrimitere după corectarea erorilor.
- Sincronizare nomenclator COR din API-ul REGES (~5.044 ocupații).
- Tab REGES pe fișa angajatului și pe contract.
- Meniu HR → REGES (Transmisii, Configurare, Nomenclator COR).
- 3 cron-uri automate (polling la 30 minute, contracte scadente zilnic, COR săptămânal) — dezactivate implicit, se activează la configurare.
- 12+ teste automate cu mock API (fără apeluri reale la REGES).

#### 3. Dependențe

- `hr_payroll`
- `l10n_ro`
- Python: `requests`

#### 4. Componente Cheie

**Modele**

- `hr.version` (extins, fostul `hr.contract`): câmpuri REGES pe contract — cod COR, tip durată/normă/loc de muncă, temei legal suspendare/încetare (`l10n_ro_temei_incetare`), număr CIM (`l10n_ro_contract_number`), stare contract REGES (`l10n_ro_reges_state`), UUID contract REGES, jurnal de transmisii asociat.
- `hr.employee` (extins): CNP, nivel studii, act de identitate (tip, serie `l10n_ro_id_series`, număr, emitent, dată eliberare), stare transmisie REGES (`l10n_ro_reges_state`), UUID angajat REGES, jurnal de transmisii asociat.
- `l10n.ro.reges.message`: jurnal mesajelor trimise/primite către REGES (payload, răspuns, stare, retrimitere după eroare).
- `l10n.ro.reges.cor`: nomenclator COR (Clasificarea Ocupațiilor din România), sincronizat din API REGES.
- `res.company` (extins): credențiale și configurare REGES per companie (mediu test/producție, utilizator, parolă, cache token JWT), metode de autentificare OpenID și apeluri API (`_l10n_ro_reges_api_get`, `_l10n_ro_reges_api_post`, `_l10n_ro_reges_build_header`).
- `res.config.settings` (extins): câmpuri de configurare REGES în Setări și acțiune de test conexiune.

**Vizualizări**

- `views/hr_employee_views.xml`: tab REGES pe fișa angajatului, buton „Trimite la REGES" / „Radiere din REGES".
- `views/hr_contract_views.xml`: tab REGES pe contract, butoane „Trimite la REGES", „Suspendă în REGES", „Radiere din REGES".
- `views/l10n_ro_reges_message_views.xml`: jurnal de transmisii, cu acțiune de reîmprospătare din coada REGES.
- `views/l10n_ro_reges_cor_views.xml`: nomenclator COR.
- `views/res_config_settings_views.xml`: secțiune de configurare REGES în Setări.
- `views/menus.xml`: meniu HR → REGES (Transmisii, Nomenclator COR).

**Acțiuni Automate / Acțiuni Server**

- `cron_poll_reges_queue`: polling coadă rezultate REGES la 30 de minute (`/api/Status/PollMessage`).
- `cron_send_pending_contracts`: trimitere zilnică a contractelor cu dată de start apropiată, înainte de termenul legal.
- `cron_sync_cor`: sincronizare săptămânală a nomenclatorului COR din API REGES.

#### 5. Conexiuni

- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): D112 folosește aceleași date de contract; REGES asigură sincronizarea acestora cu realitatea, evitând discrepanțe la depunerea declarației.
- [l10n_ro_hr_documents](../l10n_ro_hr_documents/index.md) și [l10n_ro_payroll_certificates](../l10n_ro_payroll_certificates/index.md): preiau actul de identitate al angajatului, iar decizia de încetare folosește lista de temeiuri REGES (legătură de cod din HISTORY.md, fără dependență în manifest).
- `hr_payroll`: sursa contractelor și a datelor salariale transmise la REGES.
