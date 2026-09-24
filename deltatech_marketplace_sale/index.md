# Comenzi de vânzare din Marketplace (localizat la `deltatech_marketplace_sale/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_sale`
- **Versiune:** `19.0.2.13.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_sale
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_sale`
- **Ultima Ingestie:** 2026-09-24
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul reprezintă punctul central pentru gestionarea comenzilor de vânzare provenite din diferiți conectori de marketplace, simplificând procesul de la comandă la încasare (order-to-cash) pentru retailerii care vând pe mai multe canale. Din perspectiva afacerii, elimină introducerea manuală a comenzilor și reduce erorile prin automatizarea importului și procesării vânzărilor din mai multe canale (de exemplu eMAG, Shopify, Magento etc.) direct în Odoo, oferind o imagine unificată asupra vânzărilor și menținând sincronizate statusurile comenzilor și nivelurile de stoc.

#### 2. Funcționalități Cheie

- Vizualizare unificată a vânzărilor: monitorizarea și gestionarea comenzilor de pe toate canalele de marketplace dintr-o singură interfață Odoo.
- Eficiență operațională: procesare mai rapidă a comenzilor și timpi de livrare îmbunătățiți pentru fulfillment-ul de marketplace.
- Consistența datelor: sincronizarea statusurilor comenzilor între Odoo și platformele de marketplace respective.
- Raportare financiară corectă: datele de vânzări integrate permit calculul precis al veniturilor și al indicatorilor de performanță pe marketplace.
- Fiabilitatea stocului: actualizările de inventar în timp real, declanșate de vânzările din marketplace, ajută la prevenirea rupturilor de stoc și a supravânzării.
- **Registrul cererilor de retur** (`marketplace.return.request`): ce vrea cumpărătorul să trimită înapoi, de ce, pe ce comandă și cât de departe a ajuns cererea, într-un vocabular comun al tuturor conectorilor (Solicitat / Aprobat / Primit / Finalizat / Refuzat / Anulat), cu starea brută a marketplace-ului păstrată alături. Retururile se **importă, nu se conduc**: aprobarea sau refuzul rămân în marketplace. Importul periodic se reglează pe backend (*Return Request Days*, *Disable Return Import*); fluxul de depozit îl aduce puntea [deltatech_rma_marketplace](../deltatech_rma_marketplace/index.md).
- **Registrul rambursărilor** (`marketplace.refund`): banii dați înapoi cumpărătorului, cu sumele pe linie, TVA-ul separat unde marketplace-ul îl raportează și legătura opțională către cererea de retur (o rambursare poate exista fără retur, iar un retur se poate deconta în mai multe tranșe). Totalul raportat de marketplace nu e înlocuit; pentru eMAG, care nu raportează total, se adună din linii (*Total Computed*). Nu se creează notă de credit din registru. Îl populează conectorii eMAG (19.0.2.8.0) și Shopify (19.0.1.3.0); de la 19.0.2.12.0, tipul de element `refunds` al backend-ului permite salvarea lor (fără el, prima rambursare salvată de un conector pica).
- **Anularea unei comenzi din marketplace întreabă** dacă anularea se trimite și magazinului (*Cancel & Notify Marketplace*) sau rămâne doar în Odoo (*Cancel in Odoo Only*); alegerea se scrie în istoricul comenzii. Pe backend, *Cancel Sale Order* decide dacă o comandă anulată în marketplace se anulează și în Odoo.
- O modificare a liniilor comenzii — cantitate, preț, linie adăugată sau ștearsă — ajunge la exportul către marketplace și când e făcută direct pe linii (wizard, acțiune server, alt modul), nu doar din formular; conectorul primește semnalul, nu diferența, și recitește comanda. O schimbare de preț e semnalată separat (`price_changed`), pentru marketplace-urile care nu acceptă un preț nou pe o linie existentă. Nimic din ce scrie un import nu se trimite înapoi.
- **Produs pentru vouchere** pe backend, separat de produsul de discount: un voucher al marketplace-ului e o plată a unui terț (TVA 0, decontat pe cont de decontare), nu o reducere comercială; comanda păstrează valoarea voucherului și partea decontată de marketplace.
- Cu **Confirm Sale Order** bifat, jobul de confirmare automată (`try_to_confirm`) se programează pentru **orice** comandă importată, nu doar pentru cele confirmabile chiar la import — o comandă oprită la import (mesaj de la client, ramburs peste plafon) primea altfel jobul deloc și rămânea ofertă trimisă până observa cineva. La rulare, jobul reverifică eligibilitatea (și o reîmprospătează, unde conectorul o suportă) în loc să se bazeze pe starea de la import.
- Integrare cu [deltatech_marketplace_review](../deltatech_marketplace_review/index.md) (punte instalată automat când ambele module sunt prezente): gărzile de confirmare automată — mesajul lăsat de client, rambursul (COD) peste **Max Auto-Confirm COD Amount** — devin motive de verificare vizibile pe comandă, în loc de o oprire tăcută; jobul de confirmare revine la interval scurt cât comanda e oprită doar de motive temporare.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `sale_stock`
- `stock_delivery`

#### 4. Componente Cheie

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_marketplace_get_order` (cron „Marketplace: Get Orders"): rulează metoda `model.cron_import_orders()` pe modelul `marketplace.backend`, implicit la fiecare 1 oră, pentru a importa comenzile din marketplace în Odoo. Este livrat dezactivat (`active=False`) și trebuie activat manual la configurarea integrării.
- `ir_cron_marketplace_get_return_request` (cron „Marketplace: Get Return Requests"): rulează `cron_import_return_requests()`, care apelează `<provider>_import` pe `marketplace.return.request` doar pentru conectorii care importă retururi (eMAG, Shopify). Livrat tot dezactivat.

**Modele**

- `marketplace.return.request` / `.line`: binder de sine stătător (fără `_inherits`), legat de comandă și, prin `picking_ids`, de transferurile de retur; identitatea liniei e unică pe cerere.
- `marketplace.refund` / `.line`: registrul rambursărilor, fără stare proprie (doar `external_state`), cu `compute_amount_total()` pentru conectorii fără total raportat.

#### 5. Conexiuni

- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): extinde gestionarea etapelor (stage) pentru comenzile de vânzare din marketplace.
- [deltatech_marketplace_sale_type](../deltatech_marketplace_sale_type/index.md): adaugă tipuri de comenzi de vânzare specifice fluxurilor de marketplace.
- [deltatech_rma_marketplace](../deltatech_rma_marketplace/index.md): duce retururile importate (`marketplace.return.request`) pe fluxul de depozit al `deltatech_rma` și pune rambursările (`marketplace.refund`) lângă nota de credit.
- [deltatech_marketplace_review](../deltatech_marketplace_review/index.md): punte (instalată automat cu [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)) care transformă gărzile de confirmare automată (mesaj client, ramburs peste plafon) în motive vizibile de verificare pe comandă și reprogramează jobul de confirmare cât timp acestea sunt temporare.
