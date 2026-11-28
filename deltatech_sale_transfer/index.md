# Sale Prepare Transfer (localizat la `deltatech_sale_transfer/index.md`)

- **Nume Tehnic:** `deltatech_sale_transfer`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_transfer
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_transfer`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

La confirmarea comenzii de vânzare, modulul verifică stocul din celelalte depozite și, dacă cantitatea cerută nu este disponibilă în depozitul comenzii, generează automat transferuri între depozite pentru diferență. Astfel marfa lipsă este adusă în depozitul de livrare fără intervenție manuală.

#### 2. Funcționalități Cheie

- La validarea comenzii se verifică stocul liber din alte depozite și se creează transfer pentru cantitatea lipsă.
- Deficitul se calculează în unitatea de măsură a produsului (cu conversia unității din linia de vânzare), este limitat la stocul rămas în depozitul sursă și ține cont de stocul deja folosit de liniile repetate ale aceluiași produs (corecție din 20.0.1.0.2).
- Pe depozit se configurează tipul de operațiune pentru transferul automat (**Type auto transfer**), gruparea transferului cu livrarea și confirmarea automată.
- Transferul poate fi validat automat: se verifică disponibilitatea completă (altfel apare eroare) și se postează un mesaj în chatter.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `sale.order`: suprascrie `action_confirm` și pregătește transferul (`prepare_transfer`).
- `stock.picking`: metoda `auto_transfer` rezervă, completează cantitățile și validează transferul.
- `stock.warehouse`: câmpurile `pick_type_auto_transfer_id`, `group_transfer_with_delivery`, `auto_confirm_transfer`.

**Vizualizări**

- `view_warehouse`: câmpurile de configurare adăugate pe formularul depozitului, după tipul de ieșire.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- Nu există legături funcționale cu alte module wiki.
