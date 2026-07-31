# Deltatech Sale Contracts (localizat la `deltatech_sale_contracts/index.md`)

- **Nume Tehnic:** `deltatech_sale_contracts`
- **Versiune:** `19.0.1.0.2`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_contracts`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_contracts`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul extinde comenzile de vânzare cu o stare dedicată de tip „Contract” (Agreement) și un flux controlat de comenzi părinte–copil. O ofertă acceptată poate fi transformată într-un Contract care nu generează livrări sau facturi, ci stabilește cadrul comercial. Comenzile ulterioare se leagă de Contract și consumă din cantitățile și prețurile agreate, oferind un control clar asupra a ceea ce se livrează și facturează efectiv în cadrul unei înțelegeri-cadru cu clientul.

#### 2. Funcționalități Cheie

- Stare Contract (Agreement): transformă o ofertă acceptată într-o stare de Contract non-logistică, care nu creează livrări sau facturi.
- Comenzi părinte–copil: leagă comenzile ulterioare de un Contract printr-un câmp de comandă părinte și urmărește consumul față de Contract, per produs.
- Control supraconsum: pe liniile de Contract, permite sau blochează supraconsumul per produs printr-un simplu bifaj (serviciile îl permit implicit; produsele stocabile/consumabile nu).
- Listă de prețuri de Contract: generează automat o listă de prețuri dedicată din liniile ofertei de Contract și o impune pe toate comenzile copil.
- Valori implicite pentru comenzile copil: comenzile copil moștenesc partenerul, adresele de facturare și livrare și lista de prețuri a Contractului din Contractul părinte.
- UI/Raport:
  - Variantă a barei de stare care afișează „Agreement” când comanda este în starea Contract.
  - Buton inteligent pentru navigarea către comenzile copil din Contract.
  - Titlul raportului de vânzare afișează „Agreement #” pentru starea Contract.

Note:
- Construit pentru Odoo 19: folosește expresii moderne de vizualizare (fără `attrs`/`states`).
- Modulul nu modifică logistica standard de confirmare: doar comenzile copil confirmate la stadiul Sale generează livrări și facturi.

#### 3. Dependențe

- `sale_management`

#### 4. Componente Cheie

Documentația de Sumar și Funcționalități Cheie a fost preluată din `readme/DESCRIPTION.md`, conform fluxului de ingestie. Acesta nu detaliază explicit modelele, vizualizările sau acțiunile, prin urmare analiza codului pentru componente a fost omisă. Pe baza manifestului, modulul include o secvență dedicată (`data/ir_sequence_data.xml`), extinderi de vizualizări pentru comanda de vânzare (`views/sale_order_views.xml`) și o personalizare a raportului de vânzare (`report/sale_report_templates.xml`).

#### 5. Conexiuni

Nu au fost identificate conexiuni cu alte module documentate în wiki.
