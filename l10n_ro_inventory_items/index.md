# Romania - Obiecte de inventar (303/603/8035)

- **Nume Tehnic:** `l10n_ro_inventory_items`
- **Versiune:** `20.0.2.7.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_inventory_items
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_inventory_items`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează obiectele de inventar conform OMFP 1802/2014: bunuri sub pragul fiscal al mijloacelor fixe (5.000 lei din anul fiscal 2026), recepționate pe contul 303 și consumate contabil la darea în folosință prin 603 = 303. Fiecare obiect are o fișă proprie, cu număr de inventar, responsabil și locație, iar ciclul de viață este urmărit de la recepție până la scoaterea din gestiune, cu documentele tipăribile aferente.

#### 2. Funcționalități Cheie

- **Fișă individuală per obiect:** număr de inventar `OI/AAAA/NNNN`, responsabil, locație / departament, depozit, stare fizică și stare flux (Recepționat, Dat în Folosință, Scos din Gestiune). Fișa se creează automat la validarea recepției unui produs marcat „Obiect de Inventar (RO)”, iar valoarea ei urmează factura și costurile adiționale cât timp obiectul e în stoc.
- **Dare în folosință:** individual (butonul „Dă în Folosință”) sau în bloc (Inventar → Obiecte de Inventar → Dare în Folosință (batch), ori Acțiuni din listă), cu verificarea stocului din depozitul fișei, picking de consum și nota 603 = 303; se tipărește Bonul de Dare în Folosință. Se consumă întreaga cantitate a fișei.
- **Evidență extrabilanțieră 8035** (activabilă pe companie): nota 8035 = 803999 la dare în folosință, stornată la scoatere, în jurnalul „Evidență extrabilanțieră” (EXTR) din `l10n_ro_off_balance`. Butonul „Verifică reconciliere 8035” compară soldul contului cu valoarea obiectelor aflate în folosință.
- **Scoatere din gestiune:** individuală sau în bloc, cu motiv, tip (casată, pierdută / lipsă, restituită în magazie) și comisie de inventariere; la restituire obiectul revine în starea Recepționat. Se tipărește PV-ul de scoatere.
- **Casarea obiectelor vechi:** wizard care propune obiectele aflate în folosință de peste un număr de luni (implicit 12), cu comisie și motiv obligatorii.
- **Cere factura înainte de darea în folosință** (opțional, pe companie): blochează darea în folosință până la postarea facturii furnizorului.
- **Configurare:** produsul se marchează „Obiect de Inventar (RO)” (bun stocabil), iar categoria lui se setează pe evaluare perpetuă, cu cont de stoc 303 și cont de cheltuieli 603.
- **Rapoarte PDF:** Bon de Dare în Folosință, PV de Scoatere din Gestiune și Registrul OI. Fluxul detaliat este în fișa consultantului.

#### 3. Dependențe

- `stock_account`
- `l10n_ro`
- [l10n_ro_off_balance](../l10n_ro_off_balance/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.inventory.item`: fișa obiectului de inventar, cu starea fizică și de flux, urmărire în chatter și acțiunile de dare în folosință / scoatere.
- `l10n.ro.inventory.item.use.wizard`: darea în folosință a unuia sau mai multor obiecte.
- `l10n.ro.inventory.item.dispose.wizard`: scoaterea din gestiune (individuală sau în bloc).
- `l10n.ro.inventory.item.auto.dispose.wizard`: casarea obiectelor aflate în folosință de mult timp.
- `product.template`: extins cu marcajul „Obiect de Inventar (RO)”.
- `res.company`: extins cu setările pentru 8035 și cerința facturii.
- `stock.move`: extins pentru crearea fișelor la recepție și alinierea valorii la ieșire.

**Vizualizări**

- `view_l10n_ro_inventory_item_form`, `view_l10n_ro_inventory_item_list`, `view_l10n_ro_inventory_item_search`: fișa OI, lista și căutarea.
- `view_l10n_ro_inventory_item_use_wizard_form`, `view_l10n_ro_inventory_item_dispose_wizard_form`, `view_l10n_ro_inventory_item_auto_dispose_wizard_form`: ferestrele wizardurilor.
- `view_product_template_form_oi_inherit`, `view_res_company_form_oi_inherit`: marcajul pe produs și setările pe companie.
- Meniul **Inventar → Obiecte de Inventar** (registru, dare în folosință, scoatere, casare).

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: pregătește la instalare evidența extrabilanțieră pentru companiile românești.
- `seq_l10n_ro_inventory_item`: secvența numerelor de inventar; `stock_location_oi_consumption`: locația virtuală de consum.
- Nu există acțiuni cron.

#### 5. Conexiuni

- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md): inventarierea stocurilor și notele contabile ale diferențelor.
- [l10n_ro_inventory_register](../l10n_ro_inventory_register/index.md): Registrul inventar poate prelua evidența extrabilanțieră a obiectelor de inventar.
- [l10n_ro_inventory_items_hr](../l10n_ro_inventory_items_hr/index.md): extensie pentru legătura cu angajații.
- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): mijloacele fixe, peste pragul obiectelor de inventar.
