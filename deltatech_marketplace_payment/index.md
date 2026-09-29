# Marketplace Payment Acquirer addon (localizat la `deltatech_marketplace_payment/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_payment`
- **Versiune:** `19.0.0.1.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_payment
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_payment`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Acest modul oferă un sistem dedicat de gestionare a procesatorilor de plată (payment acquirers) pentru tranzacțiile din marketplace-uri, asigurând o reconciliere financiară corectă și eficientă pentru vânzările omnichannel. Din perspectivă de business, permite companiilor să gestioneze o gamă largă de metode de plată folosite pe diferitele platforme de marketplace, păstrând totodată o vizualizare centralizată a plăților în Odoo.

#### 2. Funcționalități Cheie

- **Gestionare unificată a plăților:** Configurarea și administrarea tuturor procesatorilor de plată asociați marketplace-urilor dintr-o singură interfață Odoo.
- **Reconciliere financiară fluidă:** Sincronizarea automată a statusului plăților și a detaliilor tranzacțiilor din marketplace-uri în modulul de contabilitate Odoo.
- **Vizibilitate îmbunătățită a fluxului de numerar:** Urmărirea și gestionarea cu mai mare acuratețe a plăților și decontărilor așteptate din marketplace-uri.
- **Încredere sporită a clienților:** Asigurarea unei procesări consecvente a plăților și a actualizărilor de status pe toate canalele de marketplace conectate.
- **Reducerea erorilor:** Minimizarea introducerii manuale a datelor și a erorilor prin automatizarea procesului de sincronizare a plăților.
- **Cod de plată extern păstrat pe tranzacție:** Câmpul `external_payment_code` reține codul exact raportat de marketplace (ex. `shopify_payments`, `stripe`, `paypal`, `Cash on Delivery (COD)`), deoarece maparea pe un furnizor Odoo este cu pierdere. Se completează la crearea plății din comanda importată (`deltatech_marketplace_sale`); tranzacțiile istorice nu pot fi recuperate.
- **Raportare pe canal și metodă de plată:** Backend-ul de origine și codul extern apar pe formularul, lista (opționale) și căutarea tranzacțiilor și permit gruparea, pentru a vedea cât s-a încasat prin fiecare gateway.
- **Mapări create automat:** Rândul de mapare se creează la prima comandă importată cu un cod de plată nou (nu există import manual); consultantul îl corectează ulterior din formular. Bifa `confirm_payment` de pe mapare decide dacă tranzacția rămâne în așteptare (util la ramburs) sau este trecută direct pe Done.
- **Dependență, nu produs de sine stătător:** Modulul este marcat „Hidden" (preț simbolic 10 EUR) și este tras de conectoarele de marketplace.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `payment`

#### 4. Componente Cheie

**Modele**

- `marketplace.payment.provider`: Model de legătură (binding) între procesatorul de plată Odoo (`payment.provider`) și procesatorul de plată al marketplace-ului. Moștenește `marketplace.binding` și folosește `_inherits` către `payment.provider`. Conține metoda `save_from_marketplace`, care mapează procesatorul din marketplace la unul existent în Odoo (sau, ca fallback, la procesatorul de tip transfer bancar).
- `payment.transaction` (extins): Suprascrie `_create_payment` pentru a controla crearea plăților contabile — sare peste procesatorii de tip `custom` și validează existența unui jurnal și a unei linii de metodă de plată de tip inbound asociată procesatorului înainte de a genera `account.payment`.
- `payment.transaction` (câmpuri noi): `marketplace_backend_id` (Many2one către `marketplace.backend`, indexat, doar citire) și `external_payment_code` (Char, indexat, doar citire).
- `marketplace.backend` (extins): Adaugă câmpurile `confirm_payment` și `confirm_card_payment` (implicit bifate); nu apar în vederi și nu sunt citite de alt cod din suită.
- `marketplace.backend.item` (extins): Adaugă tipul de element `payment_acquirer` (cu pictogramă card de credit) și mapează acest tip la modelul de binding `marketplace.payment.provider` / modelul Odoo `payment.provider`.

**Vizualizări**

- `view_marketplace_payment_acquirer_form`: Formularul procesatorului de plată din marketplace, cu butoanele de acțiune `Reimport` și `Delete`.
- `view_marketplace_payment_acquirer_tree`: Lista procesatorilor de plată asociați marketplace-urilor.
- `view_marketplace_payment_acquirer_search`: Vizualizarea de căutare/filtrare după nume, identificator extern și backend.
- Moșteniri ale vederilor `payment.transaction` (formular, listă, căutare): afișează `marketplace_backend_id` și `external_payment_code`, cu filtre de grupare după ambele.
- `action_payment_acquirer`: Acțiunea de fereastră pentru deschiderea listei și formularului de procesatori de plată.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server (`ir.actions.server`).

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): Modul de bază pentru integrarea cu marketplace-uri; furnizează modelele `marketplace.binding`, `marketplace.backend` și `marketplace.backend.item` pe care acest addon le extinde pentru a gestiona procesatorii de plată.
- `payment`: Modulul standard Odoo de plăți; furnizează `payment.provider` și `payment.transaction`, modelele pe care acest addon le leagă de procesatorii din marketplace.
