# Deltatech Sale Currency (localizat la `deltatech_sale_currency/index.md`)

- **Nume Tehnic:** `deltatech_sale_currency`
- **Versiune:** `19.0.0.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_currency`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_currency`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul oferă o gestionare specializată a conversiei valutare între comenzile de vânzare și facturile generate din acestea. Este util în special pentru companiile care își mențin listele de prețuri într-o monedă (de exemplu EUR), dar doresc să emită facturile într-o altă monedă (de exemplu moneda jurnalului de vânzări sau moneda funcțională a companiei, cum ar fi RON). Astfel, prețurile sunt convertite automat la momentul facturării, iar înregistrările financiare reflectă valorile corecte în moneda dorită.

#### 2. Funcționalități Cheie

- **Moneda facturii bazată pe jurnal**: setează automat moneda facturii generate în funcție de moneda jurnalului de vânzări selectat, înlocuind comportamentul implicit Odoo de a folosi moneda comenzii de vânzare.
- **Conversie automată a prețurilor**: convertește prețurile unitare din moneda comenzii de vânzare în moneda facturii pe parcursul procesului de facturare, folosind cursul de schimb valabil la data conversiei.
- **Coerență financiară**: asigură că înregistrările din jurnalul contabil reflectă valorile corecte în moneda dorită.
- **Integrare între module**: se integrează cu modulele de Vânzări și Contabilitate pentru un flux de date consistent.

#### 3. Dependențe

- `sale`
- `account`

#### 4. Componente Cheie

*Conform DESCRIPTION.md, secțiunile de componente nu sunt detaliate explicit în Readme. Pe baza manifestului și a structurii modulului, modulul extinde modele existente prin fișierele din directorul `models/` (`sale.py`, `account_move.py`), fără modele, vizualizări sau acțiuni automate noi proprii.*

**Modele**

- `sale.order` (extins): logica de determinare a monedei facturii pe baza jurnalului de vânzări.
- `account.move` (extins): conversia prețurilor unitare în moneda facturii la generarea facturii.

**Vizualizări**

- Nu sunt definite vizualizări noi (`data` este gol în manifest).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- Nu există conexiuni funcționale suplimentare documentate către alte module cu pagină wiki.
