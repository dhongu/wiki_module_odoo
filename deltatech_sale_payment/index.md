# Sale Payment (localizat la `deltatech_sale_payment/index.md`)

- **Nume Tehnic:** `deltatech_sale_payment`
- **Versiune:** `19.0.1.2.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_payment`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_payment`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul adaugă gestionarea plăților direct în comanda de vânzare (sale order), permițând echipei de vânzări să urmărească starea încasărilor fără a părăsi documentul. Pe formularul comenzii apare un buton dedicat pentru plată, împreună cu informații despre suma plătită, furnizorul de plată și statusul plății. Astfel se obține o imagine clară, în timp real, asupra stadiului în care se află încasarea unei comenzi (fără plată, inițiată, autorizată, parțială, finalizată sau anulată).

#### 2. Funcționalități Cheie

- Buton de plată în comanda de vânzare pentru inițierea și confirmarea plăților.
- Afișarea sumei plătite și a furnizorului de plată direct pe formularul comenzii, cu decorări de culoare în funcție de status.
- Status de plată calculat automat: fără plată, inițiată, în așteptare (`pending`, tranzacții care așteaptă furnizorul: transfer bancar, 3-D Secure etc.), autorizată, parțială, finalizată, anulată. Comanda este „finalizată" când suma plătită atinge totalul, în limita rotunjirii monedei.
- Suma plătită = maximul dintre suma plătită pe facturile postate și suma tranzacțiilor confirmate. Astfel o tranzacție confirmată pe un furnizor fără jurnal (ex. card Shopify), care nu are plată contabilă, nu se pierde și nici nu se numără de două ori.
- Furnizorul afișat urmează tranzacția cea mai relevantă: finalizată, apoi autorizată, în așteptare, anulată, apoi ultima.
- Câmpurile `payment_amount`, `payment_status` și `provider_id` sunt stocate, deci lista comenzilor poate filtra, grupa și sorta pe ele direct în SQL.
- Filtre de căutare pentru fiecare status (fără plată, inițiată, în așteptare, autorizată, parțial plătită, plătită, anulată) și grupare după „Payment Status".
- Generarea unui link de plată pentru suma rămasă de încasat (totalul minus suma plătită), inclusiv după ce există o factură.
- Asistent (wizard) de confirmare a plății pentru a adăuga sau confirma o tranzacție manual.
- Migrare: câmpurile se calculează în SQL, înainte de încărcarea registry-ului, pentru baze provenite din 18.0 sau din 19.0.1.1.x (secunde în loc de recalcul ORM pe toate comenzile).
- Modulul are pictogramă proprie (din 19.0.1.2.1).

#### 3. Dependențe

- `sale`
- `payment`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): adaugă câmpurile calculate și stocate `provider_id`, `payment_amount` și `payment_status` (selecție: `without`, `initiated`, `authorized`, `partial`, `done`, `pending`, `cancelled`). Logica `_compute_payment` determină suma încasată și statusul pe baza tranzacțiilor și a facturilor postate; acțiunea `action_payment_link` generează un link de plată pentru suma rămasă.
- `sale.confirm.payment` (`models.TransientModel`): asistent pentru confirmarea/adăugarea unei plăți la o comandă. Permite alegerea furnizorului, metodei de plată, sumei și datei plății, cu acțiunile `do_add_payment` (creează/actualizează tranzacția) și `do_confirm` (marchează tranzacția ca finalizată).

**Vizualizări**

- `view_order_form`: extinde formularul comenzii de vânzare adăugând câmpurile `payment_amount`, `provider_id` și `payment_status` (cu decorări de culoare în funcție de status).
- `view_quotation_tree` / `view_order_tree`: adaugă coloanele `provider_id` (ascunsă opțional) și `payment_status` în listele de oferte și comenzi.
- `view_sales_order_filter`: adaugă filtre pentru fiecare status de plată și gruparea „Payment Status" în căutarea comenzilor.
- `view_sale_confirm_payment_form`: formularul asistentului de confirmare a plății.

**Acțiuni Automate / Acțiuni Server**

- `action_sale_confirm_payment` (`ir.actions.act_window`): acțiune contextuală (binding pe `sale.order`, formular) care deschide asistentul „Confirm Payment" din comanda de vânzare.

#### 5. Conexiuni

- `payment`: modulul folosește direct `payment.provider`, `payment.transaction`, `payment.method` și `payment.link.wizard` pentru gestionarea plăților.
- `sale`: extinde comanda de vânzare ca document principal pe care se urmăresc plățile.
