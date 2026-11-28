# Sale Margin - POS (localizat la `deltatech_sale_margin_pos/index.md`)

- **Nume Tehnic:** `deltatech_sale_margin_pos`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_margin_pos
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_margin_pos`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă în raportul de marjă (Raport analiză profit) comenzile de Point of Sale care nu au fost facturate. Comenzile facturate sunt deja în raport prin factură, deci nu sunt numărate de două ori. Modulul nu se instalează automat, pentru că modifică cifrele raportului.

#### 2. Funcționalități Cheie

- Pe fiecare linie de comandă POS: valoarea vânzării fără TVA în moneda companiei (retururile negative) și costul liniei (calculat de POS la închiderea sesiunii, altfel costul curent al produsului).
- Vânzătorul comenzii și jurnalul comenzilor POS; împreună cu `deltatech_sale_commission`, comisionul calculat folosește ratele de pe **jurnalul de facturare** al punctului de vânzare.
- Comanda însăși, cu filtrul *POS Sales* și grupare după comandă.
- Rândurile comenzilor sunt doar pentru citire: comisionul real, *Commission Paid* și prețul de achiziție rămân doar pe liniile de factură; wizardurile de comision și cost ignoră comenzile.
- Nota de credit a unui retur POS facturat pentru un bon nefacturat nu stornează nicio factură și își ia costul din liniile returului POS (costul vânzării inițiale), nu 0. O notă veche rămasă cu cost 0 se corectează cu wizardul *Update Purchase Price*.
- Raportul se vede la **Vânzări > Raportare > Profit Analysis**; fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- [deltatech_sale_margin](../deltatech_sale_margin/index.md)
- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `sale.margin.report`: extins cu liniile comenzilor POS nefacturate.
- `account.move.line`: extins pentru costul notelor de credit ale retururilor POS.

**Vizualizări**

- `view_sale_margin_report_list`: lista raportului, cu coloana comenzii POS.
- `view_sale_margin_report_filter`: filtrul *POS Sales* și gruparea după comandă.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_sale_commission](../deltatech_sale_commission/index.md): comisionul calculat pe rândurile POS folosește ratele jurnalului de facturare.
