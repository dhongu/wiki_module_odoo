# Romania - Foaie colectivă de prezență (pontaj)

- **Nume Tehnic:** `l10n_ro_hr_pontaj`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_hr_pontaj
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_pontaj`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Foaia colectivă de prezență (pontajul lunar) pentru firmele din România, construită peste modulul standard Concediu. Pontajul fiecărei luni este propus automat din programul de lucru, sărbătorile legale și concediile aprobate, iar diferențele față de realitate (absențe nemotivate, delegații, ore lucrate în concediu) se înregistrează ca corecții pe zi. Foaia se exportă în Excel și PDF, iar luna se închide după salarizare.

#### 2. Funcționalități Cheie

- **Pontaj propus din program:** fiecare zi pornește de la programul de lucru, sărbătorile legale și concediile aprobate; corecțiile manuale se fac pe zi, direct în celula din grilă (*Înapoi la codul generat* șterge corecția).
- **Ordinea codurilor pe aceeași zi:** corecția manuală; codurile care suspendă contractul (maternitate, concediu medical, fără plată, șomaj tehnic); sărbătoarea legală; concediul de odihnă și alte concedii; orele de program. Concediul medical întrerupe concediul de odihnă, iar sărbătoarea legală nu se socotește în el.
- **Ore de început și de sfârșit** ale programului fiecărui angajat, afișate pe foaie lângă nume.
- **Coduri configurabile** (`8`, `CO`, `CM`, `CFP`, `EV`, `REC`, `AC`, `D`, `N`, `SN`, `M`, `CIC`, `SL`, `ST`), legate de tipurile de prezență (work entry type); un tip de concediu apare cu codul tipului său de prezență. Codurile pot fi redenumite după regulamentul intern; prioritatea decide codul când două situații cad în aceeași zi. `N` nu suspendă contractul; `SN` se folosește când există decizia de suspendare.
- **Luna închisă:** după salarizare, ofițerul de concedii închide luna și corecțiile nu se mai pot modifica, nici prin RPC; doar administratorul o redeschide.
- **Export Excel și PDF** A4 peisaj, cu legendă și loc pentru semnături.
- **Cerere de concediu tipărită** (*Tipărește* → *Cerere de concediu (RO)*), cu angajator, funcție, departament, perioadă, zile, aprobator și sărbătorile legale din interval; cererea respinsă e marcată vizibil.
- **Sărbători legale RO** (art. 139 Codul muncii, cu Paștele și Rusaliile ortodoxe), generate pe an din *Concediu* → *Management* → *Generează sărbătorile legale*, ca zile libere în programul de lucru, fără dublare.
- **Plan de acumulare „Annual leave Romania (carry-over 18 months)”:** 20 de zile lucrătoare pe an, reportate la 1 ianuarie și valabile 18 luni; cu 60 de zile înainte de expirare, aprobatorul primește o activitate, iar angajatul un mesaj. Scoaterea zilelor din sold e doar evidență: dacă angajatorul nu poate dovedi că a oferit posibilitatea efectuării, zilele se realocă.
- **Acces:** *Concediu* → *Management* → *Pontaj* (ofițer de concedii); configurare coduri în *Concediu* → *Configurare* → *Pontaj (RO)* → *Coduri pontaj*. Fluxul pas-cu-pas este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `hr_holidays`
- `hr_work_entry_holidays`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.hr.pontaj`: model abstract care calculează foaia lunară (zile, ore, coduri, totaluri) și exporturile.
- `l10n.ro.hr.pontaj.code`: codurile de pontaj, legate de tipurile de prezență, cu prioritate.
- `l10n.ro.hr.pontaj.override`: corecțiile manuale pe angajat și zi.
- `l10n.ro.hr.pontaj.month`: starea lunii (deschisă/închisă).
- `l10n.ro.hr.public.holiday.wizard`: wizard de generare a sărbătorilor legale pe an.

**Vizualizări**

- `action_pontaj`: acțiune client cu grila lunară editabilă (componentă JS `pontaj_sheet`).
- `view_pontaj_code_list`, `view_pontaj_override_list`, `view_pontaj_month_list`: liste pentru coduri, corecții și luni de pontaj.
- `view_public_holiday_wizard_form`: formularul wizard-ului de sărbători legale.
- Rapoarte QWeb: `report_pontaj` (PDF foaie) și `report_leave_request` (cerere de concediu).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_carryover_expiry_warning`: avertizează (activitate pentru aprobator, mesaj pentru angajat) cu 60 de zile înainte de expirarea zilelor reportate.

#### 5. Conexiuni

- [deltatech_hr_leave_dashboard](../deltatech_hr_leave_dashboard/index.md): pontajul apare ca al treilea tab în tabloul „Concediile echipei”, fără dependență directă.
- [l10n_ro_hr_pontaj_payroll](../l10n_ro_hr_pontaj_payroll/index.md): transmite corecțiile de pontaj în salarizare.
