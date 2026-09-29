# Print Queue (Terrabit Connect) (localizat la `deltatech_print_queue/index.md`)

- **Nume Tehnic:** `deltatech_print_queue`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_print_queue
- **Cale Locală:** `odoo-addons/bitshop/deltatech_print_queue`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul permite tipărirea etichetelor (ZPL) și a documentelor (PDF) direct din Odoo pe imprimantele din depozit sau magazin, fără IoT Box, la fel de bine on-premise și pe odoo.sh. Odoo nu comunică niciodată cu imprimanta: pune un job în coada stației Terrabit Connect la care este conectată imprimanta, iar stația interoghează Odoo prin HTTPS, tipărește local și raportează rezultatul. Astfel serverul nu trebuie să vadă imprimanta, iar în rețeaua clientului nu se deschide niciun port. Modulul are la bază `mdtrade_print`, realizat de Alexandru Grecu (MD Trade Concept SRL).

#### 2. Funcționalități Cheie

- **Imprimante atașate unei stații:** instalate pe stația de lucru (USB, spooler; conexiune „sistem”) sau Zebra accesată direct în rețea (TCP 9100), cu dimensiunile rolei de etichete (lățime, înălțime, rezoluție). Limbaj: *Etichete (ZPL)* pentru Zebra, *Documente (PDF)* pentru laser/inkjet. Se configurează la **Setări → Terrabit Connect → Imprimante**.
- **Orice raport către o imprimantă:** pe raport (**Setări → Tehnic → Rapoarte**) se setează câmpul „Print queue printer”. Tipărirea din meniul **Print** sau dintr-un buton trimite jobul în coadă, în loc să descarce fișierul. Rapoartele text (etichetele ZPL standard din Inventar și Producție, `qweb-prn`) merg la o imprimantă de etichete, cele PDF la una de documente.
- **Siguranța etichetelor:** ZPL-ul ajunge brut în firmware, deci o etichetă ar putea reconfigura definitiv imprimanta. Etichetele randate de Odoo trec printr-o listă de comenzi permise (allow-list); ZPL-ul primit de la curier trece printr-o listă de comenzi interzise (deny-list: `^JU`, `^CC`/`~CC`, `~JR` etc.).
- **Feedback către utilizator:** cel care a tipărit primește o notificare la trimiterea în coadă și una roșie, cu motivul, dacă stația raportează eșec (imprimantă offline, nume necunoscut).
- **Etichetă de calibrare** și buton **Print test label** pe imprimantă, pentru a verifica rola configurată față de cea fizică (cadrul trebuie să cadă pe marginea etichetei).
- **Urmărirea joburilor:** **Setări → Terrabit Connect → Jobs** sau butonul **Jobs** de pe imprimantă; tipuri „Print label (ZPL)” și „Print document (PDF)”. Un job de tipărire nu se reia automat dacă rezultatul se pierde (stația nu ține încă evidența a ce a tipărit, deci s-ar dubla): rămâne în starea *Claimed*; după verificarea imprimantei se folosește **Retry** dacă nu a ieșit nimic.
- **Configurarea stației:** Terrabit Connect (Tauri, versiune ulterioară 1.6.21) înregistrat ca stație; în profil trebuie `TERRABIT_POLL_JOBS=1`. Cu funcția Labels activă, stația interoghează la 3 secunde (`TERRABIT_POLL_SEC` modifică intervalul). Pentru PDF: pe Windows SumatraPDF (portabil, `TERRABIT_SUMATRA_PATH=C:\TerrabitConnect\SumatraPDF.exe`), pe macOS/Linux `lp` (CUPS). Pentru ZPL nu e nevoie de nimic în plus.
- **Apel din cod:** `printer.print_zpl(zpl, name=..., record=...)`, `printer.print_pdf(pdf_bytes, filename=..., record=...)`, iar pentru ZPL primit de la curier (AWB) `source="external"` (deny-list în loc de allow-list). Alegerea imprimantei per depozit, utilizator sau document se face suprascriind `ir.actions.report._print_queue_get_printer(records)`.
- **Drepturi:** utilizatorii care tipăresc nu au nevoie de drepturi pe coada de joburi; joburile sunt create de modul după verificarea dreptului de citire asupra înregistrării, deci conținutul sau imprimanta unui job nu pot fi modificate prin RPC.

#### 3. Dependențe

- [deltatech_tc](../deltatech_tc/index.md)
- `web`

#### 4. Componente Cheie

**Modele**

- `deltatech.print.printer`: imprimanta atașată unei stații (limbaj, conexiune, nume în sistem, rola de etichete); metodele `print_zpl` și `print_pdf`.
- `deltatech.tc.job` (extins): joburile Terrabit Connect primesc tipurile de tipărire (ZPL/PDF) și notificarea utilizatorului la eșec.
- `ir.actions.report` (extins): câmpul „Print queue printer” și redirecționarea tipăririi către coadă (`_print_queue_get_printer`).

**Vizualizări**

- `view_deltatech_print_printer_form` / `_list` / `_search`: gestiunea imprimantelor (meniu în Setări → Terrabit Connect).
- `view_deltatech_tc_job_form_print` / `view_deltatech_tc_job_search_print`: joburile de tipărire în formularul și căutarea joburilor.
- `act_report_xml_view_print_queue`: câmpul imprimantei pe formularul raportului.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni automate sau cron-uri; regula multi-companie `rule_deltatech_print_printer_company` limitează imprimantele la compania curentă.

#### 5. Conexiuni

- [deltatech_report_prn](../deltatech_report_prn/index.md): rapoartele text `qweb-prn` (ZPL) pe care coada le poate trimite la imprimantă.
- [deltatech_report_prn_zebra_sdk](../deltatech_report_prn_zebra_sdk/index.md): alternativă, tipărire ZPL direct din browser.
- [deltatech_delivery_iot](../deltatech_delivery_iot/index.md): soluție IoT pentru livrări; coada oferă tipărire locală fără IoT Box (legătură de ecosistem, nu dependență în cod).
