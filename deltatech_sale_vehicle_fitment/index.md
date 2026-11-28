# Vânzare după utilaj (Sale Vehicle Fitment)

- **Nume Tehnic:** `deltatech_sale_vehicle_fitment`
- **Versiune:** `20.0.1.4.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_sale_vehicle_fitment
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_vehicle_fitment`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul îi permite agentului de vânzări să vândă piese după vehiculul sau utilajul clientului: se alege utilajul pe ofertă, apoi se adaugă din catalogul de produse piesele care i se potrivesc, cu stocul liber la vedere. Reduce erorile de comandă și timpul petrecut căutând piesa potrivită, mai ales la comenzile telefonice.

#### 2. Funcționalități Cheie

- **Utilajele clientului:** fila *Utilaje* pe formularul clientului; o ofertă nouă propune utilajul când clientul are unul singur, iar utilajul unei comenzi confirmate se adaugă clientului pentru data viitoare. Un contact fără utilaje folosește utilajele companiei.
- **Utilajul pe ofertă**, cu butonul **Piese compatibile** (cheie): se alege în trei pași (marcă, serie, generație), este păstrat la schimbarea clientului (comanda telefonică poate începe pe un client generic).
- **Catalogul ofertei** se deschide pe piesele care se potrivesc (la nivel de model, serie sau marcă) plus cele universale, doar cu stoc; filtrele *Se potrivește utilajului* și *În stoc* pot fi scoase. Căutarea găsește piesele după marca, seria sau modelul pe care le deservesc.
- **Stocul** din depozitul comenzii: *În stoc* păstrează produsele stocabile cu stoc liber plus cele nestocabile; cardul fiecărui produs stocabil arată stocul liber alături de cantitatea disponibilă.
- **Găsește echivalente** pe liniile de marfă neacoperite de stocul liber (și pe comenzi confirmate): deschide catalogul pe piesele aceleiași categorii care se potrivesc și sunt în stoc; pe celelalte linii rămâne pictograma *Alternative*.
- **Carduri ca în portalul B2B:** utilajul potrivit („+N” pentru celelalte), „Pe comandă” sau „Sosește ~data” când nu e stoc (sursa sosirii poate fi dată de alt modul), termenul de livrare („24 h”, „3 zile”).
- **Catalog ca linii** (comutator kanban/listă): produs și cod, potrivire, preț net, stoc, livrare și câmp cantitate cu butonul + care adaugă pe linia comenzii.
- **Avertizare:** linia al cărei produs nu se potrivește utilajului primește o pictogramă, iar oferta arată câte linii nu se potrivesc; comanda poate fi totuși confirmată.
- Categorii în panoul lateral al catalogului și grupare după categorie de produs. Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md). Necesită catalogul de utilaje și potrivirile completate în *Vehicle Fitment*, plus aplicația Inventar.

#### 3. Dependențe

- `deltatech_vehicle_fitment`
- [deltatech_widget_hierarchy_m2o](../deltatech_widget_hierarchy_m2o/index.md)
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): `vehicle_model_id`, `vehicle_incompatible_count`, deschiderea catalogului filtrat (`action_add_from_catalog`, `action_add_vehicle_parts`), adăugarea utilajului la client la confirmare.
- `sale.order.line` (extins): `vehicle_incompatible`, `vehicle_short_of_stock`, `action_vehicle_alternatives`.
- `product.product` (extins): câmpurile cardului de catalog (potrivire, stare stoc, etichete de livrare) și hook-ul `_get_catalog_arrivals`.
- `res.partner` (extins): `vehicle_model_ids`, utilajele clientului.

**Vizualizări**

- `res_partner_views.xml`: fila *Utilaje* a clientului.
- `sale_order_views.xml`: câmpul utilaj, butonul *Piese compatibile*, avertizările și *Găsește echivalente*.
- `product_catalog_views.xml`: cardurile și lista catalogului (cu active JS `product_catalog_list`).

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `deltatech_vehicle_fitment`: catalogul de utilaje și potrivirile pieselor (fără pagină wiki încă).
