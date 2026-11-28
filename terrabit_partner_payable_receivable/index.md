# Payable and Receivable in Partner Form (localizat la `terrabit_partner_payable_receivable/index.md`)

- **Nume Tehnic:** `terrabit_partner_payable_receivable`
- **Versiune:** `20.0.1.2.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/terrabit_partner_payable_receivable
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_payable_receivable`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă pe fișa partenerului și pe comanda de vânzare o vedere clară a sumelor de încasat și de plătit, plus a avansurilor facturate, direct în locurile în care se iau decizii comerciale. Echipele de vânzări și de contabilitate văd imediat situația financiară a unui partener înainte de o decizie comercială. Modulul doar informează, nu blochează și nu generează note contabile.

#### 2. Funcționalități Cheie

- **Vizibilitate în timp real:** soldul de încasat al firmei și data celei mai vechi poziții deschise, într-un banner galben pe comanda de vânzare (și pe comenzile făcute pe un contact al firmei, soldul fiind al firmei).
- **Avansuri pe fișa partenerului:** în tabul *Vânzări & Achiziții*, **Deposit Customer** (avans client, ex. 419) și **Deposit Vendor** (avans furnizor, ex. 409), cu un buton **View** care deschide liniile contabile din spatele sumei. Avansul se arată fără TVA.
- **Grupuri de conturi pentru avans:** configurate în *Facturare > Configurare > Setări*; dacă nu sunt alese ambele, se folosesc conturile 419%, respectiv 409%. Pe o bază nouă trebuie setat și **Cont plată în avans** (setarea nativă) pe 419.
- **Deducere avans:** în fereastra *Creează factură/facturi* apare opțiunea **Deducere avans** (bifată implicit, doar la factura normală, pentru o singură comandă), care scade avansurile deja facturate din factura finală.
- **Portal:** sub conținutul paginilor, clientul autentificat vede soldurile deschise ale firmei sale.
- **Evaluare de credit:** identifici rapid partenerii cu solduri deschise; modulul stă la baza controlului de limită de credit din `terrabit_partner_credit_limit`.

Fluxul pas-cu-pas, cu capturi, este în [Fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `sale_management`

#### 4. Componente Cheie

**Modele**

- `res.partner`: câmpuri calculate pentru soldul de încasat/de plătit din liniile contabile postate și nereconciliate, `receivable_date` și avansurile client/furnizor.
- `res.company` / `res.config.settings`: configurarea grupurilor de conturi de avans (`account_group_deposit_customer_id`, `account_group_deposit_vendor_id`).
- `sale.order`: datele pentru bannerul de sold.
- `sale.advance.payment.inv` (wizard): opțiunea **Deducere avans**.

**Vizualizări**

- `views/res_partner.xml`: sumele de avans și butoanele **View** pe fișa partenerului.
- `views/sale_view.xml`: bannerul de sold pe comanda de vânzare.
- `views/templates.xml`: soldurile afișate în portal.
- `views/res_config_settings_views.xml`: grupurile de conturi de avans.
- `wizard/sale_make_invoice_advance.xml`: opțiunea **Deducere avans** în fereastra de facturare.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md): depinde de acest modul; folosește soldul din comandă pentru controlul limitei de credit.
