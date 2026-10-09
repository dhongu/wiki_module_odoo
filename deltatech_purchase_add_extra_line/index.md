# Purchase Add Extra Line (localizat la `deltatech_purchase_add_extra_line/index.md`)

- **Nume Tehnic:** `deltatech_purchase_add_extra_line`
- **Versiune:** `19.0.1.5.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_add_extra_line`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_add_extra_line`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul introduce un proces automat de adăugare a unor linii suplimentare (de exemplu taxe de serviciu, costuri de manipulare sau produse adiacente) pe comenzile de achiziție din Odoo. Este conceput pentru a ajuta echipele de aprovizionare să aplice consecvent costuri sau articole suplimentare în funcție de produsele principale comandate, reducând erorile de introducere manuală și asigurând că toate costurile obligatorii sunt incluse în fiecare comandă relevantă.

#### 2. Funcționalități Cheie

- **Produse extra configurabile**: permite definirea unui *produs extra* direct pe șablonul de produs și adăugarea automată a liniei suplimentare ori de câte ori produsul principal este introdus într-o comandă de achiziție.
- **Logică flexibilă de prețuri**: prețul unitar al liniei extra poate fi calculat ca *procent* din prețul produsului principal; dacă procentul este zero, se aplică prețul de furnizor standard al produsului extra, în moneda și unitatea de măsură ale comenzii.
- **Preț manual păstrat**: un preț unitar introdus manual pe linia extra este păstrat și nu mai este recalculat din linia principală — cantitatea continuă însă să urmeze linia principală. Revenirea la prețul calculat se face prin **ștergerea liniei extra**, care se regenerează automat cu prețul calculat la următoarea modificare a liniilor comenzii.
- **Actualizare și în afara formularului**: mecanismul de sincronizare rulează și pe `write()` al liniei de comandă, nu doar la `create()` și la onchange — o editare inline în listă, un import sau o scriere prin XML-RPC pe `product_qty`, `product_id` sau `price_unit` recalculează linia extra (ticket #9275). O gardă de context (`skip_check_extra_product`) previne recursivitatea.
- **Schimbarea produsului principal** (nou în 19.0.1.4.0): dacă produsul liniei principale se schimbă, linia extra a produsului vechi este înlocuită cu una nouă (produs, unitate de măsură, cantitate și preț calculat ale noului extra); dacă noul produs nu are produs extra, linia extra veche este ștearsă. Funcționează în formular, pe `write()`, la import și prin XML-RPC. Un preț manual de pe linia veche nu se transferă, fiindcă aparținea altui produs.
- **Ștergerea liniei principale** șterge și linia extra asociată, chiar dacă produsul nu mai are extra configurat; linia extra este marcată cu câmpul tehnic `is_extra_line`, deci perechea nu depinde de configurarea curentă a produsului (migrarea marchează liniile extra create de versiunile anterioare).
- **Linia extra este obligatorie** (nou în 19.0.1.5.0): la confirmarea cererii de ofertă, o linie extra ștearsă în afara formularului (ORM, import, XML-RPC) este regenerată; anterior era refăcută abia la următoarea modificare a liniilor.
- **Cantitate și unitate de măsură doar în citire pe linia extra** (nou în 19.0.1.5.0): ambele urmează linia principală, iar o modificare manuală era oricum suprascrisă tăcut la următoarea sincronizare; prețul unitar rămâne editabil.
- **Detectare robustă a prețului manual**: caracterul „manual” al prețului este recunoscut pe orice flux, prin câmpul tehnic `extra_price_computed`; o recalculare a prețului de furnizor (care rescrie `price_unit` și `technical_price_unit` împreună) nu este confundată cu un preț manual.
- **Funcționează doar înainte de confirmare**: generarea/actualizarea liniei extra acționează exclusiv pe comenzi în starea *Cerere de ofertă* (draft) sau *Ofertă trimisă* (sent).
- **Traducere română completă** („Linie suplimentară”, „Produs suplimentar”, „Procent suplimentar”, „Cantitate suplimentară”) și **tooltip-uri identice cu modulul de vânzări**: ambele module declară aceleași câmpuri pe `product.template`, deci un text divergent ar face ca tooltip-ul să depindă de ordinea de încărcare.
- **Limitare cunoscută**: câmpul `extra_product_id` nu are constrângere împotriva auto-referirii sau a ciclurilor (A→A, A→B→A); o astfel de configurare provoacă recursie la crearea liniei (PURCHASEEXTRA-002, deschis în `readme/bugs.md`).
- **Utilizare**: pe fișa produsului (Achiziție > Produse) se configurează *Produs suplimentar*, *Procent suplimentar* și *Cantitate suplimentară*; la adăugarea produsului principal într-o comandă de achiziție, linia extra este generată automat ca linie separată cu prețul precalculat.

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): adaugă câmpurile `extra_product_id` (produsul extra asociat), `extra_percent` (procentul aplicat la prețul produsului principal) și `extra_qty` (cantitatea liniei extra, implicit 1.0). Aceste câmpuri sunt **partajate** cu modulul `deltatech_sale_add_extra_line` (declarate pe același model `product.template` de ambele module) — o capcană de configurare de reținut la instalarea concomitentă a celor două module.
- `purchase.order` (extins): `write()` sincronizează liniile abia după aplicarea tuturor comenzilor one2many dintr-o salvare (evită dublarea liniei extra la schimbarea produsului din formular); `button_confirm()` (nou în 1.5.0), `action_rfq_send()`, `print_quotation()` și onchange-ul pe `order_line` apelează `check_extra_product()`. În onchange, liniile obsolete returnate sunt scoase din `order_line`.
- `purchase.order.line` (extins): câmpuri tehnice `line_uuid` (corelarea liniei principale cu cea extra), `is_extra_line` (marchează linia extra generată; nou în 1.4.0) și `extra_price_computed` (ultimul preț calculat de modul — un preț diferit este considerat manual și păstrat). `check_extra_product()` este apelată din `create()` și din `write()` (la modificarea `product_qty`, `product_id` sau `price_unit`, cu gardă `skip_check_extra_product`); reconciliază perechea cu produsul extra curent (înlocuire/ștergere) și returnează liniile obsolete ce nu pot fi șterse (`NewId`). `_get_extra_line()` găsește linia extra prin `line_uuid` + `is_extra_line`; `unlink()` șterge perechea. Acționează doar în starea `draft`/`sent`.

**Vizualizări**

- `product_template_form_view`: extinde formularul de produs cu grupul „Linie suplimentară” (câmpurile `extra_product_id`, `extra_percent`, `extra_qty`) în zona de achiziție, cu tooltip-uri identice celor din modulul de vânzări.
- `purchase_order_form`: extinde formularul comenzii de achiziție — expune câmpurile tehnice `line_uuid`, `extra_price_computed` și `is_extra_line` (invizibile, `force_save="1"`) și face `product_qty` și `product_uom_id` doar în citire pe liniile extra (în listă și în formularul liniei).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`. Automatizarea se realizează prin metoda `check_extra_product()`, apelată din `create()`, `write()`, onchange-ul pe `order_line`, `button_confirm()`, `action_rfq_send()` și `print_quotation()`.

**Migrări**

- `migrations/19.0.1.1.0/post-migration.py`: asociat introducerii logicii de păstrare a prețului manual (câmpul `extra_price_computed`).
- `migrations/19.0.1.4.0/post-migration.py`: marchează cu `is_extra_line` liniile extra create de versiunile anterioare (în fiecare pereche cu același `line_uuid`, linia cu id mai mare).

#### 5. Conexiuni

- [deltatech_sale_add_extra_line](../deltatech_sale_add_extra_line/index.md): modul soră care aplică același mecanism de linii suplimentare pe comenzile de vânzare (Sales) în loc de achiziții; câmpurile de configurare de pe `product.template` sunt partajate între cele două module.
