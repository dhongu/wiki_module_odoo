# Payment Term Rate Wizard (localizat la `deltatech_payment_term/index.md`)

- **Nume Tehnic:** `deltatech_payment_term`
- **Versiune:** `19.0.2.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_payment_term
- **Cale Locală:** `odoo-addons/deltatech/deltatech_payment_term`
- **Ultima Ingestie:** `2026-11-01`

#### 1. Sumar

Modulul ajută echipele de finanțe și vânzări să genereze rapid termeni de plată în rate, eliminând crearea manuală a fiecărei linii de scadență. Printr-un asistent dedicat, utilizatorul completează numele, tipul, avansul, numărul de rate și ziua din lună, iar modulul generează automat termenul complet, cu avansul, ratele și scadențele corecte. În plus, facturile, comenzile de vânzare și partenerii primesc indicatori și butoane care evidențiază rapid documentele plătibile în rate.

#### 2. Funcționalități Cheie

- Asistent de generare a ratelor: un singur formular (nume, tip, avans, număr de rate, ziua din lună) creează un termen de plată complet într-un clic; ratele existente ale termenului sunt înlocuite cu cele generate.
- Moduri procent și sumă fixă: ratele pot fi un procent din total sau o valoare fixă (câmpul „Rate Value” apare doar la tipul „Fixed Amount”); ultima linie este mereu de tip sold („balance”), ca să preia diferențele de rotunjire.
- Avansul se plătește imediat (ziua 0, la data facturii), iar rata N scade în ziua aleasă din a N-a lună după factură (ziua e limitată la sfârșitul lunii, de ex. ziua 31 devine 28/29 în februarie). Corecție din 19.0.2.0.8: până atunci ziua din lună era ignorată și ratele cădeau la 30, 60, 90... de zile. Liniile folosesc acum tipul de scadență „Days end of month on the”, cu noul câmp „Extra Months” pe liniile termenului de plată.
- Indicator „In Rates” pe factură și „Sale in Rates” pe comanda de vânzare: semnalează documentele al căror termen de plată are mai multe linii, util la filtrare și raportare.
- Butonul „Rates” de pe factură listează liniile termenului de plată ale facturii (câte una per rată, cu scadența și suma rămasă); cel de pe partener listează ratele deschise de încasat din facturile postate.
- Wizardul se lansează din meniul Acțiune al comenzilor de vânzare și al facturilor (**Payment Term Rate Wizard**) sau din butonul „Create Rate” din formularul termenului de plată (**Contabilitate > Configurare > Termeni de plată**).

#### 3. Dependențe

- `account`
- `sale`

#### 4. Componente Cheie

Readme-ul nu cere explicit detalierea componentelor; mai jos sunt cele verificate în cod.

**Modele**

- `account.payment.term.rate.wizard`: asistent tranzitoriu care construiește liniile termenului de plată (avans + rate) și poate crea un termen nou sau rescrie liniile unuia existent. Validează numărul de rate și procentul avansului (0–100).
- `account.payment.term.line` (extins): adaugă câmpul `nb_months` („Extra Months”) și ajustează calculul scadenței pentru tipul „Days end of month on the”.
- `account.move` (extins): câmpul calculat `in_rates` și acțiunea `view_rate` (liniile de rată ale facturii).
- `sale.order` (extins): câmpul calculat `sale_in_rates`.
- `res.partner` (extins): acțiunea `view_rate` (ratele deschise de încasat ale partenerului, din facturi postate).

**Vizualizări**

- `view_account_payment_term_rate_wizard_form`: formularul asistentului (nume, tip, zi din lună, număr de rate, valoarea ratei, avans).
- `view_payment_term_form`: extinde formularul termenului de plată cu butonul „Create Rate” și coloana „Extra Months”.
- `view_move_line_rates_list`: lista de rate (`account.move.line`) cu scadență, sold și sumă rămasă afișate implicit.
- Vizualizările extinse din `views/sale_view.xml`, `views/account_invoice_view.xml` și `views/res_partner_view.xml`: indicatorii „Sale in Rates” / „In Rates” și butoanele „Rates”.

**Acțiuni Automate / Acțiuni Server**

- `action_sale_payment_term_rate_wizard`: acțiune contextuală (binding pe `sale.order`) care lansează asistentul.
- `action_account_payment_term_rate_wizard`: acțiune contextuală (binding pe `account.move`) care lansează asistentul.
- `action_account_moves_sale` („Rates”): deschide lista rândurilor `account.move.line`; domeniul e setat de `view_rate()` de pe factură sau partener.

#### 5. Conexiuni

- `account`: modulul extinde termenul de plată și factura, generând liniile termenului de plată standard Odoo.
- `sale`: modulul marchează comenzile de vânzare plătibile în rate.
