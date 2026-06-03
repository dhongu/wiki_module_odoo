# Work Days Report (localizat la `deltatech_work_days_report/index.md`)

- **Nume Tehnic:** `deltatech_work_days_report`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_work_days_report
- **Cale Locală:** `odoo-addons/bitshop/deltatech_work_days_report`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul **Work Days Report** generează rapoarte Excel cuprinzătoare pentru urmărirea prezenței angajaților și gestionarea tichetelor de masă. Este util departamentelor de resurse umane și proceselor de salarizare, oferind automat fișiere Excel cu orele lucrate zilnic, totalurile pe angajat, tichetele de masă cuvenite și perioadele de concediu. Astfel se simplifică monitorizarea tiparelor de lucru ale angajaților și administrarea drepturilor la tichete de masă, asigurând raportări consecvente chiar și atunci când configurarea tipurilor de concediu este incompletă.

#### 2. Funcționalități Cheie

- **Îmbunătățirea tipurilor de concediu**: adaugă un câmp configurabil „code" în formularele de tip de concediu (Time Off Type), pentru o mai bună categorisire și raportare.
- **Export Excel în masă**: permite exportul în masă accesibil din vizualizarea de listă a angajaților (Acțiune → „Export Working Days").
- **Raportare cuprinzătoare**: generează rapoarte Excel detaliate care conțin informații despre angajat și orele lucrate zilnic, totalul orelor lucrate, tichetele de masă câștigate per angajat și perioadele/datele de concediu.
- **Codificare flexibilă a concediilor**: afișează automat „ABS" (absență) pentru tipurile de concediu fără cod specificat, asigurând o raportare consecventă chiar și cu o configurare incompletă.

#### 3. Dependențe

- `hr`
- `hr_holidays`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de componente sunt sintetizate din `readme/DESCRIPTION.md`. Acolo unde Readme-ul descrie explicit comportamentul, sunt evidențiate următoarele elemente:

**Modele**

- `hr.leave.type` (extins): adaugă câmpul „code" pentru categorisirea tipurilor de concediu în rapoarte.

**Vizualizări**

- Vizualizarea de listă a angajaților: expune acțiunea „Export Working Days" pentru exportul Excel în masă.

**Acțiuni Automate / Acțiuni Server**

- „Export Working Days": acțiune disponibilă din meniul Acțiune al listei de angajați, care generează raportul Excel cu orele lucrate și tichetele de masă.

#### 5. Conexiuni

- Nicio conexiune funcțională suplimentară identificată către alte module cu pagină wiki.
