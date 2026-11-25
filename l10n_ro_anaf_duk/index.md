# Romania - DUK Integrator (prin agent local) (localizat la `l10n_ro_anaf_duk/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_duk`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_duk
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_duk`
- **Ultima Ingestie:** `2026-11-25`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul validează declarațiile ANAF cu **DUKIntegrator**, aplicația oficială Java a ANAF, fără să ruleze Java pe serverul Odoo. Spre deosebire de o simplă validare XSD, DUKIntegrator aplică regulile de business ale ANAF (sume de control, câmpuri condiționate, verificare CIF) și generează PDF-ul oficial cu XML-ul inclus. Pentru că Odoo în cloud (ex. odoo.sh) nu poate rula Java, validarea e delegată agentului Terrabit instalat pe stația contabilului — același model „cloud-safe" folosit de `l10n_ro_anaf_agent`.

#### 2. Funcționalități Cheie

- Buton **Validare DUK** pe depunerea ANAF (*Contabilitate → Raportare → Declarații ANAF → Depuneri electronice*), vizibil doar dacă depunerea are fișier XML atașat (D100, D101, D112, D300, D390, D394 sau D406): creează un job `duk_validate`, iar starea DUK devine *În așteptarea validării* până agentul întoarce rezultatul. Jobul e vizibil în *Contabilitate → Configurare → Joburi TC* (tip *Validare DUK*, cu fișierul XML și tipul declarației ca parametri).
- Rezultatul DUK nu se resetează la înlocuirea fișierului depunerii: după orice schimbare a XML-ului se apasă din nou **Validare DUK**. Butonul cere drept de creare pe joburile Terrabit Connect (rolul Contabilitate / Administrator).
- Agentul Terrabit Connect de pe stația contabilului preia jobul, rulează DUKIntegrator local (`java -jar DUKIntegrator.jar -usage p <file_type> ...`) și trimite rezultatul înapoi.
- La rezultat: dacă e **valid**, starea devine *Valid* (Status *Validat DUK*) și se atașează PDF-ul oficial (cu XML inclus) în **PDF DUK**; dacă e **invalid**, starea devine *Invalid* (Status *DUK invalid*) și erorile apar în câmpul **Erori DUK**; după corectare se atașează noul XML și se validează din nou.
- Coloana **Status** (ciclu de viață unificat) din registrul depunerilor: XML generat → validat DUK / DUK invalid → trimis la ANAF → validat ANAF; coloana **Validare DUK** arată rezultatul (*Nevalidat*, *În așteptarea validării*, *Valid*, *Invalid*).
- Gardă opțională **Necesită validare DUK înainte de depunere** (*Contabilitate → Configurare → Setări*, blocul *Depunere electronică declarație ANAF*, per companie): **Depune** e blocat, cu mesajul „Validarea DUK este obligatorie înainte de depunere…", până când validarea are rezultatul *Valid*.
- Mixin reutilizabil `l10n.ro.anaf.duk.mixin` — orice alt model poate moșteni mixin-ul, implementa `_l10n_ro_duk_xml()` și capătă automat butonul, starea, PDF-ul și erorile.
- Mapare tip declarație → tip fișier DUKIntegrator (D100, D101, D112, D300, D390, D394, D406/SAF-T), extensibilă prin suprascrierea `_l10n_ro_duk_file_type_for`.
- Configurare în Odoo: agentul Terrabit înregistrat pentru companie în *Contabilitate → Configurare → Stație ANAF* (validarea folosește stația activă a companiei), din `l10n_ro_anaf_agent`.
- Configurare pe stația contabilului: Java (JRE) + `DUKIntegrator.jar` și pachetele de validare per declarație de la ANAF, cu calea către `java` și `DUKIntegrator.jar` setată în agentul Terrabit; actualizarea pachetelor rămâne responsabilitatea agentului.
- Modulul livrează partea Odoo și contractul; rularea DUKIntegrator pe stație o face aplicația Terrabit Connect.
- Pe alte modele: un model cu `company_id` care moștenește mixin-ul și implementează `_l10n_ro_duk_xml()` capătă câmpurile și acțiunea; butonul și secțiunea „Validare DUK" se adaugă prin moștenirea view-ului.

#### 3. Dependențe

- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md)
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.duk.mixin`: mixin abstract reutilizabil — starea validării DUK (`l10n_ro_duk_state`), PDF-ul oficial, erorile și jobul asociat; modelele consumatoare suprascriu `_l10n_ro_duk_xml()`.
- `l10n.ro.anaf.submission` (extins): primul consumator natural al mixin-ului — validează XML-ul depunerii înainte de `action_submit`; adaugă câmpul calculat `l10n_ro_lifecycle` (statusul unificat draft/generated/duk_valid/duk_invalid/submitted/accepted/rejected).
- `deltatech.tc.job` (extins, din `l10n_ro_anaf_agent`): adaugă tipul de job `duk_validate` și câmpurile de back-reference (`duk_res_model`, `duk_res_id`); `_process_result()` aplică rezultatul primit de la agent înapoi pe înregistrarea sursă.
- `res.company` / `res.config.settings` (extinse): câmpul `l10n_ro_duk_required_before_submit` pentru garda de blocare a depunerii.

**Vizualizări**

- `view_l10n_ro_anaf_agent_job_form_duk`: expune detaliile jobului `duk_validate` pe formularul cozii de joburi a agentului.
- `view_l10n_ro_anaf_submission_list_duk` / `view_l10n_ro_anaf_submission_form_duk`: adaugă statusul DUK, butonul de validare și PDF-ul pe lista/formularul de depuneri ANAF.
- `res_config_settings_view_form_duk`: opțiunea *Necesită validare DUK înainte de depunere* în Setări → Contabilitate.

**Acțiuni Automate / Acțiuni Server**

- Niciuna definită direct de acest modul — procesarea rezultatului se face sincron, la revenirea jobului `duk_validate` prin `_process_result()` (mecanismul cozii de joburi vine din `l10n_ro_anaf_agent`).

#### 5. Conexiuni

- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md): furnizează coada de joburi (`deltatech.tc.job`) și mecanismul de comunicare outbound cu agentul Terrabit de pe stația contabilului, pe care se bazează jobul `duk_validate`.
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): modelul depunerii ANAF este primul consumator al mixin-ului DUK și hub-ul fluxului de validare + trimitere.
