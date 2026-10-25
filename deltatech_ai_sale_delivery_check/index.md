# Sale & Delivery Daily Check AI (localizat la `deltatech_ai_sale_delivery_check/index.md`)

- **Nume Tehnic:** `deltatech_ai_sale_delivery_check`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_sale_delivery_check
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_sale_delivery_check`
- **Ultima Ingestie:** `2026-10-23`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

În fiecare dimineață, echipa află ce comenzi și livrări cer atenție și de ce, fără să parcurgă sute de comenzi. Modulul verifică comenzile de vânzare și livrările din ziua precedentă (sau din orice perioadă) cu reguli precise, apoi cere unui agent AI să grupeze, să prioritizeze și să explice anomaliile găsite. Rezultatul este o listă de lucru clară, un rezumat al zilei trimis pe e-mail și activități pentru agenții de vânzări.

#### 2. Funcționalități Cheie

- **Reguli întâi, AI apoi**: unsprezece verificări deterministe găsesc anomaliile exact și gratuit; AI-ul primește doar anomaliile găsite, o singură dată pe rulare, nu tot portofoliul de comenzi.
- **Unsprezece verificări implicite**: comandă fără livrare, livrare întârziată (severitate crescută odată cu întârzierea), backorder vechi, livrat mai mult decât comandat, livrat dar nefacturat, facturat dar nelivrat, comandă blocată ca livrată parțial, pregătit dar neexpediat, livrare în risc (așteaptă stoc, termen apropiat), expediat fără număr de urmărire (AWB), adresă de livrare incompletă.
- **Reglabil per companie**: fiecare verificare se activează/arhivează, cu severitate și prag în zile, fără cod (**Sales → Configuration → Delivery Checks**).
- **AI care explică**: agentul grupează anomaliile după cauza comună (același produs lipsă, același curier, același client), dă fiecăreia prioritate 1–5, explicație și o acțiune concretă, plus un rezumat scurt al zilei; citește notele transferului, ultimele mesaje din chatter și situația stocului.
- **Fără dubluri și alerte perimate**: o anomalie regăsită se actualizează, una dispărută se rezolvă automat, una ignorată nu mai este raportată.
- **Rulare zilnică și la cerere**: acțiune planificată dimineața (digest pe e-mail și activități pentru agentul de vânzări pe anomaliile severe); la cerere din **Sales → Reporting → Check Orders & Deliveries** (perioadă, depozite, verificări, cu/fără analiză AI).
- **Lucru pe anomalii** (**Sales → Orders → Delivery Anomalies** sau **Inventory → Operations → Transfers → Delivery Anomalies**): Deschide document, Văzut, Rezolvat, Ignoră, Redeschide; comenzile și transferurile cu anomalii deschise au buton inteligent **Anomalies**.
- **Istoric**: **Sales → Reporting → Delivery Check Runs** cu numărători, stare AI, rezumat și retrimiterea digestului.
- **Setări** (**Settings → Sales → Daily Delivery Check**): perioada rulării zilnice, fereastra de verificare a stărilor (implicit 90 zile), destinatari, activități și severitate minimă, agentul AI, numărul maxim de anomalii trimise, limita zilnică de apeluri AI, anonimizarea clienților. Dacă AI-ul eșuează, rularea se încheie cu rezultatele pe reguli.
- **AI-ul nu modifică niciodată documente**: nu validează, nu anulează, doar grupează, prioritizează și explică.
- **AI nativ Odoo**: folosește agenții AI din Odoo 19 Enterprise și furnizorul configurat (OpenAI, Gemini sau Claude cu `deltatech_ai_anthropic`).

Fluxul detaliat, pas cu pas, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale_stock`
- `stock_delivery`
- `ai`

#### 4. Componente Cheie

**Modele**

- `sale.delivery.check.rule`: definiția unei verificări (activă, severitate, prag în zile), configurabilă per companie.
- `sale.delivery.check.run`: o rulare a verificării (perioadă, numărători, stare AI, rezumat), cu `mail.thread`; conține logica verificărilor și apelul către agent.
- `sale.delivery.check.issue`: anomalia găsită (document, client, agent de vânzări, severitate, grup și prioritate AI, stare).
- `sale.delivery.check.wizard` (tranzitoriu): lansarea verificării la cerere.
- `ai.agent`, `res.company`, `res.config.settings`, `sale.order`, `stock.picking`: extinse pentru agentul dedicat, setări, butonul Anomalies.

**Vizualizări**

- `view_sale_delivery_check_issue_list` / `_form` / `_search`: lista (grupată pe verificare sau grup AI), detaliul și filtrarea anomaliilor.
- `view_sale_delivery_check_run_list` / `_form` / `_search`: istoricul rulărilor.
- `view_sale_delivery_check_rule_list` / `_search`: configurarea verificărilor.
- `view_sale_delivery_check_wizard_form`: wizardul de verificare la cerere.
- `view_order_form_delivery_check`, `view_picking_form_delivery_check`: butonul inteligent Anomalies.
- `res_config_settings_view_form_delivery_check`: setările Daily Delivery Check.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_delivery_check_daily`: rulare zilnică (în jurul orei 05:00), trimite digestul și creează activitățile.
- `ir_cron_delivery_check_cleanup`: șterge zilnic rulările mai vechi de 90 de zile și anomaliile rezolvate văzute ultima dată înainte de acest prag.
- Date: agentul AI „Sale & Delivery Check AI", șablonul de e-mail al digestului, secvența rulărilor și regulile implicite.

#### 5. Conexiuni

- [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md): furnizor Claude; agentul de verificare folosește Claude Sonnet 5.5 implicit când e instalat.
