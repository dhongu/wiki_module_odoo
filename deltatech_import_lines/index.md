# Import Document Lines (localizat la `deltatech_import_lines/index.md`)

- **Nume Tehnic:** `deltatech_import_lines`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_import_lines
- **Cale Locală:** `odoo-addons/deltatech/deltatech_import_lines`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Încarcă liniile unui document dintr-un fișier de calcul sau text, direct din document, fără ecranul generic de import. Asistentul citește fișiere XLSX, XLS, ODS, CSV și TXT, iar modulele-punte adaugă importul în fiecare aplicație (vânzări, achiziții, stocuri, producție). Reduce timpul de introducere a comenzilor și al recepțiilor primite de la clienți și furnizori în foi de calcul.

#### 2. Funcționalități Cheie

- **Formate acceptate**: XLSX, XLS, ODS, CSV și TXT; separatorul CSV/TXT este detectat sau setat manual.
- **Mapare coloane**: fiecare coloană devine produs, cantitate, preț unitar, discount, unitate de măsură, lot/serie, descriere sau este ignorată; coloanele cu titluri uzuale (Cod, Cantitate, Preț, UM, Lot) se mapează automat.
- **Potrivire produs** după referință internă, cod de bare sau denumire (formatul `[COD] Denumire` se rezolvă după cod).
- **Previzualizare** cu starea fiecărui rând (găsit, produs negăsit, mai multe produse, cantitate sau număr invalid, UM invalidă, eroare de lot); importul e blocat cât timp există erori, dacă nu se bifează **Ignoră rândurile cu erori**.
- **Mapări salvate** pe tip de document și, opțional, pe partener; asistentul propune întâi maparea partenerului, apoi pe cea generică. Se gestionează din *Configurare > Mapări import linii* în Vânzări, Achiziții și Inventar.
- **Numere** cu virgulă sau punct zecimal; o valoare ambiguă precum `1,234` apare ca eroare, nu e ghicită.
- **Liniile se creează prin document**, deci prețurile, taxele și descrierile se completează ca la adăugarea manuală; prețul și discountul se iau din fișier doar dacă au coloană mapată.
- Punți: `deltatech_import_lines_sale` (oferte), `deltatech_import_lines_purchase` (cereri de ofertă, inclusiv după cod furnizor), [deltatech_import_lines_stock](../deltatech_import_lines_stock/index.md) (transferuri și inventar), `deltatech_import_lines_mrp` (componente ordine de producție).
- Fluxul pas cu pas e în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `product`
- `base_import`

#### 4. Componente Cheie

**Modele**

- `import.lines.wizard`, `import.lines.wizard.column`, `import.lines.wizard.row`: asistentul de import, coloanele și rândurile previzualizate.
- `import.lines.mapping`, `import.lines.mapping.column`: mapările salvate.
- `import.lines.mixin`: logica comună moștenită de documentele care primesc butonul de import.

**Vizualizări**

- `views/import_lines_mapping_view.xml`: lista și formularul mapărilor salvate.
- `wizard/import_lines_wizard_view.xml`: asistentul în pașii fișier, coloane și previzualizare.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_import_lines_stock](../deltatech_import_lines_stock/index.md): puntea pentru transferuri și inventar.
- `deltatech_import_lines_sale`, `deltatech_import_lines_purchase`, `deltatech_import_lines_mrp`: celelalte punți către documente.
