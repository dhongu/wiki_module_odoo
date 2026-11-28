# Romania - Declarația 307 (ajustări de TVA) (localizat la `l10n_ro_anaf_d307/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d307`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d307
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d307`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite completarea și exportul în XML al Declarației 307, prin care persoana impozabilă declară sumele rezultate din ajustarea, corecția ajustărilor sau regularizarea taxei pe valoarea adăugată. Scutește contabilul de formularul manual de pe portalul ANAF și produce un fișier care trece validarea oficială.

#### 2. Funcționalități Cheie

- Trei situații ale formularului: transfer de active (A), transfer al proprietății asupra activelor în leasing (L) și anularea codului de TVA (C).
- Operațiuni declarate individual, cu operatorul (cedent, finanțator sau beneficiar) preluat de pe partener și TVA-ul aferent, care poate fi negativ.
- Totaluri pe cele trei tipuri și suma de control, calculate automat după regulile ANAF.
- Temei legal al corectării (art. 105 alin. (6) lit. a/b din Legea 207/2015), cerut când declarația se depune după anularea rezervei verificării ulterioare.
- Gărzi de corelație: același operator nu poate apărea de două ori pe același tip de operațiune.
- Acces din Contabilitate → Raportare → Declarații ANAF → D307 Ajustări de TVA; flux Confirmă → Exportă XML.
- Formular acceptat: OPANAF 793/2016 (structura din 07.11.2017), schema `d307_20171205.xsd`; verificat cu DUKIntegrator la 12.09.2026.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d307`: declarația (perioadă, antet, totaluri, stări, export XML); folosește `mail.thread`, `mail.activity.mixin` și mixin-ul de handler de raport ANAF.
- `l10n.ro.anaf.d307.line`: operațiunea declarată (tip, operator, cod fiscal, denumire, TVA).

**Vizualizări**

- `view_l10n_ro_anaf_d307_list` / `view_l10n_ro_anaf_d307_form`: lista și formularul declarației.
- `action_l10n_ro_anaf_d307` și `menu_l10n_ro_anaf_d307`: acțiunea și meniul din Declarații ANAF.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`) sau acțiuni server; exportul XML se declanșează manual din formularul declarației.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună de declarații ANAF (mixin-ul de export XML, semnare, depunere).
- [l10n_ro_anaf_duk](../l10n_ro_anaf_duk/index.md): validarea fișierelor XML cu validatorul oficial ANAF (DUKIntegrator).
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): depunerea declarațiilor la ANAF.
