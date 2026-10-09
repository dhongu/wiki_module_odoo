# Romania - Adeverințe salariale (localizat la `l10n_ro_payroll_certificates/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_certificates`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_certificates
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_certificates`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul emite adeverințe salariale la cererea angajatului, direct din fluturașii validați: sumele nu se mai recopiază de mână, adeverința primește număr de înregistrare, textul rămâne editabil cât timp e ciornă, iar PDF-ul semnat de două persoane se arhivează pe fișa angajatului. Sunt disponibile cinci tipuri de adeverință: de venit (pentru bănci, chiriași sau alte instituții), cu baza de calcul pentru concediul medical (pentru noul angajator), de asigurat în sistemul de sănătate, precum și de șomaj și de creștere a copilului (ultimele două cu conținut orientativ, de confirmat cu modelul în vigoare cerut de AJOFM / AJPIS).

#### 2. Funcționalități Cheie

- **Cinci tipuri de adeverință:**
    - **Venit:** venitul brut, CAS, CASS, impozitul și venitul net pe ultimele luni încheiate (implicit 6);
    - **Bază pentru concediul medical:** ultimele 6 luni cu venit, cu plafonul lunar de 12 salarii minime brute pe țară, zilele aferente și media zilnică (OUG 158/2005, art. 10), plus certificatele medicale din aceeași perioadă; folosește aceleași reguli ca certificatul medical din [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md), iar baza nu include suma neimpozabilă;
    - **Asigurat (sănătate):** contribuția de asigurări sociale de sănătate (CASS) reținută și virată lunar, pe lunile cerute;
    - **Șomaj (conținut orientativ):** ultimele 24 de luni încheiate (la contractul încetat, perioada se oprește la încetare; temeiul încetării din REGES apare în text doar dacă există pe contract), cu *zile cu stagiu* (lucrate, de concediu de odihnă sau medical), salariul de bază brut al lunii luat din fluturaș, linia *BASIC* (fără orele suplimentare plătite, proporțional cu timpul plătit) și numărul lunilor cu stagiu; lunile fără stat de plată sunt marcate neutru («situația se completează de angajator»), fără a deduce motivul;
    - **Creșterea copilului (conținut orientativ):** pe baza *Datei nașterii copilului* (obligatorie, `child_birth_date`), fereastra de 24 de luni încheiate dinaintea lunii nașterii, cu brut, CAS, CASS, impozit, net și marcaj pentru lunile cu venit.
- **Atenție, conținut orientativ la șomaj și creșterea copilului:** textul și rubricile sunt pregătite din datele din Odoo și sunt editabile în ciornă, dar **nu reproduc un model oficial**; perioada de 24 de luni, minimul de 12 luni, baza de calcul și structura trebuie **confirmate cu modelul în vigoare cerut de AJOFM / AJPIS** înainte de utilizare.
- **Bifa „Model verificat” (`model_confirmed`):** la *Emite*, pentru aceste două tipuri, este obligatorie; confirmă că textul și coloanele au fost comparate cu modelul în vigoare.
- **Medii doar pe ecran:** media salariului de bază pe ultimele 12 luni cu stagiu (șomaj) și media netă pe ultimele 12 luni cu venit (creșterea copilului) apar doar în fila *Date*, nu pe documentul tipărit; sub 12 luni cu venit sau stagiu apare un avertisment.
- **Creare pe angajat**, cu tipul, numărul de luni (implicit 6; 24 pentru șomaj și creșterea copilului), data emiterii și destinatarul («se eliberează pentru ...»); textul se precompletează din fișa angajatului (CNP, funcție, data angajării, durata contractului) și se poate edita cât timp adeverința e ciornă.
- **Tabel calculat din fluturașii validați sau plătiți**, în fila *Date*; un avertisment apare când unele luni nu au fluturaș.
- **Două semnături** (nume și rol), cu valori implicite: «Administrator» și «Întocmit» (utilizatorul curent).
- **Emitere:** la apăsarea butonului *Emite* adeverința primește număr din secvență (`ADV/an/nr`), iar PDF-ul se arhivează ca atașament pe fișa angajatului; o adeverință emisă nu se modifică și nu se șterge, doar se anulează (stări: ciornă, emisă, anulată; istoric în chatter).
- **Meniu:** *Stat de plată → Angajați → Adeverințe salariale (RO)*; utilizatorii au nevoie de grupul *Utilizator salarizare*, iar datele companiei (denumire, adresă, CUI, număr din Registrul Comerțului) se completează pe companie, fiindcă apar în text.
- **Limite:** declarația de venituri peste salariul minim **nu este implementată** (ține de cumulul de contracte și de un model neconfirmat); modelele oficiale pentru șomaj și creșterea copilului nu au fost verificate; zilele cu stagiu includ concediul de odihnă și cel medical.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payroll.certificate` (nou, cu `mail.thread`, multi-companie): adeverința salarială, cu tipul (`income`, `cm_base`, `health`, `unemployment`, `child_care`), numărul de luni, `child_birth_date` (data nașterii copilului, obligatorie la `child_care`), `model_confirmed` (bifa „Model verificat”, obligatorie la emitere pentru `unemployment` și `child_care`), `summary_html` (mediile informative, calculate, doar pe ecran), `warning` (avertisment calculat), destinatarul, textul (`body_html`, calculat și editabil), tabelul (`table_html`, calculat), semnăturile, atașamentul PDF și metodele `action_issue`, `action_cancel`, `action_draft`, `action_print`.

**Vizualizări**

- `view_l10n_ro_payroll_certificate_form`: formularul adeverinței, cu filele *Text* și *Date*.
- `view_l10n_ro_payroll_certificate_list` și `view_l10n_ro_payroll_certificate_search`: lista și filtrele adeverințelor.
- `action_report_payroll_certificate` / `report_payroll_certificate`: raportul PDF al adeverinței, cu două semnături.
- `data/certificate_templates.xml`: șabloane QWeb pentru introducere și pentru textul fiecărui tip (`employee_intro`, `body_income`, `body_cm_base`, `body_health`, `body_unemployment`, `body_child_care`), pentru tabel (`table_certificate`) și pentru mediile informative din fila *Date* (`summary_certificate`).

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`. Definește secvența `seq_l10n_ro_payroll_certificate` (numerotarea `ADV/an/nr`) și o regulă multi-companie.

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): sursa fluturașilor, a regulilor de calcul și a certificatelor medicale; adeverința de bază pentru concediul medical cere versiunea 19.0.2.6.3 sau mai nouă, în care baza CM exclude suma neimpozabilă.
