# IAP Server (localizat la `terrabit_iap_server/index.md`)

- **Nume Tehnic:** `terrabit_iap_server`
- **Versiune:** `20.0.0.5.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_iap_server
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Implementează funcționalitatea de server IAP (In-App Purchase) a Terrabit: bazele de date client se înregistrează aici, iar serverul ține evidența serviciilor, conturilor, portofelelor și creditelor lor. Clienții își văd și completează creditele dintr-o pagină publică și din portalul `/my/iap`. DESCRIPTION.md conține doar un titlu gol, deci pagina e sintetizată din cod, HISTORY și manifest.

#### 2. Funcționalități Cheie

- **Servicii IAP** (`iap.server.service`): nume, unitate, credite inițiale gratuite, credite comune între servicii, **Wallet Rate** (EUR per unitate) și valabilitatea creditelor.
- **Înregistrarea conturilor**: ruta `/iap/register` creează contul unei baze client; ruta `/iap/services-token` și `/iap/1/get-accounts-information` returnează conturile.
- **Protocol IAP standard**: rutele `/iap/1/authorize`, `/iap/1/capture`, `/iap/1/cancel` și `/iap/1/balance` rezervă, consumă și anulează credite.
- **Portofel comun per bază de date**: un cont înregistrat intră în portofelul bazei sale după ce serverul verifică, prin `/iap/get_info`, că baza deține tokenul contului; verificarea rulează la deschiderea paginii de credite, zilnic prin cron și din butonul **Link Wallet**.
- **Tranzacții și registru**: `iap.server.transaction` reține încărcările (cumpărate, gratuite, ajustări) și consumurile.
- **Expirarea creditelor**: o achiziție prelungește valabilitatea creditelor neconsumate (12 luni de la ultima achiziție); creditele expirate rămân expirate.
- **Pagina de credite și portal**: `/iap/1/credit`, `/iap/<serviciu>/account`, `/my/iap` și `/my/iap/<id>/buy`, cu intrare în portalul clientului.
- **Securitate**: secret de callback per cont, tokenul brut al contului nu apare în portal, reguli de acces în `ir.access.csv`.
- **Roadmap**: achiziția de credite prin eCommerce este implementată în `terrabit_iap_server_sale`.

#### 3. Dependențe

- `iap`
- [terrabit_iap](../terrabit_iap/index.md)
- `website`
- `portal`
- Python extern: `json2html`

#### 4. Componente Cheie

**Modele**

- `iap.server.service`: serviciul oferit clienților, cu prețuri și reguli de credite.
- `iap.server.account`: contul unei baze client la un serviciu.
- `iap.server.wallet`: portofelul comun al unei baze (UUID, URL de bază, credite, sold, următoarea expirare).
- `iap.server.transaction`: tranzacțiile de credit (rezervare, captură, anulare).

**Vizualizări**

- `view_iap_server_service_form` / `_tree`: servicii.
- `view_iap_server_account_form` / `_tree`: conturi înregistrate.
- `view_iap_server_wallet_form` / `_tree`: portofele.
- `view_iap_server_transaction_form` / `_tree`: tranzacții.
- `views/iap_templates.xml`, `views/iap_portal_templates.xml`: paginile publice de credite și portalul.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_cancel_expired_transactions`: anulează tranzacțiile rezervate care au expirat.
- `ir_cron_expire_credits`: expiră creditele peste ultima zi valabilă.
- `ir_cron_link_wallets`: leagă conturile de portofelul bazei (50 de conturi pe rulare).

#### 5. Conexiuni

- [terrabit_iap](../terrabit_iap/index.md): clientul IAP care comunică cu acest server.
- [terrabit_iap_server_sale](../terrabit_iap_server_sale/index.md): achiziția de credite prin eCommerce.
- [terrabit_iap_server_helpdesk](../terrabit_iap_server_helpdesk/index.md): serviciu construit pe serverul IAP.
- [terrabit_iap_server_anaf](../terrabit_iap_server_anaf/index.md): serviciul de token ANAF.
- [terrabit_iap_server_ai](../terrabit_iap_server_ai/index.md): serviciul AI.
- [terrabit_iap_line_counter](../terrabit_iap_line_counter/index.md): serviciu de numărare a liniilor de cod.
