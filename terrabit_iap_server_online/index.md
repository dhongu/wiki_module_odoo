# IAP Server - Odoo Online Services (localizat la `terrabit_iap_server_online/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_online`
- **Versiune:** `20.0.1.4.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_iap_server_online
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Rulează pe serverul IAP Terrabit logica modulelor „data-only” pe care clienții de pe Odoo Online le importă ca arhivă zip, fără Python. Modulul din baza clientului trimite cererea, serverul face munca, iar rezultatul este scris înapoi în baza clientului. Astfel clienții Odoo Online pot folosi servicii Terrabit (de exemplu interogări ANAF) cu credite și facturare.

#### 2. Funcționalități Cheie

- Două intrări pentru același serviciu: `/iap_online/<serviciu>` primește webhook-ul clientului și pune cererea în coadă (webhook-ul renunță după o secundă), iar `/iap_online/<serviciu>/sync` răspunde imediat butonului dintr-un formular (JavaScript, CORS).
- Răspuns prin callback: un cron procesează coada și trimite rezultatul către automatizarea „On webhook” a clientului, cu reîncercări (după 5 încercări eșuate serverul renunță, iar clientul retrimite cererea).
- Înregistrare fără copierea cheilor: tokenul contului ajunge doar la URL-ul de callback de pe gazda bazei clientului, iar contul se leagă de acea gazdă. Creditele de probă se acordă o singură dată per bază de date.
- Contul se leagă de partenerul firmei clientului când CUI-ul este cunoscut; nu se creează parteneri din date anonime, iar o firmă necunoscută rămâne pe cont pentru verificare, cu butonul „Link Company”.
- Credite la cerere: o cerere `balance` întoarce creditele rămase, fără taxare; pagina de credite `/iap/1/credit` funcționează și pentru aceste conturi.
- Fiecare răspuns rezervă și capturează credite pe cont și întoarce clientului `cost` și `balance`; o intrare invalidă sau o sursă care nu răspunde nu se taxează.
- Înregistrare protejată: limitată per IP și la conturi noi pe oră; un cont existent își păstrează callback-ul cât timp automatizarea „On webhook” există (suport: „Reset Online Callback”).
- Limite și confidențialitate: cereri pe minut per cont; intrările și răspunsurile se șterg după 30 de zile (tranzacțiile rămân pentru facturare).
- Pe serviciu (**Settings → Technical → IAP → IAP Service**, grupul „Odoo Online”): bifa „Odoo Online”, „Credits per Answer” (0 = gratuit) și „Max Request Size” (64 de caractere implicit). Cererile se urmăresc în „Odoo Online Requests”, cu filtrele „Errors” și „Not delivered”.
- Portalul serverului IAP (`/my/iap`) afișează insigna „Odoo Online” pentru aceste conturi, cu soldul, istoricul și „Buy Credits”.
- Un modul de serviciu (de exemplu `terrabit_iap_server_online_anaf`) își adaugă codul, bifează „Odoo Online” și implementează `_service_<cod>(valoare)`. Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `terrabit_iap_server`

#### 4. Componente Cheie

**Modele**

- `iap.online.request`: cererea unei baze Odoo Online (înregistrare, sold, în coadă sau imediată), cu intrare, răspuns JSON, stare, tranzacție de credit și starea livrării.
- `iap.server.account` (extins): URL-ul de callback online, cererile contului, indicatorul de firmă necunoscută; acțiunile `action_online_link_company` și `action_online_reset_callback`.
- `iap.server.service` (extins): `online_enabled`, `online_credit`, `online_input_size` și credite partajate.

**Vizualizări**

- `view_iap_online_request_list`, `view_iap_online_request_form`, `view_iap_online_request_search`: lista, formularul și filtrele cererilor (acțiunea „Odoo Online Requests”).
- `view_iap_server_service_form`: grupul „Odoo Online” pe formularul serviciului.
- `view_iap_server_account_form`: fila „Odoo Online” pe cont, cu butoanele „Link Company” și „Reset Online Callback”.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_online_request_process`: procesează cererile din coadă și livrează răspunsurile.
- `ir_cron_online_request_cleanup`: șterge cererile vechi (intrări și răspunsuri după 30 de zile).

#### 5. Conexiuni

- [deltatech_iap_online](../deltatech_iap_online/index.md): baza „data-only” din baza de date a clientului, care trimite cererile către acest server.
- `terrabit_iap_server`: serverul IAP pe care se întemeiază creditele și conturile.
