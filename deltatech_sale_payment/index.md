# Sale Payment (localizat la `deltatech_sale_payment/index.md`)

- **Nume Tehnic:** `deltatech_sale_payment`
- **Versiune:** `19.0.1.1.4`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_payment`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_payment`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul adaugă gestionarea plăților direct în comanda de vânzare (sale order), permițând echipei de vânzări să urmărească starea încasărilor fără a părăsi documentul. Pe formularul comenzii apare un buton dedicat pentru plată, împreună cu informații despre suma plătită, furnizorul de plată și statusul plății. Astfel se obține o imagine clară, în timp real, asupra stadiului în care se află încasarea unei comenzi (fără plată, inițiată, autorizată, parțială, finalizată sau anulată).

#### 2. Funcționalități Cheie

- Buton de plată în comanda de vânzare pentru inițierea și confirmarea plăților.
- Afișarea sumei plătite și a furnizorului de plată asociat direct pe formularul comenzii.
- Status de plată calculat automat: fără plată, inițiată, autorizată, parțială, finalizată, anulată.
- Generarea unui link de plată (payment link) pentru suma rămasă de încasat din comandă.
- Asistent (wizard) de confirmare a plății pentru a adăuga sau confirma o tranzacție manual.
- Filtru în lista comenzilor pentru „Plată inițiată" și coloane opționale pentru status și furnizor în vizualizările listă.
- Căutare pe câmpul calculat `payment_status` (via `_search_payment_status`), compatibilă cu rescrierea domeniilor `=`/`!=` în `in`/`not in` din Odoo 19.

#### 3. Dependențe

- `sale`
- `payment`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): adaugă câmpurile calculate `provider_id`, `payment_amount` și `payment_status`. Conține logica `_compute_payment` care determină suma încasată și statusul plății pe baza tranzacțiilor și a facturilor postate, metoda `_search_payment_status`/`_get_payment_status_domain`/`_get_paid_order_ids` pentru căutarea pe statusul de plată, precum și acțiunea `action_payment_link` ce generează un link de plată pentru suma rămasă.
- `sale.confirm.payment` (`models.TransientModel`): asistent pentru confirmarea/adăugarea unei plăți la o comandă. Permite alegerea furnizorului, metodei de plată, sumei și datei plății, cu acțiunile `do_add_payment` (creează/actualizează tranzacția) și `do_confirm` (marchează tranzacția ca finalizată).

**Vizualizări**

- `view_order_form`: extinde formularul comenzii de vânzare adăugând câmpurile `payment_amount`, `provider_id` și `payment_status` (cu decorări de culoare în funcție de status).
- `view_quotation_tree` / `view_order_tree`: adaugă coloanele `provider_id` (ascunsă opțional) și `payment_status` în listele de oferte și comenzi.
- `view_sales_order_filter`: adaugă filtrul „Payment initiated" în vizualizarea de căutare a comenzilor.
- `view_sale_confirm_payment_form`: formularul asistentului de confirmare a plății.

**Acțiuni Automate / Acțiuni Server**

- `action_sale_confirm_payment` (`ir.actions.act_window`): acțiune contextuală (binding pe `sale.order`, formular) care deschide asistentul „Confirm Payment" din comanda de vânzare.

#### 5. Conexiuni

- `payment`: modulul folosește direct `payment.provider`, `payment.transaction`, `payment.method` și `payment.link.wizard` pentru gestionarea plăților.
- `sale`: extinde comanda de vânzare ca document principal pe care se urmăresc plățile.
