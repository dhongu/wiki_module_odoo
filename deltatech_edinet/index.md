# Deltatech EDINET (localizat la `deltatech_edinet/index.md`)

- **Nume Tehnic:** `deltatech_edinet`
- **Versiune:** `19.0.1.2.4`
- **Cale:** `https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_edinet`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_edinet`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul integrează Odoo cu platforma **Infinite EDINET**, permițând schimbul electronic de documente comerciale (EDI). Acesta automatizează schimbul de comenzi de vânzare și de facturi între Odoo și platforma EDINET, reducând efortul manual și riscul de erori. Practic, comenzile de la clienți pot fi preluate automat în Odoo, iar facturile validate pot fi trimise către EDINET cu un singur clic sau în loturi.

#### 2. Funcționalități Cheie

- **Import automat al comenzilor de vânzare:** preia și procesează automat comenzile (ORDERS) din platforma EDINET.
- **Export de facturi:** trimite facturile validate (INVOICE) direct către EDINET, individual sau în lot.
- **Integrare Infinite:** proiectat special pentru a funcționa cu serviciile EDI Infinite.
- **Suport multi-companie:** se pot configura credențiale separate pentru fiecare companie din instanța Odoo.
- **Configurare flexibilă a credențialelor:** la nivel de companie (**Setări > Companii**) sau prin parametri de sistem (`deltatech_edinet.username`, `deltatech_edinet.password`) ca metodă alternativă.

#### 3. Dependențe

- [deltatech_edi](../deltatech_edi/index.md)

Dependențe externe Python: `zeep`, `xmltodict`.

#### 4. Componente Cheie

> Conform `readme/DESCRIPTION.md`, secțiunile de business sunt acoperite mai sus. Următoarele componente sunt sintetizate din `__manifest__.py` și structura modulului, pentru orientare tehnică.

**Vizualizări**

- `views/account_move_view.xml`: extinde formularul de factură (`account.move`) pentru acțiunile de export către EDINET.
- `views/res_config_settings_view.xml`: adaugă în Setări câmpurile pentru credențialele EDINET la nivel de companie.

**Acțiuni Automate / Acțiuni Server**

- `data/ir_cron_data.xml`: definește sarcina programată (`ir.cron`) care preia automat comenzile de vânzare (ORDERS) din EDINET.

#### 5. Conexiuni

- [deltatech_edi](../deltatech_edi/index.md): cadrul EDI de bază pe care se construiește acest conector (dependență directă, hook-uri pe `account.move` și șabloane EDI).
- [deltatech_ediconnect](../deltatech_ediconnect/index.md): conector EDI din aceeași familie de module, ca alternativă/complement pentru alte platforme de schimb electronic de documente.
