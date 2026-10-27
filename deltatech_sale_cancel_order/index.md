# Sale Cancel Order (localizat la `deltatech_sale_cancel_order/index.md`)

- **Nume Tehnic:** `deltatech_sale_cancel_order`
- **Versiune:** `19.0.0.2.7`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_cancel_order`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_cancel_order`
- **Ultima Ingestie:** `2026-10-27`

#### 1. Sumar

Modulul oferă clienților posibilitatea de a solicita anularea unei comenzi de vânzare direct din portal. În loc să anuleze efectiv comanda, înregistrează în backend o cerere de anulare, însoțită obligatoriu de un motiv, astfel încât un operator să decidă manual dacă și când anulează comanda. Comenzile cu cerere de anulare sunt evidențiate vizual și pot fi filtrate, iar echipa de vânzări poate fi notificată prin e-mail, în funcție de setări. Procesul de anulare rămâne astfel controlat de companie, cu transparență față de client.

#### 2. Funcționalități Cheie

- Clientul poate solicita anularea unei comenzi din portal (prin fluxul de refuz al ofertei), cu motiv obligatoriu.
- Comanda nu este anulată efectiv: se marchează `cancel_requested`, iar un operator o poate anula manual.
- Comenzile cu cerere de anulare pot fi filtrate, apar cu roșu în listă, au o bară roșie în formular, iar în portal apare o insignă „Cancel requested” în lista de comenzi.
- Motivul cererii apare în chatter-ul comenzii și al transferurilor de stoc asociate.
- Cererea se propagă pe transferurile de stoc ale comenzii (`stock.picking.cancel_requested`), iar validarea unui transfer cu anulare solicitată este blocată cu un mesaj de eroare, ca să nu fie livrată o comandă pentru care clientul a cerut anularea.
- În Vânzări → Configurare se poate activa trimiterea unui e-mail la o cerere de anulare, către agentul de vânzări al comenzii și către parteneri suplimentari aleși în setări.
- Insigna din lista portalului este ancorată pe data comenzii, deci modulul poate coexista cu alte module care adaugă coloane în portal.

#### 3. Dependențe

- `sale_stock`
- `portal`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): câmpul `cancel_requested`; `set_to_cancel(reason)` marchează comanda și transferurile ei, postează motivul în chatter-ul transferurilor și trimite e-mailul, dacă este activat; `write` propagă `cancel_requested` pe transferuri.
- `stock.picking` (extins): câmpul `cancel_requested`; `button_validate` ridică `UserError` dacă anularea este solicitată.
- `res.config.settings` (extins): `send_cancel_mail` (parametrul `sale_cancel_order.default_email_send`) și `send_cancel_mail_to` (parametrul `sale_cancel_order.default_email_to`).
- Controller `CustomerPortal` (extins): `portal_quote_decline` tratează refuzul din portal ca o cerere de anulare, apelează `set_to_cancel` și postează motivul pe comandă.

**Vizualizări**

- `view_order_form_cancel`, `view_quotation_tree_cancel`, `view_order_tree_cancel`, `view_sales_order_filter_cancel`: bară roșie în formular, evidențiere în liste, filtru în căutare pentru comenzile de vânzare.
- `view_picking_form_cancel`, `view_picking_tree_cancel`, `view_picking_search_cancel`, `picking_view_kanban_inherit_cancel`: semnalizarea și filtrarea transferurilor cu anulare solicitată.
- `res_config_settings_view_form`: setările pentru e-mailul de anulare, în configurarea Vânzărilor.
- `sale_order_portal_content`, `sale_order_portal_template_cancel`, `portal_my_quotations_cancel`, `portal_my_orders_cancel`: formularul de cerere și insigna „Cancel requested” în portal.

**Acțiuni Automate / Acțiuni Server**

- `mail_template_cancel_order`: șablonul de e-mail trimis la o cerere de anulare, doar dacă opțiunea este activată în setări. Modulul nu definește sarcini `ir.cron` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_delivery_portal](../deltatech_delivery_portal/index.md): modifică celula de stare a livrării din lista portalului; insigna de anulare este poziționată să coexiste cu el.
- [deltatech_delivery_relay](../deltatech_delivery_relay/index.md): adaugă o coloană AWB în lista portalului; insigna de anulare este ancorată să funcționeze alături de ea.
