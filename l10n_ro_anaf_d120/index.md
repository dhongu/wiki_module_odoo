# Romania - Declarația D120 ANAF (localizat la `l10n_ro_anaf_d120/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d120`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d120
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d120`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă exportul ANAF al **Decontului privind accizele (D120)**, peste declarația de accize gestionată de modulul [l10n_ro_excise_duty](../l10n_ro_excise_duty/index.md). D120 este decontul de accize al antrepozitarilor autorizați, importatorilor, destinatarilor înregistrați și utilizatorilor industriali de produse accizabile (alcool, bere, produse energetice, tutun, energie electrică), reglementat de Codul Fiscal Titlul VIII. Modulul nu adaugă un ecran nou: pe o declarație de accize de tip D120 apar exporturile în format XML ANAF și în formularul PDF inteligent, validate față de schema oficială, astfel încât responsabilul fiscal obține fișierul de depunere fără operare manuală.

#### 2. Funcționalități Cheie

- **Declarația D120:** pe declarația de accize existentă se alege tipul **D120 — decont anual**, cu perioada anului de raportare (1 ianuarie – 31 decembrie); pentru aceeași companie, perioadă și tip poate exista o singură declarație. În XML apare cu `luna="12"`. Declarația se întocmește din **Contabilitate → Raportare → Accize → Declarații accize**.
- **Liniile declarației:** se populează automat cu **Calculează** (din facturile postate cu produse accizabile, notele de credit scad; declarația devine *Confirmată*, iar liniile existente sunt șterse) sau manual, în fila **Linii accize**. Cât timp declarația e confirmată și neexportată, se poate readuce în ciornă cu **Reset to Draft**.
- **Export XML D120 v5:** butonul **Export XML** generează fișierul `D120_<CUI>_<AAAA>12.xml`, validat față de schema XSD ANAF v5 (`d120_13052025.xsd`) înainte de descărcare, pentru import în DUKIntegrator; după export declarația trece în starea **Exportată**. Datele de identificare ale companiei (CUI, CAEN, adresă) sunt verificate la export.
- **Export XDP / formular PDF ANAF (Soft A):** butonul **Export XDP** completează formularul ANAF `D120_XML_2025_160326.pdf` cu datele declarației, după **Setări → Contabilitate → Declarații ANAF România → Tip export**: PDF cu datele incluse (implicit, de validat și semnat în Adobe Reader), arhivă ZIP cu XDP și PDF sau doar XDP. Dacă serverul nu are `pypdf` ≥ 5.0, opțiunea PDF revine la arhiva ZIP.
- **Mapare automată pe rândurile D120:** 20+ categorii de accize (B, C, D, E, A, F1–F4, G1–G7, H1–H6) sunt puse pe rândurile R0–R41 (de exemplu B → R0, A → R9, G3 → R20_1, G7 → R31, H1–H6 → R34–R39), în unitățile fiscale corespunzătoare (hl/grad Plato, hl alcool pur, tone, GJ, MWh, 1.000 bucăți, kg, ml, hl). Categoriile energetice merg pe subrândul de utilizare uzuală; pentru alte utilizări rândul se corectează în XML sau se adaugă o categorie dedicată.
- **Calcul totaluri:** subtotalurile R10, R11, R16, totalul I armonizate (R33), totalul II nearmonizate (R40) și totalul general (R41) se calculează automat din linii; `totalPlata_A` din antet este o sumă de control, întotdeauna 0.
- **Configurare necesară:** datele companiei (CUI, denumire, adresă, telefon, e-mail, cod CAEN obligatoriu), taxele de accize cu categoriile corecte (altfel sumele nu apar în D120) și unitățile de măsură fiscale ale produselor (grade Plato la bere, concentrație alcoolică la alcool).
- **Acoperire:** accize armonizate și nearmonizate (Legea 296/2023); versiune de formular acceptată OPANAF 1330/14.06.2024, verificată cu DUKIntegrator.
- **Izolare față de D103:** exportul D120 nu afectează logica declarației D103; fiecare tip folosește propriul template XML.

#### 3. Dependențe

- [l10n_ro_excise_duty](../l10n_ro_excise_duty/index.md)
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.excise.declaration`: model extins din `l10n_ro_excise_duty`, combinat cu mixinul `l10n_ro_anaf.report.handler.mixin`. Suprascrie `export_to_xml()` pentru a genera XML-ul D120 când tipul declarației este `d120` (altfel deleagă comportamentului de bază, de exemplu D103) și adaugă `action_export_d120_xdp`.

**Vizualizări**

- `view_l10n_ro_excise_declaration_form_d120`: extinde formularul declarației de accize cu butonul **Export XDP**, lângă **Export XML**.
- `views/d120_xdp_export.xml`: șablonul `d120_xdp_template` pentru exportul XDP.

**Acțiuni Automate / Acțiuni Server**

- La încărcarea modulului se înregistrează profilul de declarație ANAF D120 (`register_anaf_profile`, versiune `v5-20250513`, XSD `d120_13052025.xsd`, PDF `D120_XML_2025_160326.pdf`), folosit la export. Nu există sarcini `ir.cron`.

#### 5. Conexiuni

- [l10n_ro_excise_duty](../l10n_ro_excise_duty/index.md): furnizează declarația de accize, categoriile și cotele (modelul de bază extins de acest modul).
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună ANAF (validare date companie, profil de declarație, validare XSD).
- D103 (`cod`): decontul lunar al antrepozitului fiscal, construit pe același model de declarație de accize, dar cu alt tip și alt template XML.
