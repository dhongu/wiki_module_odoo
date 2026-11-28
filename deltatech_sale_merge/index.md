# Sale Merge (localizat la `deltatech_sale_merge/index.md`)

- **Nume Tehnic:** `deltatech_sale_merge`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_merge
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_merge`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Unește mai multe oferte ale aceluiași client într-una singură, direct din lista de oferte. Ofertele unite sunt anulate (nu șterse) și legate de oferta țintă, iar în chatter rămâne istoricul operației.

#### 2. Funcționalități Cheie

- Din **Vânzări > Comenzi > Oferte** se selectează două sau mai multe oferte și se alege *Acțiuni > Merge orders*.
- Ținta unirii: cea mai veche ofertă selectată, una dintre cele selectate sau o ofertă nouă.
- Liniile identice (același produs, descriere, UM, preț, discount, taxe și distribuție analitică) pot fi adunate sau se pot păstra toate liniile; opțional se adaugă o secțiune cu numărul fiecărei oferte unite.
- Pe fila *Other Info*, oferta țintă arată *Merged From*, iar ofertele anulate arată *Merged Into*; referința clientului și documentul sursă strâng valorile tuturor ofertelor.
- Unirea se oprește cu mesaj clar, fără nicio modificare, dacă ofertele diferă prin companie, client sau adrese, monedă, listă de prețuri, poziție fiscală, termeni de plată, depozit (cu Inventory instalat) sau incoterm, ori dacă una este semnată sau are o plată online începută.
- La adunarea liniilor identice, prețul unitar poate fi recalculat de lista de prețuri pentru noua cantitate.
- Fluxul cu capturi este în fișa consultantului.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.order`: extins cu legăturile *Merged From* / *Merged Into*.
- `sale.order.merge`: wizardul de unire a ofertelor.

**Vizualizări**

- `view_sale_order_merge_form`: formularul wizardului.
- `action_sale_order_merge`: acțiunea *Merge orders* din meniul *Acțiuni* al listei de oferte.
- `view_order_form_merge`: câmpurile de legătură pe fila *Other Info* a ofertei.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `sale`: modulul extinde fluxul standard de oferte.
