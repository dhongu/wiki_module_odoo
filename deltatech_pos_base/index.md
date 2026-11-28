# POS ECR Base (localizat la `deltatech_pos_base/index.md`)

- **Nume Tehnic:** `deltatech_pos_base`
- **Versiune:** `20.0.1.0.12`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_pos_base
- **Cale Locală:** `odoo-addons/bitshop/deltatech_pos_base`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul este stratul de bază al integrării dintre Point of Sale și casele de marcat (ECR) sau imprimantele fiscale: păstrează configurarea ECR și o publică în interfața Punctului de vânzare. Bonul fiscal propriu-zis îl produc modulele construite peste el, cum sunt `deltatech_pos` și `deltatech_ecr_connect`. Pentru companiile care își conectează POS-ul Odoo la dispozitive fiscale externe, standardizează câmpurile și metodele folosite de modulele fiscale, ca dezvoltarea pentru o piață anume să plece de pe o bază comună.

#### 2. Funcționalități Cheie

- Fundație stabilă pentru comunicarea dintre Odoo și imprimantele fiscale sau casele de marcat conectate, cu structură de date unificată pentru modulele POS front-end și back-end.
- Setări ECR per punct de vânzare, în **Point of Sale > Configuration > Settings**, secțiunea **ECR**: tipul casei (FiscalWire, FiscalNet, Optima, Daisy, Succes, Incotex), scurtarea denumirilor lungi de produs (**Trim to**, implicit 30), prefixul și extensia fișierului de comandă (implicit `order` / `inp`) și **Default Department** (pentru aparate cu departamente fixe; altfel departamentul derivă din cota TVA).
- **Transport ECR**: descărcare fișier (`.prn`/`.inp`), agent local Terrabit Connect (URL implicit `http://127.0.0.1:8765`) sau driver local DxPrint (URL, utilizator și parolă); dacă agentul sau driverul nu răspund, fluxul revine la descărcarea fișierului.
- **Simulare** a casei de marcat pentru teste și instruire, în Odoo sau prin agent, cu întârziere configurabilă și răspunsuri forțate după zecimalele totalului (hârtie epuizată, aparat deconectat, răspuns tardiv, fără răspuns, bon anulat); doar administratorul de sistem o poate porni sau opri, iar nimic tipărit în simulare nu este bon fiscal real.
- **Cod ECR** pe metoda de plată (un caracter, implicit `0`), trimis cu fiecare bon, și **Cod ECR** opțional pe taxă, necesar doar când două taxe cu aceeași cotă (ex. garanție SGR și taxare inversă, ambele 0%) trebuie să ajungă pe categorii diferite ale aparatului.
- Câmpurile se încarcă în sesiunea POS la pornire; după modificarea unui cod, sesiunea se închide și se redeschide.
- Fluxul pas-cu-pas, cu capturi, este în fișa consultant.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `pos.payment.method` (extindere): adaugă `cod_ecr` și îl expune datelor încărcate în POS.
- `account.tax` (extindere): `cod_ecr` opțional pe taxă.
- `pos.config` (extindere): tipul casei (`ecr_type`), scurtarea numelui (`ecr_trim`, `ecr_trim_to`), `file_prefix`, `file_ext`, `default_department`, transportul (`ecr_transport`, `ecr_connect_url`, `ecr_dxprint_url`/`user`/`password`) și câmpurile de simulare (`ecr_simulation`, `ecr_simulator_next`, `ecr_simulator_sticky`, `ecr_simulator_delay_ms`).
- `res.config.settings` (extindere): expune câmpurile ECR (`related`) în Setările Point of Sale.
- `ir.http` (extindere): publică datele necesare în sesiunea POS.

**Vizualizări**

- `pos_payment_method_view_form`: câmpul `cod_ecr` pe metoda de plată.
- `account_tax_view`: câmpul `cod_ecr` pe taxă.
- `res_config_settings_view_form` (secțiunea ECR): tip casă, scurtare nume, fișier, transport și simulare.

#### 5. Conexiuni

- [deltatech_pos](../deltatech_pos/index.md): modulul soră care folosește această bază pentru tipărirea bonurilor pe casa de marcat din POS.
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): agentul local și panoul „Virtual devices” folosite de transportul Terrabit Connect și de simulare.
