# Payment Forecast (localizat la `deltatech_payment_forecast/index.md`)

- **Nume Tehnic:** `deltatech_payment_forecast`
- **Versiune:** `20.0.0.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_payment_forecast
- **Cale Locală:** `odoo-addons/deltatech/deltatech_payment_forecast`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul generează un raport care estimează plățile (încasări de la clienți și plăți către furnizori) așteptate până la o anumită dată. Raportul folosește durata medie de plată calculată per partener pentru a estima când va fi decontată fiecare factură deschisă, oferind echipei financiare o imagine anticipată a cash-flow-ului. Raportul se poate genera manual, printr-un wizard, sau automat, printr-o sarcină programată.

#### 2. Funcționalități Cheie

- Raport de tip „prognoză de plăți” (`payment.forecast`) cu facturile de client și de furnizor neîncasate sau neplătite, cu suma reziduală și suma estimată a fi decontată.
- Estimarea se bazează pe durata medie de plată a partenerului, calculată de [deltatech_average_payment_period](../deltatech_average_payment_period/index.md).
- Generare manuală printr-un wizard (dată de sfârșit și companie).
- Generare automată prin sarcină programată (cron), pe un orizont fix de zile; rularea se face pentru fiecare companie a utilizatorului cron.
- Prognoza aparține unei companii (`company_id`), cu regulă multi-companie; regenerarea șterge doar rândurile companiei selectate, iar sumele în moneda companiei folosesc moneda companiei.
- Analiză în listă, formular, pivot și grafic, cu grupare după interval de zile și tip de mișcare (încasare/plată).

#### 3. Dependențe

- `account`
- [deltatech_average_payment_period](../deltatech_average_payment_period/index.md)

#### 4. Componente Cheie

Secțiunea e omisă: `readme/DESCRIPTION.md` nu cere explicit analiza componentelor tehnice.

#### 5. Conexiuni

- [deltatech_average_payment_period](../deltatech_average_payment_period/index.md): furnizează raportul `account.average.payment.report`, folosit la estimarea duratei medii de plată per partener.
- `account`: sursa facturilor (`account.move`) pe baza cărora se construiește prognoza.
