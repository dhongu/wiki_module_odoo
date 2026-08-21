# Deltatech Sale Order Stage Route (localizat la `deltatech_sale_stage_route/index.md`)

- **Nume Tehnic:** `deltatech_sale_stage_route`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_sale_stage_route](https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_sale_stage_route)
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_sale_stage_route`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul extinde fluxurile de vânzări și de gestiune a stocurilor din Odoo cu un traseu structurat de etape (faze) prin care trebuie să treacă o comandă de vânzare și livrările sale asociate. Astfel, o companie poate defini o succesiune obligatorie de pași — de la comanda inițială până la livrarea finală — cu vizibilitate clară asupra progresului, atât pentru echipa de vânzări, cât și pentru cea de depozit.

#### 2. Funcționalități Cheie

- Definirea de trasee (rute) de etape, cu cel puțin două faze, validate astfel încât aceeași etapă să nu apară de două ori în același traseu.
- Asignarea traseului de etape direct pe comanda de vânzare, cu propagare automată către livrările (`stock.picking`) asociate.
- Interfață de tip Barcode îmbunătățită: faza curentă și următoarea sunt afișate proeminent în antet, cu badge-uri mari, colorate pentru identificare vizuală rapidă.
- Flux automatizat la validarea unei livrări aflate într-o etapă intermediară: comanda de vânzare avansează la faza următoare (în loc să finalizeze livrarea), se resetează cantitățile scanate/starea "picked" pentru operatorul următor, se reverifică disponibilitatea stocului la tranziția de fază, iar aplicația revine automat la lista de livrări.
- Logică de livrare secundară: câmp nou pe fișa produsului ("Push Secondary Picking") care marchează produsele ce trebuie tratate într-o livrare secundară; livrările cu astfel de produse sunt marcate automat ca nefiind livrarea primară (`is_primary_picking_per_so = False`) pentru filtrare/prioritizare mai ușoară în depozit.
- Vizualizări Kanban dedicate pentru comenzi de vânzare și livrări, grupate pe faza curentă, cu toate coloanele de fază vizibile (chiar dacă sunt goale) și suport drag-and-drop pentru mutarea între etape (restricționat prin reguli de securitate).
- Evidențiere vizuală în Kanban: livrările "Other Pickings" (OP) apar cu fundal verde când livrarea curentă este primară și toate celelalte livrări asociate aceleiași comenzi sunt în starea "Pregătit" sau "Efectuat".
- Ajustarea contorului "Ready" din dashboard-ul aplicației Barcode pentru operațiunile de livrare, numărând doar livrările aflate în faze marcate pentru afișare în barcode (`display_in_barcode`).
- Securitate și control acces: grup dedicat "Phase Admin" cu control complet asupra tranzițiilor de etapă; utilizatorii obișnuiți pot avansa livrarea doar la etapa imediat următoare, în timp ce administratorii de fază pot sări etape sau muta liber; câmpul de selecție a fazei pe comanda de vânzare este needitabil pentru utilizatorii obișnuiți.
- Parametru de sistem `sale_stage_route.confirm_restriction` — dacă este setat, permite confirmarea doar a comenzilor de vânzare care au un traseu de etape definit.

#### 3. Dependențe

- [deltatech_sale_stage](../deltatech_sale_stage/index.md)
- `stock_barcode`
- `stock`

#### 4. Componente Cheie

**Modele**

- `sale.order.stage.route`: Definește traseele și succesiunea etapelor (fazelor) prin care trece o comandă.
- `sale.order`: Extins pentru a integra traseul de etape și a gestiona asignarea fazei inițiale.
- `stock.picking`: Extins pentru a gestiona progresul etapelor în timpul operațiunilor de depozit și integrarea cu aplicația Barcode.

**Vizualizări**

- `views/sale_phase_view.xml`: Configurarea traseelor de etape.
- `views/sale_view.xml`: Îmbunătățiri ale formularului și vizualizării Kanban pentru comanda de vânzare.
- `views/stock_picking_view.xml`: Îmbunătățiri ale formularului, listei și vizualizării Kanban pentru livrări, inclusiv vizualizările de Barcode.
- `views/product_view.xml`: Câmpul "Push Secondary Picking" pe fișa produsului (fila Inventar).

**Acțiuni Automate / Acțiuni Server**

- Nu au fost identificate `ir.cron`, `base.automation` sau `ir.actions.server` — logica de tranziție între faze este declanșată la validarea livrării (acțiune de utilizator), nu programat.

#### 5. Conexiuni

- [deltatech_sale_stage](../deltatech_sale_stage/index.md): furnizează conceptul de bază de fază/etapă pe comanda de vânzare, extins de acest modul cu trasee (rute) și automatizarea tranzițiilor din aplicația Barcode.
- `stock_barcode`: interfața de scanare este extinsă cu afișarea fazei curente/următoare și cu logica de avansare automată la validarea livrării.
