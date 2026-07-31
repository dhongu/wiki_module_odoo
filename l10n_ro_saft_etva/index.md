# Romania - Reconciliere e-TVA (Decont precompletat ANAF) (localizat la `l10n_ro_saft_etva/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_etva`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_saft_etva
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_etva`
- **Ultima Ingestie:** `2026-06-08`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul reconciliază automat **decontul precompletat RO e-TVA** (OUG 70/2024) cu Decontul de TVA (D300) calculat intern în Odoo. ANAF generează lunar un decont de TVA pre-completat din datele e-Factura, e-Transport, SAF-T și caselor de marcat, transmis prin SPV. Modulul importă fișierul XML primit, îl compară rând cu rând cu D300-ul intern și evidențiază diferențele înainte de depunere, gradate pe severitate (informativ / avertisment / eroare critică). Diferențele critice nejustificate blochează închiderea verificării e-TVA din checklistul de închidere a perioadei de TVA, astfel încât discrepanțele să fie explicate înainte de transmiterea D300.

#### 2. Funcționalități Cheie

- Import al fișierului XML „Decont precompletat de TVA" (RO e-TVA) descărcat din SPV.
- Reconciliere automată rând cu rând a decontului ANAF față de D300-ul intern calculat de modulul `l10n_ro_anaf_d300`, pe aceeași perioadă.
- Afișare pe fiecare rând a bazei/TVA ANAF, a bazei/TVA interne, a diferenței și a severității: Coincide / Avertisment / Eroare critică.
- Praguri de severitate configurabile pe companie (prag valoric, implicit 1.000 RON, și prag procentual, implicit 20%); o diferență devine eroare critică doar dacă depășește ambele praguri.
- Justificare obligatorie pe fiecare linie cu eroare critică; blocarea închiderii verificării e-TVA cât timp există erori critice nejustificate.
- Verificare blocantă integrată în checklistul return-ului de TVA (D300), accesibilă din procesul de închidere a perioadei.
- Raport de reconciliere cu export PDF.

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
- `l10n_ro_doc_screenshots`: folosit (import defensiv) pentru generarea automată a capturilor de ecran din fișa consultant.
