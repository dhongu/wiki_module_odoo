# Romania - Declarație rectificativă (D710) (localizat la `l10n_ro_anaf_d710/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d710`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d710
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d710`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite întocmirea Declarației 710, prin care se rectifică obligațiile de plată declarate la bugetul de stat (de regulă prin D100, dar și prin D112 sau alte declarații care declară creanțe fiscale). Pentru fiecare obligație se raportează atât suma inițială, cât și cea corectată, iar ANAF operează diferența. Declarația se exportă în format XML, validat cu schema oficială ANAF, gata de depus.

#### 2. Funcționalități Cheie

- Declarație cu linii de obligații, fiecare cu perechea inițial/corectat pentru suma datorată, deduceri, plăți și rest (plus sponsorizări, reduceri de impozit, bifa impozit minim pe cifra de afaceri și cota).
- Bife în antetul formularului: anulare, succesor (cu CIF-ul succesorului), dizolvare, sector energie, modificare, precum și temeiul rectificării (1 — corectarea sumelor declarate; 2 — corecție în urma unui control fiscal).
- Perioada de raportare (lună/an) și numele persoanei care semnează declarația (preluat din contactul companiei dacă nu este completat manual).
- Numărul de evidență (`nr_evid`) al fiecărei obligații se calculează automat (23 de cifre, conform regulii din structura oficială: cod obligație, perioadă, scadență, sumă de control); poate fi suprascris dacă ANAF a emis alt număr pe recipisa depunerii inițiale.
- Flux cu stări (ciornă / confirmată, cu revenire în ciornă) și istoric în chatter.
- Export XML validat cu schema oficială `d710_20012025.xsd`, cu gărzi de corelație înainte de export: declarație fără nicio linie, succesor fără CIF (sau CIF de succesor fără bifa de succesor), lipsa numelui semnatarului, obligație fără număr de evidență.
- Acces din meniul declarațiilor ANAF (D710 Rectifying Statement), pentru utilizatorii cu drepturi de contabil.
- Fluxul pas-cu-pas pentru consultant este detaliat în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d710`: declarația rectificativă (antet, perioadă, bife, temei, semnatar, stare, fișier XML generat, sumă de control); extinde `mail.thread`, `mail.activity.mixin` și `l10n_ro_anaf.report.handler.mixin`.
- `l10n.ro.anaf.d710.line`: linia de obligație (cod obligație, cod bugetar, scadență, `nr_evid`, sume inițiale/corectate pentru datorat, deduceri, plăți, rest, sponsorizări, reduceri).

**Vizualizări**

- `view_l10n_ro_anaf_d710_list`: lista declarațiilor D710.
- `view_l10n_ro_anaf_d710_form`: formularul declarației, cu antet, linii de obligații și acțiuni de confirmare/export.

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_anaf_d710`: acțiune de fereastră (listă/formular) accesată din meniul `menu_l10n_ro_anaf_d710`. Modulul nu definește acțiuni automate sau cron.

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): oferă meniul declarațiilor ANAF, mixin-ul de export și registrul de profiluri XSD în care D710 se înregistrează (verificat în cod).
