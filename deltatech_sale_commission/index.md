# Sale Commission (localizat la `deltatech_sale_commission/index.md`)

- **Nume Tehnic:** `deltatech_sale_commission`
- **Versiune:** `19.0.1.6.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_commission
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_commission`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde gestiunea vânzărilor cu un sistem de calcul al comisioanelor pentru agenții de vânzări și cu instrumente de control al profitabilității. Permite stabilirea unor reguli pentru afișarea marjei și a prețului de achiziție în facturile clienților, controlează vânzarea sub prețul de achiziție și oferă un raport de analiză a profitabilității. Comisioanele pot fi calculate fie pe baza agentului de vânzări de pe comanda de vânzare, fie pe cel de pe factură, cu posibilitatea de a condiționa plata comisionului de încasarea efectivă a facturii în termenul stabilit.

#### 2. Funcționalități Cheie

- Grup tehnic de acces pentru afișarea marjei și a prețului de achiziție în factura clientului.
- Grup tehnic de acces care împiedică modificarea prețului în factura clientului.
- Grup tehnic de acces care permite vânzarea la un preț mai mic decât prețul de achiziție.
- Avertisment / eroare la factura clientului dacă prețul de vânzare este sub prețul de achiziție, **conform politicii companiei** stabilite în [deltatech_sale_margin](../deltatech_sale_margin/index.md) (`sale_margin_check_mode`). Pe politica „Doar avertisment" factura nu se blochează — altfel o vânzare permisă pe comandă ar fi oprită abia la facturare, după ce marfa a fost livrată.
- Raport nou pentru analiza profitabilității.
- Calculul comisioanelor de vânzare pe baza agentului de pe comanda de vânzare sau de pe factură (configurabil).
- Parametru `deltatech_sale_commission.days_for_commission` (valoare întreagă): la calculul comisionului sistemul verifică dacă factura este complet plătită și dacă diferența dintre data ultimei plăți și data scadentă este mai mică decât valoarea parametrului.
- Dacă diferența este mai mare decât valoarea parametrului, comisionul devine 0.
- Drepturi: wizardurile de calcul al comisionului și de actualizare a prețului de achiziție (și intrările lor din *Acțiuni*) sunt limitate la grupul *Commission Manager*; *Aplică* funcționează și fără drept de facturare, iar butonul *Setează plătit* apare doar managerilor. Un *Commission Viewer* nu mai poate modifica sau marca plătit un comision.
- Costul liniilor de notă de credit fără retur de marfă: storno-ul unei facturi (același produs, unitate și preț) păstrează costul unitar al liniei facturii, deci perechea dă profit zero; o linie cu preț sau discount modificat, ori o notă de credit care nu stornează nicio factură, are cost 0. Costul se recalculează la schimbarea prețului sau a discountului. Wizardul de actualizare *resetează* costul (inclusiv la 0), iar cronul zilnic doar completează costul lipsă. Atenție: *Actualizare preț achiziție → pentru toate* după upgrade rescrie costul notelor de credit vechi și implicit profitul raportat.
- Tarifele de comision (`commission.users`): jurnalul este obligatoriu (doar jurnale de vânzări), iar combinația (agent, jurnal, companie) este unică; raportul de marjă ia cel mult un tarif pe linie de factură și potrivește tariful și pe companie. Migrarea completează jurnalul acolo unde compania are un singur jurnal de vânzări și raportează duplicatele rămase; înainte de upgrade în producție se rulează `scripts/sale_commission_precheck_1_6_0.py` (doar citire).
- Schimbarea setării *Salesperson commission compute* reconstruiește raportul după salvare; facturile *În plată* se socotesc plătite pentru comision, iar filtrul implicit al wizardurilor listează corect liniile plătite fără comision.
- Fluxul pas-cu-pas de configurare a agenților și de calcul/plată a comisioanelor este detaliat în [Fișa Consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_sale_margin](../deltatech_sale_margin/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune este omisă deoarece `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit analiza componentelor tehnice.

#### 5. Conexiuni

- [deltatech_sale_margin](../deltatech_sale_margin/index.md): furnizează calculul marjei și al prețului de achiziție pe care se bazează controlul profitabilității și comisioanele, precum și politica de reacție la vânzarea sub cost, respectată de constrângerea de pe linia de factură.
