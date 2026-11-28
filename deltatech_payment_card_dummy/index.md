# Card Dummy Payment (localizat la `deltatech_payment_card_dummy/index.md`)

- **Nume Tehnic:** `deltatech_payment_card_dummy`
- **Versiune:** `20.0.0.0.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_payment_card_dummy
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_card_dummy`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un furnizor de plată cu cardul „simulat”, destinat testării fluxului comandă–plată sau înregistrării rapide a plăților făcute pe un terminal extern, fără integrare bancară directă. La checkout, tranzacția este creată și marcată imediat ca reușită, iar comanda sau factura se actualizează automat. Nu cere chei API sau credențiale. Se folosește doar pe o bază de test sau staging: pe un magazin live, orice vizitator care alege metoda marchează comanda ca plătită fără să plătească.

#### 2. Funcționalități Cheie

- Simulează plata cu cardul în procesul de finalizare a comenzii din eCommerce, fără date reale de card.
- Permite înregistrarea plăților cu cardul pentru facturile din portal.
- Tranzacția este confirmată dintr-un singur pas (fără autorizare, refuz sau rambursare); pentru aceste scenarii se folosește furnizorul standard **Demo** (`payment_demo`).
- Configurare minimă: furnizorul **Card Dummy** este creat în mod test, se alege **Payment Journal** (jurnal de tip bancă pentru teste) și se publică furnizorul (**Invoicing → Configuration → Online Payments → Payment Providers**).
- În Odoo 20, un coș cu bunuri nu ajunge la pasul **Payment** fără o metodă de livrare publicată (poate fi gratuită).
- Comanda devine imediat **Sales Order**, iar plata se înregistrează în jurnalul ales (debit conturi de încasări în curs, credit creanță client).
- Fluxul pas-cu-pas, cu capturi, este în [Fișa Consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `payment`
- `sale`
- `payment_custom`

#### 4. Componente Cheie

Documentația provine din `readme/DESCRIPTION.md`, conform fluxului de ingestie. Pe scurt, modulul extinde framework-ul de plăți cu un furnizor dedicat (`models/payment_provider.py`, `models/payment_transaction.py`), plus extensii pentru `account.move` și `sale.order`, controller pentru confirmare și date inițiale pentru furnizor și metoda de plată (`payment_provider_card_dummy`, `payment_method_card_dummy`).

#### 5. Conexiuni

- `payment`: framework-ul standard Odoo de furnizori de plăți, extins cu furnizorul Card Dummy.
- `sale`: comenzile de vânzare sunt confirmate automat după plata simulată.
- `payment_custom`: modul standard Odoo de la care provine mecanismul de plată simplificat.
