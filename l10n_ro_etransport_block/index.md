# Romania - Blocare e-Transport (localizat la `l10n_ro_etransport_block/index.md`)

- **Nume Tehnic:** `l10n_ro_etransport_block`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_etransport_block
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_etransport_block`
- **Ultima Ingestie:** `2026-10-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde `l10n_ro_edi_stock` și blochează validarea avizelor care conțin produse cu risc fiscal ridicat până când ANAF confirmă codul UIT. În plus, actualizează automat starea UIT printr-un job programat, fără apăsarea manuală a butonului de preluare a stării. Ajută companiile să respecte obligația e-Transport pentru mărfurile cu risc fiscal ridicat.

#### 2. Funcționalități Cheie

- **Marcarea produselor:** câmpul **Risc fiscal ridicat (e-Transport obligatoriu)** pe fișa produsului, în fila **Contabilitate**, secțiunea „România — e-Transport”. Implicit este debifat. Categorii tipice: combustibili, tutun, alcool, metale prețioase, echipamente IT (peste pragul de valoare).
- **Blocare la validare:** dacă avizul are e-Transport activ și conține cel puțin un produs marcat, validarea este oprită cu o eroare care numește produsele, până când UIT-ul ajunge în starea **Validat** (`stock_validated`). Avizele fără produse marcate nu sunt afectate. Blocarea se aplică pe orice aviz cu e-Transport activ, inclusiv cele de intrare, și este dezactivată în contextul `demo_mode` (date demo, teste).
- **Banner pe aviz:** avertisment portocaliu cât timp validarea este blocată.
- **Avertisment în amonte:** banner informativ pe comenzile de vânzare și de achiziție care conțin produse marcate.
- **Flux:** se marchează produsul, se trimite declarația e-Transport de pe aviz (ANAF returnează UIT, starea devine **Trimis**), UIT-ul este confirmat (**Validat**), apoi avizul se validează. Dacă ANAF respinge declarația, avizul rămâne blocat până la corectarea datelor și retrimitere.
- **Actualizare automată a stării UIT:** acțiunea programată „RO e-Transport: Automatic UIT Status Update” rulează la 30 de minute pentru avizele în starea `stock_sent` ale companiilor cu țara fiscală România. Starea se poate forța și manual cu butonul **Preluare stare**. Erorile ANAF se înregistrează în documentul e-Transport al avizului (fila e-Transport → Documents).

#### 3. Dependențe

- `l10n_ro_edi_stock`
- `purchase`
- `sale`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): câmpul `l10n_ro_high_fiscal_risk`.
- `stock.picking` (extins): câmpul calculat `l10n_ro_high_risk_blocked`, verificarea `_l10n_ro_etransport_check_high_risk`, `button_validate` (apelează verificarea, în afara contextului `demo_mode`) și metoda cron `_l10n_ro_etransport_block_auto_fetch`.
- `sale.order` (extins): câmpul calculat `l10n_ro_has_high_fiscal_risk`, folosit pentru banner.
- `purchase.order` (extins): indicator similar pentru comenzile de achiziție.

**Vizualizări**

- `product_template_view.xml`: câmpul de risc fiscal pe produs.
- `stock_picking_view.xml`: bannerul de blocare pe aviz.
- `sale_order_view.xml`, `purchase_order_view.xml`: bannerul informativ pe comenzi.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_etransport_fetch_status`: „RO e-Transport: Automatic UIT Status Update”, la fiecare 30 de minute, activ implicit; actualizează starea UIT a avizelor în starea `stock_sent`.

#### 5. Conexiuni

- `l10n_ro_edi_stock`: infrastructura RO e-Transport (UIT, stări, preluarea stării), peste care se aplică blocarea.
