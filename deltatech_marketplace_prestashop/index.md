# Conector Marketplace PrestaShop (localizat la `deltatech_marketplace_prestashop/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_prestashop`
- **Versiune:** `19.0.0.2.15`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_prestashop`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_prestashop`
- **Ultima Ingestie:** `2026-08-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Conectorul Deltatech pentru marketplace PrestaShop permite integrarea directă între sistemul ERP Odoo și PrestaShop, una dintre cele mai populare platforme open-source de comerț electronic. Modulul asigură sincronizarea datelor esențiale de business, astfel încât magazinele online PrestaShop pot fi administrate direct din Odoo. Rezultatul este o soluție unificată pentru gestionarea produselor, a clienților și a comenzilor, eliminând introducerea dublă de date și păstrând o singură sursă de adevăr pentru informațiile comerciale.

#### 2. Funcționalități Cheie

- **Gestionarea completă a produselor:** sincronizarea catalogului de produse între Odoo și PrestaShop, suport pentru variante, atribute și caracteristici, import/export de imagini și conținut multimedia, gestionarea categoriilor de produse și a categoriilor publice. Exportul (creare/actualizare pe PrestaShop) trimite preț, denumire, EAN, greutate și categorii publice, la cerere sau automat la scriere (comutatorul *Active On Write*). Stocul circulă într-un singur sens: **doar din PrestaShop către Odoo** — modulul nu implementează export de stoc către PrestaShop.
- **Integrare avansată a clienților:** importul clienților PrestaShop în baza de contacte Odoo, sincronizarea datelor de client, a adreselor și a istoricului de cumpărături, gestionarea grupurilor de clienți și a asocierilor.
- **Gestionarea cuprinzătoare a comenzilor:** importul comenzilor de vânzare din PrestaShop în Odoo, cu posibilitatea de a filtra importul după statusul comenzii (pe baza statusurilor deja sincronizate prin Sale Stage), crearea automată a comenzilor de vânzare Odoo și urmărirea îndeplinirii și livrării comenzilor.
- **Push dinspre Odoo spre PrestaShop:** statusul comenzii se trimite către PrestaShop doar dacă *Active On Write* e activat pe elementul „Sale Order"; în schimb, numărul de tracking (la trimiterea coletului către curier) și legătura facturii (la postarea facturii) se trimit **necondiționat**, indiferent de acest comutator.
- **Webhook de intrare (nu ieșire):** fiecare tip de date sincronizat expune un link de webhook pe care **PrestaShop îl apelează către Odoo** (nu invers) pentru a declanșa imediat importul unei comenzi, fără a aștepta cron-ul orar.
- **Wizard „Marketplace sync":** acțiune contextuală de pe produse/șabloane de produs pentru export la cerere (implicit `Direction = Export`, `Update Mode = Stock`; comutat manual pe `All` include și preț/nume) — ignoră comutatorul Active On Write.
- **Capabilități internaționale:** suport multilingv prin legături de limbă, gestionarea multi-valută, sincronizarea țărilor și a județelor (regiuni/state), gestionarea livrărilor și a taxelor internaționale.
- **Integrare livrare și plată:** suport pentru curierii de livrare PrestaShop, sincronizarea metodelor de plată și a procesatorilor, integrarea cu depozitele pentru îndeplinirea comenzilor.
- **Îmbunătățirea procesului de vânzare:** suport pentru etapele de vânzare și urmărirea statusului comenzilor, sincronizarea etichetelor de vânzare, atribuirea comenzilor pe echipe cu asociere de depozit.
- **Operațiuni automatizate:** sarcini programate de sincronizare (cron comun „Marketplace: Get Orders"), procesare în fundal cu gestionare prin coadă (queue_job) și opțiuni de sincronizare incrementală (bifa „Only Missing").
- **API pentru facturi:** ruta `/marketplace/sale_order/get_invoice`, autentificată cu token-ul de securitate al backend-ului, prin care PrestaShop (sau alt sistem extern) poate cere URL-ul PDF-ului facturii unei comenzi importate.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de componente nu au fost extrase din cod deoarece fișierul `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie. Pentru context, descrierea menționează că implementarea folosește API-ul de servicii web PrestaShop (autentificare HTTP Basic Auth pe o singură cheie) și un sistem de binding-uri (legături) care conectează entitățile Odoo cu corespondentele lor din PrestaShop (șabloane și variante de produs, categorii și atribute, clienți și adrese, comenzi și linii de comandă, stoc, metode de plată și livrare, țări, limbi, valute), plus un controller (`controller/main.py`) pentru webhook-ul de intrare (apelat de PrestaShop către Odoo) și pentru ruta de facturi, cu procesare de joburi în fundal prin `queue_job`.

**Modele**

- Nu au fost extrase din cod (vezi nota de mai sus).

**Vizualizări**

- Nu au fost extrase din cod (vezi nota de mai sus). Modulul include `views/backend_views.xml` și `views/menu.xml`.

**Acțiuni Automate / Acțiuni Server**

- Nu au fost extrase din cod (vezi nota de mai sus). Descrierea menționează existența unor joburi programate de sincronizare și procesare în fundal; cron-ul comun „Marketplace: Get Orders" (inactiv implicit) importă comenzile pentru backend-urile fără „Disable Import Sale Order" bifat.

#### 5. Conexiuni

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): gestionarea comenzilor de vânzare provenite din marketplace, importate și din PrestaShop.
- [deltatech_marketplace_purchase](../deltatech_marketplace_purchase/index.md): latura de achiziții a ecosistemului de marketplace Deltatech.
