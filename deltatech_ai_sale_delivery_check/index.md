# Verificare zilnică comenzi și livrări cu AI (localizat la `deltatech_ai_sale_delivery_check/index.md`)

- **Nume Tehnic:** `deltatech_ai_sale_delivery_check`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_ai_sale_delivery_check
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_sale_delivery_check`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

În fiecare dimineață echipa află ce comenzi și livrări cer atenție și de ce. Modulul verifică comenzile de vânzare și livrările din ziua precedentă (sau din orice perioadă) cu reguli precise, apoi cere unui agent AI să grupeze, să prioritizeze și să explice anomaliile găsite. Nimeni nu mai trebuie să răsfoiască sute de comenzi ca să găsească livrarea întârziată, factura uitată sau expediția fără AWB.

#### 2. Funcționalități Cheie

- **Reguli întâi, AI apoi:** unsprezece verificări deterministe găsesc anomaliile, exact și gratuit; AI primește doar anomaliile găsite, o singură dată pe rulare, nu tot portofoliul de comenzi.
- **Unsprezece verificări gata făcute:** comandă fără livrare, livrare întârziată (severitate crescătoare cu întârzierea), backorder vechi, livrat mai mult decât comandat, livrat dar nefacturat, facturat dar nelivrat, comandă blocată ca livrată parțial, gata dar neexpediată, livrare în risc (așteaptă stoc, termen apropiat), expediat fără număr de urmărire, adresă de livrare incompletă.
- **Reglabil pe companie:** fiecare verificare poate fi activată sau arhivată, cu severitate și prag în zile, fără cod (**Vânzări → Configurare → Verificări livrări**).
- **AI care explică:** agentul grupează anomaliile după cauza comună (același produs fără stoc, același curier, același client), dă fiecăreia prioritate de la 1 la 5, o explicație și o acțiune concretă și scrie un rezumat al zilei; citește notele transferului, ultimele mesaje din chatter și situația stocului.
- **Fără duplicate, fără alerte vechi:** o anomalie regăsită este actualizată, una dispărută se rezolvă automat, una ignorată nu mai este raportată.
- **Rezumat zilnic și activități:** o rulare programată trimite pe e-mail rezumatul (sumar, numere, anomalii principale) și creează activitate pentru agentul de vânzări pe cele severe.
- **Verificare la cerere:** **Vânzări → Raportare → Verifică comenzi și livrări**, cu perioadă, depozite, verificări și opțiunea de analiză AI.
- **Lucrul cu anomaliile:** **Vânzări → Comenzi → Anomalii livrare** (și din Inventar); acțiuni Deschide document, Văzut, Rezolvat, Ignoră, Redeschide; butonul inteligent **Anomalii** pe comenzi și transferuri; istoric în **Delivery Check Runs**, cu retrimiterea rezumatului.
- **Cost și confidențialitate:** limită zilnică de apeluri AI, număr maxim de anomalii trimise, anonimizare opțională a clienților; dacă AI eșuează, rularea se încheie cu rezultatele din reguli. AI nu modifică, validează sau anulează niciodată un document.
- Folosește agenții AI din Odoo Enterprise și LLM-ul serviciului Odoo AI (credite IAP).

#### 3. Dependențe

- `sale_stock`
- `stock_delivery`
- `ai`

#### 4. Componente Cheie

**Modele**

- `sale.delivery.check.rule`: regula de verificare configurabilă (severitate, prag în zile, activă/arhivată).
- `sale.delivery.check.run`: o rulare de verificare, cu contoare, stare AI și rezumat.
- `sale.delivery.check.issue`: anomalia găsită, cu severitate, document, client, agent de vânzări și grup/prioritate AI.
- `sale.delivery.check.wizard`: asistentul pentru verificarea la cerere.
- `ai.agent`, `res.company`, `res.config.settings`, `sale.order`, `stock.picking` (extinderi): agentul, setările pe companie și butonul inteligent Anomalii.

**Vizualizări**

- Liste/formulare pentru anomalii, rulări și reguli; extinderi pe comandă și transfer (buton **Anomalii**); setări în **Setări → Vânzări → Verificare zilnică livrări**; asistentul de verificare.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_delivery_check_daily`: rularea zilnică, cu trimiterea rezumatului și crearea activităților.
- `ir_cron_delivery_check_cleanup`: curățarea periodică a datelor vechi.
- `ai_agent_delivery_check`: agentul AI *Sale & Delivery Check AI* (instrucțiuni traductibile, versiune în română livrată).

#### 5. Conexiuni

- `ai`: agentul AI nativ Odoo Enterprise folosit pentru analiză.
