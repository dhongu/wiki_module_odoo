# POS Cashier Close Register (localizat la `deltatech_pos_cashier_close/index.md`)

- **Nume Tehnic:** `deltatech_pos_cashier_close`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_cashier_close
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_cashier_close`
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Când în Punctul de Vânzare se folosește *Log in with Employees*, Odoo păstrează butonul *Close Register* doar pentru manageri, împreună cu alte drepturi sensibile (intrări/ieșiri de numerar, editarea plăților, crearea produselor, modificarea prețurilor). Pentru ca vânzătorul care a lucrat tura să poată închide casa, ar trebui să primească toate aceste drepturi. Modulul mută doar acest buton la casieri, fără a le da restul drepturilor de manager. Este potrivit pentru magazinele care lucrează pe ture.

#### 2. Funcționalități Cheie

- **Casierii își închid singuri tura:** angajații cu drepturi de bază (*basic rights*) văd *Close Register* în meniu, acolo unde îl găsește și managerul. Fereastra de închidere este cea standard.
- **Nimic altceva nu se mută:** celelalte drepturi rămân la manageri. Angajații cu drepturi minime tot nu pot închide casa, iar o diferență de numerar peste suma autorizată (*Cash Control*) necesită în continuare un manager.
- **Configurabil per casă:** opțiunea *Cashiers Close the Register* se află în *Point of Sale > Configuration > Settings*, sub *PoS Interface*, imediat după *Log in with Employees*. Este bifată implicit; se debifează pe casele la care închiderea rămâne la managerul magazinului. Opțiunea apare doar dacă *Log in with Employees* este activ.
- **Atenție la sesiuni deschise:** setarea se citește la încărcarea casei, deci pagina casei se reîncarcă dacă sesiunea e deja deschisă.
- Instalarea modulului este decizia: nu există alt pas de activare.

#### 3. Dependențe

- `pos_hr`

#### 4. Componente Cheie

**Modele**

- `pos.config` (extins): adaugă câmpul boolean `cashier_can_close` (*Cashiers Close the Register*, implicit `True`).
- `res.config.settings` (extins): câmpul `pos_cashier_can_close`, legat (`related`) de `pos_config_id.cashier_can_close`, editabil din Setări.

**Vizualizări**

- `res_config_settings_view_form` (moștenește `point_of_sale.res_config_settings_view_form`): adaugă setarea după `multiple_employee_session`, vizibilă doar când `pos_hr` este activ pe casă.

**Componente front-end (POS)**

- `PosStore.cashierCanCloseRegister()`: returnează adevărat dacă casa folosește `pos_hr`, opțiunea este activă și casierul curent are rolul `cashier` (drepturi de bază). Drepturile minime nu închid niciodată.
- `Navbar.showCloseSession` (patch): afișează *Close Register* și când `cashierCanCloseRegister()` este adevărat.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `point_of_sale`: oferă ecranul de setări și bara de navigare extinse de modul.
- `pos_hr`: modulul Odoo care introduce rolurile angajaților în POS (dependență).
