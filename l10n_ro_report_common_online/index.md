# Romania - Report Common for Odoo Online

- **Nume Tehnic:** `l10n_ro_report_common_online`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_report_common_online
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_report_common_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Elementele comune ale rapoartelor tipărite românești, disponibile și pe Odoo Online: antetul cu datele firmei, conturile bancare și suma în litere. Modulul nu conține cod Python și se importă ca arhivă zip (Aplicații > Importați modulul); este varianta doar cu date a modulului [l10n_ro_report_common](../l10n_ro_report_common/index.md).

#### 2. Funcționalități Cheie

- Șablonul `banks`: tipărește până la 3 conturi bancare ale partenerului bifate *Romania - Print in Report*, în moneda documentului (sau a firmei); moneda unui cont este cea a jurnalului bancar legat, altfel moneda firmei.
- Șablonul `report_address_company`: blocul de identificare a firmei (nume, adresă, conturi bancare, CUI, nr. Reg. Com., capital social).
- Șablonul `amount_in_words`: suma în litere cum se scrie pe documentele românești (ex. „douăzeci și una de mii de lei", „un leu și un ban"), apelat cu `amount` și `currency`; RON este scris în română indiferent de limba tipăririi, celelalte monede păstrează formularea standard Odoo.
- Două câmpuri manuale (`x_`), cerute de Odoo Online: *Romania - Print in Report* pe conturile bancare și *Share Capital* pe firmă (se tipărește fără zecimale).
- Configurare: **Setări > Utilizatori și companii > Companii** pentru capitalul social; **Contacte > Configurare > Conturi bancare** pentru bifa de tipărire. Modulul nu are raport propriu; rezultatul apare în rapoartele care îi apelează șabloanele. Limba română se activează înainte de import. Detalii în [fișa consultant](FISA_CONSULTANT.md).
- Nu se poate instala împreună cu `l10n_ro_report_common` (excludere în manifest): cele două țin aceleași date în câmpuri diferite.

#### 3. Dependențe

- `l10n_ro`

#### 4. Componente Cheie

Descrierea din Readme nu detaliază componentele tehnice; lista provine din analiza modulului.

**Modele**

- `res.partner.bank`: câmpul manual `x_l10n_ro_print_report`.
- `res.company`: câmpul manual `x_l10n_ro_share_capital`.

**Vizualizări**

- `views/report_templates.xml`: șabloanele QWeb `banks`, `report_address_company`, `amount_in_words`.
- `views/res_company_views.xml`: capitalul social pe formularul firmei.
- `views/res_partner_bank_views.xml`: bifa și coloana de tipărire pe conturile bancare.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_report_common](../l10n_ro_report_common/index.md): varianta cu Python; nu se instalează împreună.
- [l10n_ro_picking_report_online](../l10n_ro_picking_report_online/index.md): documentele de stoc, care folosesc blocurile comune prin `l10n_ro_invoice_report_online`.
