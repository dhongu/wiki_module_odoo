# B2B Price Tiers (Prețuri pe trepte de cantitate B2B)

- **Nume Tehnic:** `deltatech_b2b_price_tier`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_b2b_price_tier
- **Cale Locală:** `odoo-addons/bitshop/deltatech_b2b_price_tier`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Afișează pe pagina de produs din magazinul online prețul în funcție de cantitate, pentru clienții companie ai portalului B2B: „de la 10 bucăți plătești mai puțin". Treptele provin din regulile obișnuite ale listei de prețuri a clientului, deci tabelul arată exact ce va taxa coșul de cumpărături, fără un preț paralel.

#### 2. Funcționalități Cheie

- Tabelul „Your price by quantity" apare sub preț, cu cantitatea, prețul unitar și economia față de o bucată (în procente).
- Treptele sunt regulile din lista de prețuri a clientului care au **Cantitate minimă** (*Vânzări ▸ Produse ▸ Liste de prețuri*), definite pe produse, categorii sau pe toate produsele.
- Lista de prețuri se atribuie clientului din fila B2B a fișei acestuia.
- Tabelul se afișează doar contactelor unei companii cu cont B2B activ; vizitatorii și clienții retail văd pagina de produs neschimbată.
- Dacă lista nu are reguli cu cantitate minimă pentru produs, se încearcă cantitățile uzuale (1, 5, 10, 25, 50); tabelul se ascunde dacă toate au același preț.
- Limită cunoscută: prețurile sunt afișate așa cum le calculează lista de prețuri, fără a aplica setarea site-ului de afișare cu/fără taxe.

#### 3. Dependențe

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md)

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): metoda `_b2b_price_tiers(pricelist)` returnează lista `{quantity, price, saving}` pe baza regulilor listei de prețuri și a `_get_product_price`.

**Vizualizări**

- `product_price_tiers`: moștenește `website_sale.product` și adaugă tabelul de trepte în `product_details`, doar pentru utilizatori non-publici cu cont B2B activ.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md): oferă contul B2B (`_b2b_is_active`) și lista de prețuri a clientului folosite aici.
- `website_sale`: pagina de produs în care se inserează tabelul.
