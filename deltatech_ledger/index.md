# Deltatech Ledger (localizat la `deltatech_ledger/index.md`)

- **Nume Tehnic:** `deltatech_ledger`
- **Versiune:** `19.0.0.1.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_ledger`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_ledger`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul oferă un registru de intrări-ieșiri pentru documente. Fiecare document care intră în companie sau pleacă din ea primește o înregistrare numerotată, astfel încât registrul poate fi prezentat unui auditor, tipărit pentru o perioadă și căutat oricând. Numerotarea este o serie comună pentru intrări și ieșiri, reluată în fiecare an (`2026/00001`) și fără goluri: un număr nu este niciodată sărit, iar o înregistrare greșită se anulează în loc să fie ștearsă, deci numărul rămâne în registru.

#### 2. Funcționalități Cheie

- O înregistrare pe document, de tip **Intrare** sau **Ieșire**, cu număr de document, dată, contact, loc de proveniență și o scurtă descriere.
- **Rezervări:** un număr poate fi rezervat în avans și datat ulterior, între datele numărului anterior și ale celui următor, astfel încât registrul rămâne în ordine cronologică. Rezervarea se înregistrează (*Register*) sau se anulează. Meniu dedicat *Reserve a Number*.
- **Anulare** cu motiv obligatoriu (wizard), păstrat pe înregistrare și în chatter; numărul rămâne în registru și nu se reutilizează. Doar un Ledger Manager poate reactiva o înregistrare anulată sau șterge înregistrări (indicat doar pentru date de test).
- **Reguli de dată:** data trebuie să fie în același an cu numărul și nu poate scădea odată cu numărul (valabil și pentru înregistrările active, și pentru rezervări); limitele intervalului sunt permise. Un document cu dată anterioară se înregistrează rezervând întâi numărul.
- **Numerotare:** secvența *Ledger Sequence* (cod `ledger.ledger`), fără goluri, cu subsecvență pe an și prefix `%(year)s/`, lungime 5. Formatul se poate modifica din **Settings > Technical > Sequences**, iar pentru continuarea unui registru pe hârtie se setează *Next Number* în intervalul anului curent.
- **Legături (tab Links):** atașamente în chatter, linkuri web și legături către proiect, sarcină, tichet helpdesk, comandă de vânzare/achiziție, factură sau transfer (se oferă doar modelele aplicațiilor instalate); eticheta se completează automat.
- Avertisment (banner galben) la un posibil duplicat: același tip, număr de document și contact; înregistrarea se poate totuși salva.
- Chatter și activități pe fiecare înregistrare, cu urmărirea stării, tipului, datei, numărului de document și a contactului.
- Vizualizări: listă (afișează implicit toate numerele, inclusiv cele anulate), kanban pe stări, calendar, pivot și grafic (intrări vs. ieșiri pe lună); filtre pe stare, tip și dată, grupări pe tip, contact, lună și stare.
- **Raport PDF** al registrului pe perioadă (meniu *Print Ledger*, peisaj) sau pentru o selecție de înregistrări; opțional include înregistrările anulate (cu motiv) și rezervările fără dată.
- **Drepturi de acces:** orice utilizator intern citește, creează, editează, rezervă, înregistrează, anulează și tipărește; grupul *Ledger / Manager* (implicat de Administration / Settings) poate în plus șterge și reactiva.
- **Multi-companie:** fiecare înregistrare aparține unei companii și este vizibilă doar în ea; secvența este comună implicit, dar se poate crea o secvență cu același cod pe companie.
- Limitări: modulul ține evidența referințelor documentelor, nu documentele în sine și nu generează note contabile; intrările și ieșirile nu pot avea serii separate; la creare simultană de către doi utilizatori poate apărea o eroare de blocare, rezolvată prin salvare repetată.

#### 3. Dependențe

- `base`
- `mail`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, componentele nu sunt detaliate prin analiză suplimentară a codului. Pentru orientare:

**Modele**

- `ledger.ledger`: înregistrarea din registru (`mail.thread`, `mail.activity.mixin`), cu stările rezervat / activ / anulat.
- `ledger.link`: legătură a unei înregistrări către un document Odoo sau un link web.
- `ledger.cancel.wizard`: wizard pentru anularea înregistrărilor cu motiv.
- `ledger.report.wizard`: wizard pentru tipărirea registrului pe perioadă.

**Vizualizări**

- `views/ledger_view.xml`: listă, formular, kanban, calendar, pivot, grafic și căutare; meniurile *Records* și *Reserve a Number*.
- `wizard/ledger_wizard_views.xml`: formularele wizardurilor; meniul *Print Ledger*.
- `report/ledger_report.xml`: raportul PDF `action_report_ledger` (format de hârtie peisaj).

**Acțiuni Automate / Acțiuni Server**

- `ledger_sequence` (`data/ir_sequence_data.xml`): secvența fără goluri a registrului; nu există cron-uri sau acțiuni server. O migrare (`migrations/19.0.0.1.0/post-migration.py`) convertește secvența existentă.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module documentate în wiki. Legăturile din tab-ul *Links* către proiect, helpdesk, vânzări, achiziții, contabilitate și stoc apar doar dacă aplicațiile respective sunt instalate (nu sunt dependențe).
