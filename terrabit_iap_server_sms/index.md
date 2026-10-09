# IAP Server - Service SMS

- **Nume Tehnic:** `terrabit_iap_server_sms`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_sms
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_sms`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul adaugă serverului IAP Terrabit serviciul de trimitere SMS. Un client Odoo care are un cont IAP cu credit poate trimite mesaje text prin serverul Terrabit, iar acesta le transmite către un furnizor de SMS configurat (SMS 4Pay sau SMS Wapi). Fiecare mesaj trimis consumă credit din cont, iar creditul este reținut doar dacă furnizorul confirmă trimiterea.

#### 2. Funcționalități Cheie

- Serviciu nou `SMS` (cod `sms`) pentru serverul IAP, creat automat la instalare.
- Selectarea furnizorului de SMS pe serviciu: `SMS 4Pay` (implicit) sau `SMS Wapi`, cu câmpurile `SMS Secret` și `SMS Gateway` (identificatorul serviciului la 4Pay, respectiv al dispozitivului la Wapi). Grupul „SMS” apare în formularul serviciului doar când codul serviciului este `sms`.
- Endpoint de trimitere în lot, `/api/sms/3/send` (JSON-RPC), autentificat prin `account_token` al contului IAP; primește mesaje cu liste de numere, fiecare având `uuid` propriu.
- Cost de 1 credit per destinatar: tranzacția este autorizată înainte de trimitere, capturată la succes și anulată dacă furnizorul răspunde cu eroare.
- Răspuns individual pentru fiecare destinatar, cu `uuid`-ul și starea proprie: `success`, `server_error` (cu mesajul de eroare) sau `insufficient_credit`. Un destinatar eșuat nu afectează rezultatul următorilor (corecție SMS-001, versiunea 19.0.1.0.4).
- Rută declarată `readonly=False`, deci rulează direct pe o tranzacție de citire/scriere, fără reluare.
- Stadiu de dezvoltare: Beta.

#### 3. Dependențe

- `iap`
- `terrabit_iap_server`

#### 4. Componente Cheie

**Modele**

- `iap.server.service` (extins): adaugă codul `sms` în `service_code`, câmpurile `sms_provider`, `sms_secret`, `sms_gateway` și metodele `send_sms`, `_send_sms_4pay` (GET către sms.4pay.ro) și `_send_sms_wapi` (POST către smswapi.com).

**Vizualizări**

- `view_iap_server_service_form`: moștenește formularul serviciului din `terrabit_iap_server` și adaugă grupul „SMS” (furnizor, secret, gateway).

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server. Modulul încarcă înregistrarea `iap_server_service_data` (serviciul „SMS”). Controller: `IapSMSServerController.send_sms`. Teste: `tests/test_send_sms.py`.

#### 5. Conexiuni

- [terrabit_iap_server_ai](../terrabit_iap_server_ai/index.md): alt serviciu oferit prin același server IAP.
- [terrabit_iap_server_helpdesk](../terrabit_iap_server_helpdesk/index.md): alt serviciu oferit prin același server IAP.
- [terrabit_iap_server_sale](../terrabit_iap_server_sale/index.md): alt serviciu oferit prin același server IAP.
