# Deltatech Cron Progress

- **Nume Tehnic:** `deltatech_cron_progress`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_cron_progress
- **Cale Locală:** odoo-addons/deltatech/deltatech_cron_progress
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic care oferă un ajutor comun pentru acțiunile planificate (cron) ce procesează date pe loturi. Folosește progresul nativ al cron-urilor din Odoo, astfel încât planificatorul reia singur lucrarea cât timp mai sunt înregistrări de procesat, fără ca fiecare cron să se declanșeze manual după fiecare lot.

#### 2. Funcționalități Cheie

- Metoda `ir.cron._cron_report_progress(done, remaining)`, apelată o singură dată, la finalul lotului.
- Dacă `remaining > 0`, planificatorul rulează lucrarea din nou imediat (cel puțin 10 rulări și 120 de secunde per preluare, apoi la următoarea interogare); „Run manually” se repetă în același fel.
- `done == 0` forțează `remaining = 0`, deci un lot fără progres oprește bucla.
- În rularea cron, progresul este comis (`_commit_progress`) și supraviețuiește unui timeout al unui lot ulterior; în afara cron-ului (apel direct din cod) nu se comite nimic, iar metoda apelează `_trigger()` pentru restul.
- `done` este numărul de înregistrări din lotul curent, nu un total cumulat; se raportează `remaining = 0` în dry run sau când restul nu poate fi procesat.
- Apelul se face după lot, niciodată în mijlocul unei operații care trebuie să rămână atomică.
- Aceeași semnătură există și în versiunile 18.0 și 19.0, deci codul cron care o folosește este identic.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `ir.cron` (extins): adaugă `_cron_report_progress(done, remaining, deactivate=False)`.

**Vizualizări**

- Nu are vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu definește cron-uri proprii; oferă doar ajutorul pentru cron-urile altor module.

#### 5. Conexiuni

- Nu are conexiuni funcționale verificate cu alte module cu pagină wiki.
