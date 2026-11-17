# Marketplace Order Stages (localizat la `deltatech_marketplace_sale_stage/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_sale_stage`
- **Versiune:** `19.0.1.1.12`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_sale_stage
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_sale_stage`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul leagă statusurile comenzilor din marketplace-uri de fazele comenzilor de vânzare definite în Sale Stage, astfel încât comenzile importate din magazinele online să urmeze același flux de faze ca restul comenzilor din Odoo. Echipele văd imediat în ce fază se află fiecare comandă de marketplace, iar schimbările de fază sunt păstrate în istoricul comenzii. Modulul doar stochează maparea dintre statusurile magazinului și fazele Odoo; nu calculează durate pe etape și nu oferă un raport separat.

#### 2. Funcționalități Cheie

- Maparea statusurilor: pentru fiecare backend de marketplace, fiecare status al comenzii din magazin este asociat cu o fază de vânzare Odoo (**Sales → Configuration → Sale Order phase**, din `deltatech_sale_stage`).
- Faza la import: conectorii care folosesc maparea (Doraly, Extended, Magento, OpenCart, PrestaShop, Shopify, WooCommerce) setează faza mapată pe comenzile importate.
- Opțiunea **Skip Order**: marchează statusurile ale căror comenzi nu trebuie importate; este aplicată doar de conectorii care citesc indicatorul (de exemplu OpenCart).
- Istoric: schimbările de fază sunt urmărite în chatter-ul comenzii, iar lista comenzilor de vânzare poate fi grupată după fază.
- Unde se lucrează: în **Marketplace → Backends**, fila **Objects**, cardul **Sale Stage** arată numărul de statusuri mapate; din card se deschide lista **Marketplace Sale Phase** (Binder Name, Odoo Sale Phase, External ID). Pe conectorii care pot citi lista de statusuri (Marketplace Extended, PrestaShop, Magento) cardul are acțiunea **Import**; la ceilalți, un status nou se adaugă la importul primei comenzi care îl are.
- Potrivire automată: o fază Odoo cu exact același nume ca statusul din magazin (în limba utilizatorului care rulează importul) este legată automat; altfel se creează o fază nouă. La reimport, numele din magazin se scrie înapoi pe faza Odoo legată.
- Rândurile din listă apar cu roșu când aceeași fază Odoo este folosită de mai multe statusuri ale aceluiași backend; conectorii care trimit statusul înapoi în magazin folosesc atunci cea mai recentă mapare.
- Faza este setată de conector la import; Sale Stage o poate schimba și din Odoo (confirmare, livrare validată, status curier, facturare completă), iar conectorii care trimit statusul înapoi actualizează și magazinul. Indicatorii fazei se aplică la scriere: o fază marcată **Confirmed** confirmă o comandă ciornă, una marcată **Cancelled** o anulează.
- Gestionarea mapărilor cere grupul Marketplace manager și dreptul **Sales / Administrator**, fiindcă fiecare mapare scrie pe faza Odoo; câmpul **Name** din mapare este numele fazei Odoo, deci redenumirea afectează toate backend-urile.
- Pașii detaliați, cu capturi de ecran, sunt în [Fișa Consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_sale_stage](../deltatech_sale_stage/index.md)

#### 4. Componente Cheie

Modulul include un fișier `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune este omisă deoarece Readme-ul nu o solicită explicit.

#### 5. Conexiuni

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): modulul de bază pentru comenzile de vânzare din marketplace, peste care acest addon adaugă maparea statusurilor pe faze.
- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul general de integrare marketplace din care face parte ecosistemul.
- [deltatech_marketplace_sale_type](../deltatech_marketplace_sale_type/index.md): modul soră, care adaugă tipuri pentru comenzile de marketplace.
