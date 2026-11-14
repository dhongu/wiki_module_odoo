# IAP Server - Odoo Online Services (localizat la `terrabit_iap_server_online/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_online`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_online
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_online`
- **Ultima Ingestie:** `2026-11-14`

#### 1. Sumar

Modulul rulează pe serverul IAP Terrabit logica modulelor „data-only” (fără Python) pe care clienții de pe Odoo Online le importă ca arhivă zip. Modulul din baza de date a clientului trimite cererea, serverul face munca, iar rezultatul este scris înapoi în baza clientului. Astfel, clienții Odoo Online pot beneficia de servicii care altfel ar cere cod pe server, taxate prin creditele IAP.

#### 2. Funcționalități Cheie

- **Două intrări, un singur serviciu**: `/iap_online/<service>` primește acțiunea de server *Send Webhook Notification* a clientului și pune cererea în coadă (webhook-ul renunță după o secundă); `/iap_online/<service>/sync` răspunde imediat butoanelor din formulare (JavaScript, CORS).
- **Răspuns prin callback**: un cron procesează coada și trimite rezultatul către automatizarea *On webhook* din modulul clientului, cu reîncercări.
- **Înregistrare fără copierea cheilor**: modulul clientului se înregistrează singur; tokenul contului ajunge doar la URL-ul de callback, pe gazda bazei clientului, iar contul este legat de acea gazdă. Creditele de probă se acordă o singură dată per bază de date. Contul se leagă de partenerul companiei clientului dacă Codul Fiscal este cunoscut; nu se creează parteneri din aceste date anonime (compania necunoscută rămâne pe cont, pentru verificare).
- **Credite la cerere**: o cerere `balance` returnează creditele rămase, fără taxare; pagina de credite a serverului IAP (`/iap/1/credit`) funcționează și pentru aceste conturi.
- **Credite IAP**: fiecare răspuns rezervă și capturează credite pe cont (`terrabit_iap_server`); o intrare invalidă sau o sursă care nu răspunde nu se taxează. Clientul primește costul (`cost`) și creditele rămase (`balance`).
- **Înregistrare protejată**: limitată per IP și la număr de conturi noi pe oră (credite de probă); un cont existent își păstrează callback-ul cât timp automatizarea *On webhook* există, deci nimeni nu îl poate prelua sau lipsi de răspunsuri (suport: **Reset Online Callback**).
- **Limite și confidențialitate**: cereri pe minut per cont; intrările și răspunsurile se șterg după 30 de zile (tranzacțiile rămân pentru facturare).
- **Un modul per serviciu**: un modul de serviciu (ex. `terrabit_iap_server_online_anaf`) adaugă codul serviciului, bifează **Odoo Online** pe serviciu, setează **Credits per Answer** și implementează `_service_<cod serviciu>(value)`, care întoarce răspunsul și dacă este taxat.
- Baza client, în baza de date a clientului, este modulul data-only [deltatech_iap_online](../deltatech_iap_online/index.md).

#### 3. Dependențe

- [terrabit_iap_server](../terrabit_iap_server/index.md)

#### 4. Componente Cheie

**Modele**

- `iap.online.request`: coada cererilor primite de la clienții Odoo Online (intrare, răspuns, stare, reîncercări).
- `iap.server.account` (extins): URL-ul de callback online, cererile contului, legarea companiei clientului și acțiunea de resetare a callback-ului.
- `iap.server.service` (extins): marcajul **Odoo Online**, creditele per răspuns și dimensiunea maximă a intrării.

**Vizualizări**

- `view_iap_online_request_list`, `view_iap_online_request_form`, `view_iap_online_request_search`: lista, formularul și căutarea cererilor (meniu pe acțiunea `action_iap_online_request`).
- `view_iap_server_account_form`, `view_iap_server_service_form`: extensii ale formularelor de cont și serviciu.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_online_request_process`: procesează coada și trimite răspunsurile prin callback.
- `ir_cron_online_request_cleanup`: șterge cererile vechi (după 30 de zile).

#### 5. Conexiuni

- [deltatech_iap_online](../deltatech_iap_online/index.md): modulul data-only din baza clientului, care trimite cererile.
