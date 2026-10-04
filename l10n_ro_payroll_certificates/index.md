# Romania - Adeverințe salariale (localizat la `l10n_ro_payroll_certificates/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_certificates`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_certificates
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_certificates`
- **Ultima Ingestie:** `2026-10-04`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul emite adeverințe salariale la cererea angajatului, direct din fluturașii validați: sumele nu se mai recopiază de mână, adeverința primește număr de înregistrare, textul rămâne editabil cât timp e ciornă, iar PDF-ul semnat de două persoane se arhivează pe fișa angajatului. Sunt disponibile trei tipuri de adeverință: de venit (pentru bănci, chiriași sau alte instituții), cu baza de calcul pentru concediul medical (pentru noul angajator) și de asigurat în sistemul de sănătate.

#### 2. Funcționalități Cheie

- **Trei tipuri de adeverință:**
    - **Venit:** venitul brut, CAS, CASS, impozitul și venitul net pe ultimele luni încheiate (implicit 6);
    - **Bază pentru concediul medical:** ultimele 6 luni cu venit, cu plafonul lunar de 12 salarii minime brute pe țară, zilele aferente și media zilnică (OUG 158/2005, art. 10), plus certificatele medicale din aceeași perioadă; folosește aceleași reguli ca certificatul medical din [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md), iar baza nu include suma neimpozabilă;
    - **Asigurat (sănătate):** contribuția de asigurări sociale de sănătate (CASS) reținută și virată lunar, pe lunile cerute.
- **Creare pe angajat**, cu tipul, numărul de luni, data emiterii și destinatarul («se eliberează pentru ...»); textul se precompletează din fișa angajatului (CNP, funcție, data angajării, durata contractului) și se poate edita cât timp adeverința e ciornă.
- **Tabel calculat din fluturașii validați sau plătiți**, în fila *Date*; un avertisment apare când unele luni nu au fluturaș.
- **Două semnături** (nume și rol), cu valori implicite: «Administrator» și «Întocmit» (utilizatorul curent).
- **Emitere:** la apăsarea butonului *Emite* adeverința primește număr din secvență (`ADV/an/nr`), iar PDF-ul se arhivează ca atașament pe fișa angajatului; o adeverință emisă nu se modifică și nu se șterge, doar se anulează (stări: ciornă, emisă, anulată; istoric în chatter).
- **Meniu:** *Stat de plată → Angajați → Adeverințe salariale (RO)*; utilizatorii au nevoie de grupul *Utilizator salarizare*, iar datele companiei (denumire, adresă, CUI, număr din Registrul Comerțului) se completează pe companie, fiindcă apar în text.
- **Limite:** în prima versiune lipsesc tipurile pentru șomaj (Anexa 7), concediu pentru creșterea copilului și declarația de venituri peste salariul minim.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payroll.certificate` (nou, cu `mail.thread`, multi-companie): adeverința salarială, cu tipul (`income`, `cm_base`, `health`), numărul de luni, destinatarul, textul (`body_html`, calculat și editabil), tabelul (`table_html`, calculat), semnăturile, atașamentul PDF și metodele `action_issue`, `action_cancel`, `action_draft`, `action_print`.

**Vizualizări**

- `view_l10n_ro_payroll_certificate_form`: formularul adeverinței, cu filele *Text* și *Date*.
- `view_l10n_ro_payroll_certificate_list` și `view_l10n_ro_payroll_certificate_search`: lista și filtrele adeverințelor.
- `action_report_payroll_certificate` / `report_payroll_certificate`: raportul PDF al adeverinței, cu două semnături.
- `data/certificate_templates.xml`: șabloane QWeb pentru introducere și pentru textul fiecărui tip (`employee_intro`, `body_income`, `body_cm_base`, `body_health`) și pentru tabel (`table_certificate`).

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`. Definește secvența `seq_l10n_ro_payroll_certificate` (numerotarea `ADV/an/nr`) și o regulă multi-companie.

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): sursa fluturașilor, a regulilor de calcul și a certificatelor medicale; adeverința de bază pentru concediul medical cere versiunea 19.0.2.6.3 sau mai nouă, în care baza CM exclude suma neimpozabilă.
