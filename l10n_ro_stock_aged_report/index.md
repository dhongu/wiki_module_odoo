# Romania - Stock Aged Report

- **Nume Tehnic:** `l10n_ro_stock_aged_report`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_aged_report
- **Cale Locală:** odoo-addons/l10n-romania/l10n_ro_stock_aged_report
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Raport de vechime a stocului pentru localizarea românească. Împarte stocul unui depozit pe intervale de vechime și arată, pentru fiecare produs, cantitatea, valoarea, contul de stoc și data ultimei ieșiri, ca să se vadă ce marfă nu se mai mișcă. Este un instrument de analiză: nu generează note contabile.

#### 2. Funcționalități Cheie

- Urmărirea automată a ultimei intrări și a ultimei ieșiri pe fiecare poziție de stoc (`stock.quant`); la instalare, pozițiile existente se completează retroactiv din istoric.
- Wizard pentru un depozit și o dată de referință, cu intervale de vechime configurabile (de exemplu 15, 30, 90, 180, 365 zile).
- Defalcarea cantității și a valorii pe intervale, plus contul de evaluare a stocului din categoria produsului.
- Vizualizări pivot și listă pentru analiza detaliată (inclusiv pivot pe cont).
- Atenție la interpretare (detaliat în fișa consultantului): raportul pornește mereu de la stocul de azi, valoarea este cantitate x costul actual al produsului, iar vechimea înseamnă zile de la ultima intrare în locație.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.quant`: câmpurile `l10n_ro_last_in_date` și `l10n_ro_last_out_date`.
- `l10n.ro.stock.age.report`: wizard-ul raportului.
- `l10n.ro.stock.age.report.location`: locațiile incluse în raport.
- `l10n.ro.stock.age.report.line`: liniile raportului pe produs și interval.

**Vizualizări**

- `stock_age_report_form_view`: wizard-ul de generare.
- `view_age_report_line_pivot`, `view_age_report_line_tree`, `view_age_report_line_search`: analiza liniilor raportului.
- `menu_stock_age_report`: meniul din *Inventar > Raportare*.

**Acțiuni Automate / Acțiuni Server**

- `pre_init_hook`: preia înregistrările fostului modul `l10n_ro_stock_age_report` (redenumit), fără duplicate; `post_init_hook`: completează retroactiv ultimele date de intrare și ieșire pe pozițiile de stoc existente.

#### 5. Conexiuni

- `stock_account`: sursa contului de evaluare al categoriei de produs.
