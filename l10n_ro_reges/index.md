# Integrare REGES-Online România (FR-45) (localizat la `l10n_ro_reges/index.md`)

- **Nume Tehnic:** `l10n_ro_reges`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_reges
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reges`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul integrează Odoo cu **REGES-Online** (Registrul Electronic General al Salariaților), sistemul Inspecției Muncii care înlocuiește REVISAL. Permite tuturor angajatorilor din România să transmită automat angajați și contracte individuale de muncă direct din Odoo, fără dublă înregistrare în sisteme separate. Conform Legii 53/2003 (Codul Muncii) și HG 905/2017, transmiterea electronică a angajaților, contractelor, modificărilor, suspendărilor și încetărilor este obligatorie, iar nerespectarea termenelor atrage amendă de 5.000–8.000 RON per salariat neraportat.

#### 2. Funcționalități Cheie

- Autentificare OpenID Connect cu refresh automat al token-ului JWT.
- Transmitere angajați: înregistrare, modificare, radiere (`InregistrareSalariat`, `ModificareSalariat`, `RadiereSalariat`).
- Transmitere contracte: adăugare, modificare, suspendare, încetare, radiere (`AdaugareContract`, `ModificareContract`, `SuspendareContract`, `IncetareContract`, `RadiereContract`).
- Polling asincron al cozii de rezultate REGES (`/api/Status/PollMessage`).
- Auto-tracking al modificărilor pe câmpurile urmărite ale angajatului și contractului, cu retrimitere automată la `write()` dacă starea REGES e activă.
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

- `hr.version` (extins, fostul `hr.contract`): câmpuri REGES pe contract — cod COR, tip durată/normă/loc de muncă, temei legal suspendare/încetare, stare contract REGES (`l10n_ro_reges_state`), UUID contract REGES, jurnal de transmisii asociat.
- `hr.employee` (extins): CNP, nivel studii, tip act identitate, stare transmisie REGES (`l10n_ro_reges_state`), UUID angajat REGES, jurnal de transmisii asociat.
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
- `hr_payroll`: sursa contractelor și a datelor salariale transmise la REGES.
