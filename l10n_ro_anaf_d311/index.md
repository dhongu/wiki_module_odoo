# Romania - Declarația 311 (TVA la cod anulat) (localizat la `l10n_ro_anaf_d311/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d311`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d311
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d311`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite întocmirea Declarației 311 — taxa pe valoarea adăugată colectată, datorată de persoanele impozabile al căror cod de TVA a fost anulat conform art. 316 alin. (11) lit. a)–e), g) sau h) din Codul fiscal — și exportul ei în format XML pentru depunere la ANAF. Formularul urmează structura publicată la 29.01.2021 (schema `d311_20210129.xsd`, validator J2.0.0), iar rubricile, totalurile și regulile de corelație sunt controlate înainte de export.

#### 2. Funcționalități Cheie

- Două situații de depunere care se exclud reciproc, alese în câmpul „Filed As":
  - persoana cu codul anulat — secțiunea IV: livrări, achiziții cu taxare inversă și livrări dinainte de anulare exigibile în sistemul TVA la încasare;
  - persoana reînregistrată conform art. 316 alin. (12) — secțiunea V: operațiuni din perioada anulării pentru care taxa nu a fost colectată atunci.
- Alegerea situației deschide doar rubricile secțiunii corespunzătoare.
- Subtotaluri și total calculate după formulele formularului (rd. 03 = 01 + 02, rd. 05 = 03 + 04), plus suma de control peste ambele secțiuni; sumele sunt valori întregi, nenegative.
- Temeiul anulării redat prin perechea complementară de bife cerută de validator; date specifice: data anulării, data reînregistrării, CUI succesor.
- Declarație inițială sau rectificativă (depusă integral, cu toate sumele corectate) și indicator de depunere după anularea rezervei verificării ulterioare, cu temei legal obligatoriu.
- Date semnatar (nume, funcție) pentru antetul XML.
- Fluxul în două stări (Ciornă / Confirmată), cu reset la ciornă și export XML validat după regulile de corelație verificate de ANAF.
- Acces din meniul declarațiilor ANAF („D311 VAT After Code Cancellation"), pentru utilizatorii cu drepturi de contabil.
- Fluxul detaliat pas-cu-pas, cu capturi de ecran, este în [Fișa Consultant](FISA_CONSULTANT.md).

Notă: validatorul oficial acceptă valori negative pentru atributele OB_nn (din J1.0.1), dar structura publicată și XSD-ul cer `>= 0`; modulul păstrează restricția din documentație, mai strictă decât validatorul.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d311`: declarația D311 (perioadă lună/an, situația de depunere, date anulare/reînregistrare, rubricile OB_nn, totaluri calculate, suma de control, fișier XML generat). Extinde `mail.thread`, `mail.activity.mixin` și `l10n_ro_anaf.report.handler.mixin`.

**Vizualizări**

- `view_l10n_ro_anaf_d311_list`: lista declarațiilor D311.
- `view_l10n_ro_anaf_d311_form`: formularul declarației, cu antet și secțiunile IV / V.
- `action_l10n_ro_anaf_d311` și `menu_l10n_ro_anaf_d311`: acțiunea și meniul din declarațiile ANAF.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau server. Butoanele modelului: `action_confirm`, `action_reset_draft`, `action_export_xml`.

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): oferă meniul declarațiilor ANAF și mixin-ul comun de export.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): decontul de TVA, declarație conexă.
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): declarația informativă privind livrările/achizițiile pe teritoriul național, conexă ca domeniu (TVA).
