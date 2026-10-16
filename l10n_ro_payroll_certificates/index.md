# Romania - Adeverințe salariale (localizat la `l10n_ro_payroll_certificates/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_certificates`
- **Versiune:** `19.0.1.3.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_certificates
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_certificates`
- **Ultima Ingestie:** `2026-10-16`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul emite adeverințe salariale la cererea angajatului, direct din fluturașii validați: sumele nu se mai recopiază de mână, adeverința primește număr de înregistrare, textul rămâne editabil cât timp e ciornă, iar PDF-ul semnat se arhivează pe fișa angajatului. Sunt disponibile cinci tipuri de adeverință: de venit (pentru bănci, chiriași sau alte instituții), cu baza de calcul pentru concediul medical (pentru noul angajator), de asigurat în sistemul de sănătate, precum și de șomaj (formularul oficial Anexa nr. 7) și de creștere a copilului (formularul oficial Anexa nr. 2, model AJPIS).

#### 2. Funcționalități Cheie

- **Cinci tipuri de adeverință:**
    - **Venit:** venitul brut, CAS, CASS, impozitul și venitul net pe ultimele luni încheiate (implicit 6); coloanele pentru tichete de masă, rețineri / popriri și indemnizații CM apar doar când există;
    - **Bază pentru concediul medical:** stagiul de asigurare și venitul ultimelor 12 luni dinaintea lunii emiterii (OUG 158/2005, art. 7 și 10), cu zilele aferente; folosește aceleași reguli de venit ca certificatul medical din [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): venitul exclude suma neimpozabilă și include indemnizațiile de concediu medical, prezentate separat. Plafonul de 12 salarii minime **nu** se aplică în adeverință: îl aplică angajatorul care plătește concediul medical. Al doilea tabel, cu certificatele medicale confirmate din perioadă (cod de indemnizație, zile), apare doar când există concedii medicale;
    - **Asigurat (sănătate):** adeverește că societatea **a calculat și a reținut** contribuția CASS pe lunile din tabel și, dacă e cazul, că la data eliberării contractul este în derulare; nu atestă calitatea de asigurat (o stabilește casa de asigurări);
    - **Șomaj (Anexa nr. 7, fostă 26, la Normele metodologice ale Legii 76/2002):** formularul oficial, cu secțiunea A (datele angajatorului: CUI, CAEN, adresă, contact), datele salariatului (CNP, seria și numărul actului de identitate), tabelul B.1 și secțiunea C (actul de încadrare cu numărul și data CIM, data angajării, data și temeiul încetării, perioadele de suspendare cu numărul de zile de concediu medical). Tabelul B.1 are cel mult 12 luni cu stagiu, descrescător de la luna încetării (de la luna anterioară când încetarea e pe data de 1), căutate în ultimele 24 de luni; lunile fără stat de plată se sar. Coloane: *BC* (baza CAM), *BCIS* (baza indemnizației de șomaj) și natura veniturilor. BC și BCIS se iau din D112-ul validat al lunii când e instalat `l10n_ro_anaf_d112`, altfel din fluturaș, cu aceeași regulă ca în D112 (brut fără tichete și fără indemnizațiile din FNUASS, minus suma neimpozabilă), caz în care sunt egale. Temeiul încetării din REGES se tipărește cu alineatul explicitat (de ex. `Art56Alin1LitC` devine „art. 56 alin. (1) lit. c) din Codul muncii”). Numărul de înregistrare al D112 (coloana 5) nu există în Odoo și se completează de angajator;
    - **Concediu pentru creșterea copilului (Anexa nr. 2, model AJPIS):** formularul oficial, cu datele angajatorului (Nr. ORC, CUI), ale salariatului (gen, nume, numele înainte de căsătorie, CNP, cetățenie română / UE / non-UE, domiciliu, calitatea și data angajării), secțiunea I (indemnizația de maternitate, preluată din certificatele medicale cu cod 08; ziua a 42-a de lăuzie, calculată din data nașterii; indemnizația de creștere deja primită și data aprobării concediului, completate manual) și secțiunea II: luna nașterii și cele 24 de luni anterioare, cu zilele lucrate, de concediu medical, de concediu de odihnă, fără plată / absențe nemotivate și venitul net realizat (brut − CAS − CASS − impozit). Documentul tipărit are o singură semnătură, a reprezentantului legal.
- **Actul de identitate și CIM în text:** textul adeverințelor preia actul de identitate al salariatului și numărul contractului individual de muncă, când sunt completate pe angajat și pe contract (modulul `l10n_ro_reges`, care nu este dependență).
- **Luni fără fluturaș Odoo:** la creșterea copilului și la baza pentru concediul medical apar cu **celule goale** (nu 0 zile / 0,00) și o observație neutră, în coloana *Observații*: „fără stat de plată în evidența electronică; situația se completează de angajator”, respectiv „înainte de data angajării” pentru lunile dinaintea datei angajării. Modulul nu deduce și nu afirmă motivul (suspendare, concediu fără plată, perioadă înainte de punerea în funcțiune a Odoo); situația reală o completează angajatorul în textul editabil, altfel noul angajator poate calcula o bază CM mai mică.
- **Formularele de șomaj și creștere copil sunt de confirmat cu instituția:** formularele urmează modelele Anexa 7 și Anexa 2 primite de la instituții, dar rămân de confirmat: ce intră în BCIS (art. 19^1 din Normele Legii 76/2002), dacă lunile fără stagiu se sar, tipul zilelor (lucrătoare, din pontaj) și dacă indemnizația de maternitate intră în venitul net din Anexa 2. Zilele din Anexa 2 sunt cele din fluturaș, pe tipurile de pontaj.
- **Bifa „Model verificat” (`model_confirmed`):** la *Emite*, pentru șomaj și creșterea copilului, este **obligatorie** (ați comparat textul și coloanele cu modelul în vigoare cerut de AJOFM / AJPIS); fără ea apare o eroare și adeverința nu se emite.
- **Medii doar pe ecran (fila *Date*, `summary_html`, doar în ciornă, nu se tipăresc):** *Venit mediu zilnic pe 12 luni (informativ)* la baza CM, media BCIS la șomaj și media netă la creșterea copilului; sub 12 luni cu venit sau zile plătite apare un avertisment.
- **Creare pe angajat**, cu tipul, numărul de luni (implicit 6; 12 la șomaj; 24 la creșterea copilului), data emiterii și destinatarul («se eliberează pentru ...»); textul se precompletează din fișa angajatului (CNP, funcție, data angajării, durata contractului) și se poate edita cât timp adeverința e ciornă. Schimbarea oricărui câmp din formular (angajat, tip, luni, dată, destinatar, semnatari, data nașterii copilului, numele înainte de căsătorie, datele din Secțiunea I) recalculează textul și pierde editările, deci textul se editează la sfârșit. La șomaj se completează în prealabil pe angajat seria și numărul actului de identitate, iar pe contract numărul CIM și temeiul încetării.
- **Tabel calculat din fluturașii validați sau plătiți**, în fila *Date*; un avertisment apare când unele luni nu au fluturaș.
- **Semnături** (nume și rol), cu valori implicite: «Administrator» și «Întocmit» (utilizatorul curent); Anexa 2 tipărește doar prima. La șomaj și creșterea copilului PDF-ul se tipărește fără antetul firmei, cu tabel cu chenar; numărul și data adeverinței se completează la emitere.
- **Emitere:** la apăsarea butonului *Emite* adeverința primește număr din secvență (`ADV/an/nr`), iar PDF-ul se arhivează ca atașament pe fișa angajatului; o adeverință emisă nu se modifică și nu se șterge, doar se anulează (stări: ciornă, emisă, anulată; istoric în chatter); *Setează ca ciornă* o redeschide după anulare, iar la reemitere primește un număr nou. Textul și tabelul nu se recalculează la retipărire.
- **Meniu:** *Stat de plată → Angajați → Adeverințe salariale (RO)*; utilizatorii au nevoie de grupul *Utilizator salarizare*, iar datele companiei (denumire, adresă, CUI, număr din Registrul Comerțului) se completează pe companie, fiindcă apar în text.
- **Limite:** declarația de venituri peste salariul minim **nu este implementată** (ține de cumulul de contracte, art. 146 alin. 5^7 lit. e din Codul fiscal, și de un model neconfirmat); numărul de înregistrare al D112 (Anexa 7, coloana 5) se completează manual; la Anexa 2 numele și prenumele apar pe un singur rând; zilele de concediu medical se adeveresc pe 12 luni, iar cazul de 24 de luni din **art. 3^1 OUG 158/2005 nu este acoperit**.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payroll.certificate` (nou, cu `mail.thread`, multi-companie): adeverința salarială, cu tipul (`income`, `cm_base`, `health`, `unemployment`, `child_care`), numărul de luni, `child_birth_date` (data nașterii copilului, obligatorie la `child_care`), câmpurile Anexei 2 (`maiden_name`, `maternity_date_from` / `maternity_date_to`, `postpartum_end_date`, `child_care_paid_from` / `child_care_paid_to`, `leave_approved_date`), `model_confirmed` (bifa „Model verificat”, obligatorie la emitere pentru `unemployment` și `child_care`), `summary_html` (mediile informative, calculate, doar pe ecran), `warning` (avertisment calculat), destinatarul, textul (`body_html`, calculat și editabil), tabelul (`table_html`, calculat), semnăturile, atașamentul PDF și metodele `action_issue`, `action_cancel`, `action_draft`, `action_print`.

**Vizualizări**

- `view_l10n_ro_payroll_certificate_form`: formularul adeverinței, cu filele *Text* și *Date*.
- `view_l10n_ro_payroll_certificate_list` și `view_l10n_ro_payroll_certificate_search`: lista și filtrele adeverințelor.
- `action_report_payroll_certificate` / `report_payroll_certificate`: raportul PDF al adeverinței, cu două semnături.
- `data/certificate_templates.xml`: șabloane QWeb pentru introducere și pentru textul fiecărui tip (`employee_intro`, `body_income`, `body_cm_base`, `body_health`, `body_unemployment`, `body_child_care`), pentru tabel (`table_certificate`) și pentru mediile informative din fila *Date* (`summary_certificate`).

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`. Definește secvența `seq_l10n_ro_payroll_certificate` (numerotarea `ADV/an/nr`) și o regulă multi-companie.

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): sursa fluturașilor, a regulilor de calcul și a certificatelor medicale; adeverința de bază pentru concediul medical cere versiunea 19.0.2.6.3 sau mai nouă, în care baza CM exclude suma neimpozabilă.
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): opțional (nu e dependență); când e instalat, BC și BCIS din Anexa 7 se iau din D112-ul validat sau exportat al lunii.
- [l10n_ro_reges](../l10n_ro_reges/index.md): opțional (nu e dependență); furnizează actul de identitate, numărul CIM, temeiul încetării și perioadele de suspendare folosite în text.
