# Marketplace Dashboard

- **Nume Tehnic:** `deltatech_marketplace_dashboard`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_dashboard
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_dashboard`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un singur ecran pentru toate marketplace-urile conectate (eMAG, Trendyol, Shopify, PrestaShop etc.). Răspunde, în ordinea în care contează dimineața, la trei întrebări: ce am de făcut acum, cum merg vânzările și dacă se câștigă ceva. Un backend cu probleme nu este niciodată ascuns în spatele unuia sănătos, iar cifrele sunt calculate de baza de date, nu în browser.

#### 2. Funcționalități Cheie

- **Banda de conexiune:** starea sincronizării pentru fiecare backend selectat (erori în ultimele 24 de ore, joburi eșuate, backend-uri niciodată sincronizate), backend-urile cu importul de comenzi dezactivat și dacă jobul de import rulează.
- **Contoare:** câte unul pentru fiecare pas al listei de lucru (de mapat, de confirmat, de expediat, de predat, plus cele adăugate de conectori: de confirmat la marketplace, întârziate, anulare cerută pe eMAG) și *De încasat* (facturi postate neachitate). Click pe contor deschide lista comenzilor numărate, cu același domeniu pentru număr și listă.
- **De făcut, după termenul de expediere:** comenzile deschise care așteaptă ceva, fiecare cu pasul următor, sortate după termenul setat de marketplace, apoi după data comenzii (maximum 30 de rânduri). Pașii pe care un conector îi poate executa de aici (eMAG: confirmare/acknowledge) au buton pe rând; o comandă cu anulare cerută de client nu îl oferă.
- **Pașii listei de lucru:** *De mapat* (o linie e pe produsul *Dummy* al backend-ului), *De confirmat la marketplace* (comandă nouă pe eMAG, status 1, din conectorul eMAG), *De confirmat* (ofertă sau ofertă trimisă), *De expediat* (comandă confirmată, transfer de ieșire fără număr de urmărire), *De predat* (confirmată, cu număr de urmărire, transfer neterminat).
- **Vânzări pe zi, cele mai vândute produse și marja brută** (vânzări fără TVA - cost de achiziție - comision estimat) pentru 7, 30, 90 sau 365 de zile. Marja apare doar utilizatorilor care au voie să vadă costul produsului.
- **Retururi deschise** ale marketplace-urilor, cu starea afișată în limba utilizatorului.
- **Monede:** sumele în alte monede sunt convertite în moneda companiei la cursul zilei.
- **Acces:** meniul **Marketplace > Dashboard**, vizibil grupului *Marketplace Manager*; se aleg backend-urile (implicit *Toate*) și perioada.
- **Configurare:** **Marketplace > Backends > (backend) > Comision estimat (%)** (procentul reținut de marketplace din vânzările fără TVA, folosit doar pentru marja estimată; 0 = marjă înainte de comision); parametrul de sistem `deltatech_marketplace_dashboard.worklist_days` (implicit 90) exclude din lista de lucru și din contoare comenzile deschise mai vechi. Pe eMAG, termenul de expediere și cererea de anulare se citesc odată cu comanda, deci apar pentru comenzile importate sau recitite după actualizarea conectorului la 19.0.2.13.0.
- **Pentru conectori:** `deltatech_marketplace_sale` declară hook-uri goale (`_dashboard_steps()`, `_dashboard_kpis()`, `_dashboard_row_actions()`, `_dashboard_row_values()` pe `marketplace.sale.order`); un conector le suprascrie în propriul modul, fără a depinde de acesta.

Fluxul pas-cu-pas și capturile de ecran sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)

#### 4. Componente Cheie

**Modele**

- `marketplace.dashboard` (model abstract): calculează datele ecranului (bandă de conexiune, contoare, listă de lucru, vânzări, marjă, retururi).
- `marketplace.return.request` (doar citit): sursa retururilor deschise (stări cerut, aprobat, primit).
- `marketplace.backend` (extins): câmpul *Comision estimat (%)*, folosit la marja estimată.
- `marketplace.sale.order` (extins): implementează pașii și indicatorii listei de lucru ai dashboard-ului.

**Vizualizări**

- `action_marketplace_dashboard`: acțiune client cu meniul *Marketplace > Dashboard*; interfața este o componentă OWL (`static/src/dashboard/`).
- `view_marketplace_backend_form`: extinde formularul backend-ului cu comisionul estimat.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): adaugă pașii și contoarele *De preluat*, *Întârziate*, *Anulare cerută* și butonul *De preluat* pe rând, prin hook-urile dashboard-ului.
- [deltatech_marketplace](../deltatech_marketplace/index.md): backend-urile și conectorii marketplace pe care îi afișează dashboard-ul.
- [deltatech_rma_marketplace](../deltatech_rma_marketplace/index.md): lucrează cu aceleași cereri de retur marketplace (`marketplace.return.request`) afișate la *Retururi deschise*.
