# Conector Marketplace Odoo către Odoo (localizat la `deltatech_marketplace_odoo/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_odoo`
- **Versiune:** `19.0.0.1.2`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_marketplace_odoo
- **Cale Locală:** `odoo-addons/bitshop/deltatech_marketplace_odoo`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul oferă o interfață de conectare Odoo-către-Odoo prin intermediul platformei marketplace. Rolul său principal este să permită sincronizarea datelor de bază între o instanță Odoo sursă și o instanță Odoo destinație, importând automat catalogul de produse (șabloane, variante, atribute și categorii) împreună cu partenerii. Astfel, o companie care folosește deja Odoo poate prelua și menține la zi informațiile comerciale dintr-un alt sistem Odoo conectat prin marketplace, fără introducere manuală a datelor.

#### 2. Funcționalități Cheie

- Import șabloane de produs (product template).
- Import variante de produs.
- Import atribute cu valorile aferente.
- Import categorii de produse.
- Import parteneri.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `deltatech_marketplace_website`
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_purchase](../deltatech_marketplace_purchase/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)

#### 4. Componente Cheie

Documentația pentru acest modul se bazează pe fișierul `readme/DESCRIPTION.md`, conform fluxului de ingestie. Deoarece readme-ul acoperă scopul și funcționalitățile modulului, analiza detaliată a codului pentru componente (modele, vizualizări, acțiuni automate) a fost omisă. Modulul aduce vizualizări de backend (`views/backend_views.xml`) pentru configurarea conectorului.

#### 5. Conexiuni

- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): modul din aceeași suită marketplace, care extinde conectorul cu gestionarea metodelor de livrare.
