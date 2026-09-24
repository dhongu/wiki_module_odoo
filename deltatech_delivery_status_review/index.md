# Verificarea Comenzilor — Livrări Reținute (localizat la `deltatech_delivery_status_review/index.md`)

- **Nume Tehnic:** `deltatech_delivery_status_review`
- **Versiune:** `19.0.0.1.1`
- **Cale:** [https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_delivery_status_review](https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_delivery_status_review)
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_status_review`
- **Ultima Ingestie:** `2026-09-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face puntea dintre verificarea comenzilor și amânarea livrărilor: dacă o comandă are un
motiv deschis pe poarta „Înainte de livrare" (ramburs mare, adresă incompletă, plată online
nefinalizată), livrarea ei de ieșire este ținută automat în depozit — rămâne în așteptare și nu
poate fi validată — până când motivul este aprobat sau se rezolvă de la sine. Se instalează automat
când sunt prezente ambele module pe care le leagă, fără configurare suplimentară.

#### 2. Funcționalități Cheie

- O comandă cu un motiv deschis pe poarta *Înainte de livrare* are livrările de ieșire amânate
  automat: rămân în *Așteptare* și butonul **Validează** le refuză.
- Amânările deja existente în `deltatech_delivery_status` (furnizor de plată cu *Postponed
  Delivery*, transfer bancar neconfirmat, butonul **Amână**) devin motive vizibile pe comandă, cu
  autor și cale de ieșire.
- O plată finalizată închide doar propriul motiv — livrarea este eliberată doar dacă nu mai rămâne
  niciun alt motiv deschis (ex. rambursul sau adresa).
- Butonul **Eliberează** de pe comandă deschide wizardul de aprobare cu motivele care rețin
  livrarea, în loc să ridice amânarea fără verificare; un utilizator fără drept de aprobare pentru
  toate motivele primește mesajul cu lista lor, nu wizardul.
- Formularul livrării (`stock.picking`) afișează un banner cu aceleași motive ca și comanda, ca
  operatorul din depozit să știe de ce nu poate valida.
- La instalare, livrările deja amânate prin alte mijloace primesc automat un motiv manual, ca să
  intre în coada de verificare și să fie eliberate prin același flux (`post_init_hook`).
- Trei reguli noi de verificare, toate pe poarta *Înainte de livrare*: *Livrare amânată de un
  operator* (aprobare manuală), *Furnizorul de plată reține livrarea* și *Transfer bancar neprimit*
  (ambele temporare, se rezolvă singure la confirmarea tranzacției).

#### 3. Dependențe

- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.order` (extindere): adaugă logica de reținere/eliberare a livrărilor pe baza motivelor de
  verificare și butonul **Eliberează** care deschide wizardul de aprobare.
- `stock.picking` (extindere): leagă bifa **Amânată** de motivele comenzii, refuză **Validează** cât
  timp există motive deschise și afișează bannerul cu motivele pe formularul livrării.

**Vizualizări**

- `sale_order_views.xml`: adaugă pe formularul comenzii butonul **Eliberează** și bannerul motivelor
  care rețin livrarea.
- `stock_picking_views.xml`: adaugă pe formularul livrării panglica **Amânată** și bannerul cu
  motivele preluate de pe comanda de vânzare.

**Date**

- `review_rule_data.xml`: definește cele trei reguli de verificare pe poarta *Înainte de livrare*
  (amânare manuală, furnizor de plată cu livrare amânată, transfer bancar neprimit).

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): la instalare, atribuie un motiv manual livrărilor deja amânate
  prin alte mijloace, ca să intre în coada de verificare existentă.

#### 5. Conexiuni

- [deltatech_delivery_review](../deltatech_delivery_review/index.md): modul-frate opțional — dialogul „Trimite la curier" și raportul de
  validare a livrărilor numesc motivul care reține livrarea, dacă este instalat.
- `payment` (prin `deltatech_delivery_status`): tranzacțiile de plată închid motivele temporare la
  confirmare.
