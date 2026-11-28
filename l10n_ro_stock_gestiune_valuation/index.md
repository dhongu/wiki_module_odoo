# Romania - Gestiuni pe arii de evaluare (localizat la `l10n_ro_stock_gestiune_valuation/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_gestiune_valuation`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_stock_gestiune_valuation
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_gestiune_valuation`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul-punte între gestiunile contabile de stoc și ariile de evaluare. Fiecare gestiune devine automat o arie de evaluare (1:1), iar liniile notelor contabile generate de fluxurile RO poartă gestiunea ca dimensiune contabilă. Astfel soldul de stoc al fiecărei gestiuni se poate citi direct din contabilitate, fără conturi analitice separate. Se instalează automat când ambele module de bază sunt prezente.

#### 2. Funcționalități Cheie

- **Arie de evaluare automată per gestiune:** creată la crearea gestiunii și sincronizată la schimbarea numelui, codului sau companiei; gestiunile create înainte de instalare nu primesc arie automat.
- **Locațiile moștenesc aria:** la asocierea unei locații cu o gestiune, aria locației se aliniază automat.
- **Dimensiune contabilă pe note:** liniile notelor de recepție fără factură (371 = 408) și ale stornării ei, de transfer între gestiuni și de diferențe de preț și de curs primesc `valuation_area_id`, pentru balanțe și analize pe gestiune.
- Modulul nu are ecrane proprii; scopul și verificarea sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md)
- [deltatech_valuation_area](../deltatech_valuation_area/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.gestiune` (extins): `valuation_area_id` (legătură 1:1) și crearea/sincronizarea automată a ariei.
- `stock.location` (extins): aliniază `valuation_area_id` cu aria gestiunii asociate.
- `stock.move` (extins): calculează aria pentru liniile RNI și o injectează pe liniile RNI și pe fiecare latură a notei de transfer inter-gestiune.
- `account.move.line` (extins): completează `valuation_area_id` pe notele de ajustare (diferențe de preț).

**Vizualizări**

Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): furnizează modelul `l10n.ro.gestiune` și fluxurile contabile (recepție fără factură, transfer, diferențe de preț) pe care puntea le extinde.
- [deltatech_valuation_area](../deltatech_valuation_area/index.md): furnizează modelul `valuation.area` și mecanismul de dimensiune contabilă.
