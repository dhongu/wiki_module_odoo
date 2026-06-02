# Backup Attachments (localizat la `deltatech_backup_attachment/index.md`)

- **Nume Tehnic:** `deltatech_backup_attachment`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_backup_attachment
- **Cale Locală:** `odoo-addons/deltatech/deltatech_backup_attachment`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul permite salvarea (backup) a atașamentelor din Odoo pe baza unui filtru de tip domeniu. Utilizatorul alege ce categorii de fișiere dorește să exporte (de exemplu, excluzând imaginile PNG/JPEG sau fișierele PDF) și obține o arhivă cu fișierele selectate. Este util pentru a face copii de siguranță selective ale documentelor stocate, fără a descărca toate atașamentele din sistem.

#### 2. Funcționalități Cheie

- Selectarea atașamentelor de exportat pe baza unui filtru de tip domeniu (ex.: `[("mimetype","not in",["image/png", "image/jpeg","application/pdf"])]`).
- Filtrare avansată după model, câmp sau alte criterii (ex.: `[('res_model','not ilike','product'),('res_field','like','%')]`).
- Generarea unei arhive cu fișierele care corespund filtrului.

#### 3. Dependențe

- `web`
- `base`

#### 4. Componente Cheie

Documentația pentru acest modul a fost generată pe baza fișierului `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune a fost omisă deoarece nu este solicitată explicit în Readme.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module cu pagină wiki existentă.
