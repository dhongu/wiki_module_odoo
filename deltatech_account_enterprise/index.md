# Deltatech Account Enterprise (localizat la `deltatech_account_enterprise/index.md`)

- **Nume Tehnic:** `deltatech_account_enterprise`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_enterprise
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_enterprise`
- **Ultima Ingestie:** `2026-06-09`

#### 1. Sumar

Acest modul extinde funcționalitățile de contabilitate din Odoo Enterprise, concentrându-se pe îmbunătățirea rapoartelor de urmărire a clienților (Customer Follow-up). Scopul său principal este să ofere o imagine mai clară asupra situației datoriilor unui partener, prin gruparea tranzacțiilor după statusul lor și prin afișarea de subtotaluri pe fiecare grup. Astfel, persoanele responsabile cu încasările văd mai ușor ce sume sunt restante și ce sume urmează să devină scadente.

#### 2. Funcționalități Cheie

- **Linii de urmărire grupate**: tranzacțiile din raportul de urmărire sunt grupate după statusul lor, în **Restante (Overdue)** și **Scadente (Due)**.
- **Subtotaluri pe status**: fiecare grup de status (Restante/Scadente) afișează propriile subtotaluri pentru Sumă, Sumă în valută și Sold, oferind o imagine mai clară a situației datoriilor partenerului.
- **Aspect îmbunătățit al raportului**: șablonul raportului de urmărire este ajustat pentru a prezenta mai bine informațiile grupate.

#### 3. Dependențe

- `account`
- `account_accountant`
- `account_reports`

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, valoarea modulului este descrisă la nivel funcțional (rapoarte de urmărire a clienților). Analiza detaliată a componentelor tehnice nu este cerută explicit de descriere.

#### 5. Conexiuni

Nu au fost identificate conexiuni verificate către alte module documentate în wiki.
