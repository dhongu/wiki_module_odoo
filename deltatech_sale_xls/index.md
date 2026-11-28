# Sale XLS (localizat la `deltatech_sale_xls/index.md`)

- **Nume Tehnic:** `deltatech_sale_xls`
- **Versiune:** `20.0.1.0.4`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_xls`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_xls`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Clienții trimit adesea comanda, sau modificările ei, sub formă de foaie de calcul. Modulul permite agentului de vânzări să exporte liniile unei comenzi de vânzare în Excel și să le importe înapoi în aceeași comandă, cu instrumentele standard Odoo de export și import.

#### 2. Funcționalități Cheie

- Butonul inteligent „Order lines” de pe comanda de vânzare deschide lista liniilor ei (comandă, produs, cantitate, preț unitar); de aici liniile se exportă cu „Export”, iar un fișier se încarcă cu „Import records”, liniile importate intrând în această comandă.
- Import într-o comandă goală: fiecare rând din fișier devine o linie nouă.
- Import într-o comandă cu linii: fiecare rând actualizează linia existentă cu același produs (cantitate, preț și celelalte coloane importate). Produsul se recunoaște după referința internă între paranteze drepte (`[COD] Nume`, ca la export) sau, în lipsă, după numele exact; rândurile cu produs negăsit sau care nu e pe comandă sunt ignorate.
- Hook pentru formula de preț: metoda `use_specific_price_formula` se apelează pe prețurile unitare importate într-o comandă nouă, ca un modul specific clientului să poată aplica propria regulă de preț.
- Limitări: într-o comandă cu linii, rândul unui produs nou este ignorat fără mesaj (nu poate adăuga linie); dacă există două linii cu același produs, importul acelui produs eșuează; fără butonul „Order lines”, comanda se citește din coloana „Order Reference” doar dacă aceasta conține id-ul din baza de date, nu numărul comenzii.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

Secțiunea se bazează pe `readme/DESCRIPTION.md`, care o acoperă funcțional; analiza suplimentară a codului a fost omisă, cu excepția elementelor de mai jos, menționate în Readme.

**Modele**

- `sale.order` (extins): `show_order_lines` deschide lista liniilor comenzii.
- `sale.order.line` (extins): `load` / `_parse_import_data` asociază rândurile importate cu liniile existente după produs; `use_specific_price_formula` este punctul de extensie pentru prețuri.

**Vizualizări**

- `sale_order_form`: adaugă butonul inteligent „Order lines” pe comanda de vânzare.
- `sale_order_line_tree`: lista liniilor (comandă, produs, cantitate, preț) folosită pentru export/import.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_purchase_xls](../deltatech_purchase_xls/index.md): modulul echivalent pentru comenzile de achiziție, cu aceeași logică de import/export a liniilor prin Excel.
