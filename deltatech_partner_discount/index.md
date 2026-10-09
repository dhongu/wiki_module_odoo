# Deltatech Partner Discount (localizat la `deltatech_partner_discount/index.md`)

- **Nume Tehnic:** `deltatech_partner_discount`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_partner_discount
- **Cale Locală:** `odoo-addons/deltatech/deltatech_partner_discount`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul permite stabilirea unui discount propus pentru fiecare partener și îl afișează utilizatorului direct pe factură, ca avertizare vizibilă. Astfel, cei care emit facturi văd imediat discountul recomandat clientului, iar modificarea valorii este rezervată doar utilizatorilor autorizați.

#### 2. Funcționalități Cheie

- Câmp nou „Proposed discount” (procent) pe fișa partenerului, în secțiunea Vânzări.
- Modificarea câmpului este permisă doar utilizatorilor din grupul „Can modify partner discount”.
- Pe factura aflată în starea ciornă apare un banner roșu „Recommended discount: X %”, dacă partenerul comercial are discount diferit de zero.
- Restricția se aplică la crearea și la modificarea partenerului, inclusiv prin import sau RPC, nu doar în formular (corecție din versiunea 19.0.1.0.3); superuserul este exceptat.
- Discountul este doar informativ: nu se aplică automat pe liniile facturii.

#### 3. Dependențe

- `sale`
- `account`

#### 4. Componente Cheie

**Modele**

- `res.partner`: adaugă câmpul `discount` („Proposed discount”); verifică grupul de securitate în `onchange`, `create` și `write`.
- `account.move`: adaugă câmpul `partner_discount`, înrudit cu `commercial_partner_id.discount`.

**Vizualizări**

- `view_partner_form_discount`: afișează câmpul `discount` în grupul `sale` al formularului de partener.
- `invoice_form_discount_propose`: bannerul de discount recomandat, vizibil în ciornă când discountul este nenul.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

**Securitate**

- `group_partner_discount` („Can modify partner discount”): grupul care permite editarea discountului.

#### 5. Conexiuni

- `sale`: câmpul apare în secțiunea de vânzări a partenerului.
- `account`: bannerul este afișat pe formularul facturii.
