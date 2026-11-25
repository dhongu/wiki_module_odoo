# IAP Server - Odoo Online ANAF Partner (localizat la `terrabit_iap_server_online_anaf/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_online_anaf`
- **Versiune:** `19.0.1.1.3`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_online_anaf
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_online_anaf`
- **Ultima Ingestie:** `2026-11-20`

#### 1. Sumar

Serviciul „ANAF Partner (Odoo Online)” al serverului IAP Terrabit: returnează datele de partener ale unei companii românești, căutate la ANAF după CUI. Răspunde modulului de date `l10n_ro_anaf_partner_online`, pe care clienții de pe Odoo Online îl importă ca arhivă zip. Clientul primește datele gata de scris în fișa partenerului, iar Terrabit taxează corect fiecare căutare în credite IAP.

#### 2. Funcționalități Cheie

- **Date de partener gata de scris:** denumire, adresa sediului social, județ și țară ca coduri (niciodată id-uri din baza serverului), CUI cu prefixul `RO` doar pentru plătitorii de TVA, telefon.
- **Stare ANAF:** plătitor de TVA, inactiv fiscal, radiat, număr de înregistrare la registrul comerțului.
- **Taxare corectă:** 0,02 credite (1 credit = 1 EUR) pentru fiecare răspuns ANAF, găsit sau negăsit; un CUI invalid sau lipsa răspunsului ANAF nu se taxează.
- **Credit de probă:** 1 credit, adică 50 de căutări, pentru fiecare bază de date client.
- **Construit pe** `terrabit_iap_server_online` (coadă, callback, răspuns imediat, credite) și `l10n_ro_anaf_partner_lookup` (clientul ANAF).

#### 3. Dependențe

- [terrabit_iap_server_online](../terrabit_iap_server_online/index.md)
- [l10n_ro_anaf_partner_lookup](../l10n_ro_anaf_partner_lookup/index.md)

#### 4. Componente Cheie

**Modele**

- `iap.server.service` (extins): înregistrează serviciul `anaf_partner_online`.
- `iap.online.request` (extins): metoda `_service_anaf_partner_online`, care execută căutarea la ANAF și întoarce datele partenerului.

**Vizualizări**

- Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- `iap_server_service_anaf_partner_online`: înregistrare de date a serviciului (unitate „lookup”, 1 credit inițial, 0,02 credite per căutare, activ pentru Odoo Online).

#### 5. Conexiuni

- [l10n_ro_anaf_partner_online](../l10n_ro_anaf_partner_online/index.md): modulul de date importat de clienții Odoo Online, care apelează acest serviciu.
