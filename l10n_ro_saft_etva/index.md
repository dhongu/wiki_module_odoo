# Romania - Reconciliere e-TVA (decont precompletat ANAF) (localizat la `l10n_ro_saft_etva/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_etva`
- **Versiune:** `19.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_saft_etva
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_etva`
- **Ultima Ingestie:** `2026-11-23`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul reconciliază automat **decontul precompletat RO e-TVA** (OUG 70/2024) cu Decontul de TVA (D300) calculat intern în Odoo. ANAF generează lunar un decont de TVA pre-completat din datele e-Factura, e-Transport, SAF-T și caselor de marcat, transmis prin SPV. Modulul importă fișierul XML primit, îl compară rând cu rând cu D300-ul intern și evidențiază diferențele înainte de depunere, gradate pe severitate (informativ / avertisment / eroare critică). Diferențele critice nejustificate blochează închiderea verificării e-TVA din checklistul de închidere a perioadei de TVA, astfel încât discrepanțele să fie explicate înainte de transmiterea D300. Modulul nu modifică contabilitatea; este un instrument de control.

#### 2. Funcționalități Cheie

- **Import manual** al fișierului XML „Decont precompletat de TVA" (RO e-TVA) descărcat din SPV, din **Contabilitate → Raportare → e-TVA → Reconciliere decont precompletat**: se alege perioada (de la / până la), se încarcă XML-ul și se apasă **Importă fișierul**. Modulul nu se conectează la ANAF pentru preluare automată.
- **Reconciliere automată rând cu rând** (buton **Reconciliază cu D300**) a decontului ANAF față de D300-ul intern calculat de `l10n_ro_anaf_d300` pe aceeași perioadă, nu doar pe total; rândurile apar cu numărul din formularul D300 în vigoare (ex. total taxă colectată = rd. 19, chiar dacă în XML atributul este `R17_2`), inclusiv subrândurile (3.1, 5.1, 12.1, 20.1 etc.).
- **Severitate pe fiecare rând**, cu baza/TVA ANAF, baza/TVA internă și diferența: *Coincide* (fără diferență sau sub 1 leu, din rotunjire, fiindcă D300 se depune în lei întregi), *Avertisment* (cel puțin 1 leu, sub praguri), *Eroare critică* (peste ambele praguri).
- **Praguri configurabile pe companie** (**Contabilitate → Configurare → Setări**, secțiunea declarațiilor ANAF): prag valoric (implicit 1.000 RON) și prag procentual (implicit 20%); o diferență devine eroare critică doar dacă le depășește pe amândouă. Utilizatorul are nevoie de grupul **Contabilitate / Contabil** și de date de TVA postate în perioadă.
- **Justificare obligatorie** pe fiecare linie cu eroare critică; după justificarea tuturor se apasă **Marchează justificat**, apoi **Închide** (starea „Închis"). Un banner avertizează cât timp depunerea D300 este blocată.
- **Verificare blocantă în checklistul return-ului de TVA** (D300), numită „Reconciliere e-TVA", care creează sau deschide automat reconcilierea perioadei și rămâne blocată cât timp există erori critice nejustificate.
- **Raport de reconciliere** cu export PDF.
- **Limite**: nu generează și nu transmite D300 (rămâne în `l10n_ro_anaf_d300`) și nu acoperă pre-validarea SAF-T D406 (tratată de `l10n_ro_saft_validator`). Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `account`
- `mail`
- `l10n_ro`
- `l10n_ro_reports`
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md)

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, această secțiune a fost omisă: Readme-ul descrie scopul de business și funcționalitățile, dar nu solicită explicit detalierea componentelor tehnice (modele, vizualizări, acțiuni automate). Analiza suplimentară a codului nu a fost efectuată, conform fluxului de ingestie din schemă.

#### 5. Conexiuni

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): sursa valorilor D300 interne (rânduri R1..R44) cu care se face reconcilierea; valorile nu sunt recalculate în acest modul.
- `l10n_ro_reports`: furnizează tipul de return TVA (`account.return`) pe care se adaugă verificarea blocantă e-TVA în checklistul de închidere a perioadei.
- [l10n_ro_saft_validator](../l10n_ro_saft_validator/index.md): acoperă separat pre-validarea SAF-T D406, care nu face parte din acest modul.
- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md): folosit (import defensiv) pentru generarea automată a capturilor de ecran din fișa consultant.
