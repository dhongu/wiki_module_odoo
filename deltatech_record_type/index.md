# Terrabit - Record Type (localizat la `deltatech_record_type/index.md`)

- **Nume Tehnic:** `deltatech_record_type`
- **Versiune:** `19.0.1.1.17`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_record_type`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_record_type`
- **Ultima Ingestie:** `2026-10-01`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul Terrabit - Record Type oferă o modalitate îmbunătățită de a gestiona mai multe tipuri de înregistrări pentru diverse documente Odoo, inclusiv comenzi de vânzare, comenzi de achiziție și facturi. Permite companiilor să definească și să întrețină tipuri distincte de documente, fiecare cu valori implicite specifice și configurări de rutare a stocului. Astfel se standardizează crearea documentelor, se reduc erorile de introducere a datelor și fiecare utilizator vede doar tipurile relevante pentru rolul său. Tipul este o clasificare cu valori implicite și rute, fără efect contabil direct.

#### 2. Funcționalități Cheie

- Definirea de tipuri de înregistrare personalizate pentru comenzi de vânzare, comenzi de achiziție și facturi (de client); meniuri separate: Vânzări → Configurare → Tipuri comandă, Achiziții → Configurare → Tipuri comandă, Contabilitate → Configurare → Facturare → Tipuri factură.
- Asignarea de utilizatori specifici fiecărui tip, pentru control al accesului. Restricția se aplică doar pe comanda de vânzare (gol = disponibil tuturor); pe achiziții și facturi lista nu este filtrată.
- Valori implicite pentru câmpuri, aplicate la alegerea tipului pe document (onchange, nu modifică documente existente). Textul se scrie între apostrofuri, bifele ca `True`/`False`, câmpurile relaționale se aleg din lista „Înregistrare asociată". Tipul valorii se stabilește automat doar pentru many2one, char, selection, boolean și integer; câmpurile many2many/one2many nu se pot folosi.
- Configurarea rutelor de stoc pentru fiecare tip; se aplică liniilor comenzii de vânzare care nu au rută proprie (câmpul apare doar cu „Trasee în mai mulți pași" activ).
- Tipul este obligatoriu la confirmarea comenzii (vânzare și achiziție) pentru utilizatorii fără grupul „Poate confirma comenzi fără tip comandă", dacă există tipuri definite; comenzile de pe website și ofertele acceptate/semnate sau plătite de client din portal nu sunt blocate la vânzări (verificarea se aplică doar utilizatorilor interni). Pe facturi tipul rămâne opțional. Opțiunea „Confirmat fără tip comandă" se găsește în Setări → Vânzări.
- Câmpul de tip apare doar pe documentele pentru care există cel puțin un tip definit.
- Jurnal pe comanda de achiziție (manual sau ca valoare implicită a tipului), transmis facturii de furnizor generate cu **Creare factură**.
- Tipul este dimensiune de grupare în rapoartele de vânzări și achiziții, precum și în căutările și listele documentelor.
- Fluxul detaliat pas-cu-pas, verificările și erorile frecvente sunt în [Fișa Consultant](FISA_CONSULTANT.md), cu capturi de ecran.

#### 3. Dependențe

- `sale`
- `sale_stock`
- `purchase`

#### 4. Componente Cheie

**Modele**

- `record.type`: Definește configurația tipului de înregistrare, inclusiv modelul țintă (`sale.order`, `purchase.order`, `account.move`), utilizatorii permiși, rutele de stoc asociate și compania (regulă multi-companie).
- `record.type.default.values`: Valorile implicite ale câmpurilor pentru fiecare tip, cu selecție dinamică a câmpului în funcție de model.
- `sale.order` (extins): câmpul `so_type` (Tip comandă), blocarea la confirmare (doar pentru utilizatorii interni, `_skip_so_type_check`), aplicarea rutelor tipului la aprovizionare.
- `payment.transaction` (extins): confirmarea comenzii la plata online rulează cu contextul `record_type_payment_confirm`, ca să nu fie blocată de lipsa tipului.
- `purchase.order` (extins): câmpurile `po_type` și `journal_id`.
- `account.move` (extins): câmpul `invoice_type` (Tip factură).
- `sale.report`, `purchase.report` (extinse): dimensiunea tip comandă (`so_type`, `po_type`).
- `res.config.settings` (extins): opțiunea `group_confirm_order_without_record_type`.

**Vizualizări**

- `view_record_type_form` / `view_record_type_list`: formularul și lista tipurilor, cu tab-ul „Valori implicite".
- Extinderi ale formularelor și listelor de comenzi de vânzare, comenzi de achiziție și facturi, cu meniurile de configurare aferente.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_marketplace_sale_type](../deltatech_marketplace_sale_type/index.md): depinde de acest modul, folosind cadrul de tipuri de înregistrare pentru comenzile de vânzare din marketplace.
- [deltatech_sale_store](../deltatech_sale_store/index.md): depinde de acest modul (tipul comenzii, valorile implicite, selecția jurnalului).
