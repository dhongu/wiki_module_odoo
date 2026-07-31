# Conector Marketplace PrestaShop (localizat la `deltatech_marketplace_prestashop/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_prestashop`
- **Versiune:** `19.0.0.1.6`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_marketplace_prestashop`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_marketplace_prestashop`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Conectorul Deltatech pentru marketplace PrestaShop permite integrarea directă între sistemul ERP Odoo și PrestaShop, una dintre cele mai populare platforme open-source de comerț electronic. Modulul asigură sincronizarea bidirecțională a datelor esențiale de business, astfel încât magazinele online PrestaShop pot fi administrate direct din Odoo. Rezultatul este o soluție unificată pentru gestionarea produselor, a clienților și a comenzilor, eliminând introducerea dublă de date și păstrând o singură sursă de adevăr pentru informațiile comerciale.

#### 2. Funcționalități Cheie

- **Gestionarea completă a produselor:** sincronizarea catalogului de produse între Odoo și PrestaShop, suport pentru variante, atribute și caracteristici, import/export de imagini și conținut multimedia, gestionarea categoriilor de produse și a categoriilor publice, sincronizarea stocului în timp real între platforme.
- **Integrare avansată a clienților:** importul clienților PrestaShop în baza de contacte Odoo, sincronizarea datelor de client, a adreselor și a istoricului de cumpărături, gestionarea grupurilor de clienți și a asocierilor.
- **Gestionarea cuprinzătoare a comenzilor:** importul comenzilor de vânzare din PrestaShop în Odoo, crearea automată a comenzilor de vânzare Odoo, sincronizarea actualizărilor de status între sisteme și urmărirea îndeplinirii și livrării comenzilor.
- **Capabilități internaționale:** suport multilingv prin legături de limbă, gestionarea multi-valută, sincronizarea țărilor și a județelor (regiuni/state), gestionarea livrărilor și a taxelor internaționale.
- **Integrare livrare și plată:** suport pentru curierii de livrare PrestaShop, sincronizarea metodelor de plată și a procesatorilor, integrarea cu depozitele pentru îndeplinirea comenzilor.
- **Îmbunătățirea procesului de vânzare:** suport pentru etapele de vânzare și urmărirea statusului comenzilor, sincronizarea etichetelor de vânzare, atribuirea comenzilor pe echipe cu asociere de depozit.
- **Operațiuni automatizate:** sarcini programate de sincronizare, procesare în fundal cu gestionare prin coadă, optimizări de performanță pentru seturi mari de date și opțiuni de sincronizare incrementală.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `deltatech_marketplace_website`
- `deltatech_marketplace_sale_stage`
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- Dependență externă Python: `dicttoxml`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de componente nu au fost extrase din cod deoarece fișierul `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie. Pentru context, descrierea menționează că implementarea folosește API-ul de servicii web PrestaShop și un sistem de binding-uri (legături) care conectează entitățile Odoo cu corespondentele lor din PrestaShop (șabloane și variante de produs, categorii și atribute, clienți și adrese, comenzi și linii de comandă, stoc, metode de plată și livrare, țări, limbi, valute), plus controllere pentru webhook-uri și procesare de joburi în fundal.

**Modele**

- Nu au fost extrase din cod (vezi nota de mai sus).

**Vizualizări**

- Nu au fost extrase din cod (vezi nota de mai sus).

**Acțiuni Automate / Acțiuni Server**

- Nu au fost extrase din cod (vezi nota de mai sus). Descrierea menționează existența unor joburi programate de sincronizare și procesare în fundal.

#### 5. Conexiuni

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): gestionarea comenzilor de vânzare provenite din marketplace, importate și din PrestaShop.
- [deltatech_marketplace_purchase](../deltatech_marketplace_purchase/index.md): latura de achiziții a ecosistemului de marketplace Deltatech.
