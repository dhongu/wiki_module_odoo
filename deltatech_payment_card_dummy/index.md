# Payment Card Dummy (localizat la `deltatech_payment_card_dummy/index.md`)

- **Nume Tehnic:** `deltatech_payment_card_dummy`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_payment_card_dummy
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_card_dummy`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul Payment Card Dummy oferă un furnizor de plată cu cardul simulat (fictiv) pentru Odoo. Este destinat în principal testării fluxurilor de plată sau scenariilor în care plățile cu cardul sunt procesate printr-un terminal extern și trebuie înregistrate rapid în Odoo, fără o integrare bancară directă. Tranzacțiile sunt marcate instant ca finalizate, ceea ce permite verificarea rapidă a tranzițiilor de stare a comenzilor și facturilor, precum și a acțiunilor declanșate după plată (livrări automate, notificări pe e-mail), fără bani reali și fără configurări complexe de sandbox.

#### 2. Funcționalități Cheie

- Simulează plăți cu cardul în timpul procesului de checkout din eCommerce.
- Înregistrează plăți cu cardul pentru facturile din portal, fără a necesita date reale de card.
- Permite testarea fluxului complet comandă-spre-plată într-un mediu de dezvoltare sau staging.
- Poate fi folosit ca substitut (placeholder) pentru tranzacții manuale cu cardul gestionate prin terminale POS fizice.
- Flux de plată simulat care imită experiența unui furnizor de plată real.
- Suport pentru capturarea manuală (manual capture) a tranzacțiilor autorizate.
- Configurare minimă: nu necesită chei API sau credențiale externe — funcționează imediat.
- Integrare completă cu modulele standard Odoo `payment` și `website_sale`.

#### 3. Dependențe

- `payment`
- `sale`
- `payment_custom`

#### 4. Componente Cheie

Sumarul și funcționalitățile au fost preluate din `readme/DESCRIPTION.md`, care nu solicită detalierea componentelor tehnice. Conform fluxului de ingestie, analiza codului pentru această secțiune este omisă.

#### 5. Conexiuni

- [deltatech_payment](../deltatech_payment/index.md): modul înrudit din aceeași suită, dedicat fluxurilor de plată; ambele extind cadrul de plăți Odoo.
