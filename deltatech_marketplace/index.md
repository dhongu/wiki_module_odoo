# Marketplace Base Connector (localizat la `deltatech_marketplace/index.md`)

- **Nume Tehnic:** `deltatech_marketplace`
- **Versiune:** `19.0.1.14.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Marketplace Base Connector este modulul de bază al familiei de module marketplace din Odoo, conceput pentru a facilita integrarea între Odoo și diverse platforme de marketplace online. Oferă un cadru complet pentru gestionarea operațiunilor de e-commerce pe mai multe canale de vânzare, permițând companiilor să sincronizeze și să administreze listările de produse, comenzile și stocurile pe diferite marketplace-uri dintr-o singură interfață Odoo. Modulul reprezintă fundația unui ecosistem complet de management al marketplace-urilor, oferind control centralizat asupra prezenței online extinse pe mai multe platforme.

#### 2. Funcționalități Cheie

- Integrare cu platforme de marketplace pentru vânzare multi-canal simplificată
- Gestionare centralizată a listărilor de produse pe mai multe marketplace-uri
- Sincronizarea stocurilor între Odoo și platformele de marketplace
- Procesarea automată a comenzilor provenite din vânzările pe marketplace
- Suport pentru atribute și configurări specifice fiecărui marketplace
- Integrare cu managementul brandurilor pentru o prezentare consecventă pe marketplace
- Configurarea metodelor de livrare specifice cerințelor de marketplace
- Jurnalizare centralizată a tuturor operațiunilor de marketplace (actualizări de stoc, actualizări de preț etc.)
- Acces rapid la jurnale direct din produsele și șabloanele de produs de pe marketplace

#### 3. Dependențe

- `sale`
- `product`
- `account`
- `stock`
- `queue_job`
- `base_address_extended`

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune este sintetizată din `readme/DESCRIPTION.md`. Modulul este construit cu o arhitectură modulară, structurată în:

- Configurări de date (`data`)
- Modele pentru logica de business de bază și pentru jurnalele centralizate de marketplace (`models`)
- Vizualizări pentru interfața cu utilizatorul (`views`)
- Controllere pentru interacțiunile web (`controller`)
- Wizard-uri pentru procese ghidate (`wizard`)
- Definiții de securitate (`security`)
- Servicii JavaScript pentru funcționalitatea de frontend (`static`)
- Suport pentru internaționalizare (`i18n`)

#### 5. Conexiuni

Modulul servește ca fundație pentru un ecosistem complet de management al marketplace-urilor, fiind extins de următoarele module conexe:

- `deltatech_marketplace_attribute`: gestionarea atributelor de produs specifice marketplace-ului.
- [deltatech_marketplace_brand](../deltatech_marketplace_brand/index.md): managementul brandurilor pe marketplace-uri.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): metode de livrare specifice marketplace-ului.
- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): extensie specifică platformei eMAG.
- [deltatech_marketplace_magento](../deltatech_marketplace_magento/index.md): extensie specifică platformei Magento.
- [deltatech_marketplace_merchantpro](../deltatech_marketplace_merchantpro/index.md): extensie specifică platformei MerchantPro.
- [deltatech_marketplace_doraly](../deltatech_marketplace_doraly/index.md): extensie specifică platformei Doraly.
- `deltatech_marketplace_gremini`: extensie specifică platformei Gremini.
