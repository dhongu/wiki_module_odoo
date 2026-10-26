# EuPlatesc.ro Payment (localizat la `deltatech_payment_eu_platesc/index.md`)

- **Nume Tehnic:** `deltatech_payment_eu_platesc`
- **Versiune:** `19.0.0.1.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_eu_platesc
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_eu_platesc`
- **Ultima Ingestie:** `2026-10-26`

#### 1. Sumar

Acest modul conectează Odoo cu EuPlătesc, un procesator de plăți românesc, permițând afacerilor să accepte plăți online cu carduri Visa și Mastercard atât pentru comenzile din eCommerce, cât și pentru facturile din portalul de client. Oferă clienților din România o experiență de plată sigură și familiară, iar echipei de contabilitate îi reduce munca de reconciliere manuală prin actualizarea automată a stării plăților. Necesită un cont de comerciant EuPlatesc.ro activ, cu Merchant ID și cheie.

#### 2. Funcționalități Cheie

- Oferă EuPlatesc.ro ca metodă de plată la finalizarea comenzii în Odoo eCommerce; clientul plătește pe pagina securizată EuPlatesc.ro, iar datele cardului nu ajung niciodată în Odoo.
- Permite clienților să plătească facturile deschise direct din portalul de client Odoo, cu butonul **Pay Now**.
- Captură imediată: cardul este debitat într-un singur pas, iar comanda sau factura este marcată ca plătită.
- Actualizează automat starea comenzilor de vânzare și a facturilor pe baza răspunsului primit de la EuPlătesc.
- Confirmare în fundal prin notificare server-to-server (URL „silent"), astfel încât starea plății se actualizează corect chiar dacă clientul închide browserul; clientul este redirecționat înapoi în Odoo (Success URL), spre pagina standard `/payment/status`.
- Mesajele sunt semnate cu cheia comerciantului (HMAC-MD5): un răspuns nesemnat sau semnat greșit este respins, iar suma și moneda se verifică față de tranzacție.
- Configurare: **Facturare → Configurare → Procesatori de plăți → EuPlatesc.ro**; se introduc Merchant ID și cheia, se alege jurnalul în care se înregistrează plățile, apoi starea se setează pe Activat și procesatorul se publică pe site. Adresele de întoarcere și de notificare sunt trimise de Odoo către EuPlatesc.ro la fiecare plată. Pentru teste înainte de producție se folosește un cont de comerciant de test de la EuPlatesc.ro.

#### 3. Dependențe

- `account`
- `payment`

#### 4. Componente Cheie

**Modele**

- `payment.provider` (extins): adaugă opțiunea `eu_platesc` la selecția `code`, câmpurile `eu_platesc_mid` (Merchant ID) și `eu_platesc_key` (cheie), calculul semnăturii MAC (`eu_platesc_mac`), verificarea semnăturii `fp_hash` a răspunsului și URL-ul de acțiune al formularului.
- `payment.transaction` (extins): gestionează valorile de plată specifice EuPlătesc și procesarea notificărilor primite.
- `account.payment.method` (extins): metoda de plată asociată.

**Vizualizări**

- `views/payment_views.xml`: câmpurile procesatorului în formularul de configurare.
- `views/payment_templates.xml`: formularul de redirecționare către EuPlatesc.ro.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` / `uninstall_hook`: configurează, respectiv resetează procesatorul `eu_platesc` la instalare și dezinstalare.
- Controller `/payment/eu_platesc/callbacks2s/<int:provider_id>`: endpoint public (POST) pentru notificarea server-to-server; cere semnătură validă, altfel întoarce Forbidden.
- Controller `/payment/eu_platesc/success/<int:provider_id>/<string:ref>`: endpoint de retur al clientului, care procesează doar date semnate și redirecționează către `/payment/status`.
- `data/payment_method_data.xml` și `data/payment_acquirer_data.xml`: metoda de plată și înregistrarea procesatorului EuPlatesc.ro.

#### 5. Conexiuni

- `payment`: framework-ul standard Odoo de procesatori de plăți, pe care acest modul îl extinde cu procesatorul EuPlătesc.
- `website_sale`: modulul de eCommerce Odoo, prin care metoda de plată EuPlătesc devine disponibilă la checkout (integrare funcțională, nu dependență declarată în manifest).
- [deltatech_account_bank_statement_import_euplatesc](../deltatech_account_bank_statement_import_euplatesc/index.md): modul înrudit, pentru importul extraselor EuPlatesc.
