# FontAwesome Widget (localizat la `deltatech_widget_fontawesome/index.md`)

- **Nume Tehnic:** `deltatech_widget_fontawesome`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_widget_fontawesome
- **Cale Locală:** `odoo-addons/deltatech/deltatech_widget_fontawesome`
- **Ultima Ingestie:** `2026-11-06`

#### 1. Sumar

Odoo stochează pictogramele Font Awesome ca simple nume de clase (de exemplu `fa-truck`), iar un formular le arată ca text brut. Acest modul adaugă un widget de câmp care afișează pictograma în sine, în locul numelui clasei. Este un modul tehnic, mic, destinat altor module și personalizărilor de vizualizări: nu adaugă meniuri sau setări.

#### 2. Funcționalități Cheie

- **Previzualizare pictogramă**: un câmp `char`, `text` sau `selection` care conține numele unei clase Font Awesome este redat ca pictogramă (prefix `fa`), cu numele clasei ca tooltip.
- **Un singur atribut**: se folosește în orice vizualizare formular sau listă prin `<field name="icon" widget="fontawesome"/>`.
- Limitări: widgetul doar afișează pictograma, fără selector sau casetă de introducere, deci valoarea se setează din cod, prin import sau cu alt widget într-o altă vizualizare; câmpul nu trebuie să fie gol, deoarece tooltip-ul se construiește din valoarea stocată, iar o valoare goală generează o eroare JavaScript în vizualizare.
- Descrierea din 19.0.1.0.3 corectează o formulare veche: widgetul este o previzualizare, nu un selector de pictograme.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Componente Web (OWL)**

- `FieldFontAwesome` (`static/src/js/field_fontawesome.esm.js`): componentă OWL înregistrată în categoria `fields` a registry-ului sub numele `fontawesome`, pentru tipurile `char`, `text` și `selection`; afișează valoarea câmpului ca pictogramă (clasa `fa <valoare>`), cu valoarea cu inițială majusculă ca tooltip.
- `fontawesome.FieldFontAwesome` (`static/src/js/field_fontawesome.xml`): șablonul QWeb al componentei, care randează un element `<i>` cu clasa pictogramei.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale către alte module documentate în wiki.
