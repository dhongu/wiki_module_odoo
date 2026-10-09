# Terrabit IAP Server Line Counter

- **Nume Tehnic:** `terrabit_iap_server_line_counter`
- **Versiune:** `19.0.2.0.2`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_line_counter
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_line_counter`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Extinde serverul IAP Terrabit cu serviciul „Module Line Counter”, care permite numărarea liniilor de cod sursă ale modulelor instalate pe instanțele client. Din contul IAP al clientului se aduce lista modulelor instalate, se bifează cele care interesează și se cere clientului numărarea liniilor, iar rezultatul (pe modul și total) rămâne salvat pe cont. Este util pentru evaluarea volumului de cod personalizat al unui client, de exemplu pentru oferte de mentenanță sau migrare.

#### 2. Funcționalități Cheie

- Serviciu nou „Module Line Counter” (cod `line_counter`), creat automat ca înregistrare `iap.server.service`.
- Buton **Fetch Client Modules** pe contul IAP: apelează ruta `/iap/line_counter/modules` de pe instanța clientului și completează lista de module (nume tehnic, denumire, autor). Selecțiile existente se păstrează, iar modulele dezinstalate se elimină din listă.
- Opțiunea **Hide Odoo S.A. Modules** (activă implicit): omite modulele oficiale Odoo (core/enterprise), astfel încât rămân doar modulele Terrabit și ale terților. Modulele OCA rămân vizibile.
- Modulele raportate de client ca aflate direct în repo-ul principal (nu în submodul git) sunt marcate **Repo Module** și bifate automat; bifele puse manual pe submodule nu se scot niciodată la o nouă aducere a listei.
- Buton **Count Lines**: trimite către `/iap/line_counter/count` lista modulelor bifate (cel puțin unul obligatoriu) și salvează liniile per modul, totalul (**Total Lines**) și răspunsul brut în `end_data`.
- Tab-ul „Line Counter” apare pe contul IAP doar când serviciul contului este `line_counter`.
- Token-ul contului nu este scris în log la apelurile către client; ceilalți parametri sunt logați.

#### 3. Dependențe

- `terrabit_iap_server`

#### 4. Componente Cheie

**Modele**

- `iap.server.service` (extins): adaugă valoarea `line_counter` în `service_code`.
- `iap.server.account` (extins): câmpurile `line_counter_module_ids`, `line_counter_total`, `hide_official_modules`; metodele `action_fetch_client_modules`, `action_count_client_lines` și apelul JSON-RPC către client prin `iap_tools.iap_jsonrpc`.
- `iap.server.account.line.counter.module`: linie per modul al clientului (nume tehnic, denumire, autor, `repo_module`, `selected`, `lines`), ordonată descrescător după număr de linii. Acces de citire/scriere/creare/ștergere pentru `base.group_user`.

**Vizualizări**

- `view_iap_server_account_form_line_counter`: moștenește formularul contului IAP (`terrabit_iap_server.view_iap_server_account_form`); adaugă cele două butoane în antet și pagina „Line Counter” cu opțiunile, totalul și lista editabilă a modulelor.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni automate sau acțiuni server. Singura dată încărcată este serviciul `iap_server_service_line_counter`.

#### 5. Conexiuni

- [terrabit_iap_line_counter](../terrabit_iap_line_counter/index.md): partea de client, care expune rutele `/iap/line_counter/modules` și `/iap/line_counter/count` apelate de acest modul.
- [deltatech_line_counter](../deltatech_line_counter/index.md): modul înrudit pentru numărarea liniilor de cod.
- `terrabit_iap_server`: serverul IAP pe care se montează serviciul.
