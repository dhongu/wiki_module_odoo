# Conector Trendyol Marketplace (localizat la `deltatech_marketplace_trendyol/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_trendyol`
- **Versiune:** `19.0.1.1.2`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_trendyol`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_trendyol`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Conectorul Trendyol Marketplace este o extensie Odoo dezvoltată de Terrabit, construită peste cadrul Deltatech Marketplace, care asigură integrarea între Odoo și Trendyol, una dintre cele mai mari platforme de comerț electronic din Turcia și regiune. Modulul permite gestionarea produselor, prețurilor, stocurilor și comenzilor de pe Trendyol direct din Odoo, eliminând introducerea manuală și dublă a datelor și oferind control centralizat asupra vânzărilor de pe acest canal de marketplace.

#### 2. Funcționalități Cheie

- Import produse (oferte) din Trendyol după cod de bare
- Export preț și stoc prin API-ul asincron `price-and-inventory`, cu verificare automată a rezultatelor batch-ului
- Creare/actualizare produse pe Trendyol (Product API v2)
- Import colete de expediere (comenzi), cu client, adrese și linii de comandă
- Trimiterea numărului de tracking AWB și actualizarea statusului coletului către Trendyol
- Trimiterea link-ului facturii clientului după postarea facturii
- Import arbore categorii Trendyol, cu atributele și valorile aferente fiecărei categorii

#### 3. Dependențe

- `sale`
- `delivery`
- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea Sumar/Funcționalități a fost preluată din `readme/DESCRIPTION.md`; componentele de mai jos rezultă din configurarea backend-ului (`readme/CONFIGURE.md`) și din job-urile programate (`data/ir_cron_data.xml`):

- **Backend Trendyol**: se configurează pe `marketplace.backend` selectând provider-ul Trendyol, cu Seller ID, Username (API Key), Password (API Secret) și Storefront Code; locația API se setează automat (`https://apigw.trendyol.com`, respectiv gateway-ul de staging `https://stageapigw.trendyol.com` dacă mediul de producție e dezactivat — IP-urile serverului trebuie whitelistate de Trendyol pentru staging).
- `ir_cron_trendyol_import_orders`: sarcină programată „Trendyol: Import Orders", la fiecare 30 de minute, dezactivată implicit (se activează manual după validarea configurării).
- `ir_cron_trendyol_export_stock`: sarcină programată „Trendyol: Export Stock", la fiecare oră, dezactivată implicit.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază marketplace peste care este construit conectorul.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): integrarea comenzilor de vânzare importate din Trendyol.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): integrarea metodelor de livrare și transmiterea numărului AWB către Trendyol.
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): integrarea metodelor de plată specifice marketplace-ului.
