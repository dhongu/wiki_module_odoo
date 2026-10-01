# Deltatech Intrastat Fiscal Risk (localizat la `deltatech_instastat_tax_risk/index.md`)

- **Nume Tehnic:** `deltatech_instastat_tax_risk`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_instastat_tax_risk
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_instastat_tax_risk`
- **Ultima Ingestie:** `2026-10-01`

#### 1. Sumar

Modulul permite marcarea produselor care sunt supuse riscului fiscal. Marcajul se face la nivelul codurilor Intrastat (nomenclatorul de coduri de marfă), astfel încât toate produsele încadrate la un cod marcat sunt tratate ca fiind cu risc fiscal. Ajută contabilii și responsabilii de conformitate să identifice rapid bunurile sensibile în raportarea Intrastat.

#### 2. Funcționalități Cheie

- Indicator „Fiscal Risk" (da/nu) pe fiecare cod Intrastat, implicit dezactivat.
- Câmpul apare în formularul codului Intrastat.
- În lista codurilor Intrastat există o coloană opțională „Fiscal Risk" (ascunsă implicit).
- În căutare există câmpul „Fiscal Risk" și filtrul „Fiscal Risk", care afișează doar codurile marcate.
- Starea modulului: Beta; licență OPL-1.

#### 3. Dependențe

- `account_intrastat`

#### 4. Componente Cheie

**Modele**

- `account.intrastat.code` (extins): adaugă câmpul boolean `fiscal_risk`.

**Vizualizări**

- `inherit_intrastat_code_form`: adaugă câmpul `fiscal_risk` în formularul codului Intrastat.
- `inherit_intrastat_code_tree`: adaugă coloana opțională `fiscal_risk` în listă.
- `inherit_intrastat_code_search`: adaugă câmpul și filtrul „Fiscal Risk" în căutare.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_intrastat_enhancement](../l10n_ro_intrastat_enhancement/index.md): îmbunătățiri Intrastat pentru localizarea României, în același domeniu funcțional (legătură de context, nu dependență în cod).
