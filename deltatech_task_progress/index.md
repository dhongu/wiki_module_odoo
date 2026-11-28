# Task Progress (localizat la `deltatech_task_progress/index.md`)

- **Nume Tehnic:** `deltatech_task_progress`
- **Versiune:** `20.0.1.1.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_task_progress
- **Cale Locală:** `odoo-addons/deltatech/deltatech_task_progress`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic care rulează o sarcină lungă pas cu pas, într-un dialog de progres, cu mai mulți pași în paralel, în loc de o singură cerere care expiră sau blochează ecranul. Este folosit de alte module pentru operații lungi, cum ar fi citirea cu AI a unui PDF pagină cu pagină.

#### 2. Funcționalități Cheie

- Un model moștenește `task.progress.mixin` și returnează `_task_progress_action(...)` dintr-un buton; dialogul apelează metoda de pas câte o dată pe element (pagină de PDF, lot de înregistrări), câțiva în paralel, fiecare în propria cerere și tranzacție.
- Dialogul afișează bara de progres, elementele terminate, estimarea timpului rămas, contorul întors de pași și elementele eșuate cu erorile lor.
- Buton de reluare a elementelor eșuate și buton de oprire după elementele aflate în lucru; închiderea e blocată cât timp rulează elemente.
- Un pas întoarce un număr (contorul) sau `{status, message, count}` cu `success`, `warning` (terminat, de verificat manual, nu se reia) sau `error` (se reia).
- La final se apelează metoda de finalizare și se deschide acțiunea întoarsă (previzualizare, înregistrări create).
- Opțiuni: `init` (pregătire pe server cu mesajul „Preparing...”), `close` (acțiune la închidere), `auto_start`, `finish_mode`, `parallel`, etichete personalizate; funcționează și fără wizard, direct pe înregistrări, dintr-o acțiune a listei.
- Pașii simultani nu trebuie să scrie pe același rând, altfel apar erori de serializare; un `parallel` peste numărul de workeri HTTP doar așază cererile la coadă. Fluxul pas cu pas rămâne în fișa consultantului.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- `task.progress.mixin`: mixin abstract cu `_task_progress_action(...)`, care construiește acțiunea ce deschide dialogul.

**Vizualizări**

- `static/src/task_progress/task_progress.esm.js` și `task_progress.xml`: componenta OWL a dialogului de progres (`web.assets_backend`), plus teste JS în `web.assets_unit_tests`.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_ai_purchase_pdf](../deltatech_ai_purchase_pdf/index.md): citirea PDF-ului facturii de furnizor cu AI, pagină cu pagină, în acest dialog.
