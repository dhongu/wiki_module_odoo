# Terrabit IAP Client Base (localizat la `terrabit_iap/index.md`)

- **Nume Tehnic:** `terrabit_iap`
- **Versiune:** `19.0.1.2.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul de bază pentru clienții serviciilor IAP (In-App Purchase) oferite de Terrabit. Permite ca fiecare cont IAP să comunice cu propriul server (endpoint), în loc de serverul IAP oficial Odoo, astfel încât soldul de credite, serviciile disponibile și înregistrarea contului să funcționeze pentru toate serviciile Terrabit de la același furnizor. Oferă și un API prin care serverul Terrabit află datele necesare pentru identificarea clientului (CUI, module instalate, contract).

#### 2. Funcționalități Cheie

- Configurare centralizată a endpoint-ului IAP: câmpul „IAP Endpoint Service" din Setări (secțiunea IAP), salvat în parametrul de sistem `iap.endpoint`.
- Pe fiecare cont IAP (`iap.account`): URL-ul serviciului, endpoint-ul IAP propriu și opțiunea de activare/dezactivare a hashing-ului token-ului (implicit activat).
- Sincronizare automată a endpoint-ului în parametrul `<nume_serviciu>.endpoint` la modificarea contului.
- Butonul „Register account" pe contul IAP: trimite serverului token-ul brut și datele contului; serverul leagă contul de partener (după CUI) și acordă creditele inițiale ale serviciului.
- Reîmprospătarea soldului pentru conturile cu endpoint propriu: la deschiderea contului, fiecare este interogat pe propriul server (corecție 19.0.1.2.0, reactivarea unei suprascrieri rămase comentate la migrare); restul conturilor rămân pe implementarea standard.
- Preluarea serviciilor de la fiecare endpoint în parte (`get_services`), nu doar de la serverul implicit.
- Link-ul de achiziție credite respectă endpoint-ul și setarea de hashing a contului.
- API de metadate cont: rută JSON-RPC `/iap/get_info` care returnează token, nume serviciu, UUID bază de date, URL de bază, date contract, lista modulelor instalate (non-aplicații) și datele companiilor (nume, țară, CUI). Se cere CUI setat pe fiecare companie, altfel apare eroare.
- Interogarea serviciilor folosește protocolul standard JSON-RPC (nou în 19.0).
- Permite gestionarea mai multor servicii IAP de la același furnizor.

#### 3. Dependențe

- `iap`

#### 4. Componente Cheie

**Modele**

- `iap.account` (extins): adaugă `service_url`, `iap_endpoint`, `use_hashing`; suprascrie `write`, `get_services`, `get_credits_url`, `_hash_iap_token`, `_get_account_information_from_iap`; adaugă `get_account_info` și `action_register_account`.
- `res.config.settings` (extins): câmpul `iap_endpoint_url` legat de `iap.endpoint`.

**Vizualizări**

- `iap_account_view_form`: extinde formularul contului IAP cu câmpurile noi și butonul de înregistrare.
- `res_config_settings_view_form`: setarea „IAP Endpoint Service" (doar `base.group_system`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite. Modulul aplică un patch la încărcare (`patch.py`) peste `iap_tools.iap_get_endpoint`, care preferă endpoint-ul din context (`iap_endpoint`) față de cel implicit. Controller: `/iap/get_info` (auth `none`, identificare prin `account_token`).

#### 5. Conexiuni

- `iap`: modul de bază extins; serviciile Terrabit (module client de tip IAP din suita `terrabit`) se bazează pe acest modul pentru endpoint-ul propriu.
