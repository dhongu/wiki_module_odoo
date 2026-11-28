# Romania - Declarație rectificativă (D710) (localizat la `l10n_ro_anaf_d710/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d710`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d710
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d710`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite completarea și exportul în XML al Declarației 710, prin care se rectifică obligațiile de plată declarate la bugetul de stat (de regulă D100, dar și D112 sau alte declarații cu creanțe fiscale). Pentru fiecare obligație se raportează suma inițială și cea corectată, iar ANAF operează diferența.

#### 2. Funcționalități Cheie

- Linii de obligații, fiecare cu perechea inițial/corectat pentru suma datorată, deduceri, plăți, rest, reduceri și sponsorizări.
- Bifele din antet: anulare, depusă de succesor (CUI-ul succesorului devine obligatoriu), dizolvare, sector energie, modificare, plus temeiul rectificării.
- Numărul de evidență (`nr_evid`) se preia de pe recipisa depunerii inițiale și este obligatoriu pe fiecare obligație.
- Gărzi înainte de export: succesor fără CIF, obligație fără număr de evidență, declarație fără linii, sume negative.
- Acces din Contabilitate → Raportare → Declarații ANAF → D710 Declarație rectificativă; flux Confirmă → Exportă XML (cu Readu în ciornă). Nu generează note contabile.
- Formular acceptat: OPANAF 57/19.01.2026, schema `d710_20012025.xsd`; verificat cu DUKIntegrator la 12.09.2026.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d710`: declarația rectificativă (perioadă rectificată, bife de antet, stări, export XML); folosește `mail.thread`, `mail.activity.mixin` și mixin-ul de handler de raport ANAF.
- `l10n.ro.anaf.d710.line`: obligația rectificată, cu perechile inițial/corectat.

**Vizualizări**

- `view_l10n_ro_anaf_d710_list` / `view_l10n_ro_anaf_d710_form`: lista și formularul declarației.
- `action_l10n_ro_anaf_d710` și `menu_l10n_ro_anaf_d710`: acțiunea și meniul din Declarații ANAF.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`) sau acțiuni server; exportul XML se declanșează manual din formularul declarației.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună de declarații ANAF (mixin-ul de export XML, semnare, depunere).
- [l10n_ro_anaf_duk](../l10n_ro_anaf_duk/index.md): validarea fișierelor XML cu validatorul oficial ANAF (DUKIntegrator).
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): depunerea declarațiilor la ANAF.
