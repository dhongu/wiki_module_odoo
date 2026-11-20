# IAP Server - Odoo Online Sameday (localizat la `terrabit_iap_server_online_sd/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_online_sd`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_online_sd
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_online_sd`
- **Ultima Ingestie:** `2026-11-20`

#### 1. Sumar

Serviciul **Sameday (Odoo Online)** al serverului IAP Terrabit: emitere AWB, etichetă, anulare și urmărire colet cu Sameday, pentru modulul de date `deltatech_delivery_sd_online`, pe care clienții de pe Odoo Online îl importă ca arhivă zip. Serverul folosește furnizorul Sameday pe care îl întreținem deja, așa că o corecție făcută acolo servește atât clienții Odoo.sh, cât și pe cei Odoo Online.

#### 2. Funcționalități Cheie

- **Furnizorul Sameday existent**: apelurile trec prin `SDProvider` din `deltatech_delivery_sd` (token păstrat între apeluri, răspunsuri incerte detectate, referință deja folosită la Sameday reîncercată cu sufix).
- **Catalogul Sameday citit din cont**: baza clientului nu are id-uri Sameday, deci serverul preia punctul de ridicare implicit, serviciul (implicit, după id sau după nume), taxa de colet deschis a serviciului, precum și județul și localitatea potrivite după nume (fără diacritice); o localitate necunoscută se trimite ca text.
- **Expediția clientului, așa cum o citește Sameday**: colete, greutate, valoare declarată, ramburs, conținut ca observație; AWB-ul este mereu plătit de expeditor (singurul plătitor acceptat de Sameday). Refuzul Sameday ajunge la client cu mesajul său, fără taxare.
- **Etichetă PDF** în format A4 sau A6 (A5 se tipărește ca A6).
- **Urmărire** mapată pe stările: creat, în tranzit, în depozit, în livrare, livrat.
- **Taxare**: 0,01 credite per AWB nou (1 credit = 1 EUR); 5 credite de probă (500 AWB) per bază de date client.
- **Neinclus**: lockere easybox și Sameday Points, plătitor destinatar sau terț, opțiunile Sâmbătă, ePOD și SMS (nu sunt opțiuni Sameday).

#### 3. Dependențe

- [terrabit_iap_server_online_delivery](../terrabit_iap_server_online_delivery/index.md)
- [deltatech_delivery_sd](../deltatech_delivery_sd/index.md)

#### 4. Componente Cheie

**Modele**

- `iap.server.service` (extins): înregistrarea serviciului în date (`iap_server_service_sameday_online`, „Sameday (Odoo Online)").
- `iap.online.request` (extins): `_delivery_adapter_sameday_online` furnizează adaptorul Sameday către baza de curierat.
- `SamedayAdapter` (`models/sd_adapter.py`, clasă Python): autentificare, punct de ridicare, serviciu, județ/localitate, creare AWB, etichetă, anulare, stare.

**Vizualizări**

- Fără vizualizări; modulul este strict de server.

**Acțiuni Automate / Acțiuni Server**

- Fără cron-uri sau acțiuni server.

#### 5. Conexiuni

- [deltatech_delivery_sd_online](../deltatech_delivery_sd_online/index.md): modulul de date importat de clienții Odoo Online, care consumă acest serviciu.
- [deltatech_delivery_sd](../deltatech_delivery_sd/index.md): furnizorul `SDProvider` refolosit pentru apelurile Sameday.
