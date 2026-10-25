# Courier Handover Report (Proces-verbal de predare-primire colete)

- **Nume Tehnic:** `deltatech_delivery_handover`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_handover
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_handover`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite predarea coletelor către curier direct din lista de AWB-uri sau de livrări și tipărește procesul-verbal de predare-primire pe care îl semnează șoferul. Confirmarea predării marchează momentul în care coletele pleacă din depozit, iar pentru curierii care o permit, comanda de ridicare se face dintr-un singur loc, per predare, nu per AWB.

#### 2. Funcționalități Cheie

- **Creare predare din selecție:** din **Inventory → Operations → Delivery AWB → Delivery Tracking**, din lista de AWB-uri sau din orice listă de livrări (ex. *Shipping Desk*), acțiunea **Hand Over to Courier** creează câte o predare (ciornă) pentru fiecare curier.
- **Selecția AWB-urilor eligibile:** intră doar AWB-ul folosit curent de livrare, la o livrare de ieșire pe care curierul nu o are încă și care nu este deja pe altă predare; celelalte sunt lăsate deoparte, iar predarea arată motivul.
- **Conținutul predării:** curier, dată, cine a predat, șofer și vehicul, plus coletele cu destinatar, localitate, număr de colete, greutate și ramburs, cu totaluri.
- **Confirmare predare:** livrările trec în *In Transit* și păstrează data predării; un AWB poate fi pe o singură predare, cu excepția celor anulate.
- **Protecție la statusul curierului:** o interogare de status care răspunde încă cu pre-avizul AWB-ului sau cu nimic nu mai readuce livrările la stadiul anterior (curierul scanează adesea coletul la ore după ridicare).
- **Raport tipărit** (*Proces-verbal de predare-primire colete*): lista coletelor cu totaluri (AWB-uri, colete, greutate, ramburs pe monedă) și casete de semnătură pentru depozit și șofer; scanarea semnată se atașează în **Signed Report**.
- **Comandă de ridicare curier** (o singură comandă pentru toate coletele predării):
  - FAN Courier se comandă din predare (**Order Courier Pickup**), în intervalul setat pe transportator, cu posibilitate de anulare; comanda este facturabilă și se face o singură dată;
  - Cargus își creează singur comenzile din AWB-urile zilei; **Check Pickup** doar citește comanda înapoi (număr, status, AWB-uri contorizate);
  - GLS și Sameday ridică odată cu AWB-ul, nu e nimic de comandat.
- **Anulare:** o predare ciornă poate fi anulată de orice utilizator de inventar; una confirmată doar de un manager de inventar, iar coletele revin la *Pre advice* până la următoarea interogare de status.
- **Listă predări:** **Inventory → Operations → Delivery AWB → Courier Handovers**.
- **Integrare cu tabloul de bord:** cu `deltatech_delivery_dashboard`, o predare confirmată datează predarea pe AWB, pornește SLA-ul de livrare și numără coletul la *Handed Over Today* (v. [deltatech_delivery_dashboard](../deltatech_delivery_dashboard/index.md)).

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.handover`: predarea către curier (mail.thread + activități), cu secvență proprie, șofer, vehicul, raport semnat și ciclu ciornă/confirmată/anulată.
- `delivery.handover.line`: linia predării, cu AWB-ul, destinatarul, coletele, greutatea și rambursul.
- `delivery.awb` (extins): liniile de predare ale AWB-ului (`handover_line_ids`) și acțiunea de creare a predării.
- `delivery.carrier` (extins): intervalul de ridicare (*Pickup From / Pickup Until*).
- `stock.picking` (extins): data predării (`courier_handover_date`), protecția statusului de curier (`_apply_delivery_status`) și acțiunea de creare a predării.

**Vizualizări**

- `view_delivery_handover_list`, `view_delivery_handover_form`, `view_delivery_handover_search`: lista, formularul și căutarea predărilor.
- `view_delivery_carrier_form_pickup`: câmpurile de ridicare pe transportator.
- `view_picking_form_handover`: informații despre predare pe formularul livrării.
- `action_report_delivery_handover`: raportul QWeb de predare-primire.

**Acțiuni Automate / Acțiuni Server**

- `action_server_handover_from_awb`, `action_server_handover_from_picking`: acțiunea **Hand Over to Courier** din liste de AWB-uri, respectiv de livrări.
- `seq_delivery_handover`: secvența numerotării predărilor.
- `delivery_handover_company_rule`: regulă multi-companie.

#### 5. Conexiuni

- [deltatech_delivery_dashboard](../deltatech_delivery_dashboard/index.md): predarea confirmată pornește SLA-ul și contorul *Handed Over Today*.
- [deltatech_delivery_fc](../deltatech_delivery_fc/index.md): comandă de ridicare FAN Courier din predare.
- [deltatech_delivery_gls](../deltatech_delivery_gls/index.md): GLS ridică odată cu AWB-ul.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): interogarea de status nu mai suprascrie livrările predate.
