# Eu Platesc Payment Provider (localizat la `deltatech_payment_eu_platesc/index.md`)

- **Nume Tehnic:** `deltatech_payment_eu_platesc`
- **Versiune:** `19.0.0.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_eu_platesc
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_eu_platesc`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul conectează Odoo cu EuPlătesc, un procesator de plăți românesc de top, permițând afacerilor să accepte plăți online cu carduri de credit și debit (Visa, Mastercard) atât pentru comenzile din eCommerce, cât și pentru facturile din portalul de client. Oferă clienților din România o experiență de plată sigură și familiară, iar echipei de contabilitate îi reduce munca de reconciliere manuală prin actualizarea automată a stării plăților.

#### 2. Funcționalități Cheie

- Oferă opțiunea „Pay with card (EuPlatesc)” ca metodă de plată în timpul finalizării comenzii în Odoo eCommerce.
- Permite clienților să plătească facturile restante direct din portalul de client Odoo.
- Actualizează automat starea comenzilor de vânzare și a facturilor pe baza răspunsului în timp real primit de la EuPlătesc.
- Folosește notificări securizate server-to-server (S2S) prin URL-uri „silent” (callback), astfel încât starea plății se actualizează corect chiar dacă sesiunea browserului clientului este întreruptă.
- Flux prin redirecționare securizată: la checkout, Odoo generează o cerere semnată cu un cod MAC unic, clientul introduce datele cardului direct pe pagina securizată EuPlătesc, iar la finalizare este redirecționat înapoi în Odoo (Success URL), în paralel cu notificarea asincronă (Silent URL) care confirmă tranzacția.
- Suportă atât Modul de Test cât și Modul Live (producție), configurabile din fișa procesatorului de plăți.
- Verificarea integrității datelor prin semnătură HMAC-MD5, datele cardului nefiind niciodată stocate sau procesate în Odoo (conformitate PCI).

#### 3. Dependențe

- `payment`

#### 4. Componente Cheie

Documentația de business pentru acest modul provine din `readme/DESCRIPTION.md`, conform fluxului de ingestie. Componentele tehnice detaliate (modele, vizualizări, acțiuni) nu sunt enumerate exhaustiv aici, deoarece Readme-ul acoperă scopul și funcționalitățile fără a impune analiza codului. Pe scurt, modulul extinde framework-ul standard de plăți Odoo (`payment`) cu un procesator („provider”) dedicat EuPlătesc și un controller web pentru punctele terminale de callback S2S și de retur al clientului.

- `payment.provider` (extins): adaugă opțiunea `eu_platesc` la selecția `code`, împreună cu câmpurile de configurare `eu_platesc_mid` (Merchant ID) și `eu_platesc_key` (cheie secretă), plus logica de generare a semnăturii MAC (HMAC-MD5) și determinarea URL-ului de acțiune al formularului (test/producție).
- `payment.transaction` (extins): gestionează crearea valorilor de plată specifice EuPlătesc și procesarea notificărilor primite (feedback de la procesator, actualizarea stării tranzacției).
- `account.payment.method`: date de configurare pentru metoda de plată asociată.
- Controller (`/payment/eu_platesc/callbacks2s/<int:provider_id>`): endpoint public pentru notificarea IPN (server-to-server) trimisă de EuPlătesc.
- Controller (`/payment/eu_platesc/success/<int:provider_id>/<string:ref>`): endpoint de retur al clientului după finalizarea plății, care redirecționează către pagina standard `/payment/status`.

#### 5. Conexiuni

- `payment`: framework-ul standard Odoo de procesatori de plăți, pe care acest modul îl extinde cu procesorul EuPlătesc.
- `website_sale`: modulul de eCommerce Odoo, prin care metoda de plată EuPlătesc devine disponibilă la checkout (integrare funcțională, nu dependență declarată în manifest).
