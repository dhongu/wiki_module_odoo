# Romania - Report Common for Odoo Online (localizat la `l10n_ro_report_common_online/index.md`)

- **Nume Tehnic:** `l10n_ro_report_common_online`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_report_common_online
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_report_common_online`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă elementele comune ale rapoartelor românești tipărite (antetul cu datele firmei, conturile bancare și suma în litere în stilul chitanțelor românești), într-o variantă care funcționează și pe **Odoo Online**. Nu conține cod Python și se importă ca arhivă zip (Aplicații > Import Module). Este varianta „doar date” a modulului `l10n_ro_report_common`, pentru bazele de date unde codul Python personalizat nu poate rula.

#### 2. Funcționalități Cheie

- **Conturi bancare pe raport** (`l10n_ro_report_common_online.banks`): tipărește cel mult 3 conturi bancare ale partenerului, bifate cu *Romania - Print in Report*, în moneda documentului (sau a companiei).
- **Bloc de identificare a companiei** (`report_address_company`): denumire, adresă, conturi bancare, CUI, nr. de înregistrare la registrul comerțului (NRC) și capital social.
- **Suma în litere** (`amount_in_words`): scrisă în QWeb, se apelează cu `amount` și `currency`. Exemple: `500` – „cinci sute de lei”, `21000` – „douăzeci și una de mii de lei”, `1.01` – „un leu și un ban”, sumele negative încep cu „minus”. RON se scrie în română indiferent de limba de tipărire; celelalte monede păstrează formularea standard Odoo.
- **Două câmpuri manuale (`x_`)**, cerute de Odoo Online: *Romania - Print in Report* pe conturile bancare și *Share Capital* pe companie (tipărit fără zecimale).
- **Configurare**: capitalul social se completează în Setări > Utilizatori și companii > Companii (secțiunea „Company ID”); bifa pentru tipărire se pune în Contacte > Configurare > Conturi bancare. Coloana bifei apare și în lista conturilor bancare.
- Modulul nu are raport propriu: rezultatul apare în rapoartele care apelează șabloanele sale.
- **Pe Odoo Online**: se importă în planul Custom; limba română se activează înainte de import, ca etichetele să fie traduse. NRC-ul tipărit este câmpul **NRC** al contactului companiei.
- **Incompatibil cu `l10n_ro_report_common`** (manifestul le exclude reciproc): cele două module țin aceleași date în câmpuri diferite.
- Fluxul pas-cu-pas, cu capturi: [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro`

#### 4. Componente Cheie

**Modele**

Fără cod Python. Câmpuri manuale adăugate prin `data/ir_model_fields_data.xml`:

- `res.company`: `x_l10n_ro_share_capital` (Share Capital, float).
- `res.partner.bank`: `x_l10n_ro_print_report` (Romania - Print in Report, boolean).

**Vizualizări**

- `view_company_form` (moștenește `base.view_company_form`): câmpul capital social pe formularul companiei.
- `view_partner_bank_form` / `view_partner_bank_tree`: bifa de tipărire pe formularul și lista conturilor bancare.
- Șabloanele QWeb `banks`, `report_address_company`, `amount_in_words` (`views/report_templates.xml`).

**Acțiuni Automate / Acțiuni Server**

Niciuna.

#### 5. Conexiuni

- [l10n_ro_report_common](../l10n_ro_report_common/index.md): varianta cu cod Python a aceluiași set de blocuri; se exclud reciproc.
