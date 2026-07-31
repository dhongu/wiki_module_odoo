# Mentor Interface (localizat la `deltatech_mentor/index.md`)

- **Nume Tehnic:** `deltatech_mentor`
- **Versiune:** `19.0.2.1.7`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_mentor`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_mentor`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul realizează puntea de legătură între Odoo și aplicația de contabilitate WinMentor. Permite exportul datelor din Odoo (parteneri, produse și facturi) într-un format pe care WinMentor îl poate prelua prin funcția sa de „Import date din alte aplicații". Astfel, companiile care țin contabilitatea în Mentor pot transfera documentele generate în Odoo fără reintroducere manuală, pe baza unor mapări configurate în prealabil (CUI partener, cod articol, gestiune, conturi contabile și serii de facturi).

#### 2. Funcționalități Cheie

- Export de date din Odoo pentru a fi importate în WinMentor.
- Export de facturi de intrare, preluate în Mentor prin meniul MENTOR → Intrări → Import date din alte aplicații (submeniul „Facturi Intrare", cu opțiunea „Carnet NIR").
- Maparea partenerilor existenți pe baza CUI-ului completat ca „cod extern" în Mentor.
- Maparea articolelor din Mentor cu produsele Odoo prin codul extern.
- Maparea categoriilor de produse din Odoo cu tipul contabil din Mentor.
- Completarea codului de gestiune Mentor la nivelul fiecărei locații de stoc.
- Extragerea seriei de facturi din numele documentelor (separator „/"), pentru a corespunde cu secvențele de numere din Odoo.
- Trimiterea conturilor contabile către Mentor fără zerourile de la sfârșit.
- Suport pentru completarea codului de vamă din Mentor la exportul facturilor trecute prin vamă.
- Fallback: dacă un partener nu are CUI sau un produs nu are cod, se exportă id-ul intern din Odoo.

#### 3. Dependențe

- `account`
- `product`
- [deltatech_contact](../deltatech_contact/index.md)
- `stock`
- `l10n_ro`

Dependență externă Python: `configparser`.

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de mai jos sunt acoperite de fișierul `readme/DESCRIPTION.md` la nivel de funcționalitate; analiza detaliată a codului nu a fost necesară pentru Sumar și Funcționalități Cheie. Pe baza fișierului `__manifest__.py`, modulul include un wizard de export (`wizard/export_mentor_view.xml`) și extinde vizualizările pentru produse, locații de stoc și conturi contabile, plus un meniu dedicat Mentor (`views/mentor_menu.xml`).

#### 5. Conexiuni

- [deltatech_contact](../deltatech_contact/index.md): sursa datelor de contact (partenerii) folosite la export și maparea prin cod extern / CUI.
