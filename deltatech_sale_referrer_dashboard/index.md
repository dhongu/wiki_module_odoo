# Sale Referrer Margin Dashboard (localizat la `deltatech_sale_referrer_dashboard/index.md`)

- **Nume Tehnic:** `deltatech_sale_referrer_dashboard`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_sale_referrer_dashboard
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_sale_referrer_dashboard`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul adaugă un dashboard de tip spreadsheet, „Profitabilitate Vânzări", care răspunde la o
singură întrebare, dintr-o privire: cât rămâne efectiv din vânzările confirmate, după plata
comisioanelor de recomandare (referrer), a costului mărfii vândute și a unui cont de cheltuială
specific. Este gândit pentru companii care plătesc comisioane per vânzare și au nevoie de o cifră
rapidă de profitabilitate, fără să exporte date în Excel — cifrele de vânzări și cele contabile sunt
citite live din baza de date și filtrate mereu pe aceeași perioadă.

#### 2. Funcționalități Cheie

- Totaluri pe un singur ecran: vânzări confirmate fără TVA, comision referrer, cost marfă vândută și
  soldul unui cont de cheltuială, afișate una lângă alta.
- Rezultat calculat automat: vânzări − comision − cost marfă − cont de cheltuială.
- Coloană „% din vânzări" care arată ponderea fiecărei sume (comision, cost marfă, cont de
  cheltuială) în cifra de afaceri netă, plus procentul de marjă pe linia de Rezultat.
- Conversie comercială: număr de comenzi confirmate, număr de oferte încă deschise în aceeași
  perioadă și rata de conversie dintre ele.
- Un singur filtru de perioadă pentru tot dashboard-ul: vânzările și înregistrările contabile sunt
  conduse de același filtru global de dată, astfel încât cifrele nu se pot raporta la perioade
  diferite.
- Orice granularitate de perioadă: lună, trimestru, an, intervale relative (ex. ultimele 30 de
  zile) sau interval personalizat.
- Drill-down: fiecare cifră provine dintr-un pivot Odoo, astfel încât comenzile și liniile de
  jurnal din spate rămân auditabile direct din spreadsheet.
- Acces restricționat: dashboard-ul este vizibil doar utilizatorilor care au dreptul să vadă costul
  mărfii vândute.

Dashboard-ul agregă trei pivoturi live: `sale.order` (comenzi confirmate, pe data comenzii, cu
măsurile `amount_untaxed`, `commission`, `cost_of_goods` și numărul de înregistrări),
`account.move.line` (filtrat pe contul de cheltuială și pe înregistrări validate, pe data notei,
măsurând `balance`) și `sale.order` (oferte încă deschise — stare *ofertă* și *ofertă trimisă* —,
numărând înregistrările).

Citirea contului de cheltuială printr-un pivot, în loc de formula spreadsheet `ODOO.BALANCE`, este
deliberată: `ODOO.BALANCE` acceptă ca perioadă doar an, trimestru sau lună, iar pe un interval liber
ar returna tăcut un sold calculat pe altă perioadă decât cifrele de vânzări. Pivotul e filtrat nativ
de Odoo și rămâne corect pentru orice valoare de filtru.

Limitări: comisionul provine din [deltatech_sale_referrer_raport](../deltatech_sale_referrer_raport/index.md)
(dacă are pagină wiki) sau `deltatech_sale_referrer_raport`, iar costul mărfii din
[deltatech_sale_cost_product](../deltatech_sale_cost_product/index.md) — ambele sunt câmpuri stocate,
însumate de pivot. Sunt luate în calcul doar notele contabile validate (posted). Comenzile anulate
sunt excluse din ambele pivoturi de vânzări, deci nu apar nici la numărul de oferte, nici la numitorul
ratei de conversie. Dashboard-ul conține doar cifre în celule, fără grafice, deci Odoo nu îl
randează pe ecrane înguste — este gândit pentru desktop.

#### 3. Dependențe

- `deltatech_sale_referrer_raport`
- [deltatech_sale_cost_product](../deltatech_sale_cost_product/index.md)
- `spreadsheet_dashboard`
- `spreadsheet_account`

#### 4. Componente Cheie

**Modele**

Modulul nu definește modele Python noi (`__init__.py` este gol, fără director `models/`); folosește
doar câmpurile deja definite de dependențe (`sale.order.commission`, `sale.order.cost_of_goods`) prin
pivoturi de spreadsheet.

**Vizualizări**

Nu adaugă vizualizări formular/listă/kanban clasice — interfața este spreadsheet-ul din dashboard.

**Date / Acțiuni**

- `dashboard_sale_referrer_margin` (`data/dashboard.xml`): înregistrare `spreadsheet.dashboard`
  „Sales Profitability", încarcă fișierul `data/files/sale_referrer_margin_dashboard.json`, legată
  de modelul `sale.order`, plasată în grupul de dashboard-uri Vânzări
  (`spreadsheet_dashboard.spreadsheet_dashboard_group_sales`), publicată implicit și vizibilă doar
  grupului `deltatech_sale_cost_product.group_view_cost_on_sale`.

#### 5. Conexiuni

- `deltatech_sale_referrer_raport`: sursă a comisionului de referrer agregat în dashboard.
- [deltatech_sale_cost_product](../deltatech_sale_cost_product/index.md): sursă a costului mărfii
  vândute și a grupului de acces care controlează vizibilitatea dashboard-ului.
- `spreadsheet_dashboard`: infrastructura de dashboard-uri spreadsheet în care este publicat.
- `spreadsheet_account`: furnizează integrarea cu conturile contabile folosită de pivotul pe
  `account.move.line`.
