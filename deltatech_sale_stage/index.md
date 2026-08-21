# Deltatech Sale Order Stage (localizat la `deltatech_sale_stage/index.md`)

- **Nume Tehnic:** `deltatech_sale_stage`
- **Versiune:** `19.0.1.2.5`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_stage`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_stage`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul ajută echipa de vânzări să țină sub control fiecare comandă prin introducerea unui sistem de faze (etape) personalizabile pentru comenzile de vânzare. În loc să se bazeze doar pe statusurile standard din Odoo (Ciornă, Confirmat, Finalizat), echipa își poate defini propriile faze interne — precum *Confirmat*, *Pregătit*, *Expediat*, *Livrat* — și poate urmări exact în ce etapă a procesului de onorare se află fiecare comandă. Fazele avansează automat pe măsură ce comanda parcurge fluxul standard (trimitere ofertă, confirmare, facturare, anulare) și pe măsură ce livrările sunt validate sau își schimbă statusul de curierat, oferind vizibilitate completă echipelor de back-office.

#### 2. Funcționalități Cheie

- **Vizibilitate completă pentru back-office:** fiecare comandă de vânzare afișează faza curentă sub forma unui badge colorat, ușor de identificat dintr-o privire.
- **Configurare flexibilă a fazelor:** se pot defini oricâte faze sunt necesare, fiecare cu nume, culoare și secvență. Fazele se gestionează din Vânzări → Configurare → Faze comenzi de vânzare.
- **Progresie automată a fazelor:** fazele avansează automat odată cu fluxul standard Odoo — ofertă trimisă → *Trimis*, comandă confirmată → *Confirmat*, comandă facturată → *Facturat*, comandă anulată → *Anulat*.
- **Actualizare a fazei în funcție de livrare:** la validarea unei expedieri sau la schimbarea statusului de livrare (preluat de curier, livrat clientului, refuzat), faza comenzii de vânzare asociate se actualizează automat, fără intervenție manuală.
- **Declanșare de acțiuni automate:** fiecărei faze i se poate atașa o acțiune de server opțională, care rulează automat când comanda intră în acea fază (notificări, actualizări de înregistrări, integrări).
- **Impunerea fluxului de comandă:** dacă pe o comandă ciornă se setează manual o fază marcată ca *Confirmat*, comanda este confirmată automat; dacă se setează o fază marcată ca *Anulat*, comanda este anulată — păstrând datele consecvente.
- **Căutare și grupare după fază:** comenzile de vânzare pot fi filtrate și grupate după fază direct din vizualizarea listă.
- **Faza implicită pe tipul de operațiune de depozit:** fiecărui tip de operațiune (ex. comenzi de livrare) i se poate atribui o fază implicită, aplicată automat la validarea livrării de acel tip.

#### 3. Dependențe

- `sale_stock`
- [deltatech_widget_many2one_badge](../deltatech_widget_many2one_badge/index.md)

#### 4. Componente Cheie

> Conform DESCRIPTION.md, componentele de mai jos sunt cele menționate explicit în descrierea funcțională a modulului.

**Modele**

- `sale.order.phase`: definește fazele personalizabile ale comenzii de vânzare (nume, culoare, secvență, acțiune de server opțională, marcaje de tip Confirmat/Anulat).
- `sale.order` (extins): adaugă faza curentă a comenzii, progresia automată pe flux și impunerea confirmării/anulării în funcție de fază.
- `stock.picking.type` (extins): permite atribuirea unei faze implicite per tip de operațiune de depozit.
- `stock.picking` (extins): actualizează faza comenzii de vânzare la validarea livrării sau la schimbarea statusului de curierat.

**Vizualizări**

- `sale_view.xml`: badge-ul colorat al fazei pe comanda de vânzare, meniul de configurare a fazelor și filtrele/gruparea după fază.
- `stock_picking_type_view.xml`: câmpul de fază implicită pe tipul de operațiune de depozit.

**Acțiuni Automate / Acțiuni Server**

- Acțiune de server opțională per fază: configurabilă pe fiecare înregistrare `sale.order.phase`, rulează automat când comanda intră în faza respectivă.

#### 5. Conexiuni

- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): depinde de acest modul, extinzând sistemul de faze pentru comenzile provenite din marketplace.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): furnizează statusurile de curierat care declanșează schimbările automate de fază (preluat, AWB generat, livrat, refuzat).
