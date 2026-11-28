# Team Time Off Dashboard (localizat la `deltatech_hr_leave_dashboard/index.md`)

- **Nume Tehnic:** `deltatech_hr_leave_dashboard`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_hr_leave_dashboard
- **Cale Locală:** `odoo-addons/bitshop/deltatech_hr_leave_dashboard`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un singur ecran pentru concediile unei echipe, construit peste aplicația standard Time Off. Managerul vede cererile anului, aprobă sau refuză dintr-un clic, vede câți colegi din același departament lipsesc în aceeași perioadă și urmărește soldurile întregii echipe. Nu stochează nimic și nu adaugă câmpuri pe modelele standard: tabloul citește `hr.leave`, `hr.leave.allocation` și `hr.employee` la fiecare deschidere. Se bazează pe modulul de concedii al MD Trade Concept SRL.

#### 2. Funcționalități Cheie

- **Plan**: cererile anului pentru persoanele din responsabilitatea utilizatorului, aprobate sau refuzate dintr-un clic. Butoanele apelează aprobarea standard, deci dubla validare, regulile de acces și notificările rămân cele din Odoo; implicit se afișează cererile de aprobat și cele aprobate.
- **Suprapuneri**: lângă fiecare cerere, un insigne cu numărul colegilor din același departament absenți simultan (la trecerea mouse-ului, cine sunt). Standardul previne doar suprapunerea cererilor aceluiași angajat.
- **Solduri pentru toată echipa**: zile alocate, luate, de aprobat și rămase per angajat și tip de concediu, cu bară de utilizare și alocarea care expiră următoarea; cifrele sunt cele din tabloul standard Time Off, citite pentru toți angajații deodată.
- **Analiză**: zile pe tip, lună, departament și angajat, și cine lipsește azi (cererile aprobate și cele de aprobat se numără în luna în care încep).
- **Cifre cheie**: cereri de aprobat (și câte așteaptă decizia utilizatorului), zile aprobate în an, persoane absente azi.
- **Cine ce vede**: *Time Off Officer* vede toți angajații companiilor selectate; aprobatorul unui angajat vede angajații aprobați de el; managerul unui departament vede departamentul și subdepartamentele (decide doar dacă drepturile standard o permit); fiecare angajat își vede cererile și soldurile.
- **Extensibil**: alte module pot adăuga file în tablou prin registry-ul `deltatech_hr_leave_dashboard.tabs`, fără dependență reciprocă.
- Acces: *Time Off > Team Time Off*. Nu are configurare proprie; urmează setările standard (rolul *Officer*, aprobatorul și departamentul pe angajat, setarea *Approval* pe tipul de concediu). Fluxul cu capturi este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `hr_holidays`

#### 4. Componente Cheie

**Modele**

- `deltatech.hr.leave.dashboard`: model de serviciu (fără câmpuri stocate) care calculează planul, soldurile și analiza din `hr.leave`, `hr.leave.allocation` și `hr.employee`.

**Vizualizări**

- `views/hr_leave_dashboard_views.xml`: acțiunea client și meniul *Team Time Off*; interfața OWL este în `static/src/dashboard/`.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- `hr_holidays`: aplicația standard Time Off, ale cărei aprobări și solduri le reutilizează.
- `l10n_ro_hr_pontaj`: poate adăuga o filă lunară de pontaj prin registry-ul `deltatech_hr_leave_dashboard.tabs`, fără dependență (modulul nu are încă pagină wiki).
