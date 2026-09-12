# Romania - POS Fiscal Compliance / ECR Bridge (localizat la `l10n_ro_pos_fiscal_compliance_ecr/index.md`)

- **Nume Tehnic:** `l10n_ro_pos_fiscal_compliance_ecr`
- **Versiune:** `19.0.1.1.0`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_pos_fiscal_compliance_ecr](https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_pos_fiscal_compliance_ecr)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_pos_fiscal_compliance_ecr`
- **Ultima Ingestie:** `2026-09-12`

#### 1. Sumar

Modulul este puntea dintre driverul casei de marcat (`deltatech_pos` și agentul local Terrabit Connect) și evidența fiscală AMEF ținută de [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md). Driverul salvează pe comanda POS răspunsul brut al aparatului fiscal (numărul documentului fiscal, numărul bonului din raportul Z, numărul Z, starea și eventuala eroare), iar modulul de conformitate urmărește separat starea fiscală cerută de OUG 28/1999 — de fiscalizat / emis / eroare — pe care se sprijină blocarea închiderii sesiunii, raportul Z reconciliat și potrivirea cu jurnalul electronic. Fără această punte, cele două seturi de câmpuri rămân paralele: aparatul confirmă bonul, dar comanda rămâne „de fiscalizat”, iar reconcilierea cu arhiva AMEF se face doar euristic, pe dată și sumă.

#### 2. Funcționalități Cheie

- Traduce automat răspunsul driverului în starea fiscală urmărită de modulul de conformitate, la fiecare `create`/`write` pe comandă care atinge câmpurile driverului (`fiscal_state`, `fiscal_receipt_number`, `fiscal_doc_number`, `fiscal_z`, `fiscal_error`).
- Confirmare cu număr → bon emis, cu seria aparatului preluată din configurarea punctului de vânzare (`l10n_ro_fiscal_device_serial`).
- Confirmare fără număr → eroare, nu bon emis: fără număr documentul nu poate fi reconciliat cu jurnalul electronic AMEF.
- Bon anulat la casă sau eroare de tipărire → eroare fiscală, cu mesajul aparatului păstrat pe comandă.
- Pentru identificarea bonului în jurnalul electronic (`idB`) folosește numărul documentului fiscal (NR), unic pe aparat, și cade pe numărul bonului din raportul Z (BF) doar dacă aparatul nu a raportat NR — BF se reia la fiecare Z și nu identifică bonul pe o perioadă mai lungă.
- Nu are ecran de configurare propriu; se instalează automat (`auto_install`) când ambele module sunt prezente.
- Condiție operațională pentru ca puntea să primească date: punctul de vânzare trebuie să aibă `Transport ECR` setat pe **Terrabit Connect** (nu „fișier”) în Configurare → Casă de marcat, seria aparatului fiscal (AMEF) completată pe punctul de vânzare și agentul Terrabit Connect instalat/pornit pe calculatorul casei; cât timp transportul rămâne pe „fișier”, aparatul nu întoarce niciun răspuns și comenzile rămân „de fiscalizat”, ceea ce ar bloca închiderea sesiunii dacă opțiunea „Fiscalizare AMEF obligatorie” e activă.

#### 3. Dependențe

- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md)
- `deltatech_ecr_fiscal`

#### 4. Componente Cheie

**Modele**

- `pos.order`: extinde comanda POS, aplicând explicit mixinul `deltatech.ecr.fiscal.mixin` (necesar fiindcă `deltatech_ecr_fiscal` nu îl mai aplică singur pe `pos.order`, ca să nu forțeze dependența de `point_of_sale`); suprascrie `create`/`write` pentru a detecta scrierea câmpurilor driverului și a apela `_l10n_ro_sync_fiscal_state_from_driver()`, care traduce starea driverului (`done`/`canceled`/`error`) în starea fiscală AMEF prin `_l10n_ro_apply_fiscal_response()` (expusă de `l10n_ro_pos_fiscal_compliance`).

#### 5. Conexiuni

- [deltatech_pos](../deltatech_pos/index.md): driverul care scrie pe comanda POS răspunsul aparatului fiscal (numărul, starea, eroarea) pe care această punte îl citește.
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): modelul comun de document fiscal, conversia în format ECR și trimiterea prin agentul Terrabit Connect.
- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md): urmărirea bonului fiscal AMEF, reconcilierea raportului Z și blocarea sesiunii — destinația stării fiscale scrise de această punte.
- [deltatech_pos_stock](../deltatech_pos_stock/index.md): afișează stocul disponibil direct în interfața POS, parte din aceeași suită Terrabit pentru POS.
- [deltatech_pos_price_sync](../deltatech_pos_price_sync/index.md): trimite modificările de preț către sesiunile POS deja deschise, parte din aceeași suită.
- [deltatech_pos_fix](../deltatech_pos_fix/index.md): corectează calculul totalului POS la maparea de poziție fiscală cu taxă inclusă.
- [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md): raportează bonurile fiscale POS în declarația D394 (op. 2) către ANAF, pe baza stării fiscale ținute de conformitate.
- [l10n_ro_pos_returns](../l10n_ro_pos_returns/index.md): factură de retur dedicată și linie de casă separată pentru fiecare retur POS.
