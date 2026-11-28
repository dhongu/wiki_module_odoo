# Card Payment Terminal

- **Nume Tehnic:** `deltatech_payment_terminal`
- **Versiune:** `20.0.1.1.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_payment_terminal
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_terminal`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite încasarea facturilor cu cardul pe un terminal de plată, direct din Odoo, și păstrează pe fiecare plată referințele cerute de bancă: RRN, codul de autorizare, numărul mascat al cardului și bonul terminalului. Este baza integrărilor Terrabit cu terminale de card: adaptoarele de protocol (drivere locale, mărci de terminale) sunt module separate. Logica rulează pe serverul Odoo, iar browserul doar transportă cererile către driverul de pe calculatorul casierului, deci funcționează și cu Odoo în cloud. Acoperă facturile plătite la birou de firme (B2B); vânzările către persoane fizice se înregistrează pe casă de marcat fiscală, prin integrarea de Point of Sale.

#### 2. Funcționalități Cheie

- **Plată pe terminal**: în fereastra **Pay** a unei facturi clienți, butonul **Pay on Terminal** trimite suma la terminalul utilizatorului; plata se înregistrează doar după aprobarea băncii, în jurnalul bancar al terminalului (și pentru plăți parțiale).
- **Datele cardului pe plată**: RRN, cod de autorizare, card mascat, marca cardului, ID terminal și bonul, în tabul **Card** al plății.
- **Anulare**: **Void on Terminal** anulează tranzacția și plata, doar înainte de decontare și cât timp plata nu e reconciliată cu extrasul; după decontare banii se returnează printr-o plată de ramburs.
- **Fără dublă încasare**: fiecare tranzacție are o referință unică (cheie de idempotență); o tranzacție cu rezultat necunoscut devine **To verify**, se reia cu aceeași referință sau o rezolvă un manager contabil după verificarea terminalului (**Accounting > Customers > Card Transactions**).
- **Terminal per utilizator**: setat în **Settings > Users > Preferences > Payment Terminal** sau în **My Preferences**.
- **Închiderea zilei**: **Close the Day** rulează decontarea terminalului.
- **Terminal simulat** (fără dispozitiv), pentru instruire și teste: ultimele două cifre ale sumei aleg rezultatul (01 refuzat, 02 fonduri insuficiente, 03 PIN greșit, 04 anulat de client, 05 rezultat necunoscut), plus panoul **Virtual devices**.
- **Configurare**: **Invoicing > Configuration > Payment Terminals** (nume, protocol, jurnal bancar, metodă de plată opțională; pentru drivere locale, **Device Reference** și **Local Driver URL**).
- **Contabilitate România**: banii ajung în bancă la decontare, deci recomandarea este jurnal bancar pe 5121 și contul de încasări în curs al metodei de plată pe un analitic de 5125 (de ex. 512501); la extras: Dr 5121 (net) + Dr 627 (comision) = Cr 5125 (brut). Nu se postează încasările card direct pe 5121.

Fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `deltatech.payment.terminal`: terminalul (protocol, jurnal, metodă de plată, închiderea zilei).
- `deltatech.payment.terminal.transaction`: tranzacția cu cardul, cu stările ei (așteptare, aprobată, refuzată, de verificat etc.).
- `deltatech.payment.terminal.mixin`: logica comună a protocoalelor, folosită și de plată.
- `account.payment`: extins cu tabul **Card** și **Void on Terminal**.
- `account.payment.register` (wizard): butonul **Pay on Terminal**.
- `res.users`: terminalul implicit al utilizatorului.
- `ir.http`: sprijin pentru comunicarea cu driverul local.
- Protocol simulat (`payment_terminal_simulated`): extinde `deltatech.payment.terminal`.

**Vizualizări**

- `views/payment_terminal_views.xml`: formularul și lista terminalelor.
- `views/payment_terminal_transaction_views.xml`: tranzacțiile card.
- `views/account_payment_views.xml`: tabul Card pe plată.
- `wizard/account_payment_register_views.xml`: fereastra de plată a facturii.
- `views/res_users_views.xml`: terminalul în preferințele utilizatorului.
- `menu_payment_terminal` (Payment Terminals) și `menu_payment_terminal_transaction` (Card Transactions).

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni programate.

#### 5. Conexiuni

- [deltatech_payment_terminal_fiscool](../deltatech_payment_terminal_fiscool/index.md): adaptor pentru driverul local FisCool.
- `account`: plățile și reconcilierea cu extrasul bancar.
