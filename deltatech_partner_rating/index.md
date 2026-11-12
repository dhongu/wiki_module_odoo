# Evaluare parteneri (localizat la `deltatech_partner_rating/index.md`)

- **Nume Tehnic:** `deltatech_partner_rating`
- **Versiune:** `19.0.0.1.13`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_partner_rating
- **Cale Locală:** `odoo-addons/bitshop/deltatech_partner_rating`
- **Ultima Ingestie:** `2026-11-12`

#### 1. Sumar

Condițiile de creditare și de plată depind de cât de de încredere este un partener. Modulul notează clienții și furnizorii pe baza unor criterii definite de utilizator, manual sau pe baza facturilor, oferind o imagine rapidă asupra performanței și fiabilității fiecărui partener. Este modulul de bază al unei familii de module, peste care se construiesc extensii dedicate vânzărilor și service-ului.

#### 2. Funcționalități Cheie

- **Criterii de evaluare:** managerii de evaluare (*Rating Managers*) definesc criteriile în *Partner ratings* din Contacte: *Criteria Type* (*Manual* sau *Computed*), *Partner Type* (client sau furnizor), *Default value* și un *Partners domain* opțional.
- **Parametri calculați:** un criteriu calculat măsoară *Total invoiced (untaxed) last 12 months*, *Average payment time*, *First invoice* (ani de la prima factură) sau *Service agreements number*.
- **Intervale de scorare:** fiecare rând din *Criteria Lines* are un minim, un maxim, o *Rating value* și un *Rating factor*; rândul potrivit dă scorul valoare × factor, altfel se folosește valoarea implicită.
- **Scorul partenerului:** fila *Partner ratings* a partenerului listează liniile sale, iar doar cele manuale sunt editabile. O bară arată *Customer rating* și, cu *Compute supplier ratings* bifat, *Supplier rating*.
- **Acțiuni de recalculare:** *Run* pe criterii (limitat de domeniul lor) creează sau actualizează liniile; criteriile manuale adaugă o linie cu valoarea implicită. *Compute ratings* pe parteneri actualizează liniile calculate. *Reset ratings* reconstruiește liniile unui partener dacă un criteriu apare de două ori; valorile manuale revin la cele implicite.
- Utilizatorii interni citesc evaluările; doar managerii de evaluare le modifică. Nu este instalată nicio acțiune programată: nimic nu se recalculează singur (există totuși metoda `compute_ratings_cron`, apelabilă dintr-un cron definit de utilizator). *Average payment time* cere modulul Average Payment Period, iar *Service agreements number* cere Service Agreement.

#### 3. Dependențe

- `mail`
- `purchase`
- `account`
- `contacts`

#### 4. Componente Cheie

Conform fluxului de ingestie, Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`; mai jos sunt doar reperele confirmate în cod.

**Modele**

- `partner.rating.criteria`: criteriul de evaluare (cu `mail.thread`) — tip, parametru, valoare implicită, domeniu de parteneri, tip de partener; metodele `compute_ratings`, `get_value` și `compute_ratings_cron` calculează scorul.
- `partner.rating.criteria.line`: intervalele de scorare ale unui criteriu (minim, maxim, valoare, factor).
- `partner.rating.line`: scorul unui partener pentru un criteriu, cu descriere și data ultimei actualizări.
- `res.partner` (extins): liniile de evaluare, `partner_rating` (scor client), `supplier_rating` (scor furnizor), bifa `compute_supplier_ratings` și metodele `compute_ratings` și `reset_ratings`.

**Vizualizări**

- `views/rating_criteria.xml`: lista și formularul criteriilor de evaluare.
- `views/res_partner.xml`: fila *Partner ratings* și bara de scor pe partener.
- `views/assets.xml`, `static/src/scss/progressbar.scss`: stilul barei de progres a scorului.

**Acțiuni Automate / Acțiuni Server**

- `action_compute_criteria` (*Run*): recalculează evaluările pentru criteriile selectate.
- `action_compute_criteria_for_partner` (*Compute ratings*): recalculează liniile calculate ale partenerilor selectați.
- `action_reset_criteria_for_partner` (*Reset ratings*): reconstruiește liniile unui partener cu criterii duplicate; doar managerii de evaluare.
- Nu sunt definite sarcini `ir.cron` sau reguli `base.automation`.

#### 5. Conexiuni

- [deltatech_partner_rating_sale](../deltatech_partner_rating_sale/index.md): extinde modulul de bază cu evaluarea partenerilor în contextul vânzărilor.
- [deltatech_partner_rating_service](../deltatech_partner_rating_service/index.md): extinde modulul de bază cu evaluarea partenerilor în contextul service-ului.
- [deltatech_average_payment_period](../deltatech_average_payment_period/index.md): furnizează datele pentru parametrul *Average payment time* (necesar pentru acest parametru).
- [deltatech_service_agreement](../deltatech_service_agreement/index.md): furnizează acordurile de service numărate de parametrul *Service agreements number*.
