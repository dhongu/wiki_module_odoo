# Incoming and Outgoing Document Register (localizat la `deltatech_ledger/index.md`)

- **Nume Tehnic:** `deltatech_ledger`
- **Versiune:** `20.0.0.1.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_ledger
- **Cale Locală:** `odoo-addons/deltatech/deltatech_ledger`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține registrul de intrări-ieșiri al documentelor: fiecare document care intră în companie sau pleacă din ea primește o înregistrare numerotată, care poate fi arătată unui auditor, tipărită pentru o perioadă și căutată oricând. Numerotarea este comună și fără goluri, repornită anual (`2026/00001`); o înregistrare greșită se anulează, nu se șterge, deci numărul rămâne în registru.

#### 2. Funcționalități Cheie

- O înregistrare per document, de tip **Entry** sau **Exit**, cu număr document, dată, contact, loc de proveniență și descriere. Meniul aplicației **Ledger**: *Records*, *Reserve a Number*, *Print Ledger*.
- **Stări:** *Reserved* (număr păstrat, data se poate completa mai târziu), *Active*, *Canceled*.
- **Rezervări:** un număr se rezervă în avans și se datează ulterior, între datele numărului anterior și următor, ca registrul să rămână cronologic; data trebuie să fie în același an cu numărul.
- **Anulare** cu motiv obligatoriu; doar un Ledger Manager poate reactiva sau șterge înregistrări.
- **Legături:** atașamente în chatter, linkuri web și linkuri către proiect, sarcină, tichet helpdesk, comandă de vânzare/achiziție, factură sau transfer.
- Chatter și activități, cu urmărirea stării, tipului, datei, numărului și contactului; avertisment la dubluri (același tip, număr și contact).
- Vizualizări: listă, kanban pe stări, calendar, pivot și grafic; raport PDF al registrului pentru o perioadă sau o selecție, cu opțiuni pentru anulate și rezervări fără dată.
- Secvența `ledger.ledger` fără goluri, configurabilă (prefix, mărime, număr următor pentru continuarea unui registru pe hârtie), cu secvență separată per companie opțional; multi-company.
- Limitări: ține doar referințele documentelor (nu le stochează și nu postează note contabile); o serie comună pentru intrări și ieșiri; la creare simultană poate apărea eroarea „could not obtain lock", iar salvarea se repetă.

#### 3. Dependențe

- `base`
- `mail`

#### 4. Componente Cheie

**Modele**

- `ledger.ledger`: înregistrarea din registru, cu `mail.thread` și `mail.activity.mixin`.
- `ledger.link`: legăturile unei înregistrări (record Odoo sau link web).
- `ledger.cancel.wizard` (tranzitoriu): anularea cu motiv.
- `ledger.report.wizard` (tranzitoriu): parametrii raportului PDF.

**Vizualizări**

- `view_ledger_tree`, `view_ledger_form`, `view_ledger_kanban`, `view_ledger_calendar`, `view_ledger_pivot`, `view_ledger_graph`, `view_ledger_search`: interfețele registrului.
- `view_ledger_cancel_wizard_form`, `view_ledger_report_wizard_form`: ferestrele de anulare și de tipărire.
- `action_report_ledger`: raportul PDF al registrului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite cron-uri sau acțiuni server; `data/ir_sequence_data.xml` definește secvența fără goluri a registrului.

#### 5. Conexiuni

Nu au fost identificate conexiuni cu alte module documentate în wiki. Legăturile către proiect, helpdesk, vânzări, achiziții, facturi și transferuri apar doar dacă aplicațiile respective sunt instalate.
