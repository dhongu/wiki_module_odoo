# Conector Trendyol Marketplace (localizat la `deltatech_marketplace_trendyol/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_trendyol`
- **Versiune:** `19.0.1.1.8`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_trendyol`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_trendyol`
- **Ultima Ingestie:** `2026-08-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un cont de seller Trendyol lângă Odoo, fără conector, înseamnă catalog, stoc, preț și comenzi ținute manual în două locuri: fiecare actualizare de stoc sau preț trebuie repetată pe panoul de seller, fiecare comandă nouă trebuie reintrodusă, iar numerele de tracking trebuie urmărite manual astfel încât cumpărătorul să vadă statusul livrării chiar pe pagina Trendyol. Pe un marketplace de această dimensiune, o actualizare de preț ratată sau un import întârziat costă vânzări, nu doar timp. Conectorul Trendyol Marketplace închide acest gol: produsele, comenzile, stocul, prețul și facturile circulă automat între Odoo și Trendyol prin API-ul propriu V2 al Trendyol și endpoint-urile lui asincrone de tip batch — mecanismul pe care Trendyol îl cere de la un seller cu volum real, nu apeluri produs cu produs — iar pentru că se leagă de același framework comun `deltatech_marketplace` folosit și de conectorii Shopify, eMAG sau alții din suită, adăugarea Trendyol lângă un canal deja folosit nu înseamnă învățarea unui al doilea sistem.

#### 2. Funcționalități Cheie

- Import produse (oferte) existente din Trendyol, potrivite automat după cod de bare (barcode), cu status de aprobare, preț de vânzare/listă și cantitate de stoc
- Export asincron de preț și stoc prin API-ul batch `price-and-inventory`, cu verificare automată a rezultatului până când Trendyol raportează batch-ul finalizat, iar articolele respinse sunt înregistrate cu motivul exact dat de Trendyol
- Creare și actualizare de produse pe Trendyol (Product V2 API), cu categorie, atribute, cod de bare și imagine mapate din fișa produsului Odoo
- Import comenzi (pachete de expediție) cu client, adrese de livrare/facturare și linii de comandă complete, gata de pregătit și facturat ca orice altă vânzare
- Notificări de comenzi în timp real printr-un webhook Trendyol, pe lângă importul programat
- Trimiterea numărului de tracking AWB către Trendyol la validarea expedierii — **condiționată**: se declanșează doar dacă transferul are deja atribuit manual un transportator Odoo real cu integrare „rate and ship" (nu transportatorul generic „Free delivery" pe care cade implicit orice comandă Trendyol importată) și dacă tracking-ul nu a fost deja completat manual înainte de validare
- Actualizarea explicită a stării pachetului pe Trendyol (de exemplu Picking/Invoiced) — disponibilă doar ca apel de server/dezvoltator, fără declanșator automat din nicio tranziție Odoo
- Trimiterea automată a link-ului facturii către Trendyol după postarea facturii Odoo (dacă opțiunea e activă pe backend)
- Import al arborelui complet de categorii Trendyol dintr-un singur apel; atributele obligatorii și valorile permise ale unei categorii de nivel frunză se importă separat, abia la prima referire (de exemplu la importul unui produs care o folosește), nu automat odată cu arborele

#### 3. Dependențe

- `sale`
- `delivery`
- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea Sumar/Funcționalități a fost preluată din `readme/DESCRIPTION.md`; componentele de mai jos rezultă din configurarea backend-ului (`readme/CONFIGURE.md`), din fișa de consultant (`readme/FISA_CONSULTANT.md`) și din job-urile programate (`data/ir_cron_data.xml`):

- **Backend Trendyol**: se configurează pe `marketplace.backend` selectând provider-ul Trendyol, cu Seller ID, Username (API Key), Password (API Secret) și Storefront Code; locația API se setează automat (`https://apigw.trendyol.com`, respectiv gateway-ul de staging `https://stageapigw.trendyol.com` dacă mediul de producție e dezactivat — IP-urile serverului trebuie whitelistate de Trendyol pentru staging).
- **Legătura curier neautomată**: la import, conectorul creează întotdeauna o legătură `marketplace.delivery.carrier`, dar payload-ul Trendyol nu trimite un nume pe care căutarea automată (`save_from_marketplace`) să-l poată folosi — orice comandă importată cade pe transportatorul generic „Free delivery"; asocierea la un transportator Odoo real (Cargus, Sameday etc.) se face manual pe comandă.
- **`trendyol_write` pe comandă**: stub neimplementat (doar scrie un avertisment în jurnal) — nu există niciun push generic al modificărilor comenzii înapoi spre Trendyol, nici chiar cu „Active on write" bifat pe tipul de articol `orders`.
- **Marcă produs (`brandId`)**: fără câmp de mapare în interfață; valoarea se citește doar dintr-o cheie de context (`trendyol_brand_id`) pe care nimic din UI standard nu o setează.
- `ir_cron_trendyol_import_orders`: sarcină programată „Trendyol: Import Orders", la fiecare 30 de minute, dezactivată implicit (se activează manual după validarea configurării).
- `ir_cron_trendyol_export_stock`: sarcină programată „Trendyol: Export Stock", la fiecare oră, dezactivată implicit.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază marketplace peste care este construit conectorul.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): integrarea comenzilor de vânzare importate din Trendyol.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): infrastructura de mapare a curierilor; legătura creată la import nu se mapează automat la un transportator Odoo real.
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): metoda de plată „Trendyol", creată automat la prima comandă importată.
