# Romania - Foaie colectivă de prezență (pontaj)

- **Nume Tehnic:** `l10n_ro_hr_pontaj`
- **Versiune:** `19.0.1.4.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_hr_pontaj
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_pontaj`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Foaia colectivă de prezență (pontajul lunar) pentru firmele din România, construită peste modulul standard Concediu. Pontajul fiecărei luni este propus automat din programul de lucru, sărbătorile legale și concediile aprobate, iar diferențele față de realitate (absențe nemotivate, delegații, ore lucrate în concediu) se înregistrează ca corecții pe zi. Foaia se exportă în Excel și PDF, se verifică înainte de închidere, iar luna se închide după salarizare. Din aceeași foaie se obține și exportul tichetelor de masă pe zilele efectiv lucrate.

#### 2. Funcționalități Cheie

- **Pontaj propus din program:** fiecare zi pornește de la programul de lucru, sărbătorile legale și concediile aprobate; corecțiile manuale se fac pe zi, direct în celula din grilă (*Înapoi la codul generat* șterge corecția).
- **Ordinea codurilor pe aceeași zi:** corecția manuală; codurile care suspendă contractul (maternitate, concediu medical, fără plată, șomaj tehnic); sărbătoarea legală; concediul de odihnă și alte concedii; orele de program. Concediul medical întrerupe concediul de odihnă, iar sărbătoarea legală nu se socotește în el.
- **Pontaj în format grid** (*Concediu* → *Management* → *Pontaj (grid)*): angajații pe rânduri, zilele pe coloane, cu culori pe tipul zilei; celula se editează (ore, cod sau `-` pentru revenirea la program), iar ce se scrie devine corecție, cu aceleași reguli ca în foaia principală (lună închisă refuză, zilele din afara contractului sunt blocate). Lista și pivotul din același meniu servesc la rapoarte (filtre *Lucrat*, *Concediu*, *Corectat de mână*; pe pivot, măsura *Număr* dă zilele pe cod). Cere `web_grid` (Enterprise).
- **Verificările lunii** (*Concediu* → *Management* → *Verificări pontaj* sau butonul *Verificări* din foaie): reguli fără AI, care nu modifică nimic. Erori: foaie goală, angajat fără program; avertismente: cerere neaprobată, sărbători negenerate, angajat fără zile lucrătoare, `N` de cel puțin 3 ori, zi cu peste 12 ore; informații: zi lucrată în weekend sau sărbătoare, corecții fără motiv, contract fără dată de început. La *Închide luna*, erorile și avertismentele cer confirmare (*Vezi verificările* / *Închide oricum*).
- **Export tichete de masă** (*Concediu* → *Management* → *Exportă tichete de masă*, sau *Acțiune* din lista de angajați): câte un tichet pentru fiecare zi cu un cod care are indicatorul *Tichet de masă* (implicit doar `8`); concediile, sărbătorile, absențele și delegațiile nu dau tichet (Legea 165/2018). Fișier Excel în formatul Banca Transilvania (nume, CNP, valoare, IBAN), cu valoarea tichetului de pe fișa angajatului (maximum 45 lei) sau valoarea implicită din fereastră. Disponibil doar ofițerului de concedii.
- **Ore de început și de sfârșit** ale programului fiecărui angajat, afișate pe foaie lângă nume.
- **Coduri configurabile** (`8`, `CO`, `CM`, `CFP`, `EV`, `REC`, `AC`, `D`, `N`, `SN`, `M`, `CIC`, `SL`, `ST`), legate de tipurile de prezență (work entry type); un tip de concediu apare cu codul tipului său de prezență. Codurile pot fi redenumite după regulamentul intern; prioritatea decide codul când două situații cad în aceeași zi. `N` nu suspendă contractul; `SN` se folosește când există decizia de suspendare.
- **Luna închisă:** după salarizare, ofițerul de concedii închide luna și corecțiile nu se mai pot modifica, nici prin RPC; doar administratorul o redeschide.
- **Export Excel și PDF** A4 peisaj, cu legendă și loc pentru semnături.
- **Cerere de concediu tipărită** (*Tipărește* → *Cerere de concediu (RO)*), cu angajator, funcție, departament, perioadă, zile, aprobator și sărbătorile legale din interval; cererea respinsă e marcată vizibil.
- **Sărbători legale RO** (art. 139 Codul muncii, cu Paștele și Rusaliile ortodoxe), generate pe an din *Concediu* → *Management* → *Generează sărbătorile legale*, ca zile libere în programul de lucru, fără dublare.
- **Plan de acumulare „Annual leave Romania (carry-over 18 months)”:** 20 de zile lucrătoare pe an, reportate la 1 ianuarie și valabile 18 luni; cu 60 de zile înainte de expirare, aprobatorul primește o activitate, iar angajatul un mesaj. Scoaterea zilelor din sold e doar evidență: dacă angajatorul nu poate dovedi că a oferit posibilitatea efectuării, zilele se realocă.
- **Lunile de pontaj:** *Concediu* → *Management* → *Luni pontaj* arată starea fiecărei luni (cine și când a închis-o); *Corecții pontaj* listează corecțiile, unde se completează motivul și, opțional, începutul, sfârșitul și orele unei zile lucrate cu alt orar. *Șterge corecțiile* (cu confirmare) acționează pe toate corecțiile lunii din firmă.
- **Acces:** *Concediu* → *Management* → *Pontaj* (ofițer de concedii); configurare coduri în *Concediu* → *Configurare* → *Pontaj (RO)* → *Coduri pontaj*. Fluxul pas-cu-pas este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `hr_holidays`
- `hr_work_entry_holidays`
- `web_grid` (Enterprise)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.hr.pontaj`: model abstract care calculează foaia lunară (zile, ore, coduri, totaluri) și exporturile.
- `l10n.ro.hr.pontaj.code`: codurile de pontaj, legate de tipurile de prezență, cu prioritate.
- `l10n.ro.hr.pontaj.override`: corecțiile manuale pe angajat și zi.
- `l10n.ro.hr.pontaj.month`: starea lunii (deschisă/închisă).
- `l10n.ro.hr.public.holiday.wizard`: wizard de generare a sărbătorilor legale pe an.
- `l10n.ro.hr.pontaj.line`: o zi a unui angajat, pentru view-urile standard (grid, listă, pivot); e o copie reîmprospătată la fiecare citire a perioadei, nu sursa de adevăr.
- `l10n.ro.hr.pontaj.check` / `l10n.ro.hr.pontaj.check.line`: modele tranzitorii pentru verificările lunii (reguli `_check_*`, ușor de extins).
- `l10n.ro.hr.meal.voucher.export`: wizard de export al tichetelor de masă.
- `hr.employee` (extins): *Valoarea tichetului* și *Nume complet* (pentru fișierul băncii).

**Vizualizări**

- `action_pontaj`: acțiune client cu grila lunară editabilă (componentă JS `pontaj_sheet`).
- `view_pontaj_code_list`, `view_pontaj_override_list`, `view_pontaj_month_list`: liste pentru coduri, corecții și luni de pontaj.
- `view_public_holiday_wizard_form`: formularul wizard-ului de sărbători legale.
- `view_pontaj_line_grid`, `view_pontaj_line_list`, `view_pontaj_line_pivot`, `view_pontaj_line_search`: pontajul în view-urile standard (meniul *Pontaj (grid)*).
- `view_pontaj_check_form`: fereastra *Verificări pontaj*.
- `view_meal_voucher_export_form`: fereastra de export a tichetelor de masă.
- Rapoarte QWeb: `report_pontaj` (PDF foaie) și `report_leave_request` (cerere de concediu).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_carryover_expiry_warning`: avertizează (activitate pentru aprobator, mesaj pentru angajat) cu 60 de zile înainte de expirarea zilelor reportate; avertizarea nu se mai repetă după ce aprobatorul marchează activitatea ca făcută.

#### 5. Conexiuni

- [deltatech_hr_leave_dashboard](../deltatech_hr_leave_dashboard/index.md): pontajul apare ca al treilea tab în tabloul „Concediile echipei”, fără dependență directă.
- [l10n_ro_hr_pontaj_payroll](../l10n_ro_hr_pontaj_payroll/index.md): transmite corecțiile de pontaj în salarizare.
- [l10n_ro_hr_pontaj_ai](../l10n_ro_hr_pontaj_ai/index.md): asistent AI pentru corecții cerute în limbaj natural, propuse și aprobate de ofițer.
- [l10n_ro_travel_order_pontaj](../l10n_ro_travel_order_pontaj/index.md): zilele de delegație (`D`) din ordinul de deplasare trec automat în pontaj.
