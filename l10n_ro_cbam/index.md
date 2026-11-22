# Romania - CBAM (FR-56) (localizat la `l10n_ro_cbam/index.md`)

- **Nume Tehnic:** `l10n_ro_cbam`
- **Versiune:** `19.0.1.7.9`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_cbam
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_cbam`
- **Ultima Ingestie:** `2026-11-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru Carbon Border Adjustment Mechanism (CBAM), conform Regulamentului (UE) 2023/956. Sprijină importatorii români care introduc pe piața UE produse din categoriile vizate (oțel și fier, aluminiu, ciment, îngrășăminte, electricitate, hidrogen) să declare emisiile de CO₂ incorporate și, din regimul definitiv (1 ianuarie 2026), să determine certificatele CBAM necesare. Este construit peste modulul `esg` (Enterprise), reutilizând `esg.emission.factor` și `esg.emission.source` în loc să le dubleze, și peste `account_intrastat` pentru codul CN.

#### 2. Funcționalități Cheie

- **Profil produs CBAM** (tab-ul **CBAM** pe produs): bifa **Supus CBAM**, categorie derivată automat din codul CN (Intrastat), factor de conversie în tone (implicit 0,001 pentru kg), factor de emisie din nomenclator sau **Override factor emisie** verificat per instalație, țară de origine (dacă lipsește, se folosește țara furnizorului) și preț carbon plătit în origine; reducerea se aplică doar dacă bifa **Preț carbon certificat** este activă.
- **Nomenclator factori de emisie** (**ESG → CBAM → Factori emisie CBAM**): extindere `esg.emission.factor` cu factori impliciți conform Reg. delegat (UE) 2024/3212; sursă ESG dedicată „Importuri CBAM” în Scope 3 (Category 1: Purchased goods).
- **Captură automată la import:** la postarea facturii de la furnizor din afara UE se generează linii CBAM (`l10n.ro.cbam.import.line`, **ESG → CBAM → Linii import CBAM**) cu cantitatea în tone, emisiile incorporate, prețul certificatului aplicabil, emisiile acoperite de carbonul certificat, emisiile nete și costul certificatelor; buton **Linii CBAM** pe factură; retururile compensează cu semn negativ. Nu generează linii facturile de la furnizori din UE și nici bunurile de origine UE sau din țările din anexa III (Norvegia, Islanda, Liechtenstein, Elveția) — excepția urmează originea bunului, nu furnizorul. Un produs CBAM fără factor de emisie blochează postarea; la revenirea în ciornă, liniile neincluse într-o declarație depusă se șterg.
- **Declarație CBAM** (**ESG → CBAM → Declarații CBAM**): de tip **Tranziție** (trimestrială, octombrie 2023 – decembrie 2025) sau **Definitiv** (anuală, din 2026); butonul **Calculează** atașează liniile din perioadă și calculează totalul emisiilor, costul carbonului din origine, certificatele necesare (emisii nete), costul certificatelor, minimul de deținut, termenul (30 septembrie anul următor) și deficitul față de certificatele deținute/restituite. Stări: Ciornă → Depusă → Acceptată; la **Depusă** declarația se îngheață (liniile și facturile aferente nu se mai modifică).
- **Prețuri de referință ale certificatelor** (**ESG → CBAM → Prețuri certificate CBAM**, `l10n.ro.cbam.certificate.price`): nomenclator introdus manual pe măsură ce Comisia Europeană publică mediile (trimestriale pentru 2026, săptămânale din 2027); fiecare linie folosește prețul perioadei sale, apoi prețul de pe declarație, apoi prețul de rezervă al companiei.
- **Verificare trimestrială de deținere** (regula 50%, din 2027): declarație definitivă cu trimestru completat funcționează ca checkpoint de deținere (minim 50% din certificatele trimestrului; pentru 2026 minimul este 0), distinct de declarația anuală de predare, fără notă contabilă.
- **Generare notă contabilă** pentru obligația de certificate (**Generează notă certificate**, o singură dată, doar pe declarația anuală), cu jurnal și conturi configurabile în setări (implicit cheltuială 652 și obligație 462).
- **Export XML** pentru Registrul CBAM (**Export XML Registru CBAM**; necesită codul EORI din setări) și **raport PDF** „Situație CBAM”.
- **Analiză CBAM** (**ESG → CBAM → Analiză CBAM**): vizualizări grafic/pivot pe emisii, grupate pe lună, categorie și țară de origine.
- **Setări** (**Contabilitate → Configurare → Setări**, secțiunea **CBAM**): cod EORI, preț certificat implicit, jurnal note CBAM, cont obligație și cont cheltuieli.

#### 3. Dependențe

- `esg`
- `account`
- `account_intrastat`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.cbam.import.line`: liniile CBAM generate la postarea facturii de import, cu cantitate în tone, emisii incorporate, deducerea prețului carbonului din origine și sumele pe certificate; se blochează la depunerea declarației.
- `l10n.ro.cbam.declaration`: declarația CBAM (tranziție trimestrială sau definitivă anuală/checkpoint trimestrial), cu agregarea liniilor, calculul certificatelor necesare/deținute, termenului și deficitului, generarea notei contabile și exportul XML.
- `l10n.ro.cbam.certificate.price`: nomenclatorul prețurilor de referință ale certificatelor CBAM (an, trimestru sau săptămână), publicate periodic de Comisia Europeană.
- `esg.emission.factor` (extins): câmpuri CBAM (`cbam_liable`, `cbam_category`, `cbam_cn_code_pattern`, `cbam_default_factor_t`) pentru factorii impliciți din Reg. delegat (UE) 2024/3212.
- `product.template` (extins): profilul produs CBAM — `cbam_liable`, categorie derivată din codul CN, factor de emisie efectiv/override, țară de origine, preț carbon plătit în origine și indicator de certificare.
- `account.move` (extins): captura liniilor CBAM la postarea facturii de furnizor din afara UE, protecția facturilor incluse într-o declarație depusă și butonul spre liniile generate.
- `res.company` / `res.config.settings` (extinse): setările CBAM (cod EORI, preț certificat implicit, jurnal și conturi pentru nota de certificate).

**Vizualizări**

- `views/l10n_ro_cbam_declaration_views.xml`, `views/l10n_ro_cbam_import_line_views.xml`: formularele și listele pentru declarații și liniile de import.
- `views/l10n_ro_cbam_certificate_price_views.xml`: nomenclatorul prețurilor de referință.
- `views/product_template_views.xml`: tab-ul CBAM pe fișa produsului.
- `views/esg_emission_factor_views.xml`: câmpurile CBAM pe nomenclatorul de factori de emisie ESG.
- `views/account_move_views.xml`: butonul „Linii CBAM” pe factură.
- `views/res_config_settings_views.xml`: secțiunea CBAM din setările de contabilitate.
- `views/l10n_ro_cbam_menus.xml`: meniurile ESG → CBAM (Declarații, Linii import, Analiză, Factori emisie, Prețuri certificate).
- `data/cbam_country_group_data.xml`, `data/cbam_emission_source_data.xml`, `data/cbam_emission_factor_data.xml`: grupul de țări, sursa ESG dedicată și factorii de emisie impliciți.
- `report/cbam_declaration_report.xml`, `report/cbam_declaration_templates.xml`: raportul PDF „Situație CBAM”.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: la instalare derivă categoria CBAM (din codul CN/Intrastat) pentru produsele existente care au deja cod Intrastat.
- Nu există cron-uri sau reguli `base.automation`.

#### 5. Conexiuni

- [l10n_ro_environmental_tax](../l10n_ro_environmental_tax/index.md): ambele module tratează obligații de mediu specifice pieței românești, deși nu au dependență directă de cod.
- [l10n_ro_excise_duty](../l10n_ro_excise_duty/index.md): modul conex de fiscalitate specială la import/producție, din aceeași familie de localizare română enterprise.
