# Report Packaging (localizat la `deltatech_report_packaging/index.md`)

- **Nume Tehnic:** `deltatech_report_packaging`
- **Versiune:** `19.0.1.3.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_report_packaging
- **Cale Locală:** `odoo-addons/deltatech/deltatech_report_packaging`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul calculează automat cantitățile de materiale de ambalare (plastic, lemn, hârtie, PET, sticlă, metal, aluminiu) folosite pentru produsele facturate. Fiecare material are o cantitate la achiziție și una la vânzare, pentru produsele ambalate într-un fel de furnizor și în alt fel la livrare: facturile de la furnizor folosesc prima, facturile către client pe a doua. Materialele se configurează pe produs sau, ca valoare implicită, pe categoria de produs. Cantitățile de pe factură se recalculează la postare, atât timp cât factura este sub actualizare automată, iar dintr-o listă de facturi se poate genera un raport agregat cu totalul materialelor consumate.

#### 2. Funcționalități Cheie

- Configurarea materialelor de ambalare (tip material, „Cantitate achiziție” și „Cantitate vânzare”) pe fișa produsului, în secțiunea „Packaging materials” din fila Inventar; un material folosit într-o singură direcție se lasă cu zero pe cealaltă.
- Configurare pe categoria de produs: un produs fără materiale proprii preia materialele categoriei sale sau ale celei mai apropiate categorii părinte care are configurare. Materialele produsului au prioritate și le înlocuiesc integral pe cele ale categoriei; formularul produsului arată ce moștenește.
- Opțiunea „Fără material de ambalare” pe produs oprește explicit moștenirea de la categorie. Nimic nu se copiază pe produs: regula se aplică la calcul, deci o modificare pe categorie se reflectă imediat pe produse, inclusiv pe cele importate sau venite din site.
- Calcul pe factură = cantitate facturată × cantitatea configurată pe direcția documentului (achiziție pentru facturi furnizor și refuzuri, vânzare pentru facturi client și note de credit); materialele cu zero pe direcția respectivă nu apar.
- Recalculare automată la postare (`action_post`), cât timp comutatorul „Auto-update packaging materials” este activ. Editarea sau ștergerea manuală a unei cantități îl dezactivează, iar corecția supraviețuiește validării facturii.
- Butonul „Refresh” recalculează cantitățile din liniile facturii și readuce factura sub actualizare automată.
- Filă „Packaging materials” pe formularul facturii, cu lista materialelor și cantităților.
- Wizard de raport (acțiune contextuală din lista de facturi) care agregă cantitățile pentru facturile selectate.

#### 3. Dependențe

- `account`
- `product`

#### 4. Componente Cheie

**Modele**

- `product.category` (extindere): adaugă `packaging_material_ids` (materiale implicite pentru produsele categoriei) și `_get_packaging_materials()`, care caută configurarea în categorie și apoi în părinți.
- `product.template` (extindere): adaugă `packaging_material_ids`, `packaging_material_no_inherit` (oprește moștenirea), `inherited_packaging_material_ids` (calculat, afișat când produsul nu are materiale proprii) și `_get_packaging_materials()` (materialele efective: proprii, altfel din categorie).
- `packaging.product.material`: linie de configurare legată de un `product.template` sau de un `product.category`, cu `material_type`, `qty_purchase` și `qty_sale`; `_get_qty(direction)` întoarce cantitatea pe direcția cerută.
- `account.move` (extindere): adaugă `packaging_material_ids`, `packaging_material_auto` (actualizare automată) și `refresh_packaging_material()`; suprascrie `action_post()` pentru recalcularea la postare (nu pentru mișcări de tip `entry`).
- `packaging.invoice.material`: linie cu cantitatea unui material calculată pentru o factură; `create`/`write`/`unlink` scot factura din actualizarea automată la corecție manuală.
- `packaging.report.material` (tranzitoriu, wizard): agregă materialele facturilor selectate (`active_ids`).
- `packaging.report.material.line` (tranzitoriu): liniile de rezultat ale raportului.

**Vizualizări**

- `product_template_form_view`: secțiunea „Packaging materials” în fila Inventar a produsului.
- `product_category_form_view`: secțiunea de materiale pe formularul categoriei de produs.
- `account_move_form_view`: fila „Packaging materials” (ascunsă pentru mișcări de tip `entry`), comutatorul de actualizare automată și butonul „Refresh”.
- `invoice_packaging_material_form`: formular wizard cu două stări (`choose`/`get`) pentru raportul agregat.

**Acțiuni Automate / Acțiuni Server**

- `action_packaging_wizard`: acțiune de fereastră legată (`binding_model_id`) de lista de facturi (`account.move`), care deschide wizard-ul de raport.

**Migrări**

- La upgrade, cantitatea unică existentă este copiată în ambele coloane (achiziție și vânzare), deci comportamentul rămâne identic până la corectarea produselor ambalate diferit.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale suplimentare, în afara dependențelor directe (`account`, `product`).
