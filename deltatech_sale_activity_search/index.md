# Sale Order activity type search (localizat la `deltatech_sale_activity_search/index.md`)

- **Nume Tehnic:** `deltatech_sale_activity_search`
- **Versiune:** `20.0.0.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_activity_search
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_activity_search`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul reține pe fiecare comandă de vânzare tipurile activităților în așteptare, astfel încât comenzile pot fi găsite după felul urmăririi pe care o așteaptă (de exemplu *Call*, *Email* sau un tip personalizat de activitate).

#### 2. Funcționalități Cheie

- Câmpul stocat **Active Activity Types** pe comanda de vânzare conține numele tipurilor activităților deschise ale comenzii, separate prin virgulă.
- Câmpul se actualizează automat când o activitate este programată, modificată (inclusiv în masă), mutată pe altă comandă sau alt document, marcată ca efectuată sau anulată.
- Căutare: în **Vânzări > Comenzi > Oferte** sau **Comenzi**, din meniul de filtre se alege **Add Custom Filter** și se construiește o condiție pe *Active Activity Types* (de exemplu *contains* „Call”).
- Limitări: modulul nu adaugă vizualizare, filtru sau coloană, câmpul fiind accesibil doar prin filtru personalizat, grupare personalizată sau export. Câmpul se completează doar pentru activitățile create, modificate sau șterse după instalare; comenzile cu activități anterioare rămân goale până se schimbă una dintre ele.

#### 3. Dependențe

- `sale`
- `mail`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extindere): câmpul `active_activity_types` și metoda `set_active_activity_types`.
- `mail.activity` (extindere): `create`, `write` și `unlink` actualizează câmpul comenzilor afectate.

#### 5. Conexiuni

- [deltatech_sale_activity_report](../deltatech_sale_activity_report/index.md): modul înrudit, jurnal zilnic al modificărilor făcute pe comenzi.
