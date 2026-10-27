# Import Document Lines

- **Nume Tehnic:** `deltatech_import_lines`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_import_lines
- **Cale Locală:** `odoo-addons/deltatech/deltatech_import_lines`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite încărcarea liniilor unui document dintr-un fișier Excel sau text, direct din document, fără ecranul generic de import. Operatorul alege fișierul, spune ce conține fiecare coloană, vede în previzualizare rândurile cu probleme și abia apoi importă. Modulul conține asistentul și mapările salvate; butoanele de pe documente sunt adăugate de modulele-punte, instalate automat odată cu aplicația respectivă.

#### 2. Funcționalități Cheie

- **Formate acceptate:** XLSX, XLS, ODS, CSV și TXT, citite cu cititoarele importului standard; separatorul pentru CSV/TXT este detectat sau setat manual.
- **Mapare de coloane:** fiecare coloană se importă ca produs, cantitate, preț unitar, discount (%), unitate de măsură, lot/număr de serie, descriere sau se ignoră. Coloanele cu titluri uzuale (Cod, Cantitate, Preț, U.M., Lot...) sunt mapate automat. Produsul și cantitatea sunt obligatorii.
- **Identificarea produsului** după referință internă, cod de bare sau nume (formatul `[COD] Nume` este rezolvat după cod).
- **Previzualizare** cu starea fiecărui rând: găsit, produs negăsit, mai multe produse, cantitate sau număr invalid, unitate de măsură invalidă, eroare de lot/serie. Importul e blocat cât timp există erori, dacă nu e bifat **Skip Rows With Errors**.
- **Mapări salvate** pe tip de document și, opțional, pe partener; asistentul propune întâi maparea partenerului, apoi pe cea generică a tipului de document. Se pot gestiona din **Configurare → Mapări import linii** (în Vânzări, Achiziții, Inventar).
- **Numere** cu virgulă sau punct zecimal (`1,5`, `1.234,50`, `1,234.50`); forma ambiguă `1,234` este semnalată ca eroare, nu ghicită.
- **Liniile se creează prin documentul însuși**, deci prețurile, taxele și descrierile se completează ca la o linie adăugată manual; prețul și discountul vin din fișier doar dacă au coloane mapate.
- **Documente acoperite prin punți:** oferte de vânzare, cereri de ofertă (inclusiv după codul produsului la furnizor), recepții/livrări/transferuri interne, inventariere fizică și componentele comenzilor de producție.
- Fluxul detaliat pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `product`
- `base_import`

#### 4. Componente Cheie

**Modele**

- `import.lines.wizard` (+ `.column`, `.row`): asistentul tranzitoriu (stări de alegere fișier, mapare, previzualizare), coloanele detectate și rândurile cu starea lor.
- `import.lines.mapping` (+ `.column`): mapare salvată pe tip de document, partener și companie (multi-company), cu modul de căutare a produsului.
- `import.lines.mixin`: model abstract, contractul dintre asistent și document; punțile îl moștenesc și suprascriu cârligele (verificare stare, ținte de coloane, căutare produse, creare linii).

**Vizualizări**

- `import_lines_wizard_form`: formularul asistentului.
- `import_lines_mapping_list` / `import_lines_mapping_form` / `import_lines_mapping_search`: gestionarea mapărilor salvate (acțiune `action_import_lines_mapping`).

**Acțiuni Automate / Acțiuni Server**

- Nu există. Regulile `ir.rule` multi-company limitează mapările la compania curentă (sau la cele fără companie).

#### 5. Conexiuni

- [deltatech_import_lines_sale](../deltatech_import_lines_sale/index.md): import în ofertele de vânzare.
- [deltatech_import_lines_purchase](../deltatech_import_lines_purchase/index.md): import în cererile de ofertă, inclusiv după codul furnizorului.
- [deltatech_import_lines_stock](../deltatech_import_lines_stock/index.md): import în recepții, livrări, transferuri interne și inventariere fizică.
- [deltatech_import_lines_mrp](../deltatech_import_lines_mrp/index.md): import de componente în comenzile de producție.
