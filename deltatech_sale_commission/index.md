# Sale Commission (localizat la `deltatech_sale_commission/index.md`)

- **Nume Tehnic:** `deltatech_sale_commission`
- **Versiune:** `19.0.2.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_commission
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_commission`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă comisioanele agenților de vânzări peste raportul de profit din [deltatech_sale_margin](../deltatech_sale_margin/index.md). Începând cu 19.0.2.0.0, costul pe linia de factură, controlul vânzării sub cost și raportul de profitabilitate au rămas în `deltatech_sale_margin`; aici se păstrează doar partea de comisioane, care extinde raportul. Comisionul se calculează fie pe agentul de pe comanda de vânzare, fie pe cel de pe factură, cu posibilitatea de a-l condiționa de încasarea facturii în termenul stabilit.

#### 2. Funcționalități Cheie

- Coloane, filtre și meniu de comisioane pe raportul de profit din `deltatech_sale_margin` (costul pe factură și raportul în sine sunt acolo).
- Calculul comisioanelor pe agentul de pe comanda de vânzare sau de pe factură, configurabil din *Setări → Vânzări → Facturare → Salesperson commission compute*. Schimbarea ulterioară realocă toate liniile, inclusiv comisioanele deja plătite; nu se confundă cu opțiunea standard *Commissions*.
- Tarife de comision (`commission.users`, *Vânzări → Configurare → Users Commission*): tarif pentru agent, manager de vânzări și director, ca fracții din profit (0,100 = 10%). Jurnalul de vânzări este obligatoriu, iar combinația (agent, jurnal, companie) este unică.
- Lista *Comision* (*Vânzări → Comenzi → Comision*): implicit ultima lună și doar facturi plătite (inclusiv *În plată*); arată comisionul calculat (tarif agent × profit), comisionul real și comisionul plătit. Sumele pentru manager și director sunt doar informative. Comenzile de Point of Sale din `deltatech_sale_margin_pos` nu apar în această listă; comisionul lor calculat apare în *Profit Analysis*.
- Wizard *Compute Commission* (Acțiuni): comisionul real devine comisionul calculat; cu parametrul `deltatech_sale_commission.days_for_commission` (întreg, 0 = plătită la scadență) devine 0 dacă factura nu e complet plătită sau a fost plătită cu întârziere. Notele de credit păstrează comisionul calculat, negativ, care scade totalul agentului. Se scrie doar comisionul agentului.
- Comisionul real se poate corecta manual înainte de plată; butonul *Set Paid* marchează liniile plătite (plata propriu-zisă se face în afara modulului), iar filtrele *Commission not paid* / *Commission paid* separă situațiile.
- Drepturi: grupurile *Commission Manager* (calculează, modifică comisionul real și *Commission Paid*) și *Commission Viewer* (doar consultă; vede costul și marja) nu sunt atribuite nimănui la instalare, nici administratorului — meniul *Comision* rămâne ascuns până la atribuire.
- Schimbarea setării de agent reconstruiește raportul după salvare; facturile *În plată* se socotesc plătite pentru comision.
- Fluxul pas-cu-pas este detaliat în [Fișa Consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_sale_margin](../deltatech_sale_margin/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune este omisă deoarece `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit analiza componentelor tehnice.

#### 5. Conexiuni

- [deltatech_sale_margin](../deltatech_sale_margin/index.md): dependență directă; furnizează costul pe factură, politica de vânzare sub cost și raportul de profit pe care modulul îl extinde cu comisioane.
- [deltatech_sale_margin_pos](../deltatech_sale_margin_pos/index.md): comenzile POS nu intră în lista *Comision*; comisionul lor calculat apare în *Profit Analysis* (conform USAGE.md al modulului).
