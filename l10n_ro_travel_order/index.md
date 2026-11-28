# Romania - Ordin de deplasare (delegație) (localizat la `l10n_ro_travel_order/index.md`)

- **Nume Tehnic:** `l10n_ro_travel_order`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_travel_order
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_travel_order`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Ordinul de deplasare (delegația) ca document propriu: se aprobă înainte de plecare, calculează zilele de diurnă din perioadă, creează decontul de cheltuieli și se tipărește pe formularul 14-5-4, față și verso. Reduce munca manuală a contabilului și păstrează într-un singur loc deplasarea, avansul și decontul.

#### 2. Funcționalități Cheie

- **Ordinul de deplasare** numerotat din secvență (`OD/an/nr`) la aprobare, cu angajat, funcție, act de identitate, scop, destinație, mijloc de transport, perioadă planificată și efectivă, avans și unități vizitate (sosire, plecare, cazare).
- **Stări:** Ciornă → Aprobat → În deplasare → Decontat (sau Anulat); avertisment peste 60 de zile calendaristice.
- **Zile de diurnă:** în țară, fiecare 24 de ore e o zi, iar ultima fracțiune contează de la 12 ore (prag configurabil); în străinătate perioada se socotește între trecerile frontierei, fracțiunea fiind 50% până la 12 ore și integrală peste.
- **Diurna zilnică** propusă este limita neimpozabilă a cuantumului legal din modulul *Diurnă*; se poate modifica.
- **Decont din ordin:** butonul *Creează decontul* completează angajatul, avansul, zilele, diurna, țara și numărul ordinului; diurna în valută trece în lei la cursul din data plecării planificate. La validarea decontului ordinul devine *Decontat*.
- **Formular 14-5-4** tipărit, cu fața (dispoziție, căsuțe pentru ștampilele unităților) și versoul (cheltuieli, diurnă, diferența de primit sau restituit); variantă pentru străinătate; căsuța CFP opțională.
- **Setări** (Setări → Contabilitate → Ordine de deplasare): ore minime pentru ultima zi și controlul financiar-preventiv. Fluxul detaliat este în fișa consultantului.

#### 3. Dependențe

- [l10n_ro_expense_allowance](../l10n_ro_expense_allowance/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.travel.order`: ordinul de deplasare (mail.thread, mail.activity.mixin).
- `l10n.ro.travel.order.stop`: unitățile vizitate.
- `deltatech.expenses.deduction`: extins cu legătura către ordin.
- `res.company`, `res.config.settings`: setările ordinelor de deplasare.

**Vizualizări**

- `view_l10n_ro_travel_order_form`, `view_l10n_ro_travel_order_list`, `view_l10n_ro_travel_order_search`: formular, listă și căutare pentru ordine.
- `view_deltatech_expenses_deduction_form_travel_order`: legătura ordinului în decont.
- `res_config_settings_view_form_travel_order`: setările.
- `report/report_travel_order.xml`: formularul 14-5-4 PDF.

**Acțiuni Automate / Acțiuni Server**

- Secvența `ir.sequence` a ordinelor. Fără cron-uri.

#### 5. Conexiuni

- [l10n_ro_expense_allowance](../l10n_ro_expense_allowance/index.md): cuantumurile legale de diurnă și decontul din care se creează ordinul.
