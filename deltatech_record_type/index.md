# Record Types (localizat la `deltatech_record_type/index.md`)

- **Nume Tehnic:** `deltatech_record_type`
- **Versiune:** `20.0.1.1.17`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_record_type`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_record_type`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite definirea mai multor tipuri de înregistrări pentru comenzile de vânzare, comenzile de achiziție și facturi. Fiecare tip are valori implicite pentru câmpuri, utilizatori permiși și rute de stoc proprii, astfel încât documentele se completează mai repede și cu mai puține erori, iar fluxul de aprovizionare se adaptează tipului ales.

#### 2. Funcționalități Cheie

- Tipuri personalizate pentru comenzi de vânzare, comenzi de achiziție și facturi; câmpul de tip apare doar în modelele pentru care există tipuri definite.
- Utilizatori permiși pe fiecare tip (gol = disponibil tuturor), precum și companie (gol = toate companiile).
- Valori implicite pe tip, cu selecție dinamică a câmpului (**Valori implicite**): pentru câmpuri de legătură se alege înregistrarea în coloana **Related**; pentru text, valoarea se scrie între ghilimele simple (ex. `'export'`, interpretată ca expresie); pentru bifă, `True` sau `False`. Valorile se aplică la alegerea tipului și pot fi modificate manual.
- Rute de stoc pe tip (vizibile cu rutele multi-pas activate): liniile comenzii fără rută proprie primesc rutele tipului la confirmare, iar aprovizionarea (livrare, cumpărare, producție) le urmează.
- Meniuri de configurare: **Vânzări > Configurare > Tipuri comandă**, **Achiziții > Configurare > Tipuri comandă**, **Facturare > Configurare > Facturare > Tipuri factură**.
- Regula de confirmare: **Setări > Vânzări**, opțiunea **Confirmat fără tip comandă** (bifată implicit). Debifată, confirmarea unei comenzi fără tip cere dreptul **Poate confirma comenzi fără tip comandă**, acordat individual din fișa utilizatorului. Nu sunt oprite comenzile din magazinul online, cele acceptate în portal și cele confirmate prin plata online.
- Câmpul **Jurnal** este afișat pe comenzile de vânzare și de achiziție și poate fi completat din valorile implicite, pentru ca factura să meargă pe jurnalul dorit.
- Tipul nu mai poate fi schimbat după confirmare (comenzi) sau după postare (facturi). Pe facturile de furnizor tipul nu se poate alege.
- Raportare: coloană opțională, filtru și grupare pe tip în liste, plus dimensiunea **Tip comandă** în rapoartele de vânzări și achiziții.
- Modulul nu generează note contabile proprii.

#### 3. Dependențe

- `sale`
- `sale_stock`
- `purchase`

#### 4. Componente Cheie

**Modele**

- `record.type`: configurația tipului (model țintă `sale.order`, `purchase.order` sau `account.move`, utilizatori permiși, rute de stoc).
- `record.type.default.values`: valorile implicite ale câmpurilor pentru fiecare tip, cu selecție dinamică a câmpului.
- `sale.order`, `sale.order.line`, `purchase.order`, `account.move`, `sale.report`, `purchase.report`, `res.config.settings` (extinse): câmpul de tip, aplicarea valorilor implicite, regula de confirmare și dimensiunea de raportare.
- `payment.transaction` (extins): confirmarea comenzii la plata online (`_check_amount_and_confirm_order`).

**Vizualizări**

- `views/record_type_view.xml`: formularul și lista tipurilor de înregistrări.
- `views/sale_view.xml`, `views/purchase_view.xml`, `views/account_move_view.xml`: câmpul de tip pe comenzi și facturi.
- `views/res_config_settings_views.xml`: opțiunea **Confirmat fără tip comandă**.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau server.

#### 5. Conexiuni

- [deltatech_marketplace_sale_type](../deltatech_marketplace_sale_type/index.md): depinde de acest modul, folosind tipurile de înregistrare pentru comenzile de vânzare din marketplace.
