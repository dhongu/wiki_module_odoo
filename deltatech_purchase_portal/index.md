# Purchase Portal (localizat la `deltatech_purchase_portal/index.md`)

- **Nume Tehnic:** `deltatech_purchase_portal`
- **Versiune:** `19.0.1.2.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_purchase_portal`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_purchase_portal`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul deschide colaborarea cu furnizorii direct în portalul de achiziții: furnizorul poate edita, din pagina web a unei cereri de ofertă (RFQ), prețul unitar și descrierea liniilor, iar apoi poate accepta și semna oferta electronic, exact ca la comenzile de vânzare. Astfel, negocierea prețurilor și confirmarea ofertelor se pot face online, fără schimb de e-mailuri sau documente semnate manual, iar tot procesul rămâne trasabil în chatter-ul comenzii.

#### 2. Funcționalități Cheie

- **Editare linii RFQ direct din portal** (doar cât timp comanda este în starea „trimisă”): preț unitar (câmp numeric inline) și descriere (câmp text pe mai multe rânduri, cu suport pentru linii noi).
- **Interfață curată în portal**: buton „Edit” vizibil doar pe RFQ-uri, care comută pagina în mod editare; buton „Display” pentru revenirea la vizualizarea read-only; iconițe aliniate consecvent cu butonul standard „View Details”; descrierea articolului afișată inline lângă imaginea produsului.
- **Acceptare și semnătură electronică** (similar comenzilor de vânzare): fereastră modală de semnătură (`portal.signature_form`) care preia semnătura olografă și numele semnatarului; la semnare, RFQ-ul este confirmat automat ca și comandă de achiziție.
- **Trasabilitate**: se salvează pe comanda de achiziție cine a semnat (`signed_by`), când (`signed_on`) și semnătura (`signature`); PDF-ul semnat este atașat automat în chatter.
- **Securitate**: toate acțiunile sunt protejate prin token-ul standard de acces al portalului; editarea inline e permisă doar când comanda este în starea „trimisă”, iar liniile de tip afișare (secțiuni/note) nu pot fi editate.

#### 3. Dependențe

- `purchase`
- `portal`
- [deltatech_purchase_phase](../deltatech_purchase_phase/index.md)

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe fișierul `readme/DESCRIPTION.md`, care nu detaliază componentele tehnice individuale. Conform fluxului de ingestie, analiza codului pentru modele, vizualizări și acțiuni automate a fost omisă, deoarece Readme-ul este prezent și nu solicită explicit această analiză. Din manifest se remarcă totuși extinderea modelului `purchase.order` (câmpurile `signed_by`, `signed_on`, `signature`) și `purchase.order.line` (câmpul `vendor_note`, păstrat pentru compatibilitate), o rută JSON pentru actualizarea prețului/descrierii liniilor, un controller ce reutilizează controller-ul standard al portalului de achiziții pentru verificările de acces, plus un modul JS frontend (`static/src/js/purchase.esm.js`) încărcat în `web.assets_frontend`.

#### 5. Conexiuni

- [deltatech_purchase_phase](../deltatech_purchase_phase/index.md): dependența directă — furnizează faza (stadiul) comenzii de achiziție, pe care fluxul de acceptare/semnare din portal o avansează.
