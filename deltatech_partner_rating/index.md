# Evaluare parteneri (localizat la `deltatech_partner_rating/index.md`)

- **Nume Tehnic:** `deltatech_partner_rating`
- **Versiune:** `20.0.0.1.14`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_partner_rating
- **Cale Locală:** `odoo-addons/bitshop/deltatech_partner_rating`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Fiabilitatea unui partener influențează condițiile de credit și de plată. Modulul notează clienții și furnizorii după criterii definite de dumneavoastră, introduse manual sau calculate din facturi, și afișează rezultatul pe fișa partenerului. Este modulul de bază al unei familii de module, peste care se construiesc extensii dedicate vânzărilor și service-ului.

#### 2. Funcționalități Cheie

- **Criterii de evaluare**: managerii de evaluare le definesc din meniul *Evaluări parteneri* din Contacte: tip criteriu (*Manual* sau *Calculat*), tip partener, valoare implicită și, opțional, un domeniu de parteneri la care se aplică.
- **Parametri calculați**: un criteriu calculat măsoară total facturat (fără taxe) în ultimele 12 luni, timpul mediu de plată, prima factură (ani de la ea) sau numărul de contracte de service.
- **Intervale de notare**: fiecare linie de criteriu are minim, maxim, valoare de evaluare și factor; linia care se potrivește dă scorul valoare × factor, altfel se folosește valoarea implicită.
- **Scorul partenerului**: fila *Evaluări parteneri* din fișa partenerului listează liniile (doar cele manuale sunt editabile); o bară arată evaluarea de client și, cu opțiunea *Calculează evaluările de furnizor* bifată, pe cea de furnizor.
- **Acțiuni de recalculare**: *Rulează* pe criterii (limitat de domeniul lor) creează sau actualizează liniile; *Calculează evaluările* pe parteneri (doar manageri) actualizează liniile calculate; *Resetează evaluările* reconstruiește liniile unui partener, iar valorile manuale revin la implicit.
- **Drepturi și programare**: utilizatorii interni citesc evaluările, doar managerii le modifică. Acțiunea programată zilnică „Partner rating: compute ratings” este instalată inactivă; activați-o pentru recalcularea automată. Timpul mediu de plată și numărul de contracte cer [deltatech_average_payment_period](../deltatech_average_payment_period/index.md) și [deltatech_service_agreement](../deltatech_service_agreement/index.md).
- Fluxul pas cu pas se află în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `mail`
- `purchase`
- `account`
- `contacts`

#### 4. Componente Cheie

**Modele**

- `partner.rating.criteria`: criteriul de evaluare (tip, parametru calculat, valoare implicită, domeniu de parteneri), cu urmărire în chatter.
- `partner.rating.criteria.line`: intervalele de notare ale unui criteriu (minim, maxim, valoare, factor).
- `partner.rating.line`: evaluarea unui partener pe un criteriu.
- `res.partner` (extins): linii de evaluare, scorurile `partner_rating` și `supplier_rating` și opțiunea `compute_supplier_ratings`.

**Vizualizări**

- `rating_criteria_tree`, `rating_criteria_form`, `rating_criteria_line_tree`: listele și formularul criteriilor și al liniilor.
- `view_partner_form`: fila de evaluări și bara de scor pe fișa partenerului.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_compute_ratings`: recalculează zilnic evaluările lipsă sau învechite (inactivă implicit).
- `action_compute_criteria`, `action_compute_criteria_for_partner`, `action_reset_criteria_for_partner`: rulare criterii, calcul și resetare evaluări pe partener.

#### 5. Conexiuni

- [deltatech_partner_rating_sale](../deltatech_partner_rating_sale/index.md): extinde evaluarea partenerilor în contextul vânzărilor.
- [deltatech_partner_rating_service](../deltatech_partner_rating_service/index.md): extinde evaluarea partenerilor în contextul service-ului.
- [deltatech_average_payment_period](../deltatech_average_payment_period/index.md): furnizează timpul mediu de plată folosit de criteriile calculate.
- [deltatech_service_agreement](../deltatech_service_agreement/index.md): furnizează numărul de contracte de service folosit de criteriile calculate.
