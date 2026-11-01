# Project Pricelist (localizat la `deltatech_project_price_list/index.md`)

- **Nume Tehnic:** `deltatech_project_price_list`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_project_price_list
- **Cale Locală:** `odoo-addons/deltatech/deltatech_project_price_list`
- **Ultima Ingestie:** `2026-11-01`

#### 1. Sumar

Modulul permite definirea unei liste de prețuri implicite la nivel de proiect, astfel încât orice comandă de vânzare creată dintr-un proiect (sau dintr-o sarcină a acestuia) să folosească automat lista de prețuri corectă. Scopul este eliminarea erorilor de selecție manuală și menținerea unei politici de prețuri consecvente pentru fiecare proiect, fără ca alegerea explicită făcută de utilizator să fie suprascrisă. Modul nou în 19.0.

#### 2. Funcționalități Cheie

- Câmp nou pe proiecte: `Pricelist` (`project.project.pricelist_id`).
- Acțiunea de Comenzi de Vânzare a proiectului injectează `default_pricelist_id`, astfel încât ofertele noi sunt precompletate cu lista de prețuri a proiectului.
- La deschiderea unei oferte dintr-un proiect sau o sarcină, `sale.order.default_get` propune lista de prețuri a proiectului înainte de salvare.
- Siguranță pe server: în timpul `sale.order.create`, dacă o comandă este creată dintr-un proiect/sarcină și nu este furnizată o listă de prețuri, se aplică lista proiectului.
- Lista de prețuri aleasă explicit de utilizator sau furnizată prin context (`default_pricelist_id`) nu este niciodată suprascrisă, nici la creare (corecție din 19.0.1.0.3), nici la propunerea din formular.
- Mod de lucru: se deschide proiectul și se setează câmpul `Pricelist`, apoi se creează o ofertă din butonul inteligent de comenzi de vânzare al proiectului sau dintr-o sarcină a proiectului; oferta vine precompletată cu lista de prețuri a proiectului.

#### 3. Dependențe

- `sale_project`

#### 4. Componente Cheie

Readme-ul nu cere explicit detalierea componentelor; mai jos sunt cele verificate în cod.

**Modele**

- `project.project`: extins cu câmpul `pricelist_id` și cu `action_view_sos`, care adaugă `default_pricelist_id` în contextul acțiunii de comenzi de vânzare (fără a suprascrie o valoare deja setată).
- `sale.order`: extins prin `default_get` (propune lista de prețuri a proiectului la deschiderea ofertei din proiect/sarcină, dacă nu există deja una) și prin `create` (aplică lista proiectului dacă nu este furnizată una; un `default_pricelist_id` din context are prioritate).

**Vizualizări**

- `project_project_view_form_simplified_inherit_pricelist`: afișează câmpul `Pricelist` în secțiunea de setări a formularului simplificat de proiect.
- `project_project_view_edit_inherit_pricelist`: afișează `Pricelist` în pagina Setări a formularului de editare (moștenit din `sale_project`), vizibil doar când proiectul este facturabil.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau înregistrări `ir.actions.server`. Comportamentul automat se realizează prin contextul injectat în acțiunea de Comenzi de Vânzare a proiectului și prin override-urile de model.

#### 5. Conexiuni

- `sale_project`: dependența directă care asigură integrarea Proiect ↔ Vânzări pe care se construiește acest modul.
