# Website VAT Validation (localizat la `deltatech_website_vat_validation/index.md`)

- **Nume Tehnic:** `deltatech_website_vat_validation`
- **Versiune:** `19.0.0.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_vat_validation`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_vat_validation`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul îmbunătățește validarea codului de TVA în procesul de comandă (checkout) de pe website și în portalul de client din Odoo, asigurându-se că numerele de TVA sunt corect validate. Scopul principal este creșterea calității datelor și prevenirea introducerii unor coduri de TVA duplicate sau incorecte, oferind clienților feedback imediat și reducând efortul de verificare manuală al administratorilor.

#### 2. Funcționalități Cheie

- Validarea automată a codului de TVA în timpul comenzii de pe website (checkout)
- Validarea codului de TVA în portalul de client la actualizarea datelor
- Prevenirea codurilor de TVA duplicate între clienți diferiți
- Eliminarea automată a spațiilor (whitespace) din valorile introduse pentru TVA
- Integrare atât cu procesul de checkout din website sale, cât și cu portalul de client
- Mesaje de eroare clare atunci când un cod de TVA este deja utilizat

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

Documentația pentru Sumar și Funcționalități a fost preluată din `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune este omisă.

#### 5. Conexiuni

- `website_sale`: modulul standard de e-commerce Odoo pe care îl extinde pentru validarea TVA la checkout și în portal.
