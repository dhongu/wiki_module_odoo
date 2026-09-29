# Conector Marketplace Odoo către Odoo (localizat la `deltatech_marketplace_odoo/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_odoo`
- **Versiune:** `19.0.0.2.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_odoo
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_odoo`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul oferă o interfață de conectare Odoo-către-Odoo prin intermediul platformei marketplace. Rolul său principal este să permită sincronizarea datelor de bază între o instanță Odoo sursă și o instanță Odoo destinație, importând automat catalogul de produse (șabloane, variante, atribute și categorii) împreună cu partenerii. Astfel, o companie care folosește deja Odoo poate prelua și menține la zi informațiile comerciale dintr-un alt sistem Odoo conectat prin marketplace, fără introducere manuală a datelor.

#### 2. Funcționalități Cheie

- Import șabloane de produs (product template).
- Import variante de produs.
- Import atribute cu valorile aferente.
- Import categorii de produse.
- Import parteneri.
- Mapare produse (**Map Products**, din 19.0.0.2.0): produsele Odoo locale sunt căutate în baza de date la distanță după referință internă și cod de bare (potrivire exactă, câte 100 per `search_read`), pe aceeași selecție ca importul (variante active și, pe un backend B2B, doar cele publicate). Legătura primește id-ul și referința internă ale variantei la distanță, iar șablonul la distanță este legat de șablonul Odoo local dacă nu era deja legat. Nu se importă nimic: produsul local își păstrează denumirea, prețul și codurile.
- Import listă de prețuri, țări/județe și imagini de produs; export comenzi (comandă de achiziție locală confirmată devine comandă de vânzare în instanța la distanță, în flux B2B) și sincronizarea mesajelor și a stării comenzii, conform fișei consultant.
- Robustețe: erorile tranzitorii XML-RPC (rețea, `ProtocolError`) declanșează reîncercarea automată a jobului; exportul comenzilor de achiziție se face câte un job per comandă, pe canalul de ieșire.
- Ajustarea de inventar creată la import vizează prima locație configurată pe backend (`location_stock_ids[:1]`); cu mai multe locații configurate se ajustează doar prima.
- Datele de conectare ale backend-ului sunt citite cu `sudo()`, deoarece în `deltatech_marketplace` sunt vizibile doar pentru Marketplace Manager; utilizatorii fără grup pot rula în continuare fluxurile care apelează marketplace-ul.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_purchase](../deltatech_marketplace_purchase/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)

#### 4. Componente Cheie

Documentația pentru acest modul se bazează pe fișierul `readme/DESCRIPTION.md`, conform fluxului de ingestie. Deoarece readme-ul acoperă scopul și funcționalitățile modulului, analiza detaliată a codului pentru componente (modele, vizualizări, acțiuni automate) a fost omisă. Modulul extinde `marketplace.backend` cu provider-ul `odoo` (câmpuri de conexiune precum `odoo_database`, `odoo_version`, `odoo_integration_b2b`, `odoo_supplier_id`, `odoo_customer_id`) și aduce vizualizări de backend (`views/backend_views.xml`) pentru configurarea conectorului.

#### 5. Conexiuni

- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): modul din aceeași suită marketplace, care extinde conectorul cu gestionarea metodelor de livrare.
</content>
