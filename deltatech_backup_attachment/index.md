# Backup Attachments (localizat la `deltatech_backup_attachment/index.md`)

- **Nume Tehnic:** `deltatech_backup_attachment`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_backup_attachment
- **Cale Locală:** `odoo-addons/deltatech/deltatech_backup_attachment`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite administratorilor să exporte o selecție de atașamente Odoo sub forma unei singure arhive ZIP, pe baza unui filtru de tip domeniu. Utilizatorul alege ce fișiere dorește (de exemplu, doar anumite tipuri MIME sau doar fișierele legate de anumite câmpuri) și obține o copie de siguranță selectivă, fără a descărca toate atașamentele din sistem.

#### 2. Funcționalități Cheie

- Exportul atașamentelor filtrate printr-o expresie de domeniu Odoo (tip MIME, model asociat, nume de câmp etc.), din **Setări > Tehnic > Structura bazei de date > Export attachment**.
- Domeniu implicit: `[("mimetype","not in",["application/pdf"])]` (toate atașamentele care nu sunt PDF).
- Exemple de domenii: excluderea imaginilor PNG/JPEG și a PDF-urilor (`[("mimetype","not in",["image/png","image/jpeg","application/pdf"])]`) sau exportul atașamentelor legate de câmpuri, fără produse (`[("res_model","not ilike","product"),("res_field","like","%")]`).
- Toate fișierele găsite sunt împachetate într-o arhivă descărcabilă (`ExportOdooAttachment.zip`), obținută după apăsarea butonului **Apply** și a butonului de descărcare a fișierului.
- Arhiva păstrează calea internă de stocare a fiecărui fișier (`store_fname`), ceea ce o face potrivită pentru copii în afara sistemului sau pentru migrări.
- Sunt incluse doar fișierele prezente fizic pe disc (`store_fname` completat și fișier existent); atașamentele stocate în baza de date sunt omise fără avertisment.

#### 3. Dependențe

- `web`
- `base`

#### 4. Componente Cheie

Documentația pentru acest modul a fost generată pe baza fișierului `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune a fost omisă, deoarece nu este solicitată explicit în Readme.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module cu pagină wiki existentă.
