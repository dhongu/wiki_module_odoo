# Deltatech Stock Close (localizat la `deltatech_stock_close/index.md`)

- **Nume Tehnic:** `deltatech_stock_close`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_close
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_close`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul oferă instrumentele necesare pentru închiderea operațiunilor de stoc la o anumită dată. El permite marcarea valorizărilor mișcărilor de stoc drept „închise”, astfel încât acestea să poată fi excluse din fișa de magazie (raportul românesc de stocuri) după o anumită perioadă sau la închiderea exercițiului financiar, menținând astfel acuratețea și performanța rapoartelor de inventar.

#### 2. Funcționalități Cheie

- Posibilitatea de a închide operațiunile de stoc începând cu o anumită dată.
- Adaugă câmpul „Valorizare Activă” pe mișcările de stoc (în Odoo 19 valorizarea este stocată direct pe `stock.move`), pentru vizibilitate mai bună.
- Îmbunătățește performanța raportării prin filtrarea valorizărilor vechi sau închise din fișa de magazie (opțiunea „Doar active”).
- Integrare cu rapoartele de stoc din localizarea românească.
- Flux de utilizare: Inventar > Raportare > Fișa de Magazie (România), se activează opțiunea „Doar active” pentru a exclude valorizările închise din raport; valorizările mișcărilor de stoc se marchează ca închise (se debifează „Valorizare Activă”) conform nevoilor de business.

#### 3. Dependențe

- `stock_account`
- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile pentru Componente Cheie au fost acoperite de fișierul `readme/DESCRIPTION.md`, care descrie funcționalitatea principală a modulului (câmpul „Valorizare Activă” de pe `stock.move` și filtrarea aferentă din fișa de magazie `l10n_ro_stock_report`). Analiza suplimentară a codului a fost omisă în conformitate cu regula de prioritizare a Readme-ului.

#### 5. Conexiuni

- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md): modulul extins direct — acest modul adaugă filtrul „Doar active” în fișa de magazie și balanța analitică furnizate de `l10n_ro_stock_report`, pentru a exclude valorizările închise din rapoartele de gestiune.
