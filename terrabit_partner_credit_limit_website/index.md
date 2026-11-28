# Partner Credit Limit Website (localizat la `terrabit_partner_credit_limit_website/index.md`)

- **Nume Tehnic:** `terrabit_partner_credit_limit_website`
- **Versiune:** `20.0.0.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/terrabit_partner_credit_limit_website
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_credit_limit_website`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde controlul limitei de credit pe partener către magazinul online, astfel încât politica de credit să fie aplicată la fel pe toate canalele de vânzare. La checkout, clientul autentificat vede un rezumat al soldului față de limită, iar dacă limita e depășită sau există facturi restante, metodele de plată „pe încredere" sunt eliminate.

#### 2. Funcționalități Cheie

- **Restricționarea metodelor de plată:** la depășirea limitei sau la facturi restante se elimină metodele amânate (transfer bancar, numerar la livrare), rămânând cele online; opțional se elimină toate.
- **Setare unică „Restrict All Providers":** în *Pagină web > Configurare > Setări*, secțiunea eCommerce; bifată, la depășire dispar toate metodele de plată (clientul e blocat la checkout până își rezolvă soldul).
- **Rezumat pe pagina de plată:** bară de progres (valoarea comenzii față de limită, umplută după sold + comandă) și soldul curent.
- **Alertă de facturi restante:** casetă roșie cu suma restantă și documentele, plus telefonul contabilității (din setările modulului de bază) pentru clarificări.
- **Aceeași logică ca în backend:** folosește calculul din `terrabit_partner_credit_limit` (toleranță, termen imediat, clienți fără limită etc.).

Pașii și capturile sunt în [Fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md)
- `website_sale`
- `payment_custom`

#### 4. Componente Cheie

**Modele**

- `payment.provider`: filtrează furnizorii disponibili la checkout (`_find_available_providers`) când limita e depășită.
- `res.config.settings`: setarea „Restrict All Providers".

**Vizualizări**

- `views/templates.xml`: blocul cu bara de progres, soldul și alerta de restanțe pe pagina de plată.
- `views/res_config_settings_views.xml`: setarea în configurarea website-ului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md) (dependență): calculul limitei și al restanței.
- `website_sale`: șabloanele de checkout extinse.
- `payment_custom`: furnizorii de plată personalizați (transfer bancar) vizați de restricție.
