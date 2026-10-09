# Sale Prepare Transfer (localizat la `deltatech_sale_transfer/index.md`)

- **Nume Tehnic:** `deltatech_sale_transfer`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_transfer
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_transfer`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul pregătește automat aprovizionarea între depozite la confirmarea unei comenzi de vânzare. Dacă stocul din depozitul comenzii nu acoperă cantitatea cerută, dar există stoc într-un alt depozit al aceleiași companii, se generează un transfer intern către depozitul comenzii. Astfel se evită livrările blocate din lipsă de stoc local, iar transferul poate fi chiar validat automat.

#### 2. Funcționalități Cheie

- La confirmarea comenzii de vânzare se verifică stocul fiecărui produs stocabil din depozitul comenzii; pentru deficit se creează un transfer din alt depozit al companiei (primul găsit, diferit de cel al comenzii).
- Cantitatea transferată acoperă doar deficitul și nu depășește stocul disponibil în depozitul sursă; calculele se fac în unitatea de măsură a produsului, iar mișcarea se creează în aceeași unitate (corecție din 19.0.1.0.2: unități de vânzare diferite de cele de stoc, linii repetate ale aceluiași produs).
- Pe depozit se configurează: tipul de operațiune folosit pentru transferul automat (dacă lipsește, se folosește tipul de transfer intern al depozitului sursă), opțiunea de grupare a transferului cu livrarea (prin referințele de stoc ale comenzii) și opțiunea de confirmare automată.
- Cu confirmare automată activă, transferul este rezervat, completat și validat imediat; dacă nu toate produsele sunt disponibile, se afișează o eroare. Comportamentul poate fi forțat și prin cheia de context `confirm_transfer`.
- Transferul primește notă cu link către comandă, iar pe comandă se postează un mesaj cu documentul generat.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): `action_confirm` apelează `prepare_transfer()`, care calculează deficitul și creează transferul și mișcările.
- `stock.warehouse` (extins): câmpurile `pick_type_auto_transfer_id`, `group_transfer_with_delivery`, `auto_confirm_transfer`.
- `stock.picking` (extins): metoda `auto_transfer()` – verifică disponibilitatea, marchează mișcările ca procesate și validează transferul.

**Vizualizări**

- `view_warehouse`: extinde formularul depozitului (`stock.view_warehouse`) cu tipul transferului automat și opțiunea de grupare cu livrarea. Câmpul `auto_confirm_transfer` nu este afișat în această vizualizare.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `sale_stock`: baza fluxului vânzare - livrare, extinsă aici cu transferul între depozite.
- `stock`: depozite, tipuri de operațiuni și transferuri interne.
