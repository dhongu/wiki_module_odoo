# Deltatech Project Pricelist (localizat la `deltatech_project_price_list/index.md`)

- **Nume Tehnic:** `deltatech_project_price_list`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_project_price_list
- **Cale Locală:** `odoo-addons/deltatech/deltatech_project_price_list`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul permite definirea unei liste de prețuri implicite la nivel de proiect, astfel încât orice comandă de vânzare creată dintr-un proiect (sau dintr-o sarcină a acestuia) să folosească automat lista de prețuri corectă. Scopul este eliminarea erorilor de selecție manuală și menținerea unei politici de prețuri consecvente pentru fiecare proiect, fără ca alegerea explicită făcută de utilizator să fie suprascrisă.

#### 2. Funcționalități Cheie

- Câmp nou pe proiecte: `Pricelist` (`project.project.pricelist_id`).
- Acțiunea de Comenzi de Vânzare a proiectului injectează `default_pricelist_id`, astfel încât ofertele noi sunt precompletate cu lista de prețuri a proiectului.
- La deschiderea unei oferte dintr-un proiect sau o sarcină, `sale.order.default_get` propune lista de prețuri a proiectului înainte de salvare.
- Siguranță pe server: în timpul `sale.order.create`, dacă o comandă este creată dintr-un proiect/sarcină și nu este furnizată o listă de prețuri, se aplică lista proiectului.
- Lista de prețuri aleasă explicit de utilizator sau furnizată prin context nu este niciodată suprascrisă.

#### 3. Dependențe

- `sale_project`

#### 4. Componente Cheie

**Modele**

- `project.project`: extins cu câmpul `pricelist_id` (lista de prețuri implicită a proiectului).
- `sale.order`: extins prin `default_get` (propune lista de prețuri a proiectului la deschiderea ofertei din proiect/sarcină) și prin `create` (aplică lista proiectului dacă nu este furnizată una).

**Vizualizări**

- Formular proiect (simplificat): afișează câmpul `Pricelist` în secțiunea de setări.
- Vizualizare de editare a proiectului moștenită din `sale_project`: afișează `Pricelist` în pagina Setări (vizibil când proiectul este facturabil și nu este șablon).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau înregistrări `ir.actions.server` dedicate. Comportamentul automat se realizează prin injectarea contextului (`default_pricelist_id`) în acțiunea de Comenzi de Vânzare a proiectului și prin override-urile de model.

#### 5. Conexiuni

- `sale_project`: dependența directă care asigură integrarea Proiect ↔ Vânzări pe care se construiește acest modul.
