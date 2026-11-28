# Romania - Declarația 311 (TVA la cod anulat) (localizat la `l10n_ro_anaf_d311/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d311`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d311
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d311`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite completarea și exportul în XML al Declarației 311, prin care se declară taxa pe valoarea adăugată colectată de persoanele al căror cod de TVA a fost anulat sau care s-au reînregistrat ulterior. Reduce riscul de respingere la ANAF prin calculul automat al totalurilor și prin verificările de corelație.

#### 2. Funcționalități Cheie

- Alegerea situației (care se exclud reciproc): persoana cu codul anulat (secțiunea IV) sau persoana reînregistrată conform art. 316 alin. (12) (secțiunea V); se deschid doar rubricile secțiunii alese.
- Secțiunea IV: livrări (rd. 01), achiziții cu taxare inversă (rd. 02) și livrări dinainte de anulare exigibile în sistemul TVA la încasare (rd. 04), cu subtotaluri calculate (rd. 03 = 01 + 02, rd. 05 = 03 + 04).
- Temeiul anulării (din oficiu sau la cerere) redat prin perechea complementară de bife cerută de validator.
- Temei legal al corectării, când declarația se depune după anularea rezervei verificării ulterioare.
- Gărzi pentru regulile de corelație verificate de ANAF; exportul se oprește înainte de a produce un fișier respins.
- Acces din Contabilitate → Raportare → Declarații ANAF → D311 TVA după anularea codului; flux Confirmă → Exportă XML. Modulul nu produce note contabile.
- Formular acceptat: structura din 29.01.2021, schema `d311_20210129.xsd`; verificat cu DUKIntegrator la 12.09.2026.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d311`: declarația (perioadă, situație, secțiunile IV și V, totaluri, stări, export XML); folosește `mail.thread`, `mail.activity.mixin` și mixin-ul de handler de raport ANAF.

**Vizualizări**

- `view_l10n_ro_anaf_d311_list` / `view_l10n_ro_anaf_d311_form`: lista și formularul declarației.
- `action_l10n_ro_anaf_d311` și `menu_l10n_ro_anaf_d311`: acțiunea și meniul din Declarații ANAF.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`) sau acțiuni server; exportul XML se declanșează manual din formularul declarației.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună de declarații ANAF (mixin-ul de export XML, semnare, depunere).
- [l10n_ro_anaf_duk](../l10n_ro_anaf_duk/index.md): validarea fișierelor XML cu validatorul oficial ANAF (DUKIntegrator).
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): depunerea declarațiilor la ANAF.
