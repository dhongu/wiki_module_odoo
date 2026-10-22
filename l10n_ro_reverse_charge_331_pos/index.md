# Romania - Taxare inversă art. 331 în punctul de vânzare (localizat la `l10n_ro_reverse_charge_331_pos/index.md`)

- **Nume Tehnic:** `l10n_ro_reverse_charge_331_pos`
- **Versiune:** `19.0.1.1.0`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_reverse_charge_331_pos`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reverse_charge_331_pos`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Acest modul ține poziția fiscală de taxare inversă art. 331 în afara accesului casierului din Punctul de Vânzare (POS), atunci când cumpărătorul nu este înregistrat în scopuri de TVA, și obligă la facturare bonurile care poartă taxare inversă. Butonul de poziție fiscală din POS listează în mod normal toate regimurile configurate pe casă, indiferent de clientul comenzii — singura cale prin care un regim art. 331 ar putea ajunge pe o vânzare căreia nu i se cuvine. Modulul elimină aceste regimuri din listă până când comanda are un client înregistrat conform art. 316 și refuză să moștenească o astfel de poziție de la un partener al cărui statut de TVA o contrazice. Cum bonul fiscal nu documentează o livrare cu taxare inversă, comenzile cu art. 331 se facturează obligatoriu. Filtrează opțiunile disponibile, în loc să blocheze ulterior — decizia rămâne a datelor, nu a operatorului de la casă.

#### 2. Funcționalități Cheie

- Ascunde regimurile fiscale art. 331 din dialogul „Choose the tax you want to apply” cât timp beneficiarul comenzii nu este înregistrat în scopuri de TVA (art. 316).
- La schimbarea clientului pe comandă (`updatePricelistAndFiscalPosition`), anulează automat o poziție art. 331 deja aplicată dacă noul client nu este înregistrat în scopuri de TVA.
- Criteriul de „înregistrat în scopuri de TVA” folosește câmpul `l10n_ro_vat_subjected` al partenerului, cu fallback pe prefixul `RO` al codului TVA dacă acel câmp nu e disponibil în payload-ul POS — aceeași logică e oglindită în Python (`res.partner`) și JavaScript, pentru a nu diverge tăcut.
- Facturare obligatorie pentru comenzile cu taxare inversă art. 331: ecranul de plată bifează opțiunea de factură și nu mai permite debifarea (afișează o notificare de avertizare).
- Garda pe server: comenzile ajunse fără bifa de factură (sesiuni deschise înainte de actualizare, sincronizare offline, alt client API) sunt facturate automat la procesare, nu respinse — bonul e deja emis, iar refuzul ar pierde vânzarea.
- Returul unei comenzi care nu a fost niciodată facturată rămâne pe bon, ca vânzarea inițială.
- Un bon cu taxare inversă fără client nu poate fi facturat (fără beneficiar înregistrat nu există taxare inversă): comanda primește o notă în chatter, ca TVA-ul să poată fi regularizat de contabil.
- Extinde datele încărcate în POS: marcajul art. 331 pe poziția fiscală și pe taxă, plus statutul de TVA al partenerului, altfel indisponibile pe ecranul de vânzare.
- Nu afectează notele contabile de închidere a sesiunii (tip `entry`, nu documente de vânzare); un bon facturat totuși cu regim art. 331 pentru un cumpărător neînregistrat rămâne blocat la validare de garda din `l10n_ro_reverse_charge_331` (`account.move._post`).
- Se instalează automat (`auto_install`) când sunt prezente ambele dependențe.

#### 3. Dependențe

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md)
- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `pos.order` (extindere): `_l10n_ro_requires_invoice_331()` stabilește dacă liniile (taxele înainte/după poziția fiscală) conțin taxare inversă art. 331; `_process_saved_order` forțează `to_invoice` sau, fără client, postează o notă de regularizare TVA.
- `account.tax` (extindere): adaugă `l10n_ro_is_reverse_charge_331` la câmpurile încărcate în POS, ca ecranul de plată să știe că bonul trebuie facturat.
- `account.fiscal.position` (extindere): adaugă `l10n_ro_reverse_charge_331` la câmpurile încărcate în POS, astfel încât marcajul art. 331 să însoțească poziția fiscală pe fiecare casă.
- `res.partner` (extindere): adaugă statutul de TVA (`l10n_ro_vat_subjected`) la câmpurile încărcate în POS, ca decizia de filtrare să nu depindă de o alegere manuală a operatorului.

**Cod JavaScript (frontend POS)**

- `pos_order.esm.js`: expune `isVatRegistered(partner)` (oglindă a verificării Python), indicatorul `l10nRoRequiresInvoice331` și corectează `PosOrder.updatePricelistAndFiscalPosition` — anulează o poziție art. 331 dacă noul client nu e înregistrat în scopuri de TVA.
- `control_buttons.esm.js`: corectează `ControlButtons.clickFiscalPosition` — reconstruiește dialogul de selecție a poziției fiscale excluzând regimurile art. 331 cât timp clientul curent nu e înregistrat, în loc să modifice temporar starea reactivă `config.fiscal_position_ids`.
- `payment_screen.esm.js`: patch pe `PaymentScreen` — bifează factura la intrare (`setup`) și blochează debifarea (`toggleIsToInvoice`) pentru comenzile cu art. 331.

**Vizualizări**

- Nu definește vizualizări XML; modificările sunt în interfața POS (assets `point_of_sale._assets_pos`).

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md): sursa marcajului fiscal art. 331 și a gărzii de validare pe facturi (`account.move._post`); acest modul doar extinde protecția în ecranul POS.
- [deltatech_pos_fix](../deltatech_pos_fix/index.md): motivul arhitectural pentru care filtrarea se face la nivelul listei de poziții disponibile, nu la calculul taxelor — cele două module patch-uiesc metode diferite din fluxul POS, iar ordinea de încărcare a asset-urilor între suite nu e o garanție pe care să se bazeze corectitudinea calculului.
