# Deltatech Account Enterprise (localizat la `deltatech_account_enterprise/index.md`)

- **Nume Tehnic:** `deltatech_account_enterprise`
- **Versiune:** `19.0.0.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_enterprise
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_enterprise`
- **Ultima Ingestie:** `2026-08-20`

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
- `account_followup`

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, valoarea modulului este descrisă la nivel funcțional (rapoarte de urmărire a clienților). Deoarece codul conține și extensii tehnice relevante ce nu sunt acoperite de descriere (butoane pe fișa partenerului), acestea sunt documentate suplimentar mai jos.

**Modele**

- `account.followup.report.handler` (extins): exclude din raportul de urmărire liniile deja stinse (sold rezidual 0), chiar dacă nu sunt reconciliate integral, și construiește liniile de raport grupate pe status (Restante/Scadente) cu subtotaluri proprii pentru Sumă, Sumă în valută și Sold.
- `res.partner` (extins): adaugă acțiunile `open_partner_ledger` (Fișa partenerului) și `open_aged_receivable` (Creanțe scadente) și corectează `action_open_partner_followup_journal_items` — filtrează doar liniile nereconciliate, fără limitare de perioadă, astfel încât totalul afișat să coincidă cu soldul deschis din butonul „Scadent" (evită un total negativ generat de încasări care sting facturi din anul precedent).

**Vizualizări**

- `res_partner_view_form`: extinde formularul de partener (`base.view_partner_form`) cu butoane statistice în `button_box` — „Customer Statement" (situația clientului, evidențiind cu roșu suma restantă) și „Creanțe scadente" (deschide raportul de creanțe îmbătrânite pentru partenerul curent).

#### 5. Conexiuni

Nu au fost identificate conexiuni verificate către alte module documentate în wiki.
