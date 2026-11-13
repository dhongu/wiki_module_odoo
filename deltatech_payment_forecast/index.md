# Payment Forecast

- **Nume Tehnic:** `deltatech_payment_forecast`
- **Versiune:** `19.0.0.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_payment_forecast
- **Cale Locală:** `odoo-addons/deltatech/deltatech_payment_forecast`
- **Ultima Ingestie:** `2026-11-13`

#### 1. Sumar

Echipele financiare au nevoie să știe când vor fi plătite efectiv facturile. Modulul estimează plățile așteptate pe facturile deschise de client și de furnizor până la o dată de sfârșit, pornind de la cât de repede plătește de obicei fiecare partener. Rezultatul este un raport care oferă o imagine anticipată a cash-flow-ului.

#### 2. Funcționalități Cheie

- **Generarea prognozei:** meniul *Generate payment forecast* deschide o fereastră cu *End Date* și *Company*. Butonul *Compute forecast* salvează câte o linie pentru fiecare factură, factură de furnizor sau notă de credit înregistrată, neplătită sau parțial plătită, scadentă până la acea dată.
- **Estimarea plății:** întârzierea obișnuită a unui partener este media timpului de plată al facturilor sale din ultimele 365 de zile. Dacă data facturii plus această întârziere cade după data de sfârșit, *Payment amount* al liniei este zero; altfel este suma rămasă de plată.
- **Raport:** *Payment forecast report* listează partenerul, factura, datele, suma și suma rămasă în moneda companiei, cu vizualizări formular, pivot și grafic și grupare după *Days* și *Move type* (încasare/plată).
- **Instantanee:** o rulare manuală înlocuiește liniile anterioare *Custom* ale companiei sale. Metoda de wizard `get_forecast_cron(days)` reîmprospătează, pentru fiecare companie a utilizatorului, instantaneul etichetat cu acel număr de zile; acțiunea programată nu este inclusă în modul, deci trebuie creată separat dacă se dorește rularea automată.
- **Istoricul plăților și limitări:** provine din conturile cu codul 4111 (clienți) sau 401 (furnizori), ca în planul de conturi românesc; un partener fără istoric se ia în calcul integral. Grupul *Payment forecast* vede meniurile.

#### 3. Dependențe

- `account`
- [deltatech_average_payment_period](../deltatech_average_payment_period/index.md)

#### 4. Componente Cheie

**Modele**

- `payment.forecast`: o linie a prognozei — zile (eticheta instantaneului), companie, partener, factură, jurnal, datele și sumele facturii, suma rămasă (`move_amount_residual`), suma estimată de plată (`payment_amount_forecasted`) și tipul mișcării (`incoming` / `outgoing`).
- `payment.forecast.wizard` (tranzitoriu): data de sfârșit și compania; calculează data estimată de plată (`get_estimated_payment_date`), generează liniile (`get_forecast_lines`) și reîmprospătează instantaneele pe orizont de zile (`get_forecast_cron`).

**Vizualizări**

- `view_payment_forecast_report_tree` și `view_payment_forecast_report_search`: lista și căutarea raportului; acțiunea `action_payment_forecats_report` (și vizualizările formular, pivot, grafic) deschide raportul din meniu.
- `view_payment_forecast_wizard_form` și `action_payment_forecats_wizard`: fereastra de generare a prognozei.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite cron-uri sau acțiuni server. Metoda `payment.forecast.wizard.get_forecast_cron(days)` este pregătită pentru a fi apelată de o acțiune programată, dar acțiunea în sine nu face parte din modul. Securitatea: grupul `payment_forecast_manager` și regula multi-companie `payment_forecast_company_rule`.

#### 5. Conexiuni

- [deltatech_average_payment_period](../deltatech_average_payment_period/index.md): furnizează modelul `account.average.payment.report`, din care se ia durata medie de plată/încasare per partener pentru data estimată de decontare.
- `account`: sursa facturilor (`account.move`) neîncasate/neplătite pe baza cărora se construiește prognoza.
