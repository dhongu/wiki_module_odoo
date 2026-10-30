# Backup Attachments (localizat la `deltatech_backup_attachment/index.md`)

- **Nume Tehnic:** `deltatech_backup_attachment`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_backup_attachment
- **Cale Locală:** odoo-addons/deltatech/deltatech_backup_attachment
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Modulul permite administratorilor să exporte selectiv atașamentele din Odoo într-o singură arhivă ZIP. Utilizatorul alege fișierele printr-un filtru de tip domeniu — de exemplu doar un anumit tip de fișier, doar cele legate de anumite înregistrări sau stocate pe un anumit câmp — și descarcă arhiva rezultată. Este util pentru copii de siguranță selective, în afara sistemului, sau pentru migrări, fără a descărca toate atașamentele.

#### 2. Funcționalități Cheie

- Export al atașamentelor filtrate cu orice expresie de domeniu Odoo (tip MIME, model asociat, câmp etc.), din **Setări → Tehnic → Structura bazei de date → Export attachment**.
- Domeniul implicit, `[("mimetype","not in",["application/pdf"])]`, exportă toate atașamentele care nu sunt PDF; exemple utile: `[("mimetype","not in",["image/png","image/jpeg","application/pdf"])]` (fără imagini și PDF-uri) sau `[("res_model","not ilike","product"),("res_model","!=","export.attachment"),("res_field","like","%")]` (atașamente legate de câmpuri, fără produse și fără asistentul însuși).
- Fișierele găsite se adună într-o singură arhivă, `ExportOdooAttachment.zip`, descărcabilă din câmpul **File** după mesajul „Export Complete”; **Cancel** închide asistentul.
- Arhiva păstrează calea internă de stocare a fiecărui fișier (`store_fname`), deci e potrivită pentru backup în afara sistemului sau migrare.
- Se includ doar fișierele existente fizic în filestore (`store_fname` completat și fișier prezent pe disc); atașamentele stocate în baza de date sunt omise fără avertisment.

#### 3. Dependențe

- `web`
- `base`

#### 4. Componente Cheie

**Modele**

- `export.attachment` (wizard tranzitoriu): câmpurile `domain`, `data_file`, `name` și `state` (`choose` / `get`); `do_export()` caută în `ir.attachment` după domeniu, scrie fișierele din filestore în ZIP și trece wizardul în pasul de descărcare.

**Vizualizări**

- `wizard/export_attachment_view.xml`: formularul wizardului, în doi pași — alegerea domeniului, apoi descărcarea arhivei.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server; exportul rulează doar la cererea administratorului.

#### 5. Conexiuni

- `base`: exportul citește atașamentele din `ir.attachment`, în filestore-ul Odoo.
