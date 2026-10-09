# Romania - Pontaj cu asistent AI

- **Nume Tehnic:** `l10n_ro_hr_pontaj_ai`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_hr_pontaj_ai
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_pontaj_ai`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Asistent AI pentru pontajul lunar, construit peste aplicația Enterprise AI: ofițerul de concedii cere în limbaj natural corecțiile (de exemplu „Ion Popescu a lipsit pe 8 și 9 iunie"), iar asistentul le **propune**; ofițerul le aprobă sau le respinge. Asistentul nu modifică niciodată foaia de pontaj. Modulul este în stare Alpha, licență OPL-1.

#### 2. Funcționalități Cheie

- Agentul **Timesheet Assistant** (*AI → Agenți*), cu subiectul **Timesheet** și trei unelte: caută angajatul după nume, citește luna unui angajat (zile, ore, rezultatul verificărilor) și propune o corecție pe o perioadă. Butonul **Test** de pe agent deschide chatul.
- **Propuneri de corecții** în *Concediu → Management → Propuneri AI* (listă filtrată implicit pe „De aprobat"): un rând pe zi și angajat, cu data, angajatul, codul, orele, motivul și starea; coloane opționale Cerere, Decis de, Decis la. Aceeași zi propusă din nou înlocuiește propunerea de aprobat.
- **Aplică** face corecția prin aceleași reguli ca ecranul *Pontaj* (lună închisă, cod manual, drepturi); **Respinge** închide propunerea. Dacă aplicarea eșuează (de exemplu luna s-a închis între timp), propunerea rămâne de aprobat, cu motivul în coloana Eroare. Zilele aplicate apar în *Pontaj* cu colțul de corecție manuală și în *Corecții pontaj*.
- **Fără ghicit**: weekendurile și sărbătorile legale se sar la absențe și concedii, ce arată deja foaia nu se propune, lunile închise nu primesc propuneri, iar codurile care nu se pot pune manual se refuză.
- **Fără date personale în model**: uneltele întorc doar nume, departament și funcție; CNP, IBAN și adresa nu ies din Odoo.
- **Configurare**: furnizorul de model și cheia în *Setări → AI*; modelul se poate schimba pe agent. Uneltele cer rolul Concediu „Responsabil: Gestionați toate cererile". Codurile propuse sunt cele marcate Manual în *Concediu → Configurare → Pontaj (RO) → Coduri pontaj*. Mesajele din chat ajung la furnizorul de model ales (concediul medical este dată de sănătate: se verifică acordul clientului).
- Fluxul pas cu pas este în [fișa de consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md)
- `ai_app` (Odoo Enterprise)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.hr.pontaj.suggestion`: propunere de corecție (angajat, companie, dată, cod, ore, motiv, cererea originală, stare `De aprobat` / `Aplicată` / `Respinsă`, eroare, decis de/la). Conține `action_apply`, `action_reject` și metodele-unealtă `ai_tool_find_employees`, `ai_tool_month_state`, `ai_tool_propose`.

**Vizualizări**

- `view_pontaj_suggestion_list`, `view_pontaj_suggestion_form`, `view_pontaj_suggestion_search`: lista, formularul și căutarea propunerilor.
- `action_pontaj_suggestion`: acțiunea din meniul *Propuneri AI*.

**Acțiuni Automate / Acțiuni Server**

- `tool_find_employees`, `tool_month_state`, `tool_propose`: acțiuni server folosite ca unelte AI.
- `topic_pontaj` (`ai.topic`) și `agent_pontaj` (`ai.agent`): subiectul și agentul „Timesheet Assistant" livrate ca date.

#### 5. Conexiuni

- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md): foaia de pontaj în care se aplică propunerile (prin `set_cell`).
