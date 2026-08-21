# Romania - Partner Screening (localizat la `l10n_ro_partner_screening/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_screening`
- **Versiune:** `19.0.1.3.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_partner_screening
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_screening`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul de conformitate fiscală și AML (Anti-Money Laundering) pentru partenerii din Odoo,
adaptat cerințelor legislative românești. Ajută companiile să respecte obligațiile legale
privind paradisurile fiscale, sancțiunile internaționale și impozitul la sursă pentru
nerezidenți, marcând automat riscurile pe fișa partenerului, pe facturi și, opțional, la
postarea plăților.

#### 2. Funcționalități Cheie

- **Paradisuri fiscale (HG 1/2024):** marchează automat țările din lista jurisdicțiilor
  necooperante; câmpul „Paradis Fiscal" pe fișa partenerului, derivat automat din țară, cu
  avertisment portocaliu pe formularul partenerului și pe facturi.
- **Liste de sancțiuni OFAC și UE:** bază de date locală a entităților sancționate
  (`l10n.ro.sanction.entry`), cu import automat săptămânal din OFAC SDN List (Trezoreria SUA)
  și EU Consolidated Sanctions List (Registrul Oficial UE).
- **Screening pe fișa partenerului:** buton „Screening" cu potrivire fuzzy pe tokeni
  normalizați (fără diacritice/majuscule/formă juridică) față de listele locale; bănner roșu
  pe partener și pe factură dacă entitatea este sancționată, cu notă de sancțiune editabilă.
- **Screening automat la creare/modificare:** la salvarea partenerului (nume sau țară
  schimbate) rulează un screening „soft" care semnalează potriviri posibile
  (`l10n_ro_sanction_possible_match`) fără a confirma automat statusul — decizia rămâne a
  operatorului de conformitate; se notifică prin mesaj în chatter.
- **Impozit la Sursă (WHT):** câmpul „Impozit la Sursă (WHT)" sugerat automat pentru
  parteneri non-RO (`onchange` pe țară), cu avertisment informativ pe factură cu trimitere la
  D205/D207.
- **Blocaj opt-in la plăți (FR-08):** pe `account.payment`, la postarea unei plăți ieșite,
  poate bloca plata dacă partenerul e sancționat sau într-un paradis fiscal — activabil per
  companie din Setări (`l10n_ro_block_sanctioned_payment`, `l10n_ro_block_tax_haven_payment`);
  implicit rămâne doar bannerul informativ pe factură.
- **Status screening unificat:** câmp calculat `l10n_ro_screening_status` cu priorități
  sancționat > paradis fiscal > WHT > OK, afișat ca badge colorat în lista de parteneri și în
  header-ul formularului.
- **Acțiuni manuale de mentenanță:** din lista de sancțiuni, acțiuni server pentru
  actualizarea imediată a listelor OFAC/UE și re-screeningul tuturor partenerilor relevanți
  (companii, clienți, furnizori).

#### 3. Dependențe

- `base`
- `account`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.sanction.entry`: Stochează local entitățile sancționate (OFAC/UE/Manual), cu nume
  normalizat (index trigram) pentru potrivire pe tokeni, descărcare/parsare a listelor XML
  sursă și re-screening în masă al partenerilor.
- `res.partner` (extins): Câmpurile de tax haven, sancțiuni, WHT și statusul de screening
  calculat; `create`/`write` declanșează screening automat „soft"; buton
  `action_l10n_ro_check_sanctions` pentru verificare/confirmare manuală.
- `res.country` (extins): Marcajul de paradis fiscal conform HG 1/2024.
- `res.company` (extins): Setările per companie pentru blocarea plăților către parteneri
  sancționați sau din paradisuri fiscale.
- `res.config.settings` (extins): Câmpuri related către setările de blocaj de mai sus.
- `account.move` (extins): Avertismentele de screening (sancțiuni, paradis fiscal, WHT) pe
  facturi.
- `account.payment` (extins): Suprascrie `action_post` pentru a bloca opt-in plățile ieșite
  către parteneri cu risc de screening (FR-08).

**Vizualizări**

- `view_partner_form_l10n_ro_screening`, `view_partner_list_l10n_ro_screening`: bannere de
  avertisment și badge status screening pe fișa/lista de parteneri.
- `view_l10n_ro_sanction_entry_list`, `view_l10n_ro_sanction_entry_form`,
  `view_l10n_ro_sanction_entry_search`: gestiunea listei locale de sancțiuni, cu acțiunea
  `action_l10n_ro_sanction_entry`.
- `view_country_form_l10n_ro_screening`: câmpul de paradis fiscal pe fișa țării.
- `view_move_form_l10n_ro_screening`: bannerele de avertisment pe formularul facturii.
- `res_config_settings_view_form_partner_screening`: setările de blocaj plăți per companie.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_sanctions_refresh`: cron săptămânal (dezactivat implicit) care actualizează listele
  OFAC SDN și EU Consolidated Sanctions și re-screenează partenerii.
- `action_server_refresh_sanctions`: acțiune manuală din lista de sancțiuni — „Actualizează
  listele acum (OFAC / UE)".
- `action_server_rescreen_partners`: acțiune manuală din lista de sancțiuni — „Re-screenează
  partenerii".

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): impozitul la sursă (WHT) semnalat aici se
  raportează prin declarațiile ANAF D205/D207 din suita `l10n_ro_anaf`.
