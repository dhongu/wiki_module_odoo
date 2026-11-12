# Deltatech Sale Contracts (localizat la `deltatech_sale_contracts/index.md`)

- **Nume Tehnic:** `deltatech_sale_contracts`
- **Versiune:** `19.0.1.0.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_contracts
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_contracts`
- **Ultima Ingestie:** `2026-11-12`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde comenzile de vânzare cu o stare dedicată de tip „Contract” (Agreement) și un flux controlat de comenzi părinte–copil. O ofertă acceptată poate fi transformată într-un Contract care nu generează livrări sau facturi, ci stabilește cadrul comercial. Comenzile ulterioare se leagă de Contract și consumă din cantitățile și prețurile agreate, oferind un control clar asupra a ceea ce se livrează și facturează efectiv în cadrul unei înțelegeri-cadru cu clientul.

#### 2. Funcționalități Cheie

- **Stare Contract (Agreement):** butonul *Set to Contract* de pe o ofertă (cu cel puțin o linie de produs) o transformă într-un Contract non-logistic: primește număr din secvența de contracte (ex. `C00001`), este blocat și nu creează livrări sau facturi. Contractele se listează în *Sales → Orders → Contracts*.
- **Comenzi părinte–copil:** comenzile ulterioare se leagă de un Contract prin câmpul *Contract* (fila *Other Info*) sau din butonul inteligent *Child Orders*; doar documentele în starea Agreement pot fi alese.
- **Verificarea consumului la confirmare:** la confirmarea unei comenzi copil, cantitatea fiecărui produs se adaugă la cea a comenzilor copil **confirmate** ale aceluiași Contract (ofertele și comenzile anulate nu consumă) și se compară cu cantitatea contractată. Produsele care nu sunt în Contract nu sunt verificate și se vând la prețul propriu.
- **Control supraconsum:** depășirea cantității contractate refuză confirmarea, cu excepția liniilor de Contract cu *Allow Overconsumption* (implicit permis pentru servicii), unde se postează o notă în chatterul Contractului și al comenzii. Opțiunea nu apare pe niciun formular (se setează doar prin import sau API), deci din ecran o comandă care depășește Contractul este refuzată. Verificarea poate fi dezactivată prin parametrul de sistem `deltatech_sale_contracts.avoid_check`.
- **Listă de prețuri de Contract:** la trecerea în Contract se generează o listă de prețuri „Contract <număr>”, cu câte o regulă de preț fix pe produs (egală cu prețul liniei; la produse duplicate se folosește ultimul preț). Se aplică pe comenzile copil, unde nu poate fi editată. Lista se creează o singură dată: modificările ulterioare ale liniilor nu o actualizează.
- **Valori implicite pentru comenzile copil:** comenzile copil moștenesc partenerul, adresele de facturare și livrare și lista de prețuri din Contractul părinte.
- **UI/Raport:** bara de stare afișează „Agreement” în starea Contract; butonul inteligent *Child Orders* listează toate comenzile legate (inclusiv ofertele); titlul raportului de vânzare afișează „Agreement #” pentru starea Contract.
- **Limitări cunoscute:** titlul tipărit este „Agreement #” fără numărul contractului; Contractul nu poate fi anulat din formular (se folosește *Unlock* pentru modificări); nu există raport de consum, cantitățile rămase se calculează la confirmarea comenzilor copil.
- Modulul nu modifică logistica standard de confirmare: doar comenzile copil confirmate la stadiul Sale generează livrări și facturi. Fluxul pas cu pas rămâne în fișa consultant.

#### 3. Dependențe

- `sale_management`

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md` și `readme/USAGE.md`; mai jos sunt doar reperele confirmate în cod.

**Modele**

- `sale.order` (extins): starea `agreement`, câmpul `parent_id` („Contract”), `is_contract`, acțiunea `action_set_agreement`, crearea listei de prețuri de Contract (`_create_or_update_contract_pricelist`), calculul consumului pe produs și `_check_child_overconsume`, apelat din `action_confirm`.
- `sale.order.line` (extins): câmpul `allow_overconsume` („Allow Overconsumption”), implicit adevărat pentru servicii.

**Vizualizări**

- `views/sale_order_views.xml`: butonul *Set to Contract*, bara de stare cu „Agreement”, butonul inteligent *Child Orders*, câmpul *Contract* în *Other Info* și meniul *Contracts*.
- `report/sale_report_templates.xml`: titlul „Agreement #” al raportului de vânzare.
- `data/ir_sequence_data.xml`: secvența `sale.contract` a numerelor de Contract.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`.

#### 5. Conexiuni

Nu au fost identificate conexiuni cu alte module documentate în wiki.
