# Aprobări achiziții: centru de cost (localizat la `deltatech_approvals_purchase_analytic/index.md`)

- **Nume Tehnic:** `deltatech_approvals_purchase_analytic`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_approvals_purchase_analytic
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_approvals_purchase_analytic`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă **centrul de cost** (distribuția analitică) pe cererile de aprobare de achiziție din aplicația *Aprobări*. Solicitantul îl alege o singură dată, pe cerere; când cererea aprobată creează cererea de ofertă (RFQ), liniile RFQ preiau aceeași distribuție, iar de acolo ajunge și pe factura furnizorului. Cumpărătorul nu mai trebuie să seteze distribuția analitică pe fiecare linie.

#### 2. Funcționalități Cheie

- Câmpul **Centru de cost** pe cererile din categoriile cu *Creează RFQ-uri*, cu widgetul standard de distribuție analitică (mai multe conturi și procente); editabil doar cât cererea este *De trimis*, doar citire după aprobare.
- Distribuția este transmisă liniilor RFQ create sau actualizate de cerere, cât timp RFQ-ul nu este confirmat.
- Funcționează cu RFQ-urile alternative ale unui apel de oferte, care copiază distribuția liniei.
- O cerere fără centru de cost creează RFQ-ul ca înainte (rămâne doar distribuția unui model analitic potrivit, dacă există).
- Coloana **Distribuție analitică** a liniilor comenzii este opțională, se afișează din comutatorul de coloane.
- Configurare: contabilitate analitică activă și conturile analitice create; categorie de aprobare cu *Creează RFQ-uri* (produs și cantitate devin obligatorii). Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `approvals_purchase`
- `analytic`

#### 4. Componente Cheie

**Modele**

- `approval.request` (extindere): moștenește `analytic.mixin` și adaugă `analytic_distribution`; transmite distribuția liniilor RFQ.

**Vizualizări**

- `approval_request_views`: câmpul Centru de cost pe formularul cererii.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `deltatech_purchase_tender` (suita bitshop): oferte minime ale furnizorilor și aprobare peste prag, în afara domeniului acestui modul.
