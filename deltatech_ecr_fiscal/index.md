# ECR Fiscal Audit Fields (localizat la `deltatech_ecr_fiscal/index.md`)

- **Nume Tehnic:** `deltatech_ecr_fiscal`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_ecr_fiscal
- **Cale Locală:** `odoo-addons/deltatech/deltatech_ecr_fiscal`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Definește într-un singur loc câmpurile care rețin rezultatul tipăririi pe casa de marcat fiscală (ECR/AMEF). Modulul nu are ecrane proprii: oferă doar contractul de câmpuri, folosit de POS, facturare și localizări, fără a cere Point of Sale.

#### 2. Funcționalități Cheie

- **Bon fiscal (BF)**: numărul bonului în Z-ul curent; se reia de la fiecare Z.
- **Document fiscal (NR)**: număr unic per dispozitiv, cel de folosit pentru identificare fără ambiguitate.
- **Raport Z** de care aparține bonul și **Stare fiscală** raportată de driver; **Eroare fiscală** când dispozitivul a refuzat sau a eșuat.
- **Bon simulat**: bifat de drivere pe bonurile unei case simulate (emulator în Odoo sau Terrabit Connect în mod simulare); nu sunt documente fiscale, iar modulele de conformitate le exclud din raportul Z.
- Câmpurile se scriu de driver (ecranul de plată POS sau acțiunea de tipărire din magazin, după răspunsul agentului Terrabit Connect) și se citesc în rapoarte și în localizarea română.
- Câmpurile se văd prin **Acțiuni → Export** pe facturi sau pe comenzile POS; scrierea se face moștenind mixinul `deltatech.ecr.fiscal.mixin`, iar citirea cere doar `deltatech_ecr_fiscal` în `depends`.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `deltatech.ecr.fiscal.mixin`: mixin abstract cu câmpurile fiscale.
- `account.move`: extins cu mixinul (câmpurile apar pe note contabile și facturi).

**Vizualizări**

- Niciuna (modul fără ecrane proprii; `hidden`).

**Acțiuni Automate / Acțiuni Server**

- `pre_init_hook`: păstrează câmpurile deja existente în producție la mutarea lor în acest modul.

#### 5. Conexiuni

- [deltatech_sale_store](../deltatech_sale_store/index.md): tipărește bonul din factură și afișează câmpurile pe formularul facturii.
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): conectare la casa de marcat.
- [deltatech_ecr_online](../deltatech_ecr_online/index.md): casă de marcat online.
- `deltatech_pos`: completează câmpurile pe comenzile POS.
- `deltatech_tc`: stația Terrabit Connect (mod simulare).
- `l10n_ro_pos_fiscal_compliance_ecr`: exclude bonurile simulate din raportul Z.
