# Deltatech Leave Dashboard (Tablou de bord concedii echipă)

- **Nume Tehnic:** `deltatech_hr_leave_dashboard`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_hr_leave_dashboard
- **Cale Locală:** `odoo-addons/bitshop/deltatech_hr_leave_dashboard`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un singur ecran pentru concediile unei echipe, construit peste aplicația standard Time Off. Managerii și responsabilii de aprobare văd cererile anului, le pot aproba sau refuza dintr-un clic, văd cine din același departament lipsește în aceeași perioadă și urmăresc soldurile întregii echipe. Aprobarea folosește fluxul standard Odoo, deci dubla validare, drepturile de acces și notificările rămân cele din Odoo. Modulul nu stochează date și nu adaugă câmpuri pe modelele standard. Este bazat pe modulul de concedii al MD Trade (`mdtrade_concedii`), preluat cu acordul acestora.

#### 2. Funcționalități Cheie

- **Meniu:** *Time Off > Team Time Off*; se alege anul și, pentru cine vede mai mult decât propriile date, departamentul sau angajatul.
- **Tabul Plan:** cererile anului pentru persoanele din responsabilitate, cu butoane *Approve* / *Validate* (a doua aprobare) / *Refuse* pe rând, afișate doar acolo unde drepturile standard permit decizia. Filtrul implicit arată cererile de aprobat și pe cele aprobate; *To approve* păstrează doar ce așteaptă decizie.
- **Suprapuneri:** lângă fiecare cerere, un badge cu numărul de colegi din același departament absenți în aceeași perioadă (la hover apar numele). Standardul previne doar suprapunerea cererilor aceluiași angajat.
- **Solduri pentru toată echipa:** zile alocate, luate, de aprobat și rămase per angajat și tip de concediu, cu bară de utilizare (zile aprobate în culoarea principală, zile de aprobat în galben) și alocarea care expiră următoarea (îngroșat când expirarea e aproape). Cifrele sunt cele din tabloul standard Time Off, citite pentru toți angajații deodată.
- **Cerere nouă:** butonul *New request* sau *+* de pe o linie de sold deschide formularul standard de concediu pentru tine sau pentru angajatul respectiv.
- **Tabul Analiză:** zile pe tip, pe lună, pe departament și pe angajat, plus cine lipsește azi. Se numără cererile aprobate și cele de aprobat (nu refuzate/anulate), în luna în care începe cererea.
- **Cifre cheie:** cereri de aprobat (și câte așteaptă decizia utilizatorului), zile aprobate în an, persoane absente azi.
- **Cine ce vede:** *Time Off Officer* vede toți angajații companiilor selectate; aprobatorul de concedii al angajatului (câmpul *Time Off*) vede angajații aprobați de el; managerul unui departament vede angajații departamentului și ai subdepartamentelor, chiar fără rol de Time Off (vede cererile, decide doar dacă drepturile standard permit); fiecare angajat își vede propriile cereri și solduri.
- **Extensibil:** alte module pot adăuga file în tablou prin registrul `deltatech_hr_leave_dashboard.tabs` (de exemplu pontajul lunar românesc din `l10n_ro_hr_pontaj`), fără dependență reciprocă.
- **Configurare:** fără setări proprii; se completează în Odoo rolul Time Off *Officer*, aprobatorul și departamentul pe angajat, iar setarea *Approval* pe tipul de concediu decide cine aprobă și dacă e nevoie de a doua aprobare.

Fluxul detaliat pas-cu-pas, cu capturi, este în [Fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `hr_holidays`

#### 4. Componente Cheie

**Modele**

- `deltatech.hr.leave.dashboard` (model abstract, fără tabelă): citește la fiecare deschidere `hr.leave`, `hr.leave.allocation` și `hr.employee` și pregătește datele tabloului (cereri, suprapuneri, solduri, analiză).

**Vizualizări**

- `action_hr_leave_dashboard`: acțiune client care deschide tabloul (meniul `menu_hr_leave_dashboard`).
- Componentă OWL în `static/src/dashboard/` (`leave_dashboard.esm.js`, `.xml`, `.scss`), încărcată în `web.assets_backend`.

**Acțiuni Automate / Acțiuni Server**

- Nu există crone sau acțiuni server.

#### 5. Conexiuni

- `l10n_ro_hr_pontaj`: poate adăuga o filă de pontaj lunar în tablou prin registrul `deltatech_hr_leave_dashboard.tabs`.
