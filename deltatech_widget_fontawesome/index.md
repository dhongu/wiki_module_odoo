# FontAwesome Widget (localizat la `deltatech_widget_fontawesome/index.md`)

- **Nume Tehnic:** `deltatech_widget_fontawesome`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_widget_fontawesome`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_widget_fontawesome`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul adaugă un widget de tip „fontawesome” care permite afișarea unei pictograme Font Awesome direct într-un câmp dintr-o vizualizare formular. Se folosește atașând atributul `widget="fontawesome"` unui câmp text, astfel încât valoarea câmpului (numele clasei pictogramei) să fie redată ca pictogramă vizuală în interfața utilizatorului. Este un modul tehnic, mic, destinat dezvoltatorilor care vor să prezinte pictograme într-un mod prietenos în interfața backend Odoo.

#### 2. Funcționalități Cheie

- Pune la dispoziție widgetul `fontawesome` pentru câmpuri în vizualizările formular.
- Se aplică prin `<field name="icon" widget="fontawesome" />`.
- Redă valoarea câmpului ca pictogramă Font Awesome (prefix `fa`).
- Suportă tipurile de câmp `char`, `text` și `selection`.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Componente Web (OWL)**

- `FieldFontAwesome` (`static/src/js/field_fontawesome.esm.js`): componentă OWL înregistrată în categoria `fields` a registry-ului sub numele `fontawesome`; preia valoarea câmpului și o afișează ca pictogramă Font Awesome (clasa `fa <valoare>`).
- `fontawesome.FieldFontAwesome` (`static/src/js/field_fontawesome.xml`): template-ul QWeb asociat componentei, folosit pentru randarea pictogramei.

#### 5. Conexiuni

- Nu sunt identificate conexiuni funcționale cu alte module documentate.
