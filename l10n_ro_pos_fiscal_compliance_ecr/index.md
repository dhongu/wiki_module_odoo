# Romania - Punte POS ↔ casă de marcat (AMEF) (localizat la `l10n_ro_pos_fiscal_compliance_ecr/index.md`)

- **Nume Tehnic:** `l10n_ro_pos_fiscal_compliance_ecr`
- **Versiune:** `20.0.1.3.1`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_pos_fiscal_compliance_ecr](https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_pos_fiscal_compliance_ecr)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_pos_fiscal_compliance_ecr`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul este puntea dintre driverul casei de marcat (`deltatech_pos` și agentul local Terrabit Connect) și evidența fiscală AMEF ținută de [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md). Driverul salvează pe comanda POS răspunsul aparatului fiscal (numărul documentului fiscal, numărul bonului în raportul Z, numărul Z, starea și eroarea), iar modulul de conformitate urmărește separat starea fiscală cerută de OUG 28/1999 (de fiscalizat / emis / eroare), de care depind blocarea închiderii sesiunii, raportul Z reconciliat și potrivirea cu jurnalul electronic. Fără punte, cele două seturi de câmpuri rămân paralele: aparatul confirmă bonul, dar comanda rămâne „de fiscalizat", iar reconcilierea cu arhiva AMEF se face doar euristic, pe dată și sumă.

#### 2. Funcționalități Cheie

- **Confirmare cu număr** → bon emis, cu seria aparatului luată din configurarea punctului de vânzare.
- **Confirmare fără număr** → eroare, nu bon emis: fără număr, bonul nu poate fi reconciliat cu jurnalul electronic.
- **Bon anulat la casă** sau **eroare de tipărire** → eroare fiscală, cu mesajul aparatului păstrat pe comandă.
- La importul jurnalului electronic AMEF, bonul din aparat se potrivește cu comanda pe numărul raportului Z și pe numărul bonului în Z, salvate de driver; comanda păstrează seria casei și numărul documentului fiscal, care nu apar în fișierele ANAF.
- Nu are ecran de configurare propriu și se instalează automat (`auto_install`) când ambele module sunt prezente.
- Condiții operaționale: la **Punct de vânzare → Configurare → Casă de marcat**, `Transport ECR` pe **Terrabit Connect** (nu „fișier"), cu adresa agentului local; seria aparatului fiscal (AMEF) completată pe punctul de vânzare; agentul Terrabit Connect instalat și pornit pe calculatorul casei. Cât timp transportul rămâne pe „fișier", comenzile rămân „de fiscalizat", iar opțiunea „Fiscalizare AMEF obligatorie" ar bloca închiderea sesiunii.

#### 3. Dependențe

- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md)
- [deltatech_ecr_fiscal](../deltatech_ecr_fiscal/index.md)

#### 4. Componente Cheie

**Modele**

- `pos.order`: extinde comanda POS aplicând mixinul `deltatech.ecr.fiscal.mixin` și traduce răspunsul driverului în starea fiscală AMEF prin metoda expusă de `l10n_ro_pos_fiscal_compliance`.
- `l10n.ro.amef.journal`: extins pentru potrivirea bonurilor din jurnalul electronic cu comenzile pe numărul Z și numărul bonului în Z.

**Vizualizări**

- Modulul nu definește vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau acțiuni server; traducerea stării se face la scrierea câmpurilor driverului pe comandă.

#### 5. Conexiuni

- [deltatech_pos](../deltatech_pos/index.md): driverul care scrie pe comanda POS răspunsul aparatului fiscal, pe care această punte îl citește.
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): modelul comun de document fiscal, conversia în format ECR și trimiterea prin agentul Terrabit Connect.
- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md): urmărirea bonului fiscal, raportul Z reconciliat și blocarea sesiunii; destinația stării fiscale scrise de punte.
- [deltatech_pos_stock](../deltatech_pos_stock/index.md): afișează stocul disponibil în interfața POS, din aceeași suită POS.
- [deltatech_pos_price_sync](../deltatech_pos_price_sync/index.md): trimite modificările de preț către sesiunile POS deschise.
- [deltatech_pos_fix](../deltatech_pos_fix/index.md): corectează calculul totalului POS la poziții fiscale cu taxă inclusă.
- [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md): raportează bonurile fiscale POS în D394, pe baza stării fiscale ținute de conformitate.
- [l10n_ro_pos_returns](../l10n_ro_pos_returns/index.md): factură de retur dedicată pentru fiecare retur POS.
