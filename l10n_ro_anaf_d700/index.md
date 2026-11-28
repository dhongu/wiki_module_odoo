# Romania - Declarație vector fiscal (D700) (localizat la `l10n_ro_anaf_d700/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d700`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d700
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d700`
- **Ultima Ingestie:** 2026-11-28

#### 1. Sumar

Modulul permite completarea și exportul în XML al Declarației 700, prin care se înregistrează sau se modifică, în mediu electronic, categoriile de obligații fiscale declarative din vectorul fiscal. Se folosește la fiecare schimbare de regim: intrarea sau ieșirea din sistemul de TVA, trecerea de la lunar la trimestrial, adăugarea ori radierea unei obligații declarative.

#### 2. Funcționalități Cheie

- Antet complet: perioada solicitării, declarantul și identificarea contribuabilului.
- Secțiunile D, E și F: obligațiile din vectorul fiscal, cu nomenclatorul fiecărei secțiuni, periodicitatea (numai la D) și datele de adăugare sau radiere; limite de apariții (4 la D, 6 la E, 12 la F), coduri unice în secțiune, data de început și cea de sfârșit se exclud.
- Secțiunea B: bifele de subsecțiune pentru înregistrarea în scopuri de TVA (B.I, B.II, B.VII, B.VIII), schimbarea perioadei fiscale și TVA la încasare.
- Nu acoperă sediile secundare, datele contabilului, codurile CAEN, reprezentantul fiscal, stările 61/62 și subsecțiunile B rare; pentru acestea se folosește formularul de pe portalul ANAF.
- Acces din Contabilitate → Raportare → Declarații ANAF; flux Confirmă → Exportă XML.
- Formular acceptat: OPANAF 15/09.01.2026; ANAF nu publică XSD pentru D700, deci structura urmează documentația oficială, verificată cu DUKIntegrator la 12.09.2026.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d700`: declarația (antet, bifele secțiunii B, stări, export XML); folosește `mail.thread`, `mail.activity.mixin` și mixin-ul de handler de raport ANAF.
- `l10n.ro.anaf.d700.line`: obligația din vectorul fiscal (secțiunile D, E, F).

**Vizualizări**

- `view_l10n_ro_anaf_d700_list` / `view_l10n_ro_anaf_d700_form`: lista și formularul declarației.
- `action_l10n_ro_anaf_d700` și `menu_l10n_ro_anaf_d700`: acțiunea și meniul din Declarații ANAF.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`) sau acțiuni server; exportul XML se declanșează manual din formularul declarației.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună de declarații ANAF (mixin-ul de export XML, semnare, depunere).
- [l10n_ro_anaf_duk](../l10n_ro_anaf_duk/index.md): validarea fișierelor XML cu validatorul oficial ANAF (DUKIntegrator).
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): depunerea declarațiilor la ANAF.
