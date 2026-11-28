# Verificarea Comenzilor — Livrări Reținute (localizat la `deltatech_delivery_status_review/index.md`)

- **Nume Tehnic:** `deltatech_delivery_status_review`
- **Versiune:** `20.0.0.2.0`
- **Cale:** [https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_delivery_status_review](https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_delivery_status_review)
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_status_review`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face puntea dintre verificarea comenzilor și amânarea livrărilor: dacă o comandă are un motiv deschis pe poarta „Înainte de livrare" (ramburs mare, adresă incompletă, plată online nefinalizată), livrările ei sunt ținute automat în depozit — rămân în așteptare și nu pot fi validate — până când motivul este aprobat sau se rezolvă de la sine. Nu se instalează automat: se instalează explicit, doar acolo unde se folosește verificarea comenzilor.

#### 2. Funcționalități Cheie

- O comandă cu un motiv deschis pe poarta *Înainte de livrare* are livrările amânate pe toți pașii (pick, pack, out): rămân în *Așteptare*, butonul **Validează** le refuză, iar bifa **Amânată** nu poate fi debifată manual.
- Modulul eliberează doar transferurile pe care le-a reținut el; o amânare făcută altfel (manual, de alt modul) rămâne la locul ei.
- Amânările deja existente în `deltatech_delivery_status` (furnizor de plată cu *Postponed Delivery*, transfer bancar neconfirmat, butonul **Amână**) devin motive vizibile pe comandă, cu autor și cale de ieșire.
- O plată finalizată închide doar propriul motiv — livrarea este eliberată numai dacă nu mai rămâne niciun alt motiv deschis (ex. rambursul sau adresa).
- Butonul **Eliberează** de pe comandă deschide wizardul de aprobare cu motivele care rețin livrarea; acțiunea funcționează și pe mai multe comenzi selectate din listă. Un utilizator fără drept de aprobare primește mesajul cu lista motivelor, nu wizardul.
- Formularul livrării (`stock.picking`) afișează un banner cu aceleași motive ca și comanda; un utilizator de depozit fără drepturi de vânzări poate folosi **Amână** și vede motivele.
- Configurare: cele trei reguli adăugate se găsesc la **Vânzări → Configurare → Reguli de verificare a comenzilor** și pot fi dezactivate din comutatorul **Activ**; filtrul **De verificat** de pe lista comenzilor arată comenzile cu livrări amânate înainte de instalare. Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.order` (extindere): adaugă logica de reținere/eliberare a livrărilor pe baza motivelor de verificare și butonul **Eliberează** care deschide wizardul de aprobare.
- `stock.picking` (extindere): leagă bifa **Amânată** de motivele comenzii, marchează transferurile reținute de verificare, refuză **Validează** cât timp există motive deschise și afișează bannerul cu motivele pe formularul livrării.

**Vizualizări**

- `sale_order_views.xml`: adaugă pe formularul comenzii butonul **Eliberează** și bannerul motivelor care rețin livrarea.
- `stock_picking_views.xml`: adaugă pe formularul livrării panglica **Amânată** și bannerul cu motivele preluate de pe comanda de vânzare.

**Date**

- `review_rule_data.xml`: definește cele trei reguli de verificare pe poarta *Înainte de livrare* (amânare manuală, furnizor de plată cu livrare amânată, transfer bancar neprimit).

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): la instalare, atribuie un motiv manual livrărilor deja amânate prin alte mijloace, ca să intre în coada de verificare existentă.

#### 5. Conexiuni

- [deltatech_delivery_review](../deltatech_delivery_review/index.md): modul-frate opțional — dialogul „Trimite la curier" și raportul de validare a livrărilor numesc motivul care reține livrarea, dacă este instalat.
- `payment` (prin `deltatech_delivery_status`): tranzacțiile de plată închid motivele temporare la confirmare.
