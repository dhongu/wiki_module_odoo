# EMAG Marketplace Connector (localizat la `deltatech_marketplace_emag/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_emag`
- **Versiune:** `19.0.2.3.20`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_emag`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_emag`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Conectorul eMAG Marketplace este o extensie Odoo specializată, dezvoltată de Terrabit, care asigură integrarea fluidă între platforma de gestiune Odoo și eMAG Marketplace, una dintre cele mai mari platforme de comerț electronic din România și Europa de Est. Conectorul permite gestionarea prezenței pe eMAG Marketplace direct din Odoo, sincronizând produse, stocuri, comenzi și informații de livrare între cele două sisteme. Este deosebit de util pentru companiile din România și Europa de Est care doresc să își extindă reach-ul prin eMAG, păstrând în același timp operațiuni centralizate și eficiente în Odoo, fără dublă introducere de date.

#### 2. Funcționalități Cheie

- **Sincronizare bidirecțională**: sincronizare automată a produselor, nivelurilor de stoc, comenzilor și informațiilor de livrare între Odoo și eMAG Marketplace.
- **Gestiune produse**:
  - Export detalii produs, specificații și imagini către eMAG
  - Gestionarea variantelor de produs și a categoriilor
  - Configurarea atributelor de produs specifice eMAG
  - Crearea automată a ofertelor de produs pe eMAG
- **Gestiune comenzi**:
  - Import comenzi din eMAG în Odoo
  - Creare automată a comenzilor de vânzare în Odoo
  - Actualizarea statusului comenzilor înapoi către eMAG
- **Integrare stocuri**:
  - Sincronizarea nivelurilor de stoc în timp real
  - Actualizări automate de stoc pentru a preveni supravânzarea
- **Integrare livrare**:
  - Suport pentru metodele de livrare eMAG
  - Sincronizarea informațiilor de expediere
  - Integrare cu transportatorii
- **Procesare plăți**:
  - Suport pentru metodele de plată eMAG
  - Reconciliere automată a plăților
- **Operațiuni programate**:
  - Sincronizare automată în fundal prin job-uri cron
  - Intervale de sincronizare configurabile

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

- **Backend Adapter**: gestionează comunicarea API cu eMAG.
- **Modele de binding (binding)**: leagă entitățile Odoo de omoloagele lor din eMAG — binding de produs, comandă, categorie, transportator de livrare și metodă de plată.
- **Servicii de sincronizare**: gestionează fluxul de date între sisteme.
- **Job-uri programate**: automatizează sincronizarea în fundal — `ir_cron_emag_set_price` (definit în `data/ir_cron_data.xml`) rulează la fiecare 4 ore actualizarea automată a prețurilor pe backend-ul de marketplace (dezactivat implicit).

Pentru detalii suplimentare de configurare și operare, modulul include un manual de utilizare („Manual utilizare eMAG Marketplace.docx") și un ghid `readme/CONFIGURE.md`.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază marketplace peste care este construit conectorul.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): integrarea comenzilor de vânzare cu eMAG.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): integrarea metodelor și informațiilor de livrare eMAG.
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): integrarea metodelor de plată și reconcilierea plăților eMAG.
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md): integrarea cu prezența de website/e-commerce a marketplace-ului.
- [deltatech_delivery](../deltatech_delivery/index.md): gestiunea metodelor de livrare folosite de conector.
