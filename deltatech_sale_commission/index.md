# Sale Commission (localizat la `deltatech_sale_commission/index.md`)

- **Nume Tehnic:** `deltatech_sale_commission`
- **Versiune:** `20.0.2.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_commission`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_commission`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul calculează comisioanele de vânzare ale agenților pe baza profitului din raportul de profitabilitate al facturilor (din [deltatech_sale_margin](../deltatech_sale_margin/index.md)). Comisionul poate fi atribuit agentului de pe comanda de vânzare sau celui de pe factură, cu opțiunea de a-l anula când factura nu a fost încasată în termenul stabilit față de scadență. Comisioanele se calculează în masă dintr-un wizard și se marchează ca plătite după achitarea agentului, în afara modulului.

#### 2. Funcționalități Cheie

- Coloane, filtre și meniu de comisioane pe raportul de profitabilitate din `deltatech_sale_margin` (prețul de cost de pe factură și raportul în sine provin de acolo).
- Atribuire configurabilă a comisionului: agentul de pe **factură** sau agentul de pe **comanda de vânzare** din care provine linia (**Settings → Sales → Invoicing**, opțiunea *Salesperson commission compute*). Se decide la implementare — schimbarea ulterioară realocă toate liniile, inclusiv comisioanele deja plătite.
- Tabel de rate per agent și jurnal de vânzări (**Sales → Configuration → Users Commission**): rata agentului, plus manager și director de vânzări cu ratele lor, ca fracții din profit (0,100 = 10%). Un agent poate avea un singur rând per jurnal.
- Listă de comisioane de calculat (**Sales → Orders → Commission → Commission**): implicit luna trecută și doar facturile plătite; arată comisionul calculat (rată × profit), comisionul real și comisionul plătit. Comenzile POS din `deltatech_sale_margin_pos` nu apar aici, ci în analiza de profit.
- Acțiunea **Compute Commission** (wizard): comisionul real devine comisionul calculat, sau 0 dacă factura nu este plătită integral ori a fost plătită cu întârziere peste limita din parametru; pentru note de credit este mereu negativ și reduce totalul agentului. Se scrie doar comisionul agentului; sumele managerului și directorului sunt informative.
- Parametru `deltatech_sale_commission.days_for_commission` (valoare întreagă, 0 = plătit până la scadență): numărul maxim de zile între scadență și ultima plată; fără parametru, comisionul se acordă indiferent de plată.
- Corectare manuală a comisionului real înainte de plată și marcare ca plătit cu **Set Paid**; filtrele *Comision neplătit* / *Comision plătit* separă ce e achitat de ce rămâne de plată.
- Grupuri de acces neatribuite nimănui la instalare: **Manager comisioane** (calculează, modifică comisionul real și starea plății) și **Vizualizare comisioane** (doar consultare, vede costul și marja). Până la atribuire, meniul *Comision* este ascuns.
- Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_sale_margin](../deltatech_sale_margin/index.md)

#### 4. Componente Cheie

**Modele**

- `commission.users`: ratele de comision per agent, manager, director și jurnal de vânzări, cu constrângere de unicitate pe agent și jurnal și regulă multi-companie.
- `commission.compute` (wizard): calculează comisionul real al liniilor selectate.
- `commission.update.purchase.price` (extins): wizardul de actualizare a prețului de achiziție din `deltatech_sale_margin`.
- `account.move.line`, `sale.order.line` (extinse): câmpurile de comision și agentul pe linii.
- `res.config.settings` (extins): opțiunea de atribuire a comisionului (factură sau comandă).
- `sale.margin.report` (din `deltatech_sale_margin`, extins prin vizualizări): coloanele și filtrele de comision.

**Vizualizări**

- `view_commission_users_list`: lista editabilă a ratelor per agent.
- `view_commission_compute_form`: wizardul de calcul al comisioanelor.
- `view_sale_margin_report_commission_list` / `view_sale_margin_report_commission_form`: lista și formularul comisioanelor.
- `res_config_settings_view_form_stock`: opțiunea din Setări → Vânzări.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron` sau reguli `base.automation`; calculul se declanșează manual din acțiunea **Compute Commission**.

#### 5. Conexiuni

- [deltatech_sale_margin](../deltatech_sale_margin/index.md): furnizează raportul de profitabilitate, prețul de cost de pe facturi și politica de vânzare sub cost, pe care se bazează comisioanele.
- [deltatech_sale_margin_pos](../deltatech_sale_margin_pos/index.md): comenzile POS nu intră în lista de comisioane, dar comisionul lor calculat apare în analiza de profit.
