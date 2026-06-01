# Romania - Accize (FR-42) (localizat la `l10n_ro_excise/index.md`)

- **Nume Tehnic:** `l10n_ro_excise`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_excise
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_excise`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

MVP pentru FR-42 — Accize conform Titlului VIII din Codul Fiscal RO. Modulul gestionează categoriile de produse accizabile cu rate și unități de măsură, marcarea produselor cu categorie de accize și cod NC8, și generarea declarațiilor persistente D103 (lunar, antrepozit fiscal) și D120 (trimestrial, importator), calculate automat din facturile de vânzare postate, cu export XML.

## 2. Funcționalități Cheie

- **Categorii produse accizabile** cu rate și unități de măsură (alcool, bere, vinuri, tutun, combustibili, energie electrică) conform HG 2025.
- **Marcarea produselor** cu categorie de accize și cod NC8.
- **Declarații persistente D103** (lunar, antrepozit fiscal) și **D120** (trimestrial, importator).
- **Calcul automat din facturile de vânzare postate** în perioadă, incluzând stornările (semn negativ).
- **Export XML D103/D120.**

## 3. Dependențe

- `account`
- `product`
- `l10n_ro`
- `[[l10n_ro_anaf_base]]`

## 4. Componente Cheie

### Modele

- Model categorie accize: nomenclatorul categoriilor cu rate și unități de măsură.
- Model declarație accize (D103/D120): declarația persistentă pe perioadă cu calcul din facturi și export XML.
- `product.template`: extins cu categorie de accize și cod NC8.

### Vizualizări / Date

- `views/l10n_ro_excise_views.xml`: vizualizările declarațiilor de accize.
- `views/product_template_views.xml`: marcarea produselor accizabile.
- `data/excise_category_data.xml`: nomenclatorul categoriilor de accize.
- `report/d103_xml_template.xml`: șablonul XML pentru declarația D103.

### Acțiuni Automate / Acțiuni Server

*Calculul declarațiilor se realizează la cerere din facturile de vânzare postate în perioadă.*

## 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_environmental_tax]]`
- `[[l10n_ro_cbam]]`
