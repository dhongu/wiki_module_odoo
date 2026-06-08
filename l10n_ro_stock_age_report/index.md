# Romania - Stock Aged Report (localizat la `l10n_ro_stock_age_report/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_age_report`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_age_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_age_report`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Acest modul oferă un raport de vechime a stocului (Stock Aged Report) pentru localizarea românească. El ajută utilizatorii să urmărească vechimea stocurilor prin monitorizarea ultimelor date de intrare și de ieșire pentru fiecare lot de stoc (stock quant), astfel încât să se poată identifica marfa care stagnează în depozit și să se evalueze impactul ei contabil.

#### 2. Funcționalități Cheie

- Urmărește automat ultima dată de intrare și ultima dată de ieșire pentru fiecare lot de stoc (stock quant).
- Oferă un wizard pentru generarea raportului de vechime pentru un anumit depozit și o anumită dată.
- Intervale de îmbătrânire configurabile (de ex. 15, 30, 90, 180, 365 de zile).
- Defalcă valoarea și cantitatea stocului pe intervale de timp (de ex. [1] 0-15 zile, [2] 15-30 zile etc.).
- Include informații contabile, cum ar fi contul de evaluare a stocului pentru fiecare produs.
- Oferă o vizualizare de tip pivot și o listă pentru analiza detaliată a stocului învechit.
- Actualizează retroactiv loturile de stoc existente cu date istorice la momentul instalării.

#### 3. Dependențe

- `l10n_ro_stock`
- `l10n_ro_stock_account`

#### 4. Componente Cheie

Secțiune omisă: `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie, fără a solicita explicit detalierea componentelor tehnice. Conform fluxului de ingestie, analiza codului pentru această secțiune nu a fost efectuată.

#### 5. Conexiuni

- `l10n_ro_stock`: dependență de bază pentru gestiunea stocurilor în localizarea RO, sursa loturilor de stoc analizate.
- `l10n_ro_stock_account`: dependență pentru evaluarea contabilă a stocurilor, furnizează informațiile despre contul de evaluare incluse în raport.
