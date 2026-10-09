# Sale Payment (localizat la `deltatech_sale_payment/index.md`)

- **Nume Tehnic:** `deltatech_sale_payment`
- **Versiune:** `19.0.1.3.4`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_payment`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_payment`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă gestionarea plăților direct în comanda de vânzare (sale order), permițând echipei de vânzări să urmărească starea încasărilor fără a părăsi documentul. Pe formularul comenzii apare un buton dedicat pentru plată, împreună cu informații despre suma plătită, furnizorul de plată și statusul plății. Astfel se obține o imagine clară, în timp real, asupra stadiului în care se află încasarea unei comenzi (fără plată, inițiată, în așteptare, autorizată, parțială, finalizată sau anulată). Încasările primite în afara unui procesator online (transfer bancar, ramburs) se pot confirma direct de pe comandă.

#### 2. Funcționalități Cheie

- Buton de plată în comanda de vânzare pentru inițierea și confirmarea plăților.
- Afișarea sumei plătite și a furnizorului de plată direct pe formularul comenzii, cu decorări de culoare în funcție de status.
- Status de plată calculat automat: fără plată, inițiată, în așteptare (`pending`, tranzacții care așteaptă furnizorul: transfer bancar, 3-D Secure etc.), autorizată, parțială, finalizată, anulată. Comanda este „finalizată" când suma plătită atinge totalul, în limita rotunjirii monedei.
- Suma plătită este calculată în moneda comenzii: facturile (cu semn negativ pentru note de credit) și tranzacțiile în altă monedă sunt convertite la cursul de la data documentului. Valoarea = maximul dintre suma plătită pe facturile postate și suma tranzacțiilor confirmate, astfel încât o tranzacție confirmată pe un furnizor fără jurnal (ex. card Shopify) nu se pierde și nu se numără de două ori.
- Furnizorul afișat urmează tranzacția cea mai relevantă: finalizată, apoi autorizată, în așteptare, anulată, apoi ultima.
- Câmpurile `payment_amount`, `payment_status` și `provider_id` sunt stocate, deci lista comenzilor poate filtra, grupa și sorta pe ele direct în SQL.
- Filtre de căutare pentru fiecare status și grupare după „Payment Status" (inclusiv tradusă).
- Generarea unui link de plată pentru suma rămasă de încasat (totalul minus suma plătită), inclusiv după ce există o factură.
- Asistent „Confirm Payment" (acțiune în meniul Acțiuni al comenzii, vizibilă doar utilizatorilor de vânzări):
  - preia doar o tranzacție încă în așteptare (draft/pending); o tranzacție confirmată nu este niciodată anulată sau ștearsă, ci se propune restul de plată și se adaugă o tranzacție nouă;
  - refuză comenzile cu plată autorizată (autorizarea se capturează sau se anulează la furnizor);
  - data plății se păstrează în mesajul de stare al tranzacției, într-o notă pe comandă și ca dată a plății contabile (când furnizorul creează una); tranzacția este post-procesată imediat, nu de cron;
  - cine poate modifica comanda îi poate confirma încasarea, fără drept de Facturare (verificare de scriere pe comandă, scriere cu drepturi de sistem); vânzătorii pot citi tranzacțiile, nu le pot modifica.
- Securitate (SALEPAY-006): asistentul verifică la fiecare pas că tranzacția aparține comenzii, că furnizorul este din compania comenzii (sau dintr-o companie-mamă, pe comanda unei sucursale — SALEPAY-008, 19.0.1.3.4) și că metoda de plată aparține furnizorului; `update_transaction` a devenit privată (`_update_transaction`), codul extern trebuie să apeleze `do_add_payment()`.
- Furnizori fără linie de metodă de plată (transfer bancar, „none"): post-procesarea nu mai creează plată contabilă și nu mai eșuează la fiecare 10 minute; comanda se confirmă și, cu facturare automată, se facturează, iar plata o înregistrează contabilul din extras.
- Migrare: câmpurile se calculează în SQL, înainte de încărcarea registry-ului, pentru baze provenite din 18.0 sau din 19.0.1.1.x; comenzile în altă monedă decât cea a companiei se recalculează la 19.0.1.2.2.
- Mesajele de eroare ale asistentului sunt traduse în română (19.0.1.3.3).
- Modulul are pictogramă proprie și fișă consultant cu capturi de ecran, auditată contabil (19.0.1.3.3): cont implicit „Încasări restante” (5121xx) de înlocuit cu 5125, încasarea înainte de factură tratată ca avans (419 + 4427, cu **Cont plată în avans** = 419 setat), comisionul procesatorului (627) și rambursul prin curier (461).

#### 3. Dependențe

- `sale`
- `payment`
- `account_payment`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): adaugă câmpurile calculate și stocate `provider_id`, `payment_amount` și `payment_status` (selecție: `without`, `initiated`, `authorized`, `partial`, `done`, `pending`, `cancelled`). Logica `_compute_payment` determină suma încasată și statusul pe baza tranzacțiilor și a facturilor postate, cu conversie în moneda comenzii (`_payment_to_order_currency`); acțiunea `action_payment_link` generează un link de plată pentru suma rămasă.
- `payment.transaction` (extins): `_create_payment` nu creează plată contabilă pentru furnizorii fără linie de metodă de plată și preia data plății din contextul `payment_date`.
- `sale.confirm.payment` (`models.TransientModel`): asistent pentru confirmarea/adăugarea unei plăți la o comandă. Câmpuri: tranzacție, furnizor, metodă de plată, sumă, monedă, dată. Acțiuni: `do_add_payment` (creează sau actualizează tranzacția), `do_confirm` (marchează tranzacția ca finalizată și o post-procesează), `_update_transaction` (privată), `_check_payment_values` (verificări de apartenență la comandă/companie/furnizor).

**Vizualizări**

- `view_order_form`: extinde formularul comenzii de vânzare adăugând câmpurile `payment_amount`, `provider_id` și `payment_status` (cu decorări de culoare în funcție de status).
- `view_quotation_tree` / `view_order_tree`: adaugă coloanele `provider_id` (ascunsă opțional) și `payment_status` în listele de oferte și comenzi.
- `view_sales_order_filter`: adaugă filtre pentru fiecare status de plată și gruparea „Payment Status" în căutarea comenzilor.
- `view_sale_confirm_payment_form`: formularul asistentului de confirmare a plății (butoane Confirm / Add / Cancel).

**Acțiuni Automate / Acțiuni Server**

- `action_sale_confirm_payment` (`ir.actions.act_window`): acțiune contextuală (binding pe `sale.order`, formular), restricționată la grupul `sales_team.group_sale_salesman`, care deschide asistentul „Confirm Payment".

**Securitate**

- `ir.model.access.csv`: acces complet la `sale.confirm.payment` pentru utilizatori interni; citire pe `payment.provider` și `payment.transaction` pentru vânzători.

#### 5. Conexiuni

- `payment`: modulul folosește direct `payment.provider`, `payment.transaction`, `payment.method` și `payment.link.wizard` pentru gestionarea plăților.
- `sale`: extinde comanda de vânzare ca document principal pe care se urmăresc plățile.
- [deltatech_sale_store](../deltatech_sale_store/index.md): adaugă chitanțe în `invoice_ids`, luate în calcul la suma plătită (menționat în migrare).
- [deltatech_sale_commission](../deltatech_sale_commission/index.md): testele modulului vând produse fără cost pentru a nu intra în conflict cu verificarea „sub prețul de achiziție".
