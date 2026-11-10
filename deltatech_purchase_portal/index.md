# Purchase Portal (localizat la `deltatech_purchase_portal/index.md`)

- **Nume Tehnic:** `deltatech_purchase_portal`
- **Versiune:** `19.0.1.2.7`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_purchase_portal`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_purchase_portal`
- **Ultima Ingestie:** `2026-11-10`

#### 1. Sumar

Acest modul deschide colaborarea cu furnizorii direct în portalul de achiziții: furnizorul poate edita, din pagina web a unei cereri de ofertă (RFQ), prețul unitar și descrierea liniilor, iar apoi poate accepta și semna oferta electronic, exact ca la comenzile de vânzare. Astfel, negocierea prețurilor și confirmarea ofertelor se pot face online, fără schimb de e-mailuri sau documente semnate manual, iar tot procesul rămâne trasabil în chatter-ul comenzii.

#### 2. Funcționalități Cheie

- **Editare linii RFQ direct din portal** (doar cât timp comanda este în starea „trimisă”): preț unitar (câmp numeric inline) și descriere (câmp text pe mai multe rânduri, cu suport pentru linii noi); modificările se trimit prin cereri scurte și se salvează imediat. Pot fi modificate și adresa de ridicare și datele comenzii.
- **Interfață curată în portal**: buton „Edit” vizibil doar pe RFQ-uri, care comută pagina în mod editare; buton „Display” pentru revenirea la vizualizarea read-only; iconițe aliniate consecvent cu butonul standard „View Details”; descrierea articolului afișată inline lângă imaginea produsului.
- **Acceptare și semnătură electronică** (similar comenzilor de vânzare): fereastră modală de semnătură (`portal.signature_form`) care preia semnătura olografă și numele semnatarului; la semnare, RFQ-ul este confirmat automat ca și comandă de achiziție.
- **Respingerea RFQ din portal**: furnizorul poate respinge cererea de ofertă, cu motiv obligatoriu, lângă butonul de acceptare; RFQ-ul este anulat, iar motivul rămâne documentat în chatter.
- **Trasabilitate**: se salvează pe comanda de achiziție cine a semnat (`signed_by`), când (`signed_on`) și semnătura (`signature`); PDF-ul semnat este atașat în chatter, ca mesaj din partea furnizorului.
- **Adresă de ridicare**: câmp „Pickup Address” pe comanda de achiziție (implicit adresa de livrare a furnizorului), selectabil din adresele furnizorului; buton „Preview” în formularul comenzii, care deschide pagina din portal.
- **Marcaj „procesat în portal”**: comanda este marcată automat ca procesată în portal când ultimul e-mail provine de la un utilizator portal; furnizorul poate comuta marcajul din pagina comenzii.
- **Liste în portal**: coloane și filtre pentru faza comenzii (din `deltatech_purchase_phase`), coloană de stare și export XLSX al comenzilor din portal (utilizatori autentificați).
- **Securitate**: toate acțiunile sunt protejate prin token-ul standard de acces al portalului; editarea inline e permisă doar când comanda este în starea „trimisă”, iar liniile de tip afișare (secțiuni/note) nu pot fi editate; orice alt câmp, linie din altă comandă sau preț invalid refuză cererea fără a salva nimic.

#### 3. Dependențe

- `purchase`
- `portal`
- [deltatech_purchase_phase](../deltatech_purchase_phase/index.md)

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): `signed_by`, `signed_on`, `signature`, `processed_in_portal`, `partner_pickup_address_id` (calculat, stocat, obligatoriu), `_get_pickup_addresses()` (extensibilă de alte module), `action_preview_purchase_order()`; `message_post` actualizează `processed_in_portal`.
- `purchase.order.line` (extins): `vendor_note` (observație furnizor, păstrat pentru compatibilitate; portalul editează descrierea standard).

**Vizualizări**

- `view_purchase_order_form_pickup_address`: adaugă adresa de ridicare și butonul „Preview” în formularul comenzii.
- `portal_my_purchase_order`, `purchase_order_portal_content`: pagina comenzii în portal (mod editare, acceptare/semnare, respingere).
- `portal_searchbar_export_xlsx_purchase`, `portal_my_purchase_orders_phase_filter`, `portal_my_purchase_rfqs_phase_filter`, `portal_my_purchase_orders_status`, `portal_my_purchase_rfqs_status`: export XLSX, faza și starea în listele din portal.

**Rute (controller)**

- `/my/purchase/<id>/update`, `/update_pickup`, `/update_price_note` (JSON): salvare date, adresă de ridicare, preț/descriere/observație.
- `/my/purchase/<id>/accept` (JSON): semnare și confirmare; `/decline` (POST): respingere cu motiv; `/toggle_processed` (POST); `/my/purchase/export_xlsx` (GET).
- Modul JS frontend `static/src/js/purchase.esm.js` în `web.assets_frontend`.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_purchase_phase](../deltatech_purchase_phase/index.md): dependența directă — furnizează faza (stadiul) comenzii de achiziție, pe care fluxul de acceptare/semnare din portal o avansează.
