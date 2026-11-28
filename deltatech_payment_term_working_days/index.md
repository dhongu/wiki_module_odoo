# Termene de plată în zile lucrătoare (Payment Terms in Working Days)

- **Nume Tehnic:** `deltatech_payment_term_working_days`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_payment_term_working_days
- **Cale Locală:** odoo-addons/deltatech/deltatech_payment_term_working_days
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Permite ca un termen de plată să numere zilele în zile lucrătoare, nu calendaristice, și să mute scadența căzută într-un weekend sau într-o sărbătoare legală în următoarea zi lucrătoare. Odoo standard numără doar zile calendaristice, deci un termen de 3 zile emis vineri cade luni, iar unul de 30 de zile poate cădea sâmbătă sau de Crăciun.

#### 2. Funcționalități Cheie

- **Zile lucrătoare pe linie:** fiecare linie a termenului alege **Count** = `Calendar Days` (implicit, comportament neschimbat) sau `Working Days`; un plan în rate poate combina ambele. Nu se aplică liniilor cu scadență fixă „pe ziua X a lunii următoare”.
- **Mutare la următoarea zi lucrătoare:** opțiunea **Move to the Next Working Day** de pe termen mută orice scadență căzută într-o zi nelucrătoare, atât pentru liniile calendaristice, cât și pentru cele în zile lucrătoare.
- **Calendarul companiei:** zilele lucrătoare sunt cele din programul de lucru al companiei (implicit luni-vineri, dacă nu există program); sărbătorile legale sunt concediile (time off) ale companiei care nu sunt legate de o resursă. Paștele, Rusaliile și orice altă sărbătoare introdusă se iau în calcul în fiecare an.
- **Peste tot unde se folosește scadența:** scadența facturii, scadența fiecărei rate, rapoartele de vechime creanțe/datorii și urmăririle citesc datele ajustate. Noile scadențe se aplică facturilor create sau resetate la ciornă după activare; facturile postate își păstrează scadența.
- **Avertisment plafon legal:** formularul termenului avertizează când o linie în zile lucrătoare poate depăși 60 de zile calendaristice (plafonul uzual între profesioniști, Directiva UE 2011/7/UE). Întârzierea și dobânda penalizatoare se numără tot în zile calendaristice, de la ziua următoare scadenței mutate.
- **Configurare:** modulul nu creează sărbătorile. Se verifică programul de lucru al companiei (Setări > Tehnic > Resurse > Programe de lucru, în modul debug) și se adaugă sărbătorile anului în Resource Time Off (sau Time Off > Configurare > Sărbători companie), fără resursă. Sărbătorile se adaugă înainte de scadența facturilor noului an; pentru România pot fi generate cu wizardul modulului `l10n_ro_hr_pontaj`.
- **Meniu:** Contabilitate > Configurare > Termene de plată.

#### 3. Dependențe

- `account`
- `resource`

#### 4. Componente Cheie

**Modele**

- `account.payment.term` (extins): opțiunea de mutare la ziua lucrătoare, avertismentul de plafon și calculul scadențelor (`_compute_terms`).
- `account.payment.term.line` (extins): câmpul `day_count` (zile calendaristice / lucrătoare).

**Vizualizări**

- `view_payment_term_form`: adaugă pe formularul termenului câmpul Count pe linii, opțiunea de mutare și avertismentul.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_payment_term](../deltatech_payment_term/index.md): asistent de generare a ratelor unui termen de plată (fără dependență; modulele se completează).
- `l10n_ro_hr_pontaj`: wizardul său generează sărbătorile legale românești.
