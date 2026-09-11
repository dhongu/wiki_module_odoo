# Sale Product Reference (localizat la `deltatech_sale_product_reference/index.md`)

- **Nume Tehnic:** `deltatech_sale_product_reference`
- **Versiune:** `19.0.2.0.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_product_reference`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_product_reference`
- **Ultima Ingestie:** `2026-09-11`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul ține, pentru fiecare produs, **codul și denumirea sub care fiecare client îl cunoaște** și le pune automat pe descrierea liniei de comandă de vânzare — exact oglinda a ceea ce Odoo face deja în achiziții, unde descrierea liniei se compune din fișa furnizorului. Un lanț de retail nu comandă „Mere roșii 13 kg — cod intern MR-13", ci articolul 81346 din nomenclatorul lui: oferta, avizul și factura trimise acelui client trebuie să poarte codul și denumirea lui, fără ca cineva să le traducă manual pe fiecare linie. Referințele stau pe o listă dedicată în fișa produsului („Referințe client"), analoagă listei de prețuri furnizor de pe tabul Achiziții, și se aplică automat la crearea liniei sau la schimbarea clientului comenzii.

#### 2. Funcționalități Cheie

- Listă **Referințe client** pe tabul Vânzări al fișei produsului (și pe fișa variantei): câte un rând per client, cu codul și denumirea lui pentru produs, un preț convenit opțional, o perioadă de valabilitate și, pentru produse cu variante, varianta căreia i se adresează referința.
- **Descriere automată a liniei**: când clientul comenzii are o referință pentru produs, linia de vânzare preia forma `[cod client] denumire client`, urmată de descrierea de vânzare a produsului și de atributele variantei — exact structura standard, dar cu cuvintele clientului în locul celor proprii. Fără referință, rămâne descrierea standard.
- **Rezolvare pe tot clientul**: referințele se caută pe partenerul comenzii, pe părintele lui și pe entitatea lui comercială, deci o referință negociată cu firma se aplică oricărui punct de livrare sau depozit al ei.
- **Precedența variantei**: o referință setată pe o variantă anume are prioritate față de cea valabilă pentru tot produsul; la egalitate câștigă partenerul exact față de părinte, apoi secvența.
- **Valabilitate în timp**: dată de start și de sfârșit, astfel încât o referință poate fi înlocuită când se schimbă listingul clientului, păstrând istoricul descrierii unei comenzi vechi.
- **Se reaplică și pe liniile cu descriere explicită** (import EDI/API), care altfel ar ocoli mecanismul standard de calcul al descrierii.
- **Nu mai reapare denumirea proprie pe factură**: Odoo reintroduce în mod normal denumirea produsului deasupra descrierii dacă aceasta nu mai conține numele lui — comportament util pentru o descriere scrisă manual, dar care anula pe ecranul facturii, pe factura tipărită și în eticheta notei contabile exact înlocuirea pe care modulul o face pe ofertă (XML-ul e-Facturii nu era afectat — exportatorul standard elimină oricum denumirea redundantă). Când există o referință de client, factura păstrează descrierea liniei așa cum a fost compusă.
- **Listă independentă** sub Sales → Products → Customer References, pentru trecere în revistă pe toate produsele; managerii de vânzări pot crea/edita, vânzătorii doar citesc (necesare la completarea descrierii liniei).
- **Migrare automată** de la convenția veche, la actualizare: rândurile de client ținute anterior în lista de prețuri furnizor sunt copiate în noul model doar când partenerul e strict client (nu și furnizor); rândurile ambigue (client și furnizor deopotrivă) rămân pe loc și sunt numărate în jurnal, pentru revizuire manuală. Nimic nu se șterge din lista de prețuri furnizor.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `product.customerinfo` (nou, de la 19.0.2.0.0): modelul propriu al referinței de client — partener, șablon de produs, variantă opțională, cod, denumire, secvență, preț, monedă, dată de start/sfârșit, companie. Oglinda pe partea de vânzări a lui `product.supplierinfo`, izolată intenționat de acesta: până la 19.0.2.0.0 referințele clientului stăteau în `product.supplierinfo`, cu clientul înregistrat ca „furnizor" al produsului, ceea ce se scurgea în achiziții (reaprovizionarea alegea furnizorul după preț, fără să întrebe cine e partenerul, deci un rând de client cu preț 0 ieșea primul; o regulă de stoc își schimba ruta la simpla prezență a unui rând de furnizor; clientul apărea sub „Furnizori" în ecranul de reaprovizionare). Expune `_get_reference(partner, product, date, company)` — căutarea rulează ca superuser, ca și căutarea standard de afișare pe `product.supplierinfo` — și `_get_product_display_name(product)`, care randează `[cod] denumire (variantă)`. Include și `_copy_from_supplierinfo()`, folosită de migrare.
- `product.template`: extins cu câmpul one2many `customerinfo_ids` către `product.customerinfo`.
- `sale.order.line`: extins cu `_get_customer_reference()` (referința aplicabilă liniei) și suprascrie `_get_sale_order_line_multiline_description_sale()` pentru a compune descrierea din perspectiva referinței clientului, când există una. `order_partner_id` e adăugat ca dependență a `_compute_name`, ca schimbarea clientului să retrigger-uiască descrierea la fel ca schimbarea produsului. `create()` reaplică referința pe liniile create cu `name` explicit (import EDI/API), care ocolesc normal `_compute_name`. `_prepare_invoice_line()` e suprascris (nou în 19.0.2.0.1) ca să păstreze descrierea proprie a liniei pe factură, în loc să lase logica standard (`_get_journal_items_full_name`) să reintroducă denumirea internă a produsului deasupra celei a clientului.

**Vizualizări**

- `product_customerinfo_view_list` / `product_customerinfo_view_form`: lista editabilă (inline, `editable="bottom"`) și formularul modelului `product.customerinfo`, folosite ca listă încorporată în tabul Vânzări al fișei produsului și al variantei.
- `product_customerinfo_view_list_full` / `product_customerinfo_view_search`: lista și căutarea pentru ecranul independent din meniu, cu produsul vizibil pe fiecare rând și filtru „Valabile azi".
- `product_template_form_view_customerinfo`: adaugă grupul „Customer References" pe tabul Vânzări al fișei produsului (`product.product_template_form_view`), vizibil pentru grupul `sales_team.group_sale_salesman`.
- `product_normal_form_view_customerinfo`: adaptează contextul listei pe fișa variantei (`product.product_normal_form_view`), astfel încât o referință adăugată de pe variantă se leagă de acea variantă, la fel cum face lista de prețuri furnizor standard.
- `action_product_customerinfo` + `menu_product_customerinfo`: acțiunea și intrarea de meniu Sales → Products → Customer References, vizibilă pentru `sales_team.group_sale_manager`.

**Migrări**

- `migrations/19.0.2.0.0/post-migration.py`: la actualizarea de pe o versiune anterioară lui 19.0.2.0.0, apelează `product.customerinfo._copy_from_supplierinfo()` pentru a muta rândurile neambigue din `product.supplierinfo` în noul model.

#### 5. Conexiuni

- [deltatech_edi](../deltatech_edi/index.md): **limitare cunoscută, nu integrare** — conectorul EDI încă citește și scrie `product.supplierinfo` (pentru prețul negociat pe liniile de comandă importate), fără să fi trecut pe `product.customerinfo`. Referințele de client introduse prin acest modul nu influențează logica de preț a EDI, și invers; cele două module tratează în paralel același partener prin modele diferite.
- `terrabit_inedit`: modul de proiect al clientului Inedit Venture; îl declară în `depends`.
- `inedit_reports`: modul de proiect al clientului Inedit Venture; îl declară în `depends` și are teste proprii care folosesc `customerinfo_ids`.
