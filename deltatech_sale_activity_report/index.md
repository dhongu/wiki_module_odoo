# Sale Activity Log (localizat la `deltatech_sale_activity_report/index.md`)

- **Nume Tehnic:** `deltatech_sale_activity_report`
- **Versiune:** `20.0.1.2.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_activity_report
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_activity_report`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține un jurnal al celor care au lucrat pe fiecare comandă de vânzare și când, astfel încât un manager de vânzări poate vedea zilnic activitatea fiecărui vânzător. Înregistrările se pot analiza în listă, formular, pivot și grafic, iar cele vechi sunt șterse automat.

#### 2. Funcționalități Cheie

- O înregistrare de activitate per comandă, utilizator și zi: prima intervenție a unui utilizator intern pe o comandă într-o zi creează înregistrarea, iar acțiunile ulterioare din aceeași zi se adaugă la ea. Acțiunile sistemului și ale utilizatorilor de portal sau website nu se înregistrează.
- Fila **Log** a înregistrării listează cronologic: modificările de câmpuri (valoare veche și nouă, liniile comenzii descrise linie cu linie), butoanele *Confirm*, *Cancel*, *Set to Quotation*, *Lock*, *Unlock*, *Send* și mesajele din chatter. Programarea unei activități creează înregistrarea zilei, fără linie de log. Câmpurile binare nu se loghează, iar valorile lungi se trunchiază.
- Înregistrarea păstrează starea comenzii și indicatorii *Chatter Message* și *Tags Changed*.
- Raportul **Vânzări > Raportare > Activity Records** deschide înregistrările lunii curente, cu filtre *Today*, *Yesterday*, *This Month*, *This Year* și grupare după utilizator, etapă sau dată.
- Acces: vânzătorii cu drept „doar documentele proprii” citesc înregistrările comenzilor proprii și ale celor fără responsabil; „toate documentele” și administratorul le văd pe toate, în companiile permise. Doar administratorul Vânzări poate modifica sau șterge înregistrări, iar meniul Raportare este vizibil doar lui.
- Curățare automată prin **Data Cleaning**: regula *Sale Order Activity Record* șterge înregistrările mai vechi de 2 luni; perioada se schimbă din Data Cleaning > Configuration > Rules > Recycle Records.
- Cu etapele comenzii din [deltatech_website_sale_status](../deltatech_website_sale_status/index.md), înregistrarea păstrează și etapa comenzii și indicatorul *AWB Generated*, setat la trecerea în *Pre advice*.

#### 3. Dependențe

- `sale`
- `data_recycle`

#### 4. Componente Cheie

**Modele**

- `sale.order.activity.record`: înregistrarea zilnică de activitate (comandă, utilizator, dată, log).
- `sale.order` (extindere): înregistrează modificările și butoanele de pe comandă.
- `mail.activity` (extindere): creează înregistrarea zilei la programarea unei activități.

**Vizualizări**

- `view_sale_order_activity_record_tree`, `_form`, `_pivot`, `_graph`, `_search`: interfețele raportului.
- `action_sale_order_activity_record`: acțiunea meniului Activity Records din Vânzări > Raportare.

**Acțiuni Automate / Acțiuni Server**

- `data_recycle_model_sale_order_activity`: regulă Data Cleaning care șterge înregistrările mai vechi de 2 luni.

#### 5. Conexiuni

- [deltatech_website_sale_status](../deltatech_website_sale_status/index.md): etapele comenzii și indicatorul *AWB Generated* ajung în înregistrare.
- [deltatech_sale_activity_search](../deltatech_sale_activity_search/index.md): modul înrudit, filtrare a comenzilor după tipurile activităților în așteptare.
