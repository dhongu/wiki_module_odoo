# Conector Shopify Marketplace (localizat la `deltatech_marketplace_shopify/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_shopify`
- **Versiune:** `19.0.0.0.4`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_marketplace_shopify
- **Cale Locală:** `odoo-addons/bitshop/deltatech_marketplace_shopify`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Conectorul Shopify Marketplace dezvoltat de Terrabit creează o integrare directă și fluidă între sistemul ERP Odoo și platforma de magazine online Shopify. Modulul permite companiilor să sincronizeze și să gestioneze magazinele lor Shopify direct din Odoo, oferind o soluție unificată pentru administrarea produselor, clienților și comenzilor. Astfel, echipele pot opera magazinul online fără a comuta între platforme, păstrând o singură sursă de adevăr pentru informațiile despre produse și clienți, reducând introducerea manuală a datelor și eliminând discrepanțele.

#### 2. Funcționalități Cheie

- **Sincronizare produse**:
  - Export de șabloane de produs din Odoo către Shopify.
  - Import de șabloane de produs, variante și imagini din Shopify.
  - Sincronizarea prețurilor și a informațiilor de bază (cod de bare, greutate, SKU).
  - Suport pentru imagini multiple per șablon de produs și asocierea imaginilor cu variante specifice.

- **Integrare clienți**:
  - Import al clienților Shopify în baza de contacte Odoo.
  - Menținerea unor înregistrări de client consistente între platforme.
  - Detectarea automată a companiilor pe baza atributelor din nota Shopify sau a câmpului de companie.

- **Gestionarea comenzilor**:
  - Import al comenzilor de vânzare din Shopify în Odoo (creare automată a comenzilor Odoo).
  - Sincronizarea statusului comenzii din Odoo către Shopify prin etichete (faze de vânzare / Sale Phases).
  - Sincronizarea anulării comenzilor între Odoo și Shopify.
  - Suport pentru webhook-uri Shopify (`orders/updated`) pentru actualizarea automată a comenzilor în Odoo.
  - Urmărirea livrării și a onorării (trimiterea numerelor și URL-urilor de tracking către Shopify).

- **Plăți și livrare**:
  - Integrare cu metodele de plată Shopify și crearea plăților în Odoo.
  - Maparea automată a curierilor și crearea liniilor de livrare pe comenzi.
  - Suport pentru puncte de ridicare (lockere) preluate din notele Shopify.

- **Operații automate**:
  - Joburi de sincronizare programate prin `queue_job`.
  - Actualizări în timp real pentru comenzi prin webhook-uri.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- `deltatech_marketplace_website`

Dependență externă Python: `ShopifyAPI`.

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, modulul folosește biblioteca Python `ShopifyAPI` pentru comunicarea cu API-ul REST Shopify și implementează un sistem de „binding" bazat pe cadrul marketplace Deltatech:

**Modele**

- **Backend Adapter**: gestionează comunicarea cu API-ul și autentificarea cu Shopify.
- **Modele de binding** care leagă entitățile Odoo de corespondentele lor din Shopify:
  - Binding de șablon de produs și variantă de produs.
  - Binding de client și adresă.
  - Binding de comandă de vânzare și linie de comandă.
  - Binding de curier de livrare și de furnizor de plată (payment acquirer).
  - Binding de fază de vânzare (etichete / tags).

**Acțiuni Automate / Acțiuni Server**

- Sincronizare programată prin `queue_job` (funcții de job definite în `data/job_function.xml`).
- Actualizări în timp real ale comenzilor prin webhook-ul Shopify `orders/updated`.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază marketplace pe care se construiește conectorul.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): importul și sincronizarea comenzilor de vânzare.
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): integrarea metodelor de plată și crearea plăților.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): maparea curierilor și liniile de livrare.
