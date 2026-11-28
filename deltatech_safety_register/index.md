# Safety Register

- **Nume Tehnic:** `deltatech_safety_register`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_safety_register
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_safety_register`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Registru de evenimente de securitate pentru companiile cu programe de securitate sau World Class Manufacturing: aproape-accidente, incidente și accidente de muncă, fiecare cu cauza rădăcină și acțiuni corective, plus indicatorii anuali de securitate.

#### 2. Funcționalități Cheie

- **Evenimente** clasificate Near miss, Incident (fără vătămare), Injury (fără timp pierdut), Lost-time injury sau Fatal, numerotate `SAF/<an>/NNNN`, cu locație, descriere și cauză rădăcină (meniu **Safety → Events**, export XLSX).
- **Persoana accidentată**: angajat, partener (contractor, vizitator) sau nume liber; departamentul se completează din angajat.
- **Accidente de traseu** marcate separat, păstrate în registru și excluse din LTIFR.
- **Acțiuni corective** cu responsabil și termen; fiecare programează o activitate To-Do. Un eveniment se închide doar după finalizarea acțiunilor, iar unul închis poate fi modificat doar de Safety manager (și nu poate fi șters). Vedere globală în **Safety → Corrective actions**.
- **Indicatori** pe companie și an (**Safety → Reporting → Indicators**): LTIFR (accidente cu timp pierdut × 1.000.000 / ore lucrate, orele din Attendances), aproape-accidente, accidente cu timp pierdut, accidente de traseu, zile fără accident. LTIFR e ascuns, cu avertisment, dacă lipsesc orele unei luni începute.
- Două grupuri de acces, Safety officer și Safety manager, cu izolare multi-companie; dreptul de export se acordă separat.
- Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`
- `mail`
- `hr`
- `hr_attendance`

#### 4. Componente Cheie

**Modele**

- `deltatech.safety.event`: evenimentul de securitate (cu `mail.thread` și `mail.activity.mixin`).
- `deltatech.safety.action`: acțiunea corectivă.
- `deltatech.safety.indicator`: wizard-ul de indicatori (LTIFR etc.).

**Vizualizări**

- `views/safety_event_views.xml`: lista și formularul evenimentelor.
- `views/safety_action_views.xml`: lista acțiunilor corective.
- `wizard/safety_indicator_views.xml`: indicatorii pe an.
- `views/menu.xml`: meniul Safety.

**Acțiuni Automate / Acțiuni Server**

- `sequence_safety_event` (`data/ir_sequence.xml`): secvența `SAF/<an>/NNNN`.

#### 5. Conexiuni

- `hr_attendance`: sursa orelor lucrate pentru LTIFR.
