# Romania - Declarație vector fiscal (D700) (localizat la `l10n_ro_anaf_d700/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d700`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d700
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d700`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul permite pregătirea Declarației 700 — înregistrarea sau modificarea, în mediu electronic, a categoriilor de obligații fiscale declarative înscrise în vectorul fiscal al contribuabilului. Declarația se depune la fiecare schimbare de regim: intrarea sau ieșirea din sistemul de TVA, trecerea de la declarare lunară la trimestrială, adăugarea sau radierea unei obligații declarative. Din Odoo se completează declarația și se exportă fișierul XML pentru ANAF, fără reintroducerea datelor în formularul de pe portal.

#### 2. Funcționalități Cheie

- Antet complet: perioada solicitării, declarantul (semnatar implicit din contactul de declarații ANAF al companiei), tipul de contribuabil (`dec_inreg`) și felul declarației (modificare / radiere).
- **Secțiunile D, E și F** ale vectorului fiscal: fiecare obligație are cod din nomenclatorul secțiunii, periodicitate (doar la D: trimestrială, lunară la opțiune, lunară conform legii) și datele de la care obligația se adaugă sau se radiază (cele două date se exclud reciproc).
- Respectarea limitelor de apariții (4 la D, 6 la E, 12 la F) și a unicității codurilor în cadrul secțiunii.
- **Secțiunea B**: bifele de subsecțiune pentru înregistrarea în scopuri de TVA (B.I, B.II, B.VII, B.VIII), schimbarea perioadei fiscale (cu data schimbării) și TVA la încasare (cu data și cifra de afaceri).
- Flux cu stări (ciornă / confirmată), cu revenire la ciornă, urmărire prin chatter și activități.
- Validări la export: CUI configurat, semnatar completat, cerere din 2022 încolo, cel puțin o obligație sau o secțiune de TVA bifată.
- Export XML ANAF, atașat declarației și descărcabil; accesibil din meniul declarațiilor ANAF (`D700 Tax Vector`, pentru grupul Contabilitate / utilizator).
- **Nu acoperă** (se folosește formularul de pe portalul ANAF): sediile secundare, datele contabilului, codurile CAEN, reprezentantul fiscal, stările 61/62 și subsecțiunile B mai rare.
- Validare: ANAF nu publică XSD pentru D700, deci structura urmează documentația oficială; verificarea se face cu DUKIntegrator.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d700`: declarația D700 (antet, bife secțiunea B, linii de obligații, fișier XML generat); moștenește `mail.thread`, `mail.activity.mixin` și mixin-ul de handler ANAF din `l10n_ro_anaf_base`. Acțiuni: confirmare, resetare la ciornă, export XML.
- `l10n.ro.anaf.d700.line`: o obligație din vectorul fiscal (secțiune D/E/F, cod impozit, periodicitate, dată de la / până la, marcaj de modificare), cu constrângeri pe nomenclator și pe exclusivitatea datelor.

**Vizualizări**

- `view_l10n_ro_anaf_d700_list` / `view_l10n_ro_anaf_d700_form`: lista și formularul declarației.
- `action_l10n_ro_anaf_d700` și meniul `menu_l10n_ro_anaf_d700` (sub declarațiile ANAF, secvența 700).

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server. Securitate: manager contabilitate (acces complet), utilizator contabilitate (citire).

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): oferă meniul declarațiilor, profilul ANAF și funcțiile comune de export.
