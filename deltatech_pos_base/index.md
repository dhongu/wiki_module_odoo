# Deltatech POS Base (localizat la `deltatech_pos_base/index.md`)

- **Nume Tehnic:** `deltatech_pos_base`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_pos_base
- **Cale Locală:** `odoo-addons/bitshop/deltatech_pos_base`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul reprezintă stratul de integrare fundamental dintre sistemele Point of Sale (POS) și casele de marcat electronice (ECR) ale Odoo, oferind definițiile de bază și structurile de date necesare pentru tipărirea fiscală. Din punct de vedere business, este modulul esențial pentru companiile care trebuie să își conecteze POS-ul Odoo sau POS Backend la dispozitive fiscale externe, pentru a asigura conformitatea cu reglementările. El standardizează câmpurile și metodele folosite atât de modulele front-end, cât și de cele back-end de POS, astfel încât operațiunile cu ECR să fie consistente, iar dezvoltarea modulelor fiscale specifice unei piețe să fie simplificată pe o bază comună.

#### 2. Funcționalități Cheie

- Integrare robustă POS-ECR: oferă o fundație stabilă pentru comunicarea dintre Odoo și imprimantele fiscale sau casele de marcat conectate.
- Structură de date unificată: standardizează câmpurile și metodele utilizate de modulele POS de tip front-end și back-end pentru operațiuni ECR consistente.
- Conformitate fiscală simplificată: facilitează dezvoltarea și implementarea modulelor fiscale specifice fiecărei piețe pe o bază comună.
- Înregistrare fiabilă a tranzacțiilor: asigură capturarea și formatarea consecventă a datelor POS esențiale pentru fiscalizare.
- Operațiuni de retail scalabile: permite extinderea ușoară a rețelei de magazine folosind o bază POS comună pentru toate locațiile și tipurile de dispozitive fiscale.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de cod nu au fost analizate în detaliu deoarece `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie. Mai jos sunt listate elementele declarate în `__manifest__.py` și modelele care le susțin, pentru context tehnic suplimentar.

**Modele**

- `pos.payment.method` (extindere): adaugă `cod_ecr` (codul ECR asociat metodei de plată, folosit la tipărirea fiscală) și îl expune datelor încărcate în POS Frontend prin `_load_pos_data_fields`.
- `pos.config` (extindere): definește tipul casei de marcat (`ecr_type`: FiscalWire/Optima/Daisy/Succes/FiscalNet/Incotex), opțiuni de trunchiere a numelui produsului (`ecr_trim`, `ecr_trim_to`), prefixul și extensia fișierului de comandă fiscală (`file_prefix`, `file_ext`) și modul de transport al comenzii fiscale (`ecr_transport`: descărcare fișier `.prn/.inp` sau trimitere către agentul local Terrabit Connect, `ecr_connect_url`).
- `res.config.settings` (extindere): expune toate câmpurile de configurare ECR de mai sus (via `related`) în ecranul de setări al Point of Sale.

**Vizualizări**

- `pos_payment_method_view_form`: extinde formularul metodei de plată POS cu câmpul `cod_ecr`.
- `res_config_settings_view_form` (secțiunea ECR): adaugă în Settings tipul de casă de marcat, trunchierea numelui de produs, prefixul/extensia fișierului și modul de transport (fișier vs. Terrabit Connect, cu URL-ul agentului local).

#### 5. Conexiuni

- [deltatech_pos](../deltatech_pos/index.md): modul soră care folosește această bază pentru funcționalitatea de Point of Sale Deltatech.
