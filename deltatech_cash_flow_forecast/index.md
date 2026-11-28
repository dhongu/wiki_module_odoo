# Cash Flow Forecast

- **Nume Tehnic:** `deltatech_cash_flow_forecast`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_cash_flow_forecast
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_cash_flow_forecast`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Arată încasările și plățile așteptate în zilele următoare, pe baza scadențelor facturilor și a bonurilor deschise, precum și soldul de numerar la care duc. Ajută la anticiparea fluxului de numerar fără rapoarte externe.

#### 2. Funcționalități Cheie

- **Previziune pe scadență**: orice linie postată pe un cont de creanțe sau datorii cu sumă rămasă de plătit (facturi clienți, facturi furnizori, dar și salarii sau alți creditori) apare la data scadenței; conturile non-comerciale (TVA de plată sau de recuperat) sunt excluse. Se lucrează pe suma reziduală în moneda companiei, deci plățile parțiale, plățile nereconciliate și notele de credit reduc sumele.
- **Restanțe pe ziua de azi**: elementele scadente deja sunt afișate la data de azi; filtrul **Overdue** le izolează.
- **Grafic încasări și plăți**: bare zilnice (încasări deasupra axei, plăți dedesubt), pivot pe zi, săptămână sau lună și lista documentelor cu buton de deschidere.
- **Sold de numerar estimat**: linie cumulativă care pornește de la soldul curent al conturilor din jurnalele de bancă și numerar și adaugă încasări minus plăți, zi cu zi.
- Filtre pe următoarele 7, 30 și 90 de zile, pe partener, jurnal și companie; regulă multi-company.
- Meniu: **Contabilitate / Raportare / Management / Cash Flow Forecast** și **Projected Cash Balance**.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.cash.flow.forecast`: model de raportare (bazat pe liniile contabile deschise) cu sumele așteptate pe data scadenței.

**Vizualizări**

- Vizualizările din `views/account_cash_flow_forecast_views.xml`: grafic, pivot și listă pentru previziune și soldul estimat.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `account`: sursa liniilor deschise și a jurnalelor de bancă/numerar.
