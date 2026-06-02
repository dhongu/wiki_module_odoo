# Website alternative code (localizat la `deltatech_alternative_website/index.md`)

- **Nume Tehnic:** `deltatech_alternative_website`
- **Versiune:** `19.0.1.0.7`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_alternative_website`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_alternative_website`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Acest modul extinde magazinul online Odoo astfel încât clienții să poată regăsi produsele și după codurile alternative (echivalente) definite pentru acestea. În practică, atunci când un cumpărător caută pe site folosind un cod alternativ al unui produs, motorul de căutare al magazinului online identifică produsul corect, chiar dacă acel cod nu este referința principală. Modulul aduce astfel pe website funcționalitatea de coduri echivalente disponibilă deja intern, îmbunătățind experiența de căutare a clienților obișnuiți cu alte coduri (de exemplu coduri de furnizor sau coduri vechi).

#### 2. Funcționalități Cheie

- Căutarea produselor în magazinul online după codul alternativ (echivalent) al produsului.
- Afișarea codului alternativ în paginile de produs din website.

#### 3. Dependențe

- `website`
- `website_sale`
- `deltatech_alternative`

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, funcționalitatea principală este căutarea produselor folosind codul echivalent în magazinul online. Întrucât descrierea modulului este disponibilă, nu a fost efectuată o analiză detaliată a codului pentru această secțiune.

#### 5. Conexiuni

- `deltatech_alternative`: modulul de bază care definește codurile alternative (echivalente) ale produselor; acest modul de website expune respectivele coduri în magazinul online.
