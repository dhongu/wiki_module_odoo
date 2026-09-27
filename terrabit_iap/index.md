# Terrabit IAP Client Base (localizat la `terrabit_iap/index.md`)

- **Nume Tehnic:** `terrabit_iap`
- **Versiune:** `20.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_iap
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Modulul conectează instanțele Odoo la serviciile proprii Terrabit vândute prin mecanismul IAP (In-App Purchases — servicii cu credite consumate din platformă). El permite ca fiecare serviciu Terrabit (nu doar serverul oficial Odoo) să aibă propriul endpoint de facturare/credite, oferă un pas de „înregistrare" a contului pe serverul Terrabit și transmite automat datele de identificare necesare (CUI-ul companiei, modulele instalate, informații de contract) atunci când un serviciu are nevoie de ele.

#### 2. Funcționalități Cheie

- Configurare centralizată a endpoint-ului IAP implicit, disponibilă în Setări generale (secțiunea „IAP" → bloc „IAP Client", vizibil doar pentru grupul „Settings" / `base.group_system`), prin parametrul de sistem `iap.endpoint`.
- Fiecare cont IAP (`iap.account`) poate avea propriul endpoint de serviciu (`iap_endpoint`) și un `service_url` afișat pe formularul contului, permițând găzduirea mai multor servicii Terrabit pe endpoint-uri diferite.
- Opțiune per-cont „Hash IAP token" (`use_hashing`) — dezactivarea ei trimite token-ul contului necriptat (util pentru unele integrări/depanare).
- Buton „Register on Server" pe formularul contului IAP (`action_register_account`) — trimite token-ul brut al contului la endpoint-ul `/iap/register`; serverul Terrabit calculează hash-ul, leagă contul de partenerul cu CUI-ul corespunzător și acordă creditele inițiale ale serviciului.
- Preluarea soldului/creditelor funcționează și pentru conturile cu endpoint propriu: metoda standard din Odoo interoghează un singur endpoint (cel implicit), pe când acest modul interoghează separat, cont cu cont, fiecare endpoint Terrabit prin ruta `/iap/1/get-accounts-information`.
- Endpoint controller `/iap/get_info` (JSON-RPC, fără autentificare) — expune date de identificare (token de cont, CUI/nume companie, `database.uuid`, `web.base.url`, modulele instalate, informații de contract publisher warranty) pentru ca serverul Terrabit să poată valida și procesa un cont IAP.
- Descoperirea serviciilor disponibile (`get_services`) e adaptată să interogheze fiecare endpoint IAP folosit de conturile existente, nu doar serverul oficial Odoo, prin ruta `/iap/services-token`.
- Interogarea serviciilor IAP folosește protocolul standard JSON-RPC, simplificând integrarea contului de credite cu alte sisteme și aliniind-o la modul obișnuit de apelare din Odoo.

#### 3. Dependențe

- `iap`

#### 4. Componente Cheie

**Modele**

- `iap.account` (extins): adaugă `service_url`, `iap_endpoint` și `use_hashing`; redefinește `write`, `get`, `get_services`, `get_credits_url`, `_hash_iap_token`, `get_account_info`, `action_register_account` și `_get_account_information_from_iap` pentru a suporta endpoint-uri proprii per serviciu Terrabit.
- `res.config.settings` (extins): adaugă câmpul `iap_endpoint_url`, legat de parametrul de sistem `iap.endpoint`.

**Vizualizări**

- `iap_account_view_form`: extinde formularul standard al contului IAP cu butonul „Register on Server" și câmpurile `service_url`, `iap_endpoint`, `use_hashing`.
- `res_config_settings_view_form`: adaugă în Setări generale (bloc „IAP Client", vizibil pentru `base.group_system`) câmpul de configurare a endpoint-ului IAP implicit.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

**Alte componente tehnice**

- Controller `IapAccountController` (`/iap/get_info`, JSON-RPC, `auth="none"`): rulează cu utilizator superuser și returnează metadatele contului (`get_account_info`) pe baza `account_token`-ului primit.
- `patch.py`: suprascrie `iap_tools.iap_get_endpoint` pentru ca endpoint-ul IAP folosit într-un apel să poată fi forțat prin contextul `iap_endpoint` (folosit de `write`, `get_credits_url` etc. din `iap.account`).

#### 5. Conexiuni

- `iap`: modulul îl extinde direct pentru a suporta endpoint-uri IAP proprii Terrabit, în locul (sau pe lângă) serverul oficial Odoo.
