# Terrabit IAP AI (localizat la `terrabit_iap_server_ai/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_ai`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_ai
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_ai`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul adaugă un serviciu de inteligență artificială (AI) în serverul IAP Terrabit. Clienții conectați pot folosi funcții AI (generare și procesare de text) prin infrastructura serverului IAP, fără să configureze un furnizor AI pe fiecare instanță în parte. Modulul are starea de dezvoltare „Beta".

#### 2. Funcționalități Cheie

- Serviciu nou „AI" (cod `ai`) disponibil în lista de servicii a serverului IAP, creat automat la instalare.
- Generare și procesare de text prin serverul IAP, cu furnizorul AI administrat centralizat.
- Serviciul poate fi atribuit conturilor clienților IAP ca orice alt serviciu al serverului.

#### 3. Dependențe

- `terrabit_iap_server`

#### 4. Componente Cheie

**Modele**

- `iap.server.service` (extins): adaugă valoarea `ai` în câmpul de selecție `service_code`.

**Vizualizări**

- Modulul nu definește vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- `iap_server_service_ai` (înregistrare de date): serviciul „AI" cu codul `ai`, încărcat din `data/iap_server_service_data.xml`. Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- [terrabit_iap_server_helpdesk](../terrabit_iap_server_helpdesk/index.md): alt serviciu adăugat peste același server IAP.
- [terrabit_iap_server_sale](../terrabit_iap_server_sale/index.md): alt serviciu adăugat peste același server IAP.
