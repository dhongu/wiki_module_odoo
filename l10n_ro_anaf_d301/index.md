# Romania - Decont special de TVA (D301) (localizat la `l10n_ro_anaf_d301/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d301`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d301
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d301`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Decontul special de TVA (D301) se depune de persoanele care nu sunt înregistrate normal în scopuri de TVA, dar datorează taxa, de regulă pentru achiziții intracomunitare. Modulul agregă operațiunile introduse pe cele cinci secțiuni ale formularului, calculează suma de control și numărul de evidență a plății și exportă XML-ul acceptat de ANAF.

#### 2. Funcționalități Cheie

- Operațiuni declarate individual (document, dată, valută și curs); tipul operațiunii decide secțiunea: S1 achiziții intracomunitare de bunuri, S2 mijloace de transport noi, S3 produse accizabile, S4 operațiuni art. 307, S4.1 servicii intracomunitare.
- Totaluri pe secțiuni (bază și TVA), suma de control și numărul de evidență a plății calculate după regulile ANAF.
- Reguli de corelare ANAF: temeiul art. 105 alin. (6) lit. a) numai pe rectificativă; bifa pentru mijloace de transport noi cere cel puțin o operațiune S2.
- Export XML validat cu schema oficială; exportul e blocat pentru companie fără CUI, bancă sau cont necompletat, declarație fără operațiuni, sumă în valută fără curs.
- Meniu: *Contabilitate → Raportare → Declarații ANAF → Decont special de TVA (D301)*; la configurare se verifică datele companiei, banca și contul, tipul declarantului și semnatarul.
- Nu generează note contabile, iar operațiunile se introduc manual, nu se preiau din facturi.
- Versiune formular: OPANAF 591/2016, structura v0 (`d301_20200130.xsd`), verificată cu DUKIntegrator la 12.09.2026.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d301`: decontul special (perioadă, totaluri, suma de control), cu `mail.thread`, activități și mixinul de export.
- `l10n.ro.anaf.d301.line`: operațiunea declarată, cu tip, document, sume și valută.

**Vizualizări**

- `view_l10n_ro_anaf_d301_list` și `view_l10n_ro_anaf_d301_form`: lista și formularul decontului.
- `action_l10n_ro_anaf_d301`: acțiunea de meniu.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): declarația recapitulativă pentru aceleași achiziții intracomunitare se întocmește separat.
