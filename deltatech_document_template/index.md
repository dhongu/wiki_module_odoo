# Document Template Engine (localizat la `deltatech_document_template/index.md`)

- **Nume Tehnic:** `deltatech_document_template`
- **Versiune:** `19.0.1.0.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_document_template
- **Cale Locală:** `odoo-addons/bitshop/deltatech_document_template`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

`deltatech_document_template` oferă un motor generic și reutilizabil pentru definirea de șabloane de documente și generarea de documente finale pornind de la acestea, în Odoo 19. Modulul este agnostic față de domeniul de business și poate viza orice model prin `res_model`/`res_id`. Suportă conținut mixt (HTML manual, rapoarte QWeb încorporate sau vizualizări QWeb), un flux de lucru simplu pe documentele generate și o integrare cu meniul Print, care deschide sau reutilizează un document generat unic pentru fiecare șablon și înregistrare țintă.

#### 2. Funcționalități Cheie

- Agnostic față de model: vizează orice model prin `res_model` pe șablon și `res_id` pe documentul generat; modelul este verificat la salvare, nu se mai schimbă după ce șablonul are documente generate, iar un șablon cu documente generate nu se șterge.
- Asamblare de conținut mixt cu randare QWeb:
  - secțiuni HTML manuale (fragment QWeb cu substituenți și condiționale, scrise în vizualizarea cod a editorului);
  - secțiuni cu rapoarte încorporate (`ir.actions.report` existente pe modelul țintă), curățate de antet/subsol și de învelișurile `external_layout`/`div.page`;
  - secțiuni cu vizualizări QWeb încorporate prin `view_id`.
- Întreruperi de pagină între secțiuni cu `page_break_after` (niciodată după ultima secțiune).
- Integrare cu meniul Print (acțiune server cu `binding_type = 'report'`, buton „Add to the 'Print' menu" pe șablon): deschide documentul generat existent pentru înregistrarea și șablonul active sau pornește unul nou în Draft, cu valorile completate.
- Unicitate impusă la nivel de bază de date: un index unic pe (`template_id`, `res_id`) permite un singur document per șablon și înregistrare țintă, inclusiv la creare concurentă; documentele fără țintă nu sunt vizate.
- Flux de lucru Draft → Generated → Validated, impus și pe server: Generate doar din Draft, Validate doar din Generated, Reset to Draft din Generated/Validated; Print PDF în Generated/Validated. La un document validat, corpul, șablonul, ținta și data emiterii sunt blocate până la resetarea la Draft.
- Regenerarea (Reset to Draft, apoi Generate) reconstruiește corpul din șablon; modificările manuale se pierd. O secțiune care nu poate fi randată oprește generarea cu un mesaj care îi conține numele, iar documentul rămâne în Draft.
- Tipărire PDF printr-un raport QWeb dedicat, în layout-ul companiei; PDF-ul se atașează la înregistrarea țintă (doar dacă utilizatorul are drept de scriere pe ea) și apare în câmpul *Printed PDF*, actualizat la fiecare tipărire. Dacă PDF-ul nu poate fi randat, se afișează o eroare clară și nu se atașează nimic.
- Chatter: la crearea unui document generat se postează pe înregistrarea țintă o notă cu link către document, dacă modelul țintă are chatter și utilizatorul poate posta.
- Drepturi: accesul la un document urmează înregistrarea țintă (citire pentru vizualizare, scriere pentru editare/ștergere; documentul fără țintă este vizibil doar creatorului; administratorii nu sunt restricționați). Utilizatorii interni au doar citire pe șabloane și secțiuni; crearea și editarea lor e rezervată administratorilor (`base.group_system`), fiindcă șabloanele conțin cod QWeb.
- Pagină web independentă `/document/generated/<id>`, cu aceeași regulă de acces și editor pe stiva `html_builder`/`html_editor`.
- Meniuri (modul dezvoltator) sub *Setări > Tehnic > Document Templates*: Templates, Sections, Generated Documents.

#### 3. Dependențe

- `base`
- `mail`
- `website`
- `html_editor`
- `html_builder`

#### 4. Componente Cheie

**Modele**

- `document.template`: definește modelul țintă (`res_model`), lista ordonată de secțiuni (`section_ids`) și poate înregistra o acțiune server pe meniul Print al modelului țintă (`server_action_id`).
- `document.template.section`: o bucată de conținut a unui șablon, ordonată prin `sequence`; `content_type` poate fi `html` (`body_html`), `report` (`report_id`) sau `view` (`view_id`); `page_break_after` inserează o întrerupere de pagină.
- `document.generated`: instanțiază un șablon pentru o înregistrare (`res_id`). Concatenează secțiunile în `body`, are stările Draft → Generated → Validated, câmpul `attachment_id` (*Printed PDF*) și acțiunile `action_generate()`, `action_validate()`, `action_reset_to_draft()`, `action_print_pdf()`.

**Vizualizări**

- Templates: tree și form pentru definirea `res_model` și gestionarea secțiunilor inline; button box pentru adăugarea/eliminarea acțiunii din meniul Print.
- Sections: tree și form de sine stătătoare; câmpurile depind de `content_type`; widgetul HTML are vizualizare cod și substituenți dinamici, plus butonul „Clear Report".
- Generated Documents: tree și form cu butoane de flux și tipărire; `body` într-un tab pentru revizuire/editare.
- `report_document_generated_action`: raport QWeb PDF dedicat, care învelește `body` în layout-ul extern standard, fără învelișuri suplimentare de pagină.
- `document_generated_standalone`: pagina web independentă a documentului generat.

**Acțiuni Automate / Acțiuni Server**

- Acțiune server pe model (`ir.actions.server`, `binding_type='report'`): creată per șablon, apare în meniul Print al modelului țintă. Deschide `document.generated` existent pentru (`template_id`, `res_model`, `active_id`), altfel formularul de creare cu `default_template_id`, `default_res_model`, `default_res_id`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină wiki. Modulul este generic și poate viza orice model prin `res_model`/`res_id`; singurele legături sunt dependențele din manifest (`mail` pentru nota din chatter, `website` pentru pagina web a documentului, `html_editor`/`html_builder` pentru editor).
