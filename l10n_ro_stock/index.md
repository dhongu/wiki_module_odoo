# Romania - Stock (localizat la `l10n_ro_stock/index.md`)

- **Nume Tehnic:** `l10n_ro_stock`
- **Versiune:** `20.0.0.4.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_stock
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_stock`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Acest modul simplifică procesul de "Consum" și "Dare în folosință" a materialelor și obiectelor de inventar, adăugând automat locațiile și tipurile de operațiuni de stoc necesare pentru fiecare depozit nou creat al companiilor cu contabilitate românească. Practic, oferă cadrul minim de stoc pentru mișcările specifice de scoatere din gestiune a materialelor consumate în producție/exploatare sau a obiectelor de inventar date în folosință angajaților.

#### 2. Funcționalități Cheie

- Creează automat, la nivel de companie, două locații de stoc dedicate: "Consum" (`usage: consume`) și "Dare în folosință" (`usage: usage_giving`) — o singură pereche per companie cu contabilitate românească (funcțiile `create_missing_consume_location` / `create_missing_usage_location` completează locațiile lipsă și la instalare/actualizare, nu doar la crearea companiei).
- Pentru fiecare depozit (`stock.warehouse`) al unei companii românești, generează automat câte un tip de operațiune intern dedicat pentru "Consum" (cod secvență `CONS`, barcode `<COD_DEPOZIT>-CONSUME`) și pentru "Dare în Folosință" (cod secvență `USAGE`, barcode `<COD_DEPOZIT>-USAGE`), fiecare cu propria secvență de numerotare (`<cod_depozit>/CONS/` respectiv `<cod_depozit>/USAGE/`); tipurile de operațiuni sunt vizibile (needitabile) pe formularul depozitului, lângă tipul de operațiune de ieșire.
- Mișcările de stoc către locațiile "Consum" / "Dare în folosință" sunt tratate corect ca ieșiri (`_is_outgoing`), iar cele dinspre aceste locații ca intrări (`_is_incoming`), astfel încât rapoartele și valorizarea de stoc să le clasifice consecvent.
- Adaugă pe fișa produsului (și pe varianta de produs) câmpul "Greutate Netă" (`l10n_ro_net_weight`), afișat lângă câmpul de volum pe formularul de produs, cu unitatea de măsură de greutate configurată la nivel de sistem.

#### 3. Dependențe

- `stock`
- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.warehouse` (extins, cu `l10n.ro.mixin`): câmpurile `l10n_ro_consume_type_id` / `l10n_ro_usage_type_id` (tipuri de operațiuni pentru consum/dare în folosință); suprascrie `_get_picking_type_create_values`, `_get_picking_type_update_values`, `_get_sequence_values` și `_update_name_and_code` pentru a crea/actualiza automat aceste tipuri de operațiuni și secvențele lor pentru companiile românești.
- `stock.location` (extins, cu `l10n.ro.mixin`): adaugă valorile `usage_giving` ("Usage Giving") și `consume` ("Consume") la selecția `usage`, cu ștergere sigură (`ondelete: set default`).
- `stock.move` (extins): `_is_incoming` / `_is_outgoing` recunosc locațiile de tip `usage_giving`/`consume` ca intrare, respectiv ieșire.
- `res.company` (extins): câmpurile `l10n_ro_usage_location_id` / `l10n_ro_consume_location_id` (readonly, necopiate); metodele `create_missing_usage_location` / `create_missing_consume_location` (rulate la instalare, prin `data/stock_data.xml`) și `_create_usage_location` / `_create_consume_location` creează locațiile lipsă pentru companiile cu `l10n_ro_accounting = True`; suprascrie `_create_per_company_locations` pentru a le crea automat la înființarea unei companii noi.
- `product.template` / `product.product` (extinse, cu `l10n.ro.mixin`): câmpul `l10n_ro_net_weight` (Greutate Netă) — pe șablon e calculat/inversat din variantele produsului, pe variantă e stocat direct; `l10n_ro_net_weight_uom_name` afișează eticheta unității de măsură de greutate configurate.

**Vizualizări**

- `view_warehouse` (moștenire pe `stock.view_warehouse`): afișează, readonly, câmpurile `l10n_ro_consume_type_id` și `l10n_ro_usage_type_id` lângă tipul de operațiune de ieșire al depozitului.
- `l10n_ro_product_template_form_inherit` (moștenire pe `product.product_template_form_view`): adaugă câmpul "Greutate Netă" (`l10n_ro_net_weight`) și eticheta unității de măsură, lângă câmpul de volum, ascuns când există mai multe variante și nu se editează o variantă anume.

**Acțiuni Automate / Acțiuni Server**

- La instalare/actualizare, `data/stock_data.xml` apelează direct (via `<function>`) `res.company.create_missing_consume_location` și `create_missing_usage_location` — completează locațiile de consum/dare în folosință lipsă pentru toate companiile cu contabilitate românească; nu sunt `ir.cron` sau `base.automation`, ci funcții rulate o singură dată la (re)instalarea modulului.

#### 5. Conexiuni

- [l10n_ro_config](../l10n_ro_config/index.md): dependința directă, oferă mixin-ul `l10n.ro.mixin` și câmpul `l10n_ro_accounting` folosite pentru a limita comportamentul la companiile cu contabilitate românească.
- `stock`: dependința directă, extinde `stock.warehouse`, `stock.location` și `stock.move`.
