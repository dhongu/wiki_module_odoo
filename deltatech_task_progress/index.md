# Task Progress

- **Nume Tehnic:** `deltatech_task_progress`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_task_progress
- **Cale Locală:** `odoo-addons/deltatech/deltatech_task_progress`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic care rulează o operație lungă pe elemente, câteva deodată, într-un dialog de progres comun, în loc de o singură cerere care depășește timpul serverului sau blochează ecranul. Operatorul vede cât s-a făcut și cât mai durează, ce a eșuat și poate relua doar elementele nereușite. Ce s-a terminat rămâne salvat, chiar dacă un alt element eșuează sau se închide browserul. Modulul nu are meniuri, câmpuri sau acțiuni programate; fiecare modul care îl folosește decide ce este un element și ce se întâmplă la final.

#### 2. Funcționalități Cheie

- Dialog de progres cu bară, elemente terminate, estimare a timpului rămas și contor al rezultatului pașilor (linii citite, înregistrări create).
- Fiecare element rulează în cererea și tranzacția lui; `parallel` elemente rulează simultan (implicit 3). Pașii simultani nu trebuie să scrie pe același rând, altfel apar erori de serializare; un `parallel` peste numărul de procese web doar așază cererile la coadă.
- Elementele eșuate sunt afișate cu eroarea lor și pot fi rulate din nou printr-un buton; operația poate fi oprită după elementele aflate în lucru. Închiderea dialogului este blocată cât rulează elemente.
- Un pas întoarce un număr (contorul) sau `{"status", "message", "count"}`: `success`; `warning` (terminat, de verificat de mână, nu se mai rulează) sau `error` (se reia prin butonul de reîncercare).
- La final se apelează metoda `finish`, iar acțiunea returnată se deschide (previzualizare, înregistrări create). Cu `finish_mode="button"` finalul devine un buton, apelat pe elementele reușite, iar dialogul rămâne deschis.
- Pașii pot rula direct pe înregistrări, fără wizard (parametrul `model`), de exemplu dintr-o acțiune pe listă; lista elementelor cu stare și mesaj se activează cu `show_items`.
- Pornire cu introducere și buton (`auto_start=False`, `intro`), pregătirea lucrului pe server la deschidere (`init`, cu mesajul „Se pregătește...”) și metodă `close` apelată la închiderea după o rulare completă.
- Texte personalizabile (`labels`, `unit_label`, `count_label`, `detail`, `title`).
- Folosit de `deltatech_ai_purchase_pdf` (citirea pe părți a facturilor PDF cu AI), `deltatech_delivery` (Trimite la curier) și de exportul/importul contabil pe bucăți. Fluxul pas-cu-pas este în fișa consultant.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- `task.progress.mixin` (model abstract): oferă `_task_progress_action(...)`, care întoarce acțiunea client `deltatech_task_progress.run` cu parametrii dialogului. Modelul consumator îl moștenește și returnează acțiunea dintr-un buton.

**Vizualizări**

- Fără vizualizări XML de backend. Componenta OWL `TaskProgressDialog` (`static/src/task_progress/task_progress.esm.js` și `.xml`) este înregistrată în registrul `actions` cu eticheta `deltatech_task_progress.run`.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni programate sau acțiuni server.

#### 5. Conexiuni

- [deltatech_ai_purchase_pdf](../deltatech_ai_purchase_pdf/index.md): citirea pe părți a facturilor PDF de furnizor cu AI, cu final automat.
- [deltatech_delivery](../deltatech_delivery/index.md): dialogul „Trimite la curier” din lista comenzilor, cu rând pe comandă.
