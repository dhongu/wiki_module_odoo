# Romania - Producție în curs (331/711) OMFP 1802 (localizat la `l10n_ro_wip_closing/index.md`)

- **Nume Tehnic:** `l10n_ro_wip_closing`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_wip_closing
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_wip_closing`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează evaluarea și stornarea în roșu a producției în curs de execuție (WIP) conform OMFP 1802/2014 (Cap. 16, conturile 331 și 711; pct. 69, stornarea). Este destinat companiilor cu activitate de producție care contabilizează lunar WIP cu nota Dr 331 = Cr 711 și storno în roșu la prima zi a lunii următoare, cu un model persistent și audit trail.

#### 2. Funcționalități Cheie

- Model persistent `l10n.ro.wip.closing` cu mașină de stări Ciornă, Postată, Anulată.
- Calcul automat al WIP din ordinele de fabricație în curs (confirmate, în producție, de finalizat): componente consumate plus manoperă (timp lucrat × cost pe oră al centrului de lucru).
- Stornare la 1 a lunii următoare: asistentul standard `mrp.account.wip.accounting` propune data + 1 zi, iar modulul fixează data corectă pentru companiile cu țara RO.
- Proces-Verbal de evaluare în PDF, cu semnături Director Economic / Contabil Șef / Responsabil Producție (OMFP 2861/2009).
- Închidere automată opțională în ultima zi a lunii (acțiune planificată instalată inactivă; compania se marchează din **Contabilitate → Configurare → Setări**, secțiunea „Închidere WIP (OMFP 1802)").
- Evaluările se creează din **Contabilitate → Închidere → WIP Producție în Curs (OMFP 1802)**; jurnalul este de tip Diverse, iar conturile 331 și 711 se caută automat după prefix.
- Câmpul `l10n_ro_wip_closing_date` de pe companie se actualizează la fiecare WIP postat, pentru checklistul de închidere lunară.
- Fluxul detaliat pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `mrp_account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.wip.closing`: Evaluarea WIP lunară, cu audit trail (`mail.thread`), legături către nota WIP și storno.
- `l10n.ro.wip.closing.line`: Detaliul pe ordin de fabricație (componente, manoperă, total).
- `mrp.account.wip.accounting`: Asistent standard, extins pentru data stornării.
- `res.company` și `res.config.settings`: Setările de închidere automată, jurnalul WIP și data ultimei închideri.

**Vizualizări**

- `view_l10n_ro_wip_closing_list`, `view_l10n_ro_wip_closing_form`: lista și formularul evaluărilor.
- `res_config_settings_view_form_wip`: setările de închidere WIP.
- `action_report_wip_closing`: raportul PDF Proces-Verbal de evaluare.

**Acțiuni Automate / Acțiuni Server**

- `cron_l10n_ro_wip_auto_close`: acțiune planificată zilnică, inactivă implicit, care postează WIP-ul în ultima zi a lunii pentru companiile cu închidere automată.

#### 5. Conexiuni

- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): checklistul de închidere lunară folosește data ultimei închideri WIP.
