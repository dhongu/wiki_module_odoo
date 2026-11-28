# POS Payment Method Correction (localizat la `deltatech_pos_payment_correction/index.md`)

- **Nume Tehnic:** `deltatech_pos_payment_correction`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_pos_payment_correction
- **Cale Locală:** `odoo-addons/bitshop/deltatech_pos_payment_correction`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite corectarea metodei de plată a unei comenzi POS deja plătite, atunci când casierul a apăsat butonul greșit (de exemplu numerar în loc de card), fără diferențe de casă la închidere și fără a pierde urma cine a modificat ce. Corectarea devine o operațiune controlată: doar de către manager, cu motiv obligatoriu și cu jurnal de audit, în locul editării libere și fără urmă din Odoo standard.

#### 2. Funcționalități Cheie

- **Doar managerul**: în backend administratorii POS, pe ecranul POS casierul cu rol de manager. Casierii nu mai modifică plățile unei comenzi plătite.
- **Din comandă sau din casă**: butonul *Correct Payment Method* pe formularul comenzii, respectiv *Correct Payment* în lista de comenzi din ecranul POS.
- **Motiv obligatoriu**: fiecare corecție păstrează metoda veche și cea nouă, suma, utilizatorul, casierul și motivul.
- **Jurnal de audit**: *Point of Sale → Reporting → Payment Corrections* (doar citire), cu buton inteligent pe comandă și notă în chatter.
- **Închiderea urmează corecția**: numerarul așteptat și notele contabile de închidere folosesc metoda corectată, deoarece sesiunea este încă deschisă.
- **Doar cazuri sigure**: comenzile facturate, sesiunile închise, comenzile cu rest, plățile pe contul clientului, terminalele de plată și numerarul cu rotunjire sunt refuzate cu mesaj clar.
- **Avertisment extensibil**: un hook afișează un avertisment înainte de corecție, folosit de localizări (de exemplu puntea către bonul fiscal).
- Configurare: grupul *Point of Sale > Administrator* pentru utilizatorii autorizați; cu `pos_hr`, rolul de manager și PIN-ul pe fișa angajatului. Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `pos.payment.correction`: jurnalul corecțiilor (metodă veche/nouă, sumă, utilizator, casier, motiv).
- `pos.payment.correction.wizard`: dialogul de corecție (plată, metodă nouă, motiv).
- `pos.order`, `pos.payment` (extinse): acțiunea de corecție, butonul inteligent și legătura cu jurnalul.

**Vizualizări**

- `view_pos_pos_form`: butonul de corecție și butonul inteligent pe comanda POS.
- `view_pos_payment_correction_wizard_form`: dialogul de corecție.
- `view_pos_payment_correction_list` / `_form` / `_search`: jurnalul corecțiilor.
- Front-end POS (`static/src/pos`): `ticket_screen` și `pos_store` adaugă *Correct Payment* în lista de comenzi.

**Acțiuni Automate / Acțiuni Server**

- `action_pos_payment_correction`: acțiunea de fereastră din meniul *Reporting → Payment Corrections*. Nu are sarcini cron.

#### 5. Conexiuni

- `pos_hr`: rolul de manager și PIN-ul angajatului pentru corecția de la casă.
- [deltatech_pos_payment_terminal](../deltatech_pos_payment_terminal/index.md): plățile pe terminal nu pot fi corectate.
