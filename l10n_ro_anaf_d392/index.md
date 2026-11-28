# Romania - Declarație informativă anuală (D392) (localizat la `l10n_ro_anaf_d392/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d392`
- **Versiune:** `20.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d392
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d392`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul pregătește Declarația 392, informativa anuală privind livrările, prestările și achizițiile persoanelor impozabile cu cifră de afaceri sub plafon. Sumele se completează din facturile anului, iar fișierul XML rezultat trece validarea oficială ANAF.

#### 2. Funcționalități Cheie

- Două variante: 392A pentru persoanele înregistrate în scopuri de TVA (livrări cu TVA, către parteneri înregistrați și neînregistrați) și 392B pentru cele neînregistrate (în plus, blocul de achiziții).
- Buton Calculează din facturi: sumele din facturile anului, separate după prefixul `RO` al codului fiscal al partenerului; valorile rămân editabile.
- Gardă pe plafonul cifrei de afaceri (300.000 lei de la anul 2019), verificată automat la 392A; la 392B se verifică manual.
- Pe companie se completează CUI, adresă, Cod CAEN și Contact declarații (persoana care semnează).
- Acces din Contabilitate → Raportare → Declarații ANAF → D392 Informativa anuală; flux Confirmă → Exportă XML.
- Formular acceptat: OPANAF 522/26.01.2016, schema `d392.xsd`; verificat cu DUKIntegrator la 12.09.2026. Aplicarea art. 324 alin. (4)-(6) este suspendată până la 31.12.2026 (OUG 115/2023).

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d392`: declarația anuală (an, tip 392A/392B, cifra de afaceri, blocuri de livrări/achiziții, calcul din facturi, export XML); folosește `mail.thread`, `mail.activity.mixin` și mixin-ul de handler de raport ANAF.

**Vizualizări**

- `view_l10n_ro_anaf_d392_list` / `view_l10n_ro_anaf_d392_form`: lista și formularul declarației.
- `action_l10n_ro_anaf_d392` și `menu_l10n_ro_anaf_d392`: acțiunea și meniul din Declarații ANAF.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`) sau acțiuni server; exportul XML se declanșează manual din formularul declarației.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună de declarații ANAF (mixin-ul de export XML, semnare, depunere).
- [l10n_ro_anaf_duk](../l10n_ro_anaf_duk/index.md): validarea fișierelor XML cu validatorul oficial ANAF (DUKIntegrator).
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): depunerea declarațiilor la ANAF.
