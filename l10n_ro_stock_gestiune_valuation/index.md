# Romania - Gestiuni pe arii de evaluare (localizat la `l10n_ro_stock_gestiune_valuation/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_gestiune_valuation`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_gestiune_valuation
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_gestiune_valuation`
- **Ultima Ingestie:** `2026-09-12`

#### 1. Sumar

Modulul este puntea automată între gestiunile contabile de stoc și ariile de evaluare din Odoo: fiecare gestiune devine, fără nicio configurare manuală, o arie de evaluare, iar notele contabile generate de fluxurile de stoc specifice României (recepție fără factură 371=408, transfer inter-gestiune prin 481, diferențe de preț) poartă dimensiunea contabilă a gestiunii respective. Astfel, o companie poate obține balanțe și analize contabile pe gestiune, direct din contabilitate, fără raportări separate.

#### 2. Funcționalități Cheie

- Arie de evaluare automată per gestiune — la crearea unei gestiuni se creează automat aria de evaluare 1:1 corespunzătoare (același nume și cod); redenumirea gestiunii sincronizează aria.
- Locațiile moștenesc aria de evaluare — la asocierea unei locații de stoc cu o gestiune, aria de evaluare a locației se aliniază automat la cea a gestiunii.
- Dimensiune contabilă pe notele contabile RO — liniile notelor de recepție fără factură (371=408), de transfer inter-gestiune (prin 481) și de diferențe de preț primesc automat `valuation_area_id` al gestiunii implicate (pe recepție: gestiunea destinație, cu fallback pe gestiunea sursă sau pe aria companiei; pe transfer: aria gestiunii laturii respective).
- Funcționare complet automată — nu există meniu sau ecran de configurare propriu; verificarea se face deschizând o gestiune (câmpul Arie de evaluare este completat automat) sau postând o recepție fără factură (liniile notei 371=408 poartă aria gestiunii destinație).
- Instalare automată (`auto_install`) — modulul se activează singur imediat ce `l10n_ro_stock_gestiune` și `deltatech_valuation_area` sunt ambele prezente în bază.

#### 3. Dependențe

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md)
- [deltatech_valuation_area](../deltatech_valuation_area/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.gestiune` (extindere): adaugă `valuation_area_id` (Many2one către `valuation.area`, legătură 1:1) și garantează crearea/sincronizarea automată a ariei la `create`/`write` (nume, cod, companie).
- `stock.location` (extindere): aliniază automat `valuation_area_id` al locației cu aria gestiunii asociate (`l10n_ro_gestiune_id`), la creare și la schimbarea gestiunii.
- `stock.move` (extindere): calculează aria de evaluare pentru liniile RNI (`_l10n_ro_rni_area` — gestiune destinație, apoi sursă, apoi returul de origine, cu fallback pe aria companiei) și injectează `valuation_area_id` pe liniile RNI și pe liniile de transfer inter-gestiune.
- `account.move.line` (extindere): completează `valuation_area_id` pe liniile notelor de ajustare (diferențe de preț RNI), pornind de la mișcările de stoc aferente.

#### 5. Conexiuni

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): furnizează modelul `l10n.ro.gestiune` și fluxurile contabile RO (RNI, transfer inter-gestiune, diferențe de preț) pe care acest modul le extinde cu dimensiunea de evaluare.
- [deltatech_valuation_area](../deltatech_valuation_area/index.md): furnizează modelul `valuation.area` și mecanismul de dimensiune contabilă pe care acest modul îl leagă 1:1 de gestiuni.
