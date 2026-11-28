# FontAwesome Widget (localizat la `deltatech_widget_fontawesome/index.md`)

- **Nume Tehnic:** `deltatech_widget_fontawesome`
- **Versiune:** `20.0.1.0.4`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_widget_fontawesome`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_widget_fontawesome`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Odoo stochează pictogramele ca simple nume (de exemplu `fa-truck`), iar un formular le arată ca text. Modulul adaugă un widget de câmp care afișează pictograma în sine, nu numele ei. Este un element tehnic pentru alte module și pentru personalizări de vizualizări; nu adaugă meniuri sau setări.

#### 2. Funcționalități Cheie

- Previzualizare: un câmp `char`, `text` sau `selection` cu numele unei pictograme este redat ca pictogramă, cu o etichetă lizibilă a numelui ca tooltip (de exemplu *Truck* pentru `fa-truck`).
- Compatibilitate cu numele Font Awesome: Odoo 20 nu mai livrează Font Awesome și desenează pictogramele cu Material Symbols; numele salvate (`fa-globe`, `fa fa-globe` sau `globe`) sunt traduse prin maparea oficială Odoo. Se poate salva direct și un nume Material Symbols (`public`, `shopping_cart`).
- Utilizare: `<field name="icon" widget="fontawesome"/>` în formulare sau liste.
- Limitări: widgetul doar afișează (fără selector sau câmp de introducere); un nume Font Awesome fără echivalent în mapare apare doar dacă este și nume valid Material Symbols, altfel nu se afișează nimic; un câmp gol nu afișează nimic.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

Secțiune omisă: `readme/DESCRIPTION.md` este prezent și nu solicită explicit analiza codului pentru componente.

#### 5. Conexiuni

Nu există conexiuni funcționale documentate cu alte pagini din wiki.
