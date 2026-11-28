# Background Jobs

- **Nume Tehnic:** `deltatech_background_job`
- **Versiune:** `20.0.2.4.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_background_job
- **Cale Locală:** `odoo-addons/bitshop/deltatech_background_job`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Rulează sarcinile lungi în fundal, inclusiv pe odoo.sh, și permite urmărirea și controlul lor. O sarcină construită pe dialogul de progres (citirea unui PDF pagină cu pagină, un import, comenzi trimise unui curier) primește butonul **Run in background**: sarcina continuă și după închiderea paginii, iar cel care a lansat-o este notificat la final. Este o alternativă la `queue_job`, cu monitorizare și control în plus. Modulul este în stadiul Beta.

#### 2. Funcționalități Cheie

- **Pornire în câteva secunde, fără acțiuni programate**: munca rulează în workerii HTTP, ca lanțuri de cereri care se relansează singure (sloturi), deci nu așteaptă intervalul acțiunilor programate de pe odoo.sh.
- **Sarcini lungi**: fiecare element are propria tranzacție; un slot se oprește înainte de limitele cererii, iar următoarea cerere continuă cu elementele rămase, fără cod suplimentar pentru reluare.
- **Monitor**: *Running Processes > Jobs* listează job-urile (filtrul *My jobs* e activ implicit) sub carduri KPI (în lucru, oprite, cu erori, finalizate) care filtrează lista dintr-un clic; din formular, *Show progress* deschide dialogul de progres live, cu elemente, mesaje și erori.
- **Procese**: un ecran cu tot ce rulează acum în baza de date (ca SAP SM50/SM66): cererile utilizatorilor, sloturi și acțiuni programate, cu durata, interogarea curentă, cine pe cine blochează și întreruperea forțată a cererii unui utilizator (pentru manageri).
- **Control**: Stop, Resume, Retry failed (doar elementele eșuate) și Cancel pentru manageri (elementele în lucru se întrerup și se anulează tranzacția).
- **Încărcare**: fiecare element păstrează durata, timpul CPU, interogările SQL și memoria workerului; ecranul *Slots* arată fiecare slot live față de limitele workerului, plus CPU și memoria serverului.
- **Sigur**: pașii rulează ca utilizatorul care a lansat job-ul, cu companiile și limba lui; un worker pierdut e detectat prin heartbeat, iar elementul se reia (maximum 3 încercări).
- **Alternativă la `queue_job`**: `record.with_delay(...).method(...)` cu aceeași semnătură, chei de identitate, canale cu capacitate, funcții de job, erori reluabile și prioritate. Refuză instalarea cât timp `queue_job` este instalat (și invers); trecerea se face golind coada, dezinstalând `queue_job`, apoi instalând modulul.
- **Setări** (*Settings > Background Jobs*, doar manageri): numărul de sloturi (implicit un slot per worker, maximum un sfert din locurile HTTP), secunde per cerere, zile de păstrare a job-urilor terminate (30 implicit), timeout heartbeat, URL-ul slotului, afișarea utilizatorului și operației în ecranul Procese.
- **Canale și funcții de job** (*Configuration > Channels / Job Functions*): capacitatea canalelor (ex. `root.marketplace`), canalul implicit, tiparul de reîncercare și acțiunea asociată butonului *Related records*.
- Lanțurile de sloturi întrerupte (repornire server, deploy) se repornesc din browser, la deschiderea ecranelor de progres sau de acțiunea programată *Background jobs: restart broken slots*.
- Fluxul pas cu pas rămâne în fișa consultantului.
- **Limite recunoscute**: nu e dovedit încă pe o producție cu volum real timp de săptămâni; câștigul cu mai multe sloturi pe odoo.sh e limitat, deoarece sloturile unui worker sunt thread-uri ale aceluiași proces Python.

#### 3. Dependențe

- `deltatech_task_progress`
- `deltatech_web_kpi_cards`
- `bus`

#### 4. Componente Cheie

**Modele**

- `bg.job`: job-ul în fundal, cu stare, progres, contoare și încărcare.
- `bg.job.item`: elementul unui job, cu mesaj/eroare, durată, CPU, SQL și memorie.
- `bg.slot`: slotul (lanțul de cereri) care execută elementele, cu heartbeat și watchdog.
- `bg.channel`: canal cu capacitate pentru apelurile întârziate.
- `bg.job.function`: canal implicit, tipar de reîncercare și acțiune asociată pentru o metodă.
- `task.progress.mixin` (extins): adaugă rularea în fundal (`background=True`).
- `base` (extins): oferă `with_delay`.
- `ir.cron`, `ir.http`, `ir.module.module`, `res.config.settings` (extinse): integrare cu procesele, pornirea slotului, verificarea față de `queue_job` și setările.

**Vizualizări**

- `bg_job_list` / `bg_job_form` / `bg_job_search`: lista cu carduri KPI, formularul și căutarea job-urilor.
- `bg_job_item_list` / `bg_job_item_form` / `bg_job_item_search`: elementele job-urilor.
- `bg_slot_list`: sloturile și ecranul Procese.
- `bg_channel_list`, `bg_job_function_list`: canale și funcții de job.
- `res_config_settings_view_form`: *Settings > Background Jobs*.

**Acțiuni Automate / Acțiuni Server**

- *Background jobs: restart broken slots*: acțiune programată, la 5 minute, repornește lanțurile de sloturi întrerupte.

#### 5. Conexiuni

- `deltatech_queue_job`: modulul însoțitor al `queue_job`; trebuie dezinstalat înainte de instalarea acestui modul.
- `queue_job`: alternativă exclusivă (nu pot fi instalate împreună).
- `deltatech_ai_purchase_pdf`: exemplu de sarcină cu dialog de progres care primește butonul *Run in background*.
