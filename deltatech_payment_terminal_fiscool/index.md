# Card Payment Terminal - FisCool

- **Nume Tehnic:** `deltatech_payment_terminal_fiscool`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_payment_terminal_fiscool
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_terminal_fiscool`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaptor pentru [deltatech_payment_terminal](../deltatech_payment_terminal/index.md) care permite încasarea cu cardul pe terminalele conduse de FisCool, driverul local pentru case de marcat fiscale și terminale de card din România. Cererea pleacă din browser către FisCool de pe același calculator, deci funcționează și cu Odoo în cloud. La prima utilizare, FisCool cere operatorului să permită adresa Odoo.

#### 2. Funcționalități Cheie

- **Protocol FisCool pe terminal**: adresa driverului (`http://127.0.0.1:10123`) se completează automat.
- **Alegerea terminalului din FisCool**: butonul **Select in FisCool** listează terminalele de card configurate în driver și completează **Device Reference**, fără copiat UUID.
- **Vânzare, anulare, decontare**: plata facturilor pe terminal, **Void on Terminal** cu RRN și codul de autorizare ale vânzării, **Close the Day**; fluxul este cel din modulul de bază.
- **Fără dublă încasare**: fiecare cerere poartă referința tranzacției ca `Idempotency-Key`; când răspunsul se pierde, tranzacția devine **To verify**, iar reluarea întoarce rezultatul primei execuții.
- **Rezultate clare**: codurile de eroare FisCool sunt mapate pe stările tranzacției: refuzat (fonduri insuficiente, card expirat, PIN greșit), anulat, de verificat (timeout, legătură întreruptă), eroare (dispozitiv indisponibil, operațiune eșuată, pagină nepermisă).
- **Configurare**: instalezi și pornești FisCool pe calculatorul casierului, creezi terminalul cu protocolul **FisCool** în **Invoicing > Configuration > Payment Terminals**, alegi terminalul cu **Select in FisCool** și îl setezi pe utilizatori; terminalele de tip **Simulated** din FisCool servesc la instruire.

Fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_payment_terminal](../deltatech_payment_terminal/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.payment.terminal`: extins cu protocolul FisCool, selecția terminalului și maparea codurilor de eroare.

**Vizualizări**

- `views/payment_terminal_views.xml`: câmpurile FisCool pe formularul terminalului.
- Active JS `fiscool_devices.esm.js` / `fiscool_devices.xml`: fereastra **Card Terminals in FisCool**.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni programate.

#### 5. Conexiuni

- `account`: plățile pe care le generează tranzacțiile card.
