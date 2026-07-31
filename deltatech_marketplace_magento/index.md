# Conector Marketplace Magento (localizat la `deltatech_marketplace_magento/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_magento`
- **Versiune:** `19.0.0.0.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_marketplace_magento
- **Cale Locală:** `odoo-addons/bitshop/deltatech_marketplace_magento`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Conectorul Magento Marketplace este o extensie Odoo dezvoltată de Terrabit care realizează o integrare fluidă între sistemul ERP Odoo și Magento, o platformă de e-commerce de nivel enterprise. Conectorul permite afacerilor să sincronizeze și să gestioneze magazinele online Magento direct din Odoo, oferind o soluție unificată pentru gestionarea produselor, datelor clienților, comenzilor și a stocurilor pe ambele platforme. Astfel, Magento devine canalul de vânzare online, iar Odoo rămâne sursa unică de adevăr pentru operațiunile de back-office.

#### 2. Funcționalități Cheie

- **Sincronizare completă a produselor**:
  - Import de produse configurabile (cu variante) din Magento în Odoo
  - Gestionarea șabloanelor de produs și a variantelor cu atributele lor
  - Sincronizarea categoriilor de produs și a categoriilor publice
  - Suport pentru seturi de atribute și atribute de produs
  - Procesare în loturi a importului de produse, cu paginare
- **Gestionarea stocurilor**:
  - Sincronizare în timp real a nivelurilor de stoc între Odoo și Magento
  - Prevenirea supravânzării prin actualizări corecte ale stocului
  - Gestionarea stocurilor pe mai multe depozite
- **Integrarea clienților**:
  - Import al clienților Magento în baza de contacte Odoo
  - Menținerea unor înregistrări de client consecvente între platforme
  - Sincronizarea datelor de client și a istoricului de achiziții
- **Gestionarea comenzilor**:
  - Import al comenzilor de vânzare din Magento în Odoo
  - Crearea automată de comenzi de vânzare Odoo pentru achizițiile din Magento
  - Sincronizarea actualizărilor de stare a comenzilor între sisteme
  - Suport pentru echipe de vânzări cu asociere de depozit
  - Sincronizarea etapelor de vânzare (stările comenzilor)
  - Suport pentru webhook-uri Magento pentru procesarea comenzilor aproape în timp real
- **Procesare livrare și plată**:
  - Integrare cu metodele de livrare Magento
  - Suport pentru mai mulți procesatori de plată
  - Sincronizarea informațiilor de livrare și de plată
- **Operațiuni automatizate**:
  - Procesare în fundal a sarcinilor cu gestionare a cozii de job-uri
  - Paginare și dimensiuni de lot configurabile pentru optimizarea performanței
  - Sarcini de sincronizare programate

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `deltatech_marketplace_website`
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- `deltatech_marketplace_sale_stage`

#### 4. Componente Cheie

Documentația principală pentru acest modul provine din `readme/DESCRIPTION.md`, conform fluxului de ingestie; prin urmare analiza detaliată a codului pentru această secțiune este omisă. Implementarea tehnică descrisă în Readme se bazează pe API-ul REST Magento și pe un sistem de binding sofisticat:

**Modele**

- **Backend Adapter**: gestionează autentificarea pe API-ul REST (bazată pe token) și comunicarea cu Magento.
- **Modele de binding**: leagă entitățile Odoo de corespondentele lor din Magento — binding pentru șablon și variantă de produs, pentru atribut de produs și set de atribute, pentru categorii, pentru clienți, pentru comenzi de vânzare și pentru etape de vânzare.

Implementarea urmează modele de procesare asincronă cu cozi de job-uri pentru a gestiona eficient volume mari de date, cu paginare, procesare în fundal prin `with_delay()` și dimensiuni de lot configurabile prin setarea `items_per_page`.

#### 5. Conexiuni

- [deltatech_marketplace_purchase](../deltatech_marketplace_purchase/index.md): extensie de aprovizionare a aceleiași suite marketplace; nu este dependență, dar completează fluxul de comenzi de cumpărare.
- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): conector frate pentru un alt marketplace (eMAG), bazat pe aceeași infrastructură marketplace.
- [deltatech_marketplace_extended](../deltatech_marketplace_extended/index.md): extinderi suplimentare ale funcționalității de bază marketplace.
