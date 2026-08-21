# NAP (localizat la `deltatech_nap/index.md`)

- **Nume Tehnic:** `deltatech_nap`
- **Versiune:** `19.0.1.8.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_nap`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_nap`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

NAP (Necesar de Aprovizionare / Purchase requirements) este o unealtă simplă și rapidă pentru determinarea necesarului de achiziție în Odoo, dezvoltată de Terrabit. Utilizatorul deschide un raport, obține o listă justificată de „ce trebuie comandat” și lansează direct reaprovizionarea, fără obiecte de planificare permanente și fără un flux de lucru greoi. Nucleul modulului este Raportul de Prognoză Stoc (Stock Forecast Report): pentru o perioadă, un depozit/locație și, opțional, un furnizor sau un produs selectat, se calculează cererea medie zilnică din istoric și se determină, pentru fiecare produs, cantitatea de comandat pentru orizontul de prognoză, ținând cont de stocul disponibil, de intrări, ieșiri și de cantitățile aflate deja în circuitul de aprovizionare.

#### 2. Funcționalități Cheie

- **Raport „ce trebuie comandat”**: cerere medie zilnică × (zile de prognoză + timp de livrare), ajustată cu stocul disponibil, intrările, ieșirile și cantitățile în curs de aprovizionare; fiecare linie are o explicație pas cu pas a calculului.
- **Surse multiple de cerere**: mișcări de stoc finalizate (ieșiri către clienți și retururi), un istoric de livrări importat, înregistrări manuale de cerere de stoc și cerere prognozată.
- **Cantități comandabile**: cantitatea propusă respectă cantitatea minimă de comandă a furnizorului (`product.supplierinfo.min_qty`) și este rotunjită la multiplul de ambalare, astfel încât poate fi trimisă furnizorului ca atare.
- **Reaprovizionare consolidată**: lansarea reaprovizionării grupează liniile aceluiași furnizor într-o singură comandă de achiziție, în loc de o comandă per produs.
- **Stoc de siguranță statistic (opțional)**: în loc de un procent fix de stoc de siguranță, un mod opțional adaugă `Z × σ_zilnic × √(timp de livrare)`, unde σ este deviația standard a cererii săptămânale (inclusiv săptămânile fără cerere), iar Z provine din nivelul de serviciu ales (90 / 95 / 97,5 / 99%).
- **Clasificare XYZ**: produsele sunt clasificate după predictibilitatea cererii, folosind coeficientul de variație — X (stabil), Y (variabil), Z (eratic). Produsele erratice (clasa Z) sunt excluse din calculul automat al stocului de siguranță și marcate pentru verificare manuală, astfel încât nu se propune o cifră fals-precisă pe o cerere imprevizibilă.
- **Majorări de vânzări și siguranță**: creșteri procentuale opționale, plus filtrarea vânzărilor excepționale (ignorarea mișcărilor mari, punctuale, peste un prag).
- **Produse de înlocuire**: cererea unui produs scos din uz este preluată de produsul său de înlocuire.
- **Gestionarea sfârșitului de ciclu de viață (EOL)**: un indicator `EOL` și o acțiune programată care arhivează produsele EOL odată ce stocul acestora ajunge la zero.
- **Relevanță pentru planificare**: un indicator `planning_relevant` (specific variantei de produs) pentru a exclude din raport produsele care nu sunt planificate.
- **Raport de stoc cu mișcare lentă (slow move)**: identifică produsele cu stoc pozitiv și fără ieșiri semnificative într-o perioadă, cu filtrare inteligentă care exclude produsele recent recepționate sau nou create.

#### 3. Dependențe

- `purchase`
- `product`
- `stock`
- `purchase_stock`
- `sale`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, modulul extinde mai multe modele de bază Odoo:

**Modele**

- `product.template` / `product.product`: extindere cu câmpurile `planning_relevant`, `replacement_product_id` și `eol`; începând cu versiunea 18.0.1.4.1 (istoric), `planning_relevant` și `replacement_product_id` sunt specifice variantei de produs.
- `stock.demand`: model dedicat pentru înregistrarea manuală și analiza cererii de produse.
- `stock.delivery.history`: istoricul livrărilor, folosit ca sursă suplimentară de cerere pentru prognoză.
- `stock.forecast.report` (wizard): raportul principal „ce trebuie comandat”, cu agregare grea în SQL pentru performanță și citirea în batch a cifrelor de stoc.
- `stock.slow.move` (wizard): raportul de stoc cu mișcare lentă.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_archive_product_eol_at_zero_stock`: rulează zilnic și arhivează produsele marcate EOL odată ce stocul lor ajunge la zero (`cron_archive_product_eol_at_zero_stock`).

#### 5. Conexiuni

- [deltatech_nap_website](../deltatech_nap_website/index.md): modul soră care adaugă integrarea pe website a categoriei publice NAP; completează acest modul de planificare a necesarului.
