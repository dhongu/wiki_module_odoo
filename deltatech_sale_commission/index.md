# Sale Commission (localizat la `deltatech_sale_commission/index.md`)

- **Nume Tehnic:** `deltatech_sale_commission`
- **Versiune:** `19.0.1.4.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_commission
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_commission`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Modulul extinde gestiunea vânzărilor cu un sistem de calcul al comisioanelor pentru agenții de vânzări și cu instrumente de control al profitabilității. Permite stabilirea unor reguli pentru afișarea marjei și a prețului de achiziție în facturile clienților, controlează vânzarea sub prețul de achiziție și oferă un raport de analiză a profitabilității. Comisioanele pot fi calculate fie pe baza agentului de vânzări de pe comanda de vânzare, fie pe cel de pe factură, cu posibilitatea de a condiționa plata comisionului de încasarea efectivă a facturii în termenul stabilit.

#### 2. Funcționalități Cheie

- Grup tehnic de acces pentru afișarea marjei și a prețului de achiziție în factura clientului.
- Grup tehnic de acces care împiedică modificarea prețului în factura clientului.
- Grup tehnic de acces care permite vânzarea la un preț mai mic decât prețul de achiziție.
- Avertisment / eroare la factura clientului dacă prețul de vânzare este sub prețul de achiziție.
- Raport nou pentru analiza profitabilității.
- Calculul comisioanelor de vânzare pe baza agentului de pe comanda de vânzare sau de pe factură (configurabil).
- Parametru `deltatech_sale_commission.days_for_commission` (valoare întreagă): la calculul comisionului sistemul verifică dacă factura este complet plătită și dacă diferența dintre data ultimei plăți și data scadentă este mai mică decât valoarea parametrului.
- Dacă diferența este mai mare decât valoarea parametrului, comisionul devine 0.

#### 3. Dependențe

- [deltatech_sale_margin](../deltatech_sale_margin/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune este omisă deoarece `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit analiza componentelor tehnice.

#### 5. Conexiuni

- [deltatech_sale_margin](../deltatech_sale_margin/index.md): furnizează calculul marjei și al prețului de achiziție pe care se bazează controlul profitabilității și comisioanele.
