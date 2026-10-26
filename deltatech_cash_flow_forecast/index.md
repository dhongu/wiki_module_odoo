# Cash Flow Forecast (Prognoză de trezorerie)

- **Nume Tehnic:** `deltatech_cash_flow_forecast`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_cash_flow_forecast
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_cash_flow_forecast`
- **Ultima Ingestie:** `2026-10-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul arată încasările și plățile așteptate în zilele următoare, pe baza scadențelor facturilor și a obligațiilor deschise, precum și soldul de trezorerie la care duc acestea. Ajută la anticiparea golurilor de numerar și la planificarea plăților.

#### 2. Funcționalități Cheie

- **Prognoză pe scadență:** fiecare element contabilizat pe un cont de creanțe sau datorii, cu sumă rămasă de plătit (facturi clienți, facturi furnizori, dar și salarii sau alți creditori), apare la data scadenței. Conturile non-comerciale (TVA de plată sau de recuperat) sunt excluse. Plățile parțiale, plățile nereconciliate și notele de credit reduc sumele, deoarece prognoza lucrează pe suma reziduală în moneda companiei.
- **Restanțe pe ziua curentă:** elementele scadente în trecut sunt afișate la data de azi, astfel încât graficul pornește de la azi; filtrul **Overdue** le izolează.
- **Grafic încasări și plăți:** bare zilnice, cu încasările deasupra axei și plățile dedesubt, plus pivot pe zi, săptămână sau lună și lista documentelor din spatele fiecărei sume, cu buton de deschidere a documentului.
- **Sold estimat de trezorerie:** linie cumulată care pornește de la soldul curent al conturilor din jurnalele de bancă și casă (împrumuturile pe termen scurt și avansele de trezorerie nu sunt luate în calcul) și adaugă zi de zi încasările minus plățile.
- Filtre pentru următoarele 7, 30 și 90 de zile, după partener, jurnal și companie; regulă multi-company.
- Meniu: **Contabilitate / Raportare / Management / Cash Flow Forecast** și **Projected Cash Balance**.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.cash.flow.forecast`: model de raportare bazat pe view SQL (`_auto = False`), cu câmpurile dată, scadență, restanță, tip, partener, document, jurnal, cont, încasări, plăți, sumă netă și sold cumulat.

**Vizualizări**

- `view_account_cash_flow_forecast_graph`: grafic zilnic al încasărilor și plăților.
- `view_account_cash_flow_forecast_balance_graph`: grafic al soldului estimat de trezorerie.
- `view_account_cash_flow_forecast_pivot`: pivot pe zi, săptămână sau lună.
- `view_account_cash_flow_forecast_list`: lista documentelor, cu restanțele evidențiate.
- `view_account_cash_flow_forecast_search`: filtre (7/30/90 zile, restanțe, partener, jurnal, companie).
- Acțiuni: `action_account_cash_flow_forecast` și `action_account_cash_flow_forecast_balance`.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `account`: sursa elementelor contabile, a jurnalelor de bancă/casă și a soldurilor.
