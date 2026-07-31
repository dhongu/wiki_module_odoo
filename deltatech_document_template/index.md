# Deltatech Document Template (localizat la `deltatech_document_template/index.md`)

- **Nume Tehnic:** `deltatech_document_template`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_document_template
- **Cale Locală:** `odoo-addons/bitshop/deltatech_document_template`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

`deltatech_document_template` oferă un motor generic și reutilizabil pentru definirea de șabloane de documente și generarea de documente finale pornind de la acestea, în Odoo 19. Modulul este agnostic față de domeniul de business și poate viza orice model prin `res_model`/`res_id`. Suportă conținut mixt (HTML manual, rapoarte QWeb încorporate sau vizualizări QWeb), un flux de lucru simplu pe documentele generate și o integrare cu meniul Print care deschide sau reutilizează un document generat unic pentru fiecare șablon și înregistrare țintă.

#### 2. Funcționalități Cheie

- Agnostic față de model: vizează orice model prin setarea `res_model` pe șablon și `res_id` pe documentul generat.
- Asamblare de conținut mixt cu randare QWeb:
  - Secțiuni HTML manuale (fragment QWeb cu substituenți și condiționale).
  - Secțiuni cu rapoarte încorporate (`ir.actions.report` existente pe modelul țintă), curățate pentru a evita învelișurile imbricate `external_layout`/`div.page`.
  - Secțiuni cu vizualizări QWeb încorporate prin `view_id`.
- Întreruperi de pagină între secțiuni (`page-break-before`) atunci când `page_break_after` este setat (niciodată după ultima secțiune).
- Integrare cu meniul Print (acțiune server cu `binding_type = 'report'`): deschide un `document.generated` existent pentru înregistrarea și șablonul active, sau pornește unul nou dacă nu există încă.
- Unicitate impusă: un singur document generat per (`template_id`, `res_model`, `res_id`), printr-o constrângere Python (fără `_sql_constraints` în Odoo 19).
- Flux de lucru clar cu vizibilitate a butoanelor în funcție de stare: Generate (Draft/Generated), Validate (doar Generated), Reset to Draft (Generated/Validated), Print PDF (Generated/Validated).
- Tipărirea atașează automat PDF-ul rezultat (sau HTML ca alternativă) la înregistrarea țintă `res_model`/`res_id`.
- Integrare cu chatter-ul: la crearea unui document generat se postează automat o notă cu link către documentul generat pe chatter-ul înregistrării țintă.

#### 3. Dependențe

- `base`
- `mail`
- `website`
- `html_editor`
- `html_builder`

#### 4. Componente Cheie

**Modele**

- `document.template`: Definește modelul țintă (`res_model`), lista ordonată de secțiuni (`section_ids`) și poate înregistra o acțiune server pe meniul Print al modelului țintă (`server_action_id`).
- `document.template.section`: O bucată de conținut a unui șablon, ordonată prin `sequence`. Tipul de conținut (`content_type`) poate fi `html` (HTML manual în `body_html`), `report` (`report_id`) sau `view` (`view_id`); `page_break_after` inserează o întrerupere de pagină după secțiune.
- `document.generated`: Instanțiază un șablon pentru o înregistrare specifică (`res_id`). Concatenează toate secțiunile în `body` (cu randare QWeb și curățarea rapoartelor încorporate), are stările Draft → Generated → Validated și acțiunile `action_generate()`, `action_validate()`, `action_reset_to_draft()`, `action_print_pdf()`.

**Vizualizări**

- Templates: vizualizări tree și form pentru a defini `res_model` și a gestiona secțiunile inline; button box pentru a adăuga/elimina acțiunea server din meniul Print.
- Sections: tree și form de sine stătătoare; câmpurile afișate depind de `content_type` (report/view/body_html); widgetul HTML are vizualizare cod și substituenți dinamici activați, plus buton „Clear Report".
- Generated Documents: tree și form cu butoane de header pentru flux și tipărire; vizibilitatea butoanelor se adaptează la stare; `body` afișat într-un tab de notebook pentru revizuire/editare.
- Meniuri sub Settings → Technical → Document Templates: Templates, Sections, Generated Documents.
- `report_document_generated_action`: raport QWeb PDF dedicat care învelește `body` în layout-ul extern standard, evitând învelișuri suplimentare de pagină pentru a nu duplica rapoartele încorporate.

**Acțiuni Automate / Acțiuni Server**

- Acțiune server pe model (`ir.actions.server`, `binding_type='report'`): înregistrată per șablon, apare sub meniul Print al modelului țintă. La invocare deschide `document.generated` existent pentru (`template_id`, `res_model`, `active_id`) dacă există; altfel deschide formularul de creare cu valori implicite (`default_template_id`, `default_res_model`, `default_res_id`).

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale către alte module cu pagină wiki. Modulul este generic și poate viza orice model prin `res_model`/`res_id`.
