# Vânzare din magazin - Plată cu cardul pe terminal (Sale from Store - Card Payment Terminal)

- **Nume Tehnic:** `deltatech_sale_store_payment_terminal`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_sale_store_payment_terminal
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_store_payment_terminal`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul leagă fluxul *Vânzare din magazin* de terminalele de card ale modulului *Card Payment Terminal*. Casierul încasează pe terminal, iar marfa este livrată, factura (sau bonul) postată și plata înregistrată abia după aprobarea băncii; cu card refuzat nu se livrează și nu se facturează nimic. Se instalează automat când ambele module sunt prezente (`auto_install`).

#### 2. Funcționalități Cheie

- **Plătește pe terminal:** în fereastra *Vânzare din magazin*, alegerea jurnalului terminalului de card înlocuiește butonul *Tipărește* cu *Plătește pe terminal*; suma este trimisă terminalului.
- **Stoc verificat înaintea cardului:** comanda este confirmată și marfa rezervată înainte de încasare; lipsa stocului oprește vânzarea fără a taxa clientul.
- **Bon fiscal după aprobare:** la închiderea ferestrei terminalului, bonul fiscal al facturii este trimis la casa de marcat, cu plata pe jurnalul cardului (se configurează *Cod ECR* pe jurnal).
- **Card refuzat:** nimic nu se livrează sau facturează; comanda rămâne confirmată și rezervată, iar *Vânzare din magazin* rămâne disponibil până la facturare, pentru reîncasare pe terminal sau cu altă metodă.
- **Fără dublă taxare:** o comandă cu plată cu cardul în curs, de verificat sau aprobată nu poate porni alta; o tranzacție de verificat este reluată cu aceeași referință.
- **Aprobat, dar nelivrat:** dacă după aprobare marfa nu mai poate fi livrată, încasarea rămâne pe tranzacție cu cauza, iar *Creează plata* încheie vânzarea după remedierea cauzei, fără a taxa din nou cardul.
- **Plăți cu cardul** pe comandă: buton inteligent către tranzacțiile cu cardul ale comenzii.
- **Configurare:** terminalul și jurnalul în *Contabilitate > Configurare > Terminale de plată*, terminalul setat pe utilizatorul casierului, *Cod ECR* pe jurnal, iar jurnalul terminalului adăugat în *Jurnale* pe utilizator dacă acestea sunt restricționate. Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_sale_store](../deltatech_sale_store/index.md)
- [deltatech_payment_terminal](../deltatech_payment_terminal/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.payment.terminal.transaction` (extins): legătura cu comanda din magazin (`sale_store_order_id`), finalizarea vânzării după aprobare (`_on_approved`, `_create_payment`, `_sale_store_finish`).
- `sale.order` (extins): tranzacțiile cu cardul și contorul lor, `action_view_payment_terminal_transactions`.
- `sale.store` (extins): setările vânzării din magazin pentru plata pe terminal.

**Vizualizări**

- `sale_order_views.xml`: butonul inteligent *Plăți cu cardul*.
- `payment_terminal_transaction_views.xml`: câmpurile și butoanele tranzacției (magazin, plată, *Creează plata*).
- `sale_store_views.xml`: fereastra *Confirmă vânzarea* cu *Plătește pe terminal*.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_payment_terminal_fiscool](../deltatech_payment_terminal_fiscool/index.md): protocol de terminal care se conectează la modulul de bază.
