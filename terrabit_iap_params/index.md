# Terrabit IAP Params

- **Nume Tehnic:** `terrabit_iap_params`
- **Versiune:** `19.0.1.2.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_params
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_params`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Sincronizează parametrii de sistem (`ir.config_parameter`) de pe serverul IAP Terrabit în baza de date a clientului, astfel încât configurațiile gestionate centralizat pe server să ajungă automat la clienții conectați. Modulul este tehnic (categoria „Hidden”, stadiu Beta) și nu are interfață proprie; permite Terrabit să administreze de la distanță doar un set restrâns și sigur de parametri.

#### 2. Funcționalități Cheie

- Primește de la serverul IAP parametri de sistem și îi scrie în baza clientului sau îi șterge, după cum parametrul este marcat activ sau nu (`enabled`). Este acceptat și formatul vechi, în care valoarea vine direct.
- Autentificare strictă: token-ul este acceptat doar pentru contul serviciului `params_sync`, comparat în timp constant; un token gol este refuzat.
- Listă de chei permise: se scriu doar `database_notification_banner` și cheile cu prefixul `terrabit.` sau `terrabit_`. Celelalte (de ex. `web.base.url`, `database.*`, `auth_signup.*`) sunt ignorate și returnate serverului în lista `rejected`.
- Răspunsul către server nu conține mesajul excepției, doar un mesaj generic de eroare.
- Endpoint de diagnoză care returnează momentul pornirii procesului și versiunea Odoo, util pentru a confirma că un update a fost pus în producție după deploy.
- La instalare creează automat, pentru fiecare companie, un cont IAP pentru serviciul „System Parameters Sync” (`params_sync`) și îl asociază companiei.

#### 3. Dependențe

- `terrabit_iap`

#### 4. Componente Cheie

**Modele**

- `iap.account` (extins): metoda `action_update_system_parameters` aplică parametrii primiți, filtrați prin lista de chei permise, și întoarce cheile refuzate.

**Vizualizări**

- Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server. Modulul expune rutele HTTP JSON-RPC (`auth="none"`):
  - `/iap/update_params` și aliasul `/iap/params_sync_response`: primesc și aplică parametrii (rute cu `readonly=False`).
  - `/iap/system_info`: returnează `server_start` și `odoo_version`.
- Înregistrarea `iap_service_params_sync` (`iap.service`, `noupdate`): serviciul `params_sync`.
- `post_init_hook`: creează conturile IAP pe companii.

#### 5. Conexiuni

- `terrabit_iap`: modulul de bază pentru conectarea la serverul IAP Terrabit (nu are încă pagină wiki).
