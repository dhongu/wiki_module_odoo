# Romania - Taxare inversă art. 331 în punctul de vânzare (localizat la `l10n_ro_reverse_charge_331_pos/index.md`)

- **Nume Tehnic:** `l10n_ro_reverse_charge_331_pos`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_reverse_charge_331_pos`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reverse_charge_331_pos`
- **Ultima Ingestie:** `2026-09-12`

#### 1. Sumar

Acest modul ține poziția fiscală de taxare inversă art. 331 în afara accesului casierului din Punctul de Vânzare (POS), atunci când cumpărătorul nu este înregistrat în scopuri de TVA. Butonul de poziție fiscală din POS listează în mod normal toate regimurile configurate pe casă, indiferent de clientul comenzii — singura cale prin care un regim art. 331 ar putea ajunge pe o vânzare căreia nu i se cuvine. Modulul elimină aceste regimuri din listă până când comanda are un client înregistrat conform art. 316 și refuză să moștenească o astfel de poziție de la un partener al cărui statut de TVA o contrazice. Filtrează opțiunile disponibile, în loc să blocheze ulterior — decizia rămâne a datelor, nu a operatorului de la casă.

#### 2. Funcționalități Cheie

- Ascunde regimurile fiscale art. 331 din dialogul „Choose the tax you want to apply” cât timp beneficiarul comenzii nu este înregistrat în scopuri de TVA (art. 316).
- La schimbarea clientului pe comandă (`updatePricelistAndFiscalPosition`), anulează automat o poziție art. 331 deja aplicată dacă noul client nu este înregistrat în scopuri de TVA.
- Criteriul de „înregistrat în scopuri de TVA” folosește câmpul `l10n_ro_vat_subjected` al partenerului, cu fallback pe prefixul `RO` al codului TVA dacă acel câmp nu e disponibil în payload-ul POS — aceeași logică e oglindită în Python (`res.partner`) și JavaScript, pentru a nu diverge tăcut.
- Extinde datele încărcate în POS: marcajul `l10n_ro_reverse_charge_331` pe poziția fiscală și statutul de TVA al partenerului, altfel indisponibile pe ecranul de vânzare.
- Nu afectează notele contabile de închidere a sesiunii (tip `entry`, nu documente de vânzare); un bon facturat totuși cu regim art. 331 pentru un cumpărător neînregistrat rămâne blocat la validare de garda din `l10n_ro_reverse_charge_331` (`account.move._post`).

#### 3. Dependențe

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md)
- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `account.fiscal.position` (extindere): adaugă `l10n_ro_reverse_charge_331` la câmpurile încărcate în POS, astfel încât marcajul art. 331 să însoțească poziția fiscală pe fiecare casă.
- `res.partner` (extindere): adaugă statutul de TVA (`l10n_ro_vat_subjected`) la câmpurile încărcate în POS, ca decizia de filtrare să nu depindă de o alegere manuală a operatorului.

**Cod JavaScript (frontend POS)**

- `pos_order.esm.js`: expune `isVatRegistered(partner)` (oglindă a verificării Python) și corectează `PosOrder.updatePricelistAndFiscalPosition` — anulează o poziție art. 331 dacă noul client nu e înregistrat în scopuri de TVA.
- `control_buttons.esm.js`: corectează `ControlButtons.clickFiscalPosition` — reconstruiește dialogul de selecție a poziției fiscale excluzând regimurile art. 331 cât timp clientul curent nu e înregistrat, în loc să modifice temporar starea reactivă `config.fiscal_position_ids`.

#### 5. Conexiuni

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md): sursa marcajului fiscal art. 331 și a gărzii de validare pe facturi (`account.move._post`); acest modul doar extinde protecția în ecranul POS. Nu are încă pagină wiki proprie.
- [deltatech_pos_fix](../deltatech_pos_fix/index.md): motivul arhitectural pentru care filtrarea se face la nivelul listei de poziții disponibile, nu la calculul taxelor — cele două module patch-uiesc metode diferite din fluxul POS, iar ordinea de încărcare a asset-urilor între suite nu e o garanție pe care să se bazeze corectitudinea calculului.
