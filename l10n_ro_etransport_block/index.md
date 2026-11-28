# Romania - Blocare e-Transport (localizat la `l10n_ro_etransport_block/index.md`)

- **Nume Tehnic:** `l10n_ro_etransport_block`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_etransport_block
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_etransport_block`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde `l10n_ro_edi_stock` pentru a bloca validarea transferurilor care conțin produse cu risc fiscal ridicat până când UIT-ul primit de la ANAF devine **Validat**, și pentru a actualiza automat starea UIT printr-un job programat. Asigură astfel conformitatea cu e-Transport pentru categoriile de mărfuri cu risc fiscal ridicat.

#### 2. Funcționalități Cheie

- Câmpul **Risc fiscal ridicat (e-Transport obligatoriu)** pe produs, în fila Contabilitate, secțiunea „România — e-Transport". Categorii tipice ANAF: combustibili, tutun, alcool, metale prețioase, echipamente IT și electrocasnice.
- Blocarea validării (`button_validate`) cât timp UIT-ul nu este în starea **Validat**, cu mesaj care numește produsele și banner de avertizare pe aviz. Avizele fără produse marcate nu sunt afectate.
- Blocarea se aplică doar transferurilor declarate de companie (OUG 41/2022, art. 8 alin. (1)): avize, recepții din achiziții intracomunitare și din import. La achiziția internă declară furnizorul, deci recepția nu se blochează, iar UIT-ul lui se reține în câmpul **UIT furnizor** (fila eTransport).
- Bannere informative pe comenzile de vânzare și de achiziție care conțin astfel de produse.
- Actualizare automată a stării UIT: acțiunea programată **RO e-Transport: Actualizare automată status UIT** rulează la 30 de minute pentru avizele în starea Trimis, ca alternativă la butonul **Preluare stare**; erorile se înregistrează în documentul e-Transport al avizului.
- În import de date demo și în teste (context `demo_mode`) blocarea este dezactivată. Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `l10n_ro_edi_stock`
- `purchase`
- `sale`

#### 4. Componente Cheie

**Modele**

- `product.template` (extindere): câmpul de risc fiscal ridicat.
- `stock.picking` (extindere): blocarea validării după starea UIT și câmpul UIT furnizor.
- `purchase.order` / `sale.order` (extinderi): bannerele de avertizare și datele de risc fiscal/UIT.

**Vizualizări**

- `views/product_template_view.xml`, `views/stock_picking_view.xml`, `views/purchase_order_view.xml`, `views/sale_order_view.xml`: câmpul și bannerele.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_etransport_fetch_status` (`data/ir_cron.xml`): la 30 de minute interogează ANAF pentru avizele cu UIT în starea Trimis și actualizează starea.

#### 5. Conexiuni

- `l10n_ro_edi_stock`: asigură declarația e-Transport și starea UIT pe care se bazează blocarea.
- [l10n_ro_esigiliu](../l10n_ro_esigiliu/index.md): evidența sigiliilor electronice pe transporturile monitorizate, cu UIT e-Transport.
