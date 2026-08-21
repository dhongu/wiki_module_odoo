# Purchase Add Extra Line (localizat la `deltatech_purchase_add_extra_line/index.md`)

- **Nume Tehnic:** `deltatech_purchase_add_extra_line`
- **Versiune:** `19.0.1.3.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_add_extra_line`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_add_extra_line`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul introduce un proces automat de adăugare a unor linii suplimentare (de exemplu taxe de serviciu, costuri de manipulare sau produse adiacente) pe comenzile de achiziție din Odoo. Este conceput pentru a ajuta echipele de aprovizionare să aplice consecvent costuri sau articole suplimentare în funcție de produsele principale comandate, reducând erorile de introducere manuală și asigurând că toate costurile obligatorii sunt incluse în fiecare comandă relevantă.

#### 2. Funcționalități Cheie

- **Produse extra configurabile**: permite definirea unui *produs extra* direct pe șablonul de produs și adăugarea automată a liniei suplimentare ori de câte ori produsul principal este introdus într-o comandă de achiziție.
- **Logică flexibilă de prețuri**: prețul unitar al liniei extra poate fi calculat ca *procent* din prețul produsului principal; dacă procentul este zero, se aplică prețul de furnizor standard al produsului extra, în moneda și unitatea de măsură ale comenzii.
- **Preț manual păstrat**: un preț unitar introdus manual pe linia extra este păstrat și nu mai este recalculat din linia principală — cantitatea continuă însă să urmeze linia principală. Revenirea la prețul calculat se face prin **ștergerea liniei extra**, care se regenerează automat cu prețul calculat la următoarea modificare a liniilor comenzii.
- **Actualizare și în afara formularului** (nou în 19.0.1.3.0): mecanismul de sincronizare rulează acum și pe `write()` al liniei de comandă, nu doar la `create()` și la onchange-ul din formular — o editare inline în listă, un import sau o scriere prin XML-RPC pe `product_qty`, `product_id` sau `price_unit` declanșează acum și ea recalcularea liniei extra. Anterior, o astfel de modificare lăsa linia extra la cantitatea și prețul vechi, fără nicio eroare vizibilă (ticket #9275). O gardă de context (`skip_check_extra_product`) previne recursivitatea provocată de scrierea pe linia extra însăși.
- **Detectare robustă a prețului manual**: caracterul „manual” al prețului este recunoscut pe orice flux (formular, `write()`, import, XML-RPC), nu doar la editare în formular — este marcat prin câmpul tehnic `extra_price_computed`; o recalculare a prețului de furnizor (care rescrie `price_unit` și `technical_price_unit` împreună) nu mai este confundată cu un preț introdus manual.
- **Funcționează doar înainte de confirmare**: mecanismul de generare/actualizare a liniei extra acționează exclusiv pe comenzi în starea *Cerere de ofertă* (draft) sau *Ofertă trimisă* (sent); după confirmarea comenzii, liniile extra nu mai sunt actualizate automat.
- **Traducere română completă**: grupul de configurare și câmpurile aferente sunt traduse integral — „Linie suplimentară”, „Produs suplimentar”, „Procent suplimentar”, „Cantitate suplimentară” (`i18n/ro.po`).
- **Tooltip-uri identice cu modulul de vânzări**: cele trei câmpuri de configurare au descrieri de ajutor (tooltip), păstrate intenționat **identice** cu cele din `deltatech_sale_add_extra_line` — ambele module declară aceleași câmpuri pe `product.template`, deci la instalarea ambelor module ultimul încărcat câștigă; un text divergent ar face ca tooltip-ul afișat să depindă de ordinea de încărcare.
- **Utilizare**: pe fișa produsului (Achiziție > Produse) se configurează *Produs suplimentar*, *Procent suplimentar* și *Cantitate suplimentară*; la crearea unei comenzi de achiziție și adăugarea produsului principal, linia extra este generată automat ca linie separată cu prețul precalculat.

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): adaugă câmpurile `extra_product_id` (produsul extra asociat), `extra_percent` (procentul aplicat la prețul produsului principal) și `extra_qty` (cantitatea liniei extra, implicit 1.0). Aceste câmpuri sunt **partajate** cu modulul `deltatech_sale_add_extra_line` (declarate pe același model `product.template` de ambele module) — o capcană de configurare de reținut la instalarea concomitentă a celor două module.
- `purchase.order` (extins): apelează `check_extra_product()` din `action_rfq_send()`, din `print_quotation()` și din onchange-ul pe `order_line`, pentru a genera/actualiza liniile extra înainte de trimiterea ofertei către furnizor.
- `purchase.order.line` (extins): adaugă câmpurile tehnice `line_uuid` (corelarea liniei principale cu linia extra generată) și `extra_price_computed` (ultimul preț unitar calculat de modul pentru linia extra — un preț diferit de acesta este considerat introdus manual și este păstrat). Metoda `check_extra_product()` este apelată din `create()` și, începând cu 19.0.1.3.0, și din `write()` atunci când se modifică `product_qty`, `product_id` sau `price_unit` (protejat cu contextul `skip_check_extra_product` pentru a evita recursivitatea); `unlink()` elimină automat linia extra asociată la ștergerea liniei principale. Mecanismul acționează doar când comanda este în starea `draft` sau `sent`.

**Vizualizări**

- `product_template_form_view`: extinde formularul de produs cu grupul „Linie suplimentară” (câmpurile `extra_product_id`, `extra_percent`, `extra_qty`) în zona de achiziție, cu tooltip-uri identice celor din modulul de vânzări.
- `purchase_order_form`: extinde formularul comenzii de achiziție, expunând câmpurile tehnice `line_uuid` și `extra_price_computed` pe liniile comenzii (coloane invizibile, `force_save="1"`) pentru corelarea liniilor extra și detectarea prețului manual.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`. Automatizarea se realizează prin metoda `check_extra_product()`, apelată din `create()`, din `write()`, din onchange-ul pe `order_line`, din `action_rfq_send()` și din `print_quotation()`.

**Migrări**

- `migrations/19.0.1.1.0/post-migration.py`: script de migrare asociat introducerii logicii de păstrare a prețului manual (câmpul `extra_price_computed`).

#### 5. Conexiuni

- [deltatech_sale_add_extra_line](../deltatech_sale_add_extra_line/index.md): modul soră care aplică același mecanism de linii suplimentare pe comenzile de vânzare (Sales) în loc de achiziții; câmpurile de configurare de pe `product.template` sunt partajate între cele două module.
