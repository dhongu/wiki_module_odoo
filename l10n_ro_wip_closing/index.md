# Romania - Producție în curs (331/711) OMFP 1802 (localizat la `l10n_ro_wip_closing/index.md`)

- **Nume Tehnic:** `l10n_ro_wip_closing`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_wip_closing
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_wip_closing
- **Ultima Ingestie:** `2026-10-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează evaluarea și stornarea în roșu a producției în curs de execuție (WIP) conform OMFP 1802/2014 pct. 302–305, pentru companiile cu activitate de producție. Lunar, calculează valoarea ordinelor de fabricație neterminate, postează nota `Dr 331 = Cr 711` și, la 1 a lunii următoare, stornarea ei în roșu; corectează astfel comportamentul nativ Odoo, care stornează la data + 1 zi. Produce și un Proces-Verbal de Evaluare în PDF. Operațiunea mișcă doar conturile 331 și 711 și nu intră în D300 sau D394.

#### 2. Funcționalități Cheie

- **Evaluare WIP persistentă:** **Contabilitate → Închidere → WIP Producție în Curs (OMFP 1802)**, cu stări Ciornă → Postată → Anulată și audit trail; data stornării (1 a lunii următoare) se calculează automat și nu se modifică.
- **Calcul automat din ordinele de fabricație** confirmate, în producție sau de finalizat: valoarea componentelor (cantitatea consumată × prețul standard, sau prețul lotului la valorizare pe lot) plus manopera (operațiile finalizate până la data evaluării, la costul pe oră al centrului de lucru; fără cost pe oră, manopera este zero, fără eroare). Un ordin fără componente preluate are valoare zero și nu apare în tabel.
- **Nota WIP și storno:** „Postează" generează `331 Producție în curs = 711 Variația stocurilor` la data evaluării și, în același pas, stornarea în roșu la 1 a lunii următoare, cu valori negative (nu o notă inversă).
- **Corectarea datei de stornare** în wizardul nativ `mrp.account.wip.accounting` pentru companiile cu țara România.
- **PV PDF:** Procesul-Verbal de Evaluare cu semnături Director Economic / Contabil Șef, conform OMFP 2861/2009, din butonul „PV PDF".
- **Anulare:** „Anulează" anulează ambele note, dacă sunt postate; dacă storno-ul este în luna curentă și reflectat în balanță, anularea îi elimină efectul din balanța lunii.
- **Configurare:** în **Contabilitate → Configurare → Setări**, secțiunea „Închidere WIP (OMFP 1802)": jurnalul WIP (de tip Diverse) și închiderea automată; conturile 331 și 711 se caută automat prin prefix, iar la lipsa lor postarea eșuează.
- **Cron opțional**, inactiv implicit, care rulează zilnic și postează WIP-ul în ultima zi a lunii dacă închiderea automată este activată; rularea manuală oferă control complet.
- **Integrare cu închiderea de perioadă:** la fiecare WIP postat se actualizează data ultimei închideri WIP pe companie, folosită de `l10n_ro_period_close_enhanced`.

#### 3. Dependențe

- `mrp_account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.wip.closing`: evaluarea WIP, cu stări, nota WIP și storno-ul generate, raportul PV (are chatter).
- `l10n.ro.wip.closing.line`: linia per ordin de fabricație, cu valoarea componentelor, manopera și total WIP.
- `mrp.account.wip.accounting` (extins): corectează data de stornare pe companiile din România.
- `res.company` (extins): `l10n_ro_wip_closing_date`, data ultimei închideri WIP.
- `res.config.settings` (extins): jurnalul WIP și opțiunea de închidere automată.

**Vizualizări**

- `view_l10n_ro_wip_closing_list` / `view_l10n_ro_wip_closing_form`: lista și formularul evaluărilor WIP (meniu `menu_l10n_ro_wip_closing`).
- `res_config_settings_view_form_wip`: secțiunea „Închidere WIP (OMFP 1802)" din setări.
- `action_report_wip_closing`: raportul PDF Proces-Verbal de Evaluare.

**Acțiuni Automate / Acțiuni Server**

- `cron_l10n_ro_wip_auto_close` („Automatic WIP Closing — Last Day of Month (OMFP 1802)"): rulează zilnic și postează evaluarea în ultima zi a lunii; inactiv implicit.

#### 5. Conexiuni

- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): checklistul de închidere lunară folosește data ultimei închideri WIP pentru verificarea automată.
