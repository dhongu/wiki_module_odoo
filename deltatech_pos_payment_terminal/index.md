# POS Card Payment Terminal (localizat la `deltatech_pos_payment_terminal/index.md`)

- **Nume Tehnic:** `deltatech_pos_payment_terminal`
- **Versiune:** `20.0.1.1.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_pos_payment_terminal
- **Cale Locală:** `odoo-addons/bitshop/deltatech_pos_payment_terminal`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite plata cu cardul în Point of Sale pe terminalele de card Terrabit din modulul [deltatech_payment_terminal](../deltatech_payment_terminal/index.md): simulat, FisCool și celelalte protocoale conectate la el. Suma ajunge la terminal, iar linia de plată devine plătită doar după aprobarea băncii; datele cardului (RRN, cod de autorizare) rămân pe plată.

#### 2. Funcționalități Cheie

- **Metodă de plată de tip Terrabit Card Terminal**: selectată pe ecranul de plată, trimite suma la terminalul punctului de vânzare.
- **Terminal per punct de vânzare**: câmpul *Card Terminal* în setările POS (*Point of Sale → Configuration → Settings*, secțiunea *Payment*). Cu *Automatically validate order*, comanda se validează imediat după aprobarea cardului.
- **Date card pe plata POS**: RRN, cod de autorizare, tip card și bonul terminalului se copiază pe plată la sincronizarea comenzii; bonul terminalului se tipărește pe bonul POS.
- **Fără dublă încasare la Retry**: referința tranzacției rămâne pe linia de plată; *Retry* pe o linie cu rezultat necunoscut reia aceeași tranzacție, inclusiv după reîncărcarea POS.
- **Plățile forțate rămân vizibile**: o linie forțată fără tranzacție aprobată nu primește date de card și iese în evidență în back office.
- **Card Transactions**: fiecare plată POS cu cardul este o tranzacție, cu punctul de vânzare și comanda, alături de plățile facturilor.
- Configurare: terminalul în *Invoicing → Configuration → Payment Terminals*; metoda de plată POS cu *Integration* = *Terminal* și *Integrate with* = *Terrabit Card Terminal*, cu jurnal bancar și cont de încasări în curs. Pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- `point_of_sale`
- [deltatech_payment_terminal](../deltatech_payment_terminal/index.md)

#### 4. Componente Cheie

**Modele**

- `pos.payment` (extins, cu `deltatech.payment.terminal.mixin`): datele cardului pe plata POS.
- `pos.payment.method`: integrarea cu *Terrabit Card Terminal*.
- `pos.config`, `res.config.settings`: terminalul de card al punctului de vânzare.
- `deltatech.payment.terminal.transaction` (extins): legătura tranzacției cu POS și comanda.

**Vizualizări**

- `view_pos_payment_form`: datele cardului pe plata POS.
- `view_payment_terminal_transaction_form`: punctul de vânzare și comanda pe tranzacție.
- `res_config_settings_view_form`: câmpul *Card Terminal* în setările POS.
- Front-end POS: `static/src/app/payment_tb_terminal.esm.js` (interfața de plată, cu releul și terminalul virtual din `deltatech_payment_terminal`).

**Acțiuni Automate / Acțiuni Server**

- Nu are sarcini cron sau acțiuni server.

#### 5. Conexiuni

- [deltatech_payment_terminal_fiscool](../deltatech_payment_terminal_fiscool/index.md): protocolul FisCool, utilizabil prin același terminal.
- [deltatech_pos_payment_correction](../deltatech_pos_payment_correction/index.md): plățile pe terminal nu pot fi corectate.
