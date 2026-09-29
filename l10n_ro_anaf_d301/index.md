# Romania - Decont special de TVA (D301) (localizat la `l10n_ro_anaf_d301/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d301`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d301
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d301`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul construiește **decontul special de TVA (formularul 301)**, depus de persoanele care nu sunt înregistrate normal în scopuri de TVA, dar datorează totuși taxa, cel mai frecvent pentru achiziții intracomunitare de bunuri sau servicii. Contabilul introduce operațiunile una câte una, iar modulul le agregă pe secțiunile formularului, calculează valorile de control și exportă fișierul XML acceptat de ANAF.

#### 2. Funcționalități Cheie

- Operațiuni declarate individual, cu documentul, data și, la achizițiile în valută, suma în valută, valuta și cursul (coloanele de valută sunt ascunse implicit în listă); suma intră automat în secțiunea dată de tipul operațiunii.
- Cele cinci secțiuni ale decontului, cu baze și TVA agregate: S1 (achiziții intracomunitare de bunuri), S2 (mijloace de transport noi), S3 (produse accizabile), S4 (operațiuni art. 307 Cod fiscal) și S4.1 (servicii intracomunitare cu TVA în sarcina beneficiarului).
- Suma de control și numărul de evidență a plății, calculate după regulile ANAF (numărul nu se copiază de pe recipisă); termenul de depunere este data de 25 a lunii următoare.
- Antet cu perioada (lună și an), tipul declarantului, opțiunea „Numai mijloace de transport", temeiul legal, banca și contul (obligatorii în schema ANAF) și semnatarul.
- Reguli de corelare verificate ca în validatorul ANAF: temeiul art. 105 alin. (6) lit. a) se poate invoca numai pe o rectificativă, iar declarația pentru mijloace de transport noi trebuie să conțină cel puțin o operațiune din S2.
- Flux cu stări ciornă/confirmată: **Confirmă**, **Exportă XML**, **Resetează la ciornă**; validare față de schema oficială `d301_20200130.xsd`.
- Meniu: Contabilitate → Raportare → Declarații ANAF → Decont special de TVA (D301), vizibil pentru grupul Contabil.
- Modulul nu generează note contabile; declarația se construiește din datele introduse, nu din registrul contabil. Fluxul pas-cu-pas este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d301`: declarația (perioadă, tip declarant, temei, bancă, stare, totaluri); moștenește `mail.thread`, `mail.activity.mixin` și `l10n_ro_anaf.report.handler.mixin`.
- `l10n.ro.anaf.d301.line`: operațiunea declarată (tip operațiune, document, dată, bază, TVA, valută, curs).

**Vizualizări**

- `view_l10n_ro_anaf_d301_list`: lista deconturilor speciale.
- `view_l10n_ro_anaf_d301_form`: formularul declarației, cu butoanele Confirmă, Exportă XML și Resetează la ciornă.
- `action_l10n_ro_anaf_d301` și `menu_l10n_ro_anaf_d301`: acțiunea și meniul de sub Declarații ANAF.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): decontul de TVA obișnuit, depus de plătitorii înregistrați normal (D301 îl înlocuiește pentru cei neînregistrați).
