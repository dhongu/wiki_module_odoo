# EMAG Marketplace Connector (localizat la `deltatech_marketplace_emag/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_emag`
- **Versiune:** `19.0.2.3.26`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_emag`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_emag`
- **Ultima Ingestie:** `2026-08-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un cont de seller eMAG lângă Odoo, fără conector, înseamnă catalog, comenzi și stoc ținute manual în două locuri — și, spre deosebire de un magazin propriu, prețul afișat pe eMAG nu e neapărat cel pe care îl vede primul cumpărătorul: o ofertă mai bine clasată pe același produs câștigă butonul „Adaugă în coș" (buy box). Modulul închide acest gol pentru piața din România specific: produsele, categoriile (cu caracteristicile lor obligatorii), comenzile și stocul circulă automat între Odoo și eMAG, adresele de livrare cu geografia românească (județe, localități, sectoarele Bucureștiului) se potrivesc automat cu identificatorii eMAG, iar etichetele AWB pentru curier se generează direct din Odoo. Conectorul se leagă de același framework comun (`deltatech_marketplace`) folosit și de conectorii Shopify, WooCommerce sau Magento, deci adăugarea eMAG lângă un canal deja folosit nu înseamnă învățarea unui al doilea sistem.

#### 2. Funcționalități Cheie

- **Sincronizare bidirecțională**: produsele, comenzile și informațiile de livrare circulă automat între Odoo și eMAG; stocul se exportă periodic, la un interval configurabil, nu instantaneu la fiecare mișcare.
- **Gestiune produse**:
  - Export detalii produs, specificații și imagini către eMAG
  - Gestionarea variantelor de produs și a categoriilor (cu caracteristicile obligatorii/opționale importate odată cu fiecare categorie)
  - Configurarea atributelor de produs specifice eMAG
  - Crearea automată a ofertelor de produs pe eMAG
- **Gestiune comenzi**:
  - Import comenzi din eMAG aflate în starea `NEW`, `IN_PROGRESS` sau `PREPARED` (filtru fix în cod, valabil și pe calea webhook) — comenzile `CANCELED`, `FINALIZED` sau `RETURNED` nu sunt aduse pe această cale
  - Creare automată a comenzilor de vânzare în Odoo, cu județe, localități și sectoarele Bucureștiului mapate la geografia eMAG
  - Comenzile noi sunt confirmate automat înapoi la eMAG (`/order/acknowledge`) dacă bifa **Active On Write** e activă; NU există o sincronizare generică de status înapoi spre eMAG, în afara acestui acknowledge și a push-ului de factură
  - O comandă deja importată care trece ulterior în `CANCELED` pe eMAG **nu** se anulează automat — necesită un **Reimport** manual pe acea comandă
- **Integrare stocuri**:
  - Export periodic, configurabil, al nivelurilor de stoc către eMAG (nu în timp real)
  - Actualizări automate de stoc pentru a preveni supravânzarea
- **Integrare livrare**:
  - Suport pentru metodele de livrare eMAG, inclusiv puncte easybox/locker
  - Generare AWB cu etichetă în format PDF (A4/A5/A6) și ZPL (imprimantă termică Zebra)
  - Istoric al stării livrării, mapat din codurile de stare AWB ale eMAG
  - Import al geografiei românești (localități, sectoare) printr-un pas manual, unic per backend — butonul **Get city** de pe metoda de livrare eMAG; nu se importă automat cu restul datelor și e obligatoriu înainte de primul AWB
- **Buy Box Auto-Pricing**:
  - Cron opțional, dezactivat implicit, care ajustează prețul unei oferte în funcție de rangul ei în buy box-ul eMAG, plafonat între **Min sale price**/**Max sale price** configurate pe produs
  - **Atenție**: dacă Min/Max sale price rămân necompletate (0) pe un produs cu Auto Price activ și rang cunoscut, cron-ul nu sare produsul — trimite efectiv prețul 0 la eMAG; limitele trebuie completate ÎNAINTE de activarea Auto Price
  - Re-ajustare limitată la un număr fix de pași per rulare, ca să nu ruleze necontrolat
- **Facturare**:
  - Push automat al unui **link** către PDF-ul facturii din portalul Odoo (nu conținutul PDF-ului) când o factură legată de o comandă eMAG e validată, dacă backend-ul are activă bifa **Enable Order Push Invoice** ȘI **Active On Write**; cere ca `web.base.url` să fie public
- **Plăți**:
  - Metodele de plată eMAG sunt mapate la payment provideri Odoo; metodele nerecunoscute cad pe Wire Transfer, ca o comandă să nu rămână fără metodă de plată
  - **Fără borderou/decontare prin API**: eMAG Marketplace API (v4.x) nu expune nicio resursă pentru raportul de decontare/comisioane — nu există `/settlement`, `/financial-report` sau echivalent. Borderoul de plăți se obține doar prin descărcare manuală (Excel/CSV) din panoul de vânzător eMAG (Financiar > Rapoarte); conectorul nu îl importă/reconciliază automat
- **Operațiuni programate**:
  - Sincronizare în fundal prin job-uri cron și coada de job-uri comună
  - Intervale de sincronizare configurabile; cron-ul de auto-pricing pe buy box vine dezactivat implicit

#### 3. Dependențe

- `sale`
- `delivery`
- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Modulul este construit peste cadrul marketplace al Deltatech și implementează adaptoare și binder-e specifice cerințelor API ale eMAG. Conform documentației din `readme/DESCRIPTION.md`, implementarea urmează o abordare modulară cu separarea responsabilităților:

- **Backend Adapter**: gestionează comunicarea API cu eMAG (`https://marketplace-api.emag.ro/api-3`), autentificare Basic Auth (nu API key, nu OAuth); rate-limiting-ul (3 apeluri/secundă implicit) e generic, moștenit din `deltatech_marketplace` (token bucket).
- **Modele de binding (binding)**: leagă entitățile Odoo de omoloagele lor din eMAG — binding de produs, comandă, categorie, transportator de livrare și metodă de plată.
- **Servicii de sincronizare**: gestionează fluxul de date între sisteme; webhook-ul care primește push-uri de comenzi de la eMAG este un controller comun din `deltatech_marketplace`, nu unul definit de acest modul.
- **Job-uri programate**: automatizează sincronizarea în fundal — `ir_cron_emag_set_price` (definit în `data/ir_cron_data.xml`) rulează auto-pricing-ul pe buy box (dezactivat implicit).

Pentru detalii suplimentare de configurare și operare, modulul include un manual de utilizare („Manual utilizare eMAG Marketplace.docx"), un ghid `readme/CONFIGURE.md` și un ghid pas-cu-pas `readme/USAGE.md`.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază marketplace peste care este construit conectorul (backend, indicator de sănătate, job-uri, rate-limiting).
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): comanda de vânzare Odoo generată din comanda eMAG importată.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): maparea transportatorului și linia de livrare pe comandă.
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): maparea metodei de plată eMAG către payment provider Odoo (fallback pe Wire Transfer).
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md): link-ul de produs eMAG folosește rutele website-ului Odoo la export.
- [deltatech_delivery](../deltatech_delivery/index.md): contractul de capabilități al curierilor (`cities`, `ship`, `tracking`), butonul **Get city** și cron-ul comun de stare livrare.
- `l10n_ro_edi` / `l10n_ro_edi_stock`: e-Factura (SPV) și eTransport — rămân neatinse de acest conector; push-ul de factură eMAG e doar un link către PDF, nu o depunere SPV.
