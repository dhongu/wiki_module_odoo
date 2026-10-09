# Romania - Ordin de deplasare (delegație) (localizat la `l10n_ro_travel_order/index.md`)

- **Nume Tehnic:** `l10n_ro_travel_order`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_travel_order
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_travel_order`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Ordinul de deplasare (delegația) devine un document propriu: se aprobă înainte de plecare, calculează zilele de diurnă din perioada deplasării, creează decontul de cheltuieli al angajatului și se tipărește pe formularul 14-5-4, față și verso. Astfel, deplasarea este urmărită de la dispoziția de plecare până la decontarea finală, fără reintroducerea datelor.

#### 2. Funcționalități Cheie

- **Ordinul de deplasare:** număr din secvență (`OD/AAAA/NNNN`) dat la aprobare; angajat, funcție (păstrată la aprobare), act de identitate, scop, destinație, mijloc de transport; perioadă planificată și efectivă; deplasare în țară sau în străinătate (cu țară și cuantum legal al diurnei din modulul Diurnă); avans la plecare și în timpul deplasării, cu penalizări calculate.
- **Unități vizitate:** sosire, plecare și cazare pentru fiecare unitate; din ele se completează căsuțele de confirmare de pe față.
- **Stări:** Ciornă → Aprobat → În deplasare → Decontat (sau Anulat); avertisment la depășirea a 60 de zile calendaristice.
- **Zile de diurnă în țară:** fiecare 24 de ore înseamnă o zi; ultima fracțiune și deplasarea de o zi contează numai de la 12 ore (prag configurabil în setări).
- **Zile de diurnă în străinătate:** perioada se socotește între trecerile frontierei; fracțiunea de zi se plătește 50% până la 12 ore și integral peste (zilele pot fi 2,5). Diurna zilnică propusă este limita neimpozabilă, modificabilă.
- **Decont de cheltuieli:** butonul „Creează decontul” completează angajatul, avansul, zilele, diurna, tipul deplasării, țara, cuantumul legal și numărul ordinului; diurna în valută trece în lei la cursul din data avansului (și limita neimpozabilă la fel); pentru străinătate sunt necesare trecerile frontierei. La validarea decontului ordinul devine „Decontat”, la invalidare revine în „În deplasare”.
- **Formular tipărit 14-5-4:** fața cuprinde datele unității, dispoziția, durata, actul de identitate și căsuțele „Sosit / Plecat / Cu (fără) cazare”; versoul cuprinde plecarea/sosirea efective, avansul, cheltuielile din decont, diurna, totalul, diferența de primit sau restituit cu documentul de casă aferent și semnăturile. Pentru străinătate apar țara și diurna în valută cu echivalent în lei. Căsuța „Control financiar-preventiv” apare doar dacă e activată în setări.
- **Meniu și configurare:** Contabilitate → Furnizori → Ordine de deplasare; setări în Setări → Contabilitate → Ordine de deplasare (ore minime pentru ultima zi, implicit 12; control financiar-preventiv). Drepturile sunt cele din Decont cheltuieli: Aprobatorul aprobă și anulează, Contabilul creează și validează decontul. Numerotarea se schimbă din secvența „Travel Order”.

#### 3. Dependențe

- [l10n_ro_expense_allowance](../l10n_ro_expense_allowance/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.travel.order`: ordinul de deplasare (cu `mail.thread` și `mail.activity.mixin`); stări, calcul zile de diurnă, creare decont.
- `l10n.ro.travel.order.stop`: unitățile vizitate (sosire, plecare, cazare).
- `deltatech.expenses.deduction` (extins): legătura cu ordinul de deplasare și sincronizarea stării la validare/invalidare.
- `res.company` și `res.config.settings` (extinse): pragul de ore pentru ultima zi și opțiunea Control financiar-preventiv.

**Vizualizări**

- `view_l10n_ro_travel_order_form` / `view_l10n_ro_travel_order_list` / `view_l10n_ro_travel_order_search`: formular, listă și căutare pentru ordine; acțiune `action_l10n_ro_travel_order`, meniu `menu_l10n_ro_travel_order`.
- `view_deltatech_expenses_deduction_form_travel_order`: completări pe formularul decontului.
- `res_config_settings_view_form_travel_order`: setările modulului.
- `action_report_l10n_ro_travel_order`: raportul tipărit „Ordin de deplasare (14-5-4)”.

**Acțiuni Automate / Acțiuni Server**

- `seq_l10n_ro_travel_order`: secvența de numerotare (prefix `OD/%(year)s/`). Modulul nu definește acțiuni cron sau server.

#### 5. Conexiuni

- [deltatech_expenses](../deltatech_expenses/index.md): decontul de cheltuieli creat din ordin (dependență tranzitivă, prin Diurnă).
- [l10n_ro_expense_allowance](../l10n_ro_expense_allowance/index.md): cuantumurile legale ale diurnei (Contabilitate → Configurare → Contabilitate → Cuantumuri legale diurnă).
