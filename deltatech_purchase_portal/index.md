# Purchase Portal (localizat la `deltatech_purchase_portal/index.md`)

- **Nume Tehnic:** `deltatech_purchase_portal`
- **Versiune:** `20.0.1.2.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_purchase_portal
- **Cale Locală:** `odoo-addons/bitshop/deltatech_purchase_portal`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul deschide colaborarea cu furnizorii direct în portalul de achiziții: furnizorul poate edita, din pagina web a unei cereri de ofertă (RFQ), prețul unitar și descrierea liniilor, iar apoi poate accepta și semna oferta electronic, la fel ca la comenzile de vânzare. Negocierea prețurilor și confirmarea ofertelor se fac online, fără schimb de e-mailuri sau documente semnate manual, iar procesul rămâne trasabil în chatter-ul comenzii.

#### 2. Funcționalități Cheie

- **Editare linii RFQ din portal** (doar în starea „RFQ Sent"): preț unitar și descriere multilinie; modificările se salvează automat. Liniile de tip secțiune/notă nu pot fi editate.
- **Interfață clară în portal**: butonul **Edit** comută pagina în mod editare, **Display** revine la vizualizarea doar-citire cu totalurile recalculate.
- **Acceptare și semnătură electronică**: fereastra „Validate RFQ" preia semnătura și numele semnatarului; RFQ-ul devine comandă de achiziție (sau „To Approve" dacă aprobarea în două trepte o cere), iar PDF-ul semnat se atașează în chatter.
- **Respingere cu motiv obligatoriu**: RFQ-ul se anulează, iar motivul apare în chatter.
- **Fază și stare de procesare**: în lista din portal apar coloanele **Phase** și **Status** (Not processed / Processed); starea urmează mesajele din chatter (furnizor vs. cumpărător). Filtrul implicit este „For processing".
- **Comenzile furnizorului** (**My Account > Our Orders**): filtre pe fază și buton **Export Excel** pentru pagina afișată.
- **Trasabilitate**: pe comandă se păstrează `signed_by`, `signed_on` și semnătura.
- **Securitate**: acces prin token-ul standard de portal; editarea este permisă doar în starea „RFQ Sent".
- **Pași în Odoo**: furnizorul primește acces portal (**Grant portal access**) pe persoana de contact; RFQ-ul apare în portal doar după trimiterea efectivă a e-mailului (**Send RFQ**). Pe Odoo 20 portalul afișează doar descrierea liniei, deci aceasta trebuie completată înainte de trimitere. Fluxul detaliat este în fișa consultantului.

#### 3. Dependențe

- `purchase`
- `portal`
- [deltatech_purchase_phase](../deltatech_purchase_phase/index.md)

#### 4. Componente Cheie

Pe baza `readme/DESCRIPTION.md` (secțiunea „Technical notes"):

**Modele**

- `purchase.order`: extins cu `signed_by`, `signed_on`, `signature`.
- `purchase.order.line`: extins cu `vendor_note` (păstrat pentru compatibilitate; portalul editează descrierea standard `name`).

**Vizualizări**

- `views/portal_templates.xml`: șabloanele portalului (butoane Edit / Accept & Sign / Reject, coloane Phase și Status).
- `views/purchase_view.xml`: adaptări în formularul comenzii de achiziție.
- `static/src/js/purchase.esm.js`: logica front-end de editare, încărcată în `web.assets_frontend`.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri; un controller extinde controllerul standard al portalului de achiziții și expune o rută JSON pentru actualizarea prețului/descrierii liniilor, cu validări de acces și stare.

#### 5. Conexiuni

- [deltatech_purchase_phase](../deltatech_purchase_phase/index.md): dependență directă; furnizează faza comenzii de achiziție afișată și avansată în portal.
