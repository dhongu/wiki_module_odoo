# Romania - Declarație informativă anuală (D392) (localizat la `l10n_ro_anaf_d392/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d392`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d392
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d392`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul permite pregătirea și depunerea Declarației 392 — informativa anuală privind livrările, prestările și achizițiile — pentru persoanele impozabile cu cifra de afaceri sub plafon (300.000 lei pentru anii de raportare de la 2019). Sumele se completează automat din facturile anului, iar declarația se exportă în format XML, validat cu schema oficială ANAF, gata de încărcat în SPV.

#### 2. Funcționalități Cheie

- Două variante de declarație: **392A** pentru persoanele înregistrate în scopuri de TVA (livrări cu TVA aferent, separat către parteneri înregistrați și neînregistrați) și **392B** pentru cele neînregistrate (în plus, blocul de achiziții); modelul cere exact blocurile obligatorii fiecărei variante.
- Completare automată a sumelor din facturile anului, separate după prefixul `RO` al codului fiscal al partenerului (criteriul folosit și de ANAF); valorile rămân editabile manual.
- Gardă pe plafonul cifrei de afaceri, verificat pe anul de raportare.
- Flux cu stări (ciornă / confirmat), cu revenire la ciornă; numele declarației este generat din varianta, CUI și anul fiscal.
- Semnatar al declarației: implicit contactul ANAF al companiei, dar poate fi completat manual pe declarație.
- Export XML validat cu schema oficială `d392.xsd`.
- Acces din meniul declarațiilor ANAF (**D392 Annual Informative**), pentru utilizatorii cu drepturi de contabil.
- Istoric de discuții și activități pe fiecare declarație (chatter).

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d392`: declarația 392A/392B (an fiscal, tip, sume pe blocuri, stare, semnatar); metode pentru completarea din contabilitate, confirmare, resetare la ciornă și generare/export XML. Moștenește `mail.thread`, `mail.activity.mixin` și `l10n_ro_anaf.report.handler.mixin`.

**Vizualizări**

- `view_l10n_ro_anaf_d392_list`: lista declarațiilor.
- `view_l10n_ro_anaf_d392_form`: formularul declarației, cu butoane pentru completare, confirmare și export XML.
- `action_l10n_ro_anaf_d392` / `menu_l10n_ro_anaf_d392`: acțiunea și meniul din declarațiile ANAF.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): oferă meniul declarațiilor ANAF în care este montat D392 și mixin-ul de raportare `l10n_ro_anaf.report.handler.mixin`.
