# Termene de plată în zile lucrătoare

- **Nume Tehnic:** `deltatech_payment_term_working_days`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_payment_term_working_days
- **Cale Locală:** odoo-addons/deltatech/deltatech_payment_term_working_days
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Modulul permite ca un termen de plată să numere zilele în zile lucrătoare, nu în zile calendaristice, și să mute o scadență care pică într-un weekend sau într-o sărbătoare legală în prima zi lucrătoare următoare. În Odoo standard se numără doar zilele calendaristice: un termen de 3 zile pentru o factură emisă vineri se scade duminica, iar un termen de 30 de zile poate cădea sâmbătă sau de Crăciun. Cu acest modul, scadențele de pe factură, din rapoartele de creanțe și datorii și din reminderele de plată sunt cele ajustate.

#### 2. Funcționalități Cheie

- **Zile lucrătoare per linie:** fiecare linie a termenului de plată are câmpul **Count** (`Calendar Days` = comportamentul standard, implicit; `Working Days`). Un plan în rate poate combina ambele tipuri. Numărătoarea nu se aplică liniilor cu scadență fixă „în ziua X a lunii următoare”.
- **Mutare la următoarea zi lucrătoare:** opțiunea **Move to the Next Working Day** de pe termen mută orice scadență căzută într-o zi nelucrătoare, atât la liniile în zile calendaristice, cât și la cele în zile lucrătoare.
- **Calendarul companiei:** zilele lucrătoare sunt cele din programul de lucru al companiei, iar sărbătorile legale sunt concediile (time off) ale companiei fără resursă asociată. Fără program de lucru, zilele lucrătoare sunt luni–vineri. O sărbătoare legată de alt program sau de altă companie este ignorată.
- **Sărbători mobile:** Paștele, Rusaliile și orice altă sărbătoare introdusă ca time off public sunt luate în calcul pentru fiecare an. Modulul citește sărbătorile, nu le creează; ele se adaugă în **Setări > Tehnic > Resurse > Concedii resurse** (mod debug) sau în **Time Off > Configurare > Sărbători legale**, înaintea scadențelor din anul respectiv. Pentru firmele românești, sărbătorile din Codul Muncii pot fi generate cu wizardul din [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md).
- **Peste tot unde se folosește scadența:** scadența facturii, scadența fiecărei rate, rapoartele de vechime a creanțelor/datoriilor și reminderele citesc datele ajustate. Noile scadențe se aplică facturilor create sau resetate la ciornă după configurare; facturile postate își păstrează scadențele.
- **Avertisment plafon legal:** formularul termenului de plată avertizează când o linie în zile lucrătoare poate depăși 60 de zile calendaristice, plafonul legal uzual între profesioniști (Directiva UE 2011/7/UE). Zilele de întârziere și dobânda de întârziere rămân în zile calendaristice, de la ziua următoare scadenței (mutate).
- **Meniu:** **Contabilitate > Configurare > Termene de plată**; previzualizarea (Preview) din formular arată scadențele calculate cu calendarul companiei.
- **Limitări cunoscute (ROADMAP):** data de scont pentru plata anticipată rămâne în zile calendaristice; zilele de întârziere nu se numără în zile lucrătoare.

#### 3. Dependențe

- `account`
- `resource`

#### 4. Componente Cheie

**Modele**

- `account.payment.term` (extins): adaugă `postpone_to_working_day` și `working_days_warning` (calculat, pentru avertismentul de 60 de zile); suprascrie `_compute_terms` pentru a recalcula data fiecărei linii în zile lucrătoare și a o muta la următoarea zi lucrătoare.
- `account.payment.term.line` (extins): adaugă `day_count` (calendar/lucrătoare) și metodele `_get_working_due_date`, `_estimated_calendar_days`.
- `WorkingDays` (clasă Python, `models/working_days.py`): determină zilele lucrătoare ale companiei (program de lucru minus sărbătorile legale din `resource.calendar.leaves` fără resursă, citite an cu an), cu metode de adunare a zilelor lucrătoare și de găsire a următoarei zile lucrătoare.

**Vizualizări**

- `view_payment_term_form`: moștenește `account.view_payment_term_form`; adaugă avertismentul de plafon legal, coloana **Count** pe liniile termenului (ascunsă la scadența fixă în luna următoare) și bifa **Move to the Next Working Day**.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md): wizardul său generează sărbătorile legale românești (inclusiv Paște și Rusalii) pentru un an întreg, folosite de acest modul drept calendar.
