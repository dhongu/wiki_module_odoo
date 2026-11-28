# Romania - Foaie colectivă de prezență (pontaj)

- **Nume Tehnic:** `l10n_ro_hr_pontaj`
- **Versiune:** `20.0.1.4.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_hr_pontaj
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_pontaj`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Foaia colectivă de prezență (pontajul lunar) pentru firmele din România, construită peste modulul standard Concediu (`hr_holidays`) și tipurile de prezență din `hr_work_entry`. Pontajul fiecărei luni se propune din programul de lucru, sărbătorile legale și concediile aprobate, iar ce s-a întâmplat altfel se scrie ca corecție pe zi.

#### 2. Funcționalități Cheie

- Pontajul lunii propus din program, cu corecții pe zi (absență nemotivată, delegație, zi lucrată în concediu, alte ore) și ordinea codurilor pe aceeași zi: corecția manuală, apoi coduri care suspendă contractul, sărbătoarea legală, concediile, programul.
- Orele de început și de sfârșit ale programului fiecărui angajat pe foaie (Codul muncii, art. 119).
- Pontaj în format grid, în Concediu → Management → Pontaj (grid), plus listă și pivot pentru rapoarte.
- Coduri configurabile (`8`, `CO`, `CM`, `CFP`, `EV`, `REC`, `AC`, `D`, `N`, `SN`, `M`, `CIC`, `SL`, `ST`), legate de tipurile de prezență; un concediu apare cu codul tipului lui.
- Închiderea lunii după salarizare: corecțiile nu se mai schimbă, iar doar administratorul de concedii redeschide luna.
- Export Excel și PDF A4 peisaj, cu legendă și semnături; cerere de concediu tipărită, cu sărbătorile din interval.
- Sărbătorile legale ale României (art. 139 Codul muncii, cu Paștele și Rusaliile ortodoxe) generate pe an prin wizard.
- Tichete de masă din pontaj: câte unul pe zi lucrată, cu export Excel pentru bancă (Banca Transilvania) și valoarea de pe fișa angajatului.
- Verificările lunii înainte de închidere (Concediu → Management → Verificări pontaj): concedii neaprobate, sărbători negenerate, absențe repetate, zile lucrate în sărbătoare.
- Planul de acumulare „Annual leave Romania (carry-over 18 months)”: 20 de zile pe an, reportate și valabile 18 luni, cu avertizare cu 60 de zile înainte de expirare (activitate pentru aprobator, mesaj pentru angajat).
- Fluxul pas cu pas stă în fișa consultantului.

#### 3. Dependențe

- `hr_holidays`
- `web_grid`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.hr.pontaj`, `l10n.ro.hr.pontaj.line`, `l10n.ro.hr.pontaj.override`: pontajul, liniile pe zi și corecțiile.
- `l10n.ro.hr.pontaj.code`: codurile de pontaj, legate de tipurile de prezență.
- `l10n.ro.hr.pontaj.month`: luna, cu închidere și redeschidere.
- `l10n.ro.hr.pontaj.check`, `l10n.ro.hr.pontaj.check.line`: verificările lunii.
- `l10n.ro.hr.public.holiday.wizard`: generarea sărbătorilor legale.
- `l10n.ro.hr.meal.voucher.export`: exportul tichetelor de masă.
- `hr.employee`: extins pentru tichetele de masă și programul afișat.

**Vizualizări**

- `view_pontaj_line_grid`, `view_pontaj_line_list`, `view_pontaj_line_pivot`, `view_pontaj_line_search` (acțiunea `action_pontaj_grid`): pontajul în grid, listă și pivot.
- `view_pontaj_check_form`, `view_pontaj_code_list`: verificările lunii și codurile de pontaj.
- Foaia lunară editabilă (`pontaj_sheet`) și rapoartele PDF ale pontajului și ale cererii de concediu.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_carryover_expiry_warning`: avertizează înainte de expirarea concediului raportat (activitate pentru aprobator, mesaj pentru angajat).

#### 5. Conexiuni

- [l10n_ro_hr_pontaj_payroll](../l10n_ro_hr_pontaj_payroll/index.md): corecțiile din pontaj devin prezențe în salarizare.
- [deltatech_hr_leave_dashboard](../deltatech_hr_leave_dashboard/index.md): pontajul apare ca al treilea tab în tabloul Concediile echipei, fără dependență între module.
