# Deltatech - Schiță și vedere 3D pe liniile comenzii (Sketch 3D)

- **Nume Tehnic:** `deltatech_sketch_3d`
- **Versiune:** `20.0.1.5.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_sketch_3d
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sketch_3d`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul afișează pe linia comenzii de vânzare schița (SVG) unei ferestre, uși sau a unui panou, împreună cu vederea ei 3D. Schița este desenată de alt modul (de exemplu un configurator de produs sau importul unei oferte dintr-un program de ofertare); acest modul o arată în liniile comenzii, pe comanda tipărită și pe comanda clientului din portal. Clientul și vânzătorul văd astfel elementul comandat, pot să-l rotească, să-i deschidă canaturile și să-l secționeze pentru a vedea profilele.

#### 2. Funcționalități Cheie

- Coloana *Schiță* în liniile comenzii de vânzare: apare doar dacă cel puțin o linie are schiță; o schiță cu vedere 3D afișează cursor de mărire, iar un clic o deschide în 3D.
- **Schiță detaliată:** piesele ei poartă datele vederii 3D (`data-k` tip, `data-d` adâncime, canaturi, geamuri, secțiunile de profil folosite).
- **Vedere 3D (three.js)**, încărcată la primul clic: bara are titlul în stânga și comenzile pe un singur rând (sub titlu, pe ecran îngust), cu butonul rotund ✕ în colț, iar sugestia *Trage pentru a roti, rotița pentru zoom* rămâne deasupra până la prima rotire; tragere pentru rotire, rotița pentru zoom; *Deschidere*, *Rabatare* și *Oblon* mișcă canaturile; *Cer și podea* așază elementul sub un cer; *Secțiune* taie elementul la jumătatea înălțimii; *Închide* (sau Esc) revine.
- **Clic pe canat sau pe mâner** (din 20.0.1.4.0): deschide doar acel canat (rabatat sau oscilo-batant, după opțiunea aleasă), un al doilea clic îl închide; glisorul deschide toate canaturile împreună.
- **Vedere 3D încorporabilă în pagină** prin `embedSketch3d` (din 20.0.1.4.0): dimensionată de pagina gazdă; un alt element afișat în ea păstrează punctul de vedere și crește de la dimensiunea celui anterior. O folosește configuratorul de tâmplărie din portal.
- Schița apare lângă fiecare linie pe **comanda tipărită**.
- Pe **comanda clientului (portal)**, butonul **3D** de sub sau de lângă o schiță detaliată deschide aceeași vedere.
- **Secțiuni de profil** (*Vânzări → Configurare → Secțiuni de profil*, pentru administratorii de vânzări): conturul, camerele și oțelul unui profil, după codul lui. Tipuri: cadru, montant, canat, stulp, profil adăugat, cuplare. Profilele fără secțiune sunt desenate ca bare aproximative.
- **Citire din desenul DXF** al producătorului de profile (ex. `102.311.dxf`): conturul, camerele, dimensiunea și oțelul se citesc din fișier; o secțiune nouă își ia codul din numele fișierului. Stulpul nu se poate citi din desen, el se așază pe canatul lui. Codul trebuie să fie cel folosit de schițe; o secțiune adăugată ulterior apare în 3D după ce schița liniei este redesenată. Biblioteci necesare doar pentru DXF: `ezdxf` și `shapely` (importate la utilizare, intenționat absente din `external_dependencies`; fără ele modulul funcționează și refuză desenele cu un mesaj).
- Modul cu plată pe Odoo Apps (100 EUR, licență OPL-1, stadiu Beta). Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale`
- `portal`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): câmpul `sketch_shown`, care controlează afișarea coloanei Schiță.
- `sale.order.line` (extins): `sketch_svg` (schița SVG, stocată în rând), `sketch_has_3d` (calculat: schița are datele vederii 3D) și `sketch_title` (titlul vederii 3D).
- `sketch.profile.section`: secțiune de profil (cod, tip, lățime, înălțime, contur, camere, oțel, fișier DXF, sursă: desen DXF sau trasat).
- `ir.http` (extins): încarcă traducerile modulului în frontend.

**Vizualizări**

- `view_order_form_sketch`: coloana Schiță în liniile comenzii.
- `report_saleorder_document_sketch`: schița lângă linii în comanda tipărită.
- `sale_order_portal_content_sketch` / `portal_sketch`: schița și butonul 3D în portal.
- `profile_section_view_list`, `profile_section_view_form`, `profile_section_action`: lista, formularul și meniul secțiunilor de profil.

**Acțiuni Automate / Acțiuni Server**

- Nu există. Active JS: `sketch_3d_loader.esm.js` (încărcare leneșă a vizualizatorului, `embedSketch3d`), câmpul `sketch_field` în backend și interacțiunea `sketch_3d` în portal.

#### 5. Conexiuni

- `deltatech_window_configurator`: configuratorul de tâmplărie din portal, care încorporează vederea 3D prin `embedSketch3d` (fără pagină wiki încă).
