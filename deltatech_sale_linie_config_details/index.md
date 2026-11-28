# Sale Line Configuration Details (localizat la `deltatech_sale_linie_config_details/index.md`)

- **Nume Tehnic:** `deltatech_sale_linie_config_details`
- **Versiune:** `20.0.1.1.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_linie_config_details
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_linie_config_details`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Păstrează configurația produsului vândut pe o linie de comandă (dimensiuni, profil, culoare, părți, imagini de machetă) ca date structurate și o arată vânzătorului dintr-o pictogramă **Detalii** de pe linie. Conectorii și importatorii de marketplace scriu configurația primită într-un câmp comun, în loc să-și inventeze fiecare câmp și popup propriu.

#### 2. Funcționalități Cheie

- Câmpul JSON `config_details` pe liniile de comandă, copiat odată cu linia la duplicarea comenzii.
- Pictograma **Detalii** (ⓘ) într-o coloană îngustă a liniilor, vizibilă doar pe liniile cu detalii.
- Popup cu detaliile ca tabel compact, câte un rând pe grup; valorile apar ca `cheie: valoare`, grupurile imbricate pe linii compacte, imaginile cu legătura *Open image*.
- Sigur: toate textele sunt escapate și nimic nu este evaluat ca cod.
- Citește formatele scrise de importatorii vechi (text JSON sau text de listă Python) și convertește detaliile unei baze venite din 19.0 la upgrade.
- Ajutoare pentru rapoartele de proiect: `get_html_config_details()` și `get_images_config_detail()`.
- Detaliile nu se pot scrie din interfață, ci doar de conectori; modulul nu are setări și nici meniu. Nu apar pe ofertă, aviz sau factură standard.
- Formatul câmpului: listă de grupuri `{"name": ..., "value": ...}`; cheia `id` nu se afișează, iar cheile `image` și `src` se afișează ca imagini.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.order.line`: extins cu câmpul `config_details` (JSON) și metodele ajutătoare pentru rapoarte.
- `sale.order.line.config.details`: model tranzitoriu din spatele popup-ului **Config Details**.

**Vizualizări**

- `sale_order_view_form`: coloana cu pictograma **Detalii** în liniile comenzii.
- `sale_order_line_config_details_form`: popup-ul cu tabelul detaliilor.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- Conectori de proiect (configuratoare de ferestre, importatori de marketplace) scriu în `config_details`; modulul este baza lor comună.
