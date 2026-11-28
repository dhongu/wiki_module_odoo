# Cash Statement Extension (localizat la `deltatech_cash_statement/index.md`)

- **Nume Tehnic:** `deltatech_cash_statement`
- **Versiune:** `20.0.3.1.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_cash_statement
- **Cale Locală:** `odoo-addons/deltatech/deltatech_cash_statement`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul menține soldurile extraselor de casă în concordanță cu contabilitatea și înregistrează o diferență de casă constatată ca o notă datată, în loc să suprascrie tăcut un sold. Este util contabililor care trebuie să alinieze registrele de casă și să documenteze corect plusurile sau minusurile găsite la inventar.

#### 2. Funcționalități Cheie

- Asistent disponibil din lista extraselor bancare, la **Acțiune > Cash Update Balances**, după selectarea unuia sau mai multor extrase ale aceluiași jurnal (**Contabilitate > Contabilitate > Extrase bancare**, vizualizare listă).
- Modul **Align with the accounting balance**: soldul inițial al primului extras selectat devine soldul contului de numerar din înregistrările poștate dinaintea lui, iar fiecare extras următor pornește de la soldul final real al celui precedent; nu se creează notă contabilă.
- Modul **Register a cash difference**: se introduce **Counted Balance** (numerarul numărat la începutul zilei), iar diferența se înregistrează ca linie de extras la data inventarului, pe contul de venituri (plus) sau de cheltuieli (minus). La o companie românească implicit se folosesc 7588 și 6588; în alte cazuri, conturile de diferențe de casă ale jurnalului. Contul se poate schimba, de exemplu pe 4282 când lipsa se imputează casierului (cu **Responsible Person**).
- Data diferenței nu poate fi anterioară extrasului; nota apare deja poștată, iar soldurile extraselor se aliniază automat.
- O lipsă neimputată (6588) este de regulă cheltuială nedeductibilă la impozitul pe profit; se verifică cu contabilul.

Pașii ilustrați cu capturi sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

Documentația pentru acest modul a fost generată pe baza fișierului `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune a fost omisă, deoarece nu este solicitată explicit în Readme. Funcționalitatea este un asistent (wizard) pe `account.bank.statement`, definit în `wizard/account_cash_update_balances_view.xml`.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module cu pagină wiki existentă. Singura dependență este modulul standard `account`.
