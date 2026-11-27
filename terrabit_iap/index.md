# Terrabit IAP Client Base (localizat la `terrabit_iap/index.md`)

- **Nume Tehnic:** `terrabit_iap`
- **Versiune:** `20.0.1.4.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_iap
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap`
- **Ultima Ingestie:** `2026-11-27`

#### 1. Sumar

Modulul conectează instanțele Odoo la serviciile proprii Terrabit vândute prin mecanismul IAP (In-App Purchases — servicii cu credite consumate din platformă). El permite ca fiecare serviciu Terrabit (nu doar serverul oficial Odoo) să aibă propriul endpoint de facturare/credite, oferă un pas de „înregistrare" a contului pe serverul Terrabit și transmite automat datele de identificare necesare (CUI-ul companiei, modulele instalate, informații de contract) atunci când un serviciu are nevoie de ele.

#### 2. Funcționalități Cheie

- Configurare centralizată a endpoint-ului serviciilor Terrabit, în Setări generale (setarea „IAP Endpoint Service", vizibilă doar pentru `base.group_system`), prin parametrul propriu `terrabit_iap.endpoint` (implicit `https://terrabit.odoo.com`). Parametrul global `iap.endpoint` rămâne al serviciilor Odoo, deci un „Save" în Setări nu mai mută butoanele standard (View My Services, Buy Credit, Manage, Rotate) pe serverul Terrabit.
- Conturile IAP ale serviciilor Terrabit (servicii definite de un modul `terrabit_*`) primesc la creare endpoint-ul Terrabit; conturile celorlalte servicii păstrează endpoint-ul Odoo. La actualizare, o migrare repară conturile și parametrii rămași pe endpoint greșit (un endpoint setat intenționat pe alt server nu se atinge).
- Secret de apel invers (callback secret, terrabit#537): fiecare cont primește la creare (și prin migrare, pe cele existente) un secret generat în baza de date, trimis o singură dată în corpul cererii `/iap/register`, niciodată în URL. După ce serverul Terrabit confirmă că îl deține, rutele pe care serverul le apelează în această bază (`/iap/get_info`) refuză apelurile fără secret — `account_token` nu mai este suficient. Până la confirmare (server neactualizat, cont neînregistrat) rutele se comportă ca înainte. Schimbarea `account_token` șterge confirmarea; formularul contului arată câmpul read-only „Callback Secret Registered" (secretul nu este afișat).
- Fiecare cont IAP (`iap.account`) poate avea propriul endpoint de serviciu (`iap_endpoint`) și un `service_url` afișat pe formularul contului, permițând găzduirea mai multor servicii Terrabit pe endpoint-uri diferite.
- Opțiune per-cont „Hash IAP token" (`use_hashing`) — dezactivarea ei trimite token-ul contului necriptat (util pentru unele integrări/depanare).
- Buton „Register on Server" pe formularul contului IAP (`action_register_account`) — trimite token-ul brut al contului la endpoint-ul `/iap/register`; serverul Terrabit calculează hash-ul, leagă contul de partenerul cu CUI-ul corespunzător și acordă creditele inițiale ale serviciului.
- Preluarea soldului/creditelor funcționează și pentru conturile cu endpoint propriu: metoda standard din Odoo interoghează un singur endpoint (cel implicit), pe când acest modul interoghează separat, cont cu cont, fiecare endpoint Terrabit prin ruta `/iap/1/get-accounts-information`.
- Endpoint controller `/iap/get_info` (JSON-RPC, fără autentificare de sesiune, protejat prin `account_token` și, după confirmare, prin secretul de apel invers) — expune date de identificare (token de cont, CUI/nume companie, `database.uuid`, `web.base.url`, modulele instalate, informații de contract publisher warranty) pentru ca serverul Terrabit să poată valida și procesa un cont IAP.
- Descoperirea serviciilor disponibile (`get_services`) e adaptată să interogheze fiecare endpoint IAP folosit de conturile existente, nu doar serverul oficial Odoo, prin ruta `/iap/services-token`.
- Interogarea serviciilor IAP folosește protocolul standard JSON-RPC, simplificând integrarea contului de credite cu alte sisteme și aliniind-o la modul obișnuit de apelare din Odoo.

#### 3. Dependențe

- `iap`
- `mail` (`get_account_info()` folosește `publisher_warranty.contract`, definit în `mail`)

#### 4. Componente Cheie

**Modele**

- `iap.account` (extins): adaugă `service_url`, `iap_endpoint`, `use_hashing`, `callback_secret` (grup `base.group_system`) și `callback_secret_registered`; redefinește `create`, `write`, `get`, `get_services`, `get_credits_url`, `_hash_iap_token`, `get_account_info`, `action_register_account` (trimite și secretul) și `_get_account_information_from_iap` pentru a suporta endpoint-uri proprii per serviciu Terrabit.
- `res.config.settings` (extins): adaugă câmpul `terrabit_iap_endpoint_url`, legat de parametrul de sistem `terrabit_iap.endpoint`.
- Metode noi pe `iap.account`: `_check_callback_secret` (comparație `hmac.compare_digest`), `_ensure_callback_secret`, `_terrabit_iap_fix_endpoints` (folosită de migrarea 20.0.1.3.0).

**Vizualizări**

- `iap_account_view_form`: extinde formularul standard al contului IAP cu butonul „Register on Server" și câmpurile `service_url`, `iap_endpoint`, `use_hashing` și `callback_secret_registered`.
- `res_config_settings_view_form`: adaugă în Setări generale setarea „IAP Endpoint Service" (vizibilă pentru `base.group_system`) cu endpoint-ul serviciilor Terrabit.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

**Alte componente tehnice**

- Controller `IapAccountController` (`/iap/get_info`, JSON-RPC, `auth="none"`): rulează cu utilizator superuser, verifică `account_token` și `callback_secret`, apoi returnează metadatele contului (`get_account_info`); eroare „Account not found” dacă nu se potrivesc.
- Migrări: `20.0.1.3.0` (repară endpoint-urile) și `20.0.1.4.0` (generează secretul pe conturile existente). Teste: `test_iap_account`, `test_iap_controller`, `test_callback_secret`.
- `patch.py`: suprascrie `iap_tools.iap_get_endpoint` pentru ca endpoint-ul IAP folosit într-un apel să poată fi forțat prin contextul `iap_endpoint` (folosit de `write`, `get_credits_url` etc. din `iap.account`).

#### 5. Conexiuni

- `mail`: dependență necesară pentru `publisher_warranty.contract`.
- `iap`: modulul îl extinde direct pentru a suporta endpoint-uri IAP proprii Terrabit, în locul (sau pe lângă) serverul oficial Odoo.
