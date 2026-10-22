# Sale Margin - POS (localizat la `deltatech_sale_margin_pos/index.md`)

- **Nume Tehnic:** `deltatech_sale_margin_pos`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_margin_pos
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_margin_pos`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă în raportul de profit din vânzări (*Raport analiză profit*, din `deltatech_sale_margin`) și comenzile de Punct de Vânzare (POS) care nu au fost facturate. Comenzile facturate apar deja în raport prin factura lor, deci nu sunt numărate de două ori. Astfel, marja vânzărilor din magazin (bonuri fiscale) este vizibilă împreună cu cea din facturi.

#### 2. Funcționalități Cheie

Pentru fiecare linie de comandă POS, raportul afișează:

- valoarea vânzării fără TVA, în moneda companiei; returnările apar cu semn negativ;
- costul liniei, așa cum îl calculează POS la închiderea sesiunii, sau costul curent al produsului cât timp sesiunea este încă deschisă;
- vânzătorul comenzii și jurnalul de facturi al punctului de vânzare (casa); împreună cu `deltatech_sale_commission`, ratele de comision setate pe acel jurnal dau comisionul calculat al vânzătorului;
- comanda în sine, cu filtrul *POS Sales* și grupare după comandă.

Rândurile provenite din comenzile POS sunt doar în citire: comisionul real, *Comision plătit* și prețul de achiziție se păstrează doar pe liniile de factură, iar wizardurile de comision și de cost lasă comenzile POS deoparte.

Modulul nu se instalează automat, deoarece modifică cifrele raportului.

#### 3. Dependențe

- [deltatech_sale_margin](../deltatech_sale_margin/index.md)
- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `sale.margin.report`: raportul SQL existent, extins pentru a include liniile comenzilor POS nefacturate.

**Vizualizări**

- `view_sale_margin_report_list`: extinde lista raportului cu informațiile comenzii POS.
- `view_sale_margin_report_filter`: adaugă filtrul *POS Sales* și gruparea după comandă.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_sale_commission](../deltatech_sale_commission/index.md): ratele de comision de pe jurnalul de facturi al punctului de vânzare dau comisionul calculat pentru comenzile POS.
- [deltatech_pos](../deltatech_pos/index.md): funcționalități POS din aceeași suită; modulul nu depinde de el.
