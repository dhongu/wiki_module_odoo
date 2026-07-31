# Terrabit Payment Forecast (localizat la `deltatech_payment_forecast/index.md`)

- **Nume Tehnic:** `deltatech_payment_forecast`
- **Versiune:** `19.0.0.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_payment_forecast`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_payment_forecast`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul generează un raport care estimează plățile (încasări de la clienți și plăți către furnizori) așteptate până la o anumită dată. Raportul folosește durata medie de plată/încasare calculată per partener pentru a estima cât de probabil este ca o factură neîncasată sau neplătită să fie decontată până la data țintă, oferind echipei financiare o imagine anticipată a cash-flow-ului. Generarea raportului se poate face manual, printr-un wizard, sau automat, printr-o sarcină programată (cron).

#### 2. Funcționalități Cheie

- Generează un raport de tip „prognoză de plăți" (`payment.forecast`) cu toate facturile de client și furnizor neîncasate/neplătite, scadente până la o dată aleasă.
- Estimează, pentru fiecare factură, data probabilă de decontare pe baza duratei medii de plată istorice a partenerului (calculată de modulul `deltatech_average_payment_period`).
- Include în raport suma reziduală a facturii și suma estimată a fi efectiv plătită/încasată până la data țintă.
- Permite generarea manuală a raportului printr-un wizard (cu dată de sfârșit și companie configurabile).
- Suportă generare automată, programabilă printr-o sarcină cron, cu regenerare pe un orizont fix de zile (parametrul `days`).
- Raportul poate fi analizat în listă, formular, pivot și grafic, cu grupare/filtrare după interval de zile și tip de mișcare (încasare/plată).

#### 3. Dependențe

- `account`
- [deltatech_average_payment_period](../deltatech_average_payment_period/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile Sumar și Funcționalități Cheie au fost preluate din `readme/DESCRIPTION.md`, care nu solicită explicit analiza codului pentru Componente Cheie. Această secțiune este, prin urmare, omisă.

#### 5. Conexiuni

- [deltatech_average_payment_period](../deltatech_average_payment_period/index.md): furnizează modelul `account.average.payment.report`, folosit pentru a estima durata medie de plată/încasare per partener, pe baza căreia se calculează data probabilă de decontare a fiecărei facturi.
- `account`: sursa facturilor (`account.move`) neîncasate/neplătite pe baza cărora se construiește prognoza.
