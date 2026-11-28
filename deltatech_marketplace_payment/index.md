# Marketplace Payment Acquirer addon (localizat la `deltatech_marketplace_payment/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_payment`
- **Versiune:** `20.0.0.1.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_payment
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_payment`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă o gestiune dedicată a procesatorilor de plată folosiți în tranzacțiile din marketplace-uri. Permite companiei să urmărească într-un singur loc, în Odoo, metodele de plată întâlnite pe canalele conectate și să le coreleze corect cu contabilitatea, pentru reconciliere financiară precisă și mai puține erori de introducere manuală.

#### 2. Funcționalități Cheie

- Configurarea tuturor procesatorilor de plată din marketplace dintr-o singură interfață Odoo, ca element **Payment Acquirer** în fila **Objects** a backend-ului.
- Mapare între procesatorul din marketplace și un procesator de plată Odoo existent; dacă nu există potrivire, se folosește ca rezervă procesatorul de tip transfer bancar.
- Sincronizarea stării plăților și a detaliilor tranzacțiilor în contabilitate, cu vizibilitate mai bună asupra încasărilor așteptate.
- Opțiuni pe backend pentru confirmarea automată a plății (`confirm_payment`, `confirm_card_payment`).
- Tranzacția de plată păstrează legătura cu backend-ul marketplace; plata contabilă se generează doar dacă procesatorul are jurnal și linie de metodă de plată de tip inbound.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `payment`

#### 4. Componente Cheie

**Modele**

- `marketplace.payment.provider`: legătura (binding) dintre procesatorul de plată Odoo (`payment.provider`) și cel din marketplace; `save_from_marketplace` face maparea.
- `payment.transaction` (extins): leagă tranzacția de backend și controlează `_create_payment` (sare peste procesatorii de tip `custom`, validează jurnalul și metoda de plată inbound).
- `marketplace.backend` (extins): opțiunile `confirm_payment` și `confirm_card_payment`.
- `marketplace.backend.item` (extins): tipul de element `payment_acquirer`, legat de `marketplace.payment.provider` / `payment.provider`.

**Vizualizări**

- `view_marketplace_payment_acquirer_form`, `view_marketplace_payment_acquirer_tree`, `view_marketplace_payment_acquirer_search`: formular, listă și căutare pentru mapările procesatorilor (`action_payment_acquirer`).
- `view_payment_transaction_form`, `view_payment_transaction_list`, `view_payment_transaction_search`: tranzacția de plată cu backend-ul marketplace.
- `view_marketplace_backend_form` (moștenită): opțiunile de confirmare a plății.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_marketplace_opencart](../deltatech_marketplace_opencart/index.md): conector care mapează metodele de plată OpenCart prin acest modul.
- [deltatech_marketplace_prestashop](../deltatech_marketplace_prestashop/index.md): conector care sincronizează metodele de plată PrestaShop prin acest modul.
- [deltatech_marketplace_odoo](../deltatech_marketplace_odoo/index.md): conector Odoo-către-Odoo care depinde de acest modul.
- `payment`: modulul standard Odoo, sursa `payment.provider` și `payment.transaction`.
