# Deltatech Markdown Field (localizat la `deltatech_markdown_field/index.md`)

- **Nume Tehnic:** `deltatech_markdown_field`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_markdown_field
- **Cale Locală:** `odoo-addons/deltatech/deltatech_markdown_field`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul adaugă un widget nou de câmp în Odoo — `markdown` — care oferă utilizatorilor o experiență de editare WYSIWYG (bold, italic, titluri, liste, citate, blocuri de cod, link-uri) pentru orice câmp de tip `Text`, în timp ce valoarea stocată în baza de date rămâne text Markdown brut, portabil și ușor de citit sau versionat în afara Odoo.

#### 2. Funcționalități Cheie

- Bară de instrumente WYSIWYG: bold, italic, titluri, liste, citate, blocuri de cod și link-uri.
- Stochează Markdown brut — portabil, prietenos pentru diff-uri și lizibil oriunde.
- Conversie instantanee Markdown ↔ HTML, complet în browser (fără dependențe server la runtime): la încărcare se folosește biblioteca [marked](https://marked.js.org/) (Markdown → HTML), iar la salvare [turndown](https://github.com/mixmark-io/turndown) (HTML → Markdown).
- Ambele biblioteci sunt incluse local ca build-uri UMD, deci modulul funcționează offline, fără CDN extern.
- Respectă starea `readonly`: în modul doar-citire afișează Markdown-ul randat ca HTML, fără bara de instrumente.
- Înălțime minimă configurabilă a editorului, prin opțiunea `min_height`.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

*Notă: conform priorității Readme din `schema.md`, secțiunea 1 și 2 provin din `readme/DESCRIPTION.md`; analiza codului de mai jos e adăugată suplimentar deoarece modulul e pur front-end (fără modele Python) și componentele tehnice relevante sunt exclusiv widget-ul OWL.*

**Componente Frontend (OWL)**

- `markdown_field.esm.js`: definește widget-ul de câmp `markdown` (componentă OWL) care leagă un `Text` field de un editor WYSIWYG; convertește Markdown → HTML la încărcare (`marked`) și HTML → Markdown la salvare (`turndown`); acceptă opțiunea `min_height` și respectă `readonly`.
- `markdown_field.xml`: template-ul QWeb/OWL al widget-ului (bara de instrumente și zona de editare).
- `markdown_field.scss`: stilurile widget-ului.
- `lib/marked/marked.min.js`, `lib/turndown/turndown.umd.js`: biblioteci JavaScript vendorizate (build-uri UMD), incluse local pentru a evita orice dependență de CDN.

Modulul nu definește modele Python, vizualizări XML de date sau acțiuni automate/server — este strict un widget de câmp, activat prin atributul `widget="markdown"` pe orice câmp `Text` existent.

**Utilizare**

```xml
<field name="notes" widget="markdown"/>
<field name="notes" widget="markdown" options="{'min_height': 300}"/>
```

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale specifice către alte module — este un widget generic, reutilizabil de orice modul care are un câmp `Text` și dorește editare Markdown WYSIWYG.
