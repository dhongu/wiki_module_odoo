# Deltatech Cron Progress

- **Nume Tehnic:** `deltatech_cron_progress`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_cron_progress
- **Cale Locală:** `odoo-addons/deltatech/deltatech_cron_progress`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic care oferă o regulă comună pentru acțiunile programate ce lucrează pe loturi. După fiecare lot, acțiunea spune câte înregistrări a procesat și câte au rămas; progresul se salvează, iar planificatorul reia lotul următor imediat, până se termină tot. Un lot care nu a procesat nimic oprește rularea, ca acțiunea să nu fie reluată la nesfârșit. Regula are aceeași formă pe 18.0, 19.0 și 20.0, deci codul modulelor care o folosesc nu se schimbă la migrare.

#### 2. Funcționalități Cheie

- Metodă comună `ir.cron._cron_report_progress(done, remaining)`, apelată o singură dată, la finalul lotului, în metoda rulată de acțiunea programată; `done` este numărul procesat în lotul curent, nu un total cumulat.
- Folosește mecanismul nativ de progres din Odoo 19 (`_commit_progress`): cât timp `remaining > 0`, planificatorul rulează din nou acțiunea imediat (cel puțin 10 rulări și 10 secunde la o preluare, apoi la următoarea interogare), deci acțiunea nu mai trebuie să se autodeclanșeze cu `_trigger()` după fiecare lot. Butonul **Rulează manual** se comportă la fel.
- Un lot cu `done == 0` forțează `remaining = 0`, deci se oprește (în 19.0, `done == 0` cu `remaining > 0` ar fi reluat imediat).
- În rularea unei acțiuni progresul este salvat (commit), deci supraviețuiește unui timeout la un lot ulterior; de aceea se apelează după lot, nu în mijlocul unei operații care trebuie să rămână atomică.
- La apel direct din cod, în afara unei rulări a acțiunii, nu se face commit; dacă mai e de lucru, acțiunea pe care s-a apelat metoda este pornită în fundal (`_trigger()`) pentru rest.
- Parametru opțional `deactivate`: dezactivează acțiunea după procesarea completă (acțiuni care rulează o singură dată, ex. migrări de date).
- Raportați `remaining = 0` în mod dry run sau când restul nu poate fi procesat.
- Modulul nu are ecrane, setări sau meniuri proprii; verificarea se face pe **Setări → Tehnic → Automatizare → Acțiuni planificate** (mod dezvoltator) și în jurnalul serverului (`fully done` / `partially done` / `failed`). Pas-cu-pas, cu acțiuni demo de test: vezi [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `ir.cron` (extins): adaugă metoda `_cron_report_progress(done, remaining, deactivate=False)`, care returnează valoarea `remaining` efectiv raportată.

**Vizualizări**

- Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni programate proprii; regula este folosită de acțiunile programate ale altor module.

#### 5. Conexiuni

- [deltatech_actions](../deltatech_actions/index.md): pe 18.0 folosește regula la unirea partenerilor duplicați și la curățarea atașamentelor; pe 19.0 trecerea urmează.
- [deltatech_cron_monitor_webhook](../deltatech_cron_monitor_webhook/index.md): pornește acțiunile din exterior, ca butonul **Rulează manual**; regula funcționează și acolo.
