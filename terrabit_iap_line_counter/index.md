# Terrabit IAP Line Counter (localizat la `terrabit_iap_line_counter/index.md`)

- **Nume Tehnic:** `terrabit_iap_line_counter`
- **Versiune:** `19.0.2.0.3`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_line_counter
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_line_counter`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul expune serverului IAP Terrabit inventarul modulelor instalate într-o instanță Odoo și numărul de linii de cod sursă ale fiecărui modul. Serverul îl poate interoga ca să afle ce module rulează la un client și cât de mari sunt, fără acces direct la instanță. Modulul nu are interfață pentru utilizatori (categorie „Hidden”) și este în stadiul Beta. Nu are `readme/DESCRIPTION.md`; sumarul provine din manifest și din cod.

#### 2. Funcționalități Cheie

- Înregistrează serviciul IAP „Module Line Counter” (`line_counter`) și creează automat, la instalare, un cont IAP pentru fiecare companie existentă.
- Endpoint `/iap/line_counter/modules` (POST, JSON-RPC): returnează modulele instalate (nume, denumire, autor) și dacă fiecare se află într-un submodul git (`true`), direct în repo-ul principal (`false`) sau în afara oricărui checkout git (`null`).
- Endpoint `/iap/line_counter/count` (POST, JSON-RPC): numără liniile de cod pentru modulele cerute (sau pentru toate cele instalate, dacă lista e goală) și returnează numărul pe modul plus totalul.
- Numărarea e de tip `cloc`: se iau în calcul doar liniile de cod din fișierele `.py`, `.xml`, `.js`, `.css`, `.scss`; liniile goale, comentariile și docstring-urile nu se numără. Sunt excluse directoarele `tests`, `i18n`, `migrations` și `static/lib`.
- Securitate: rutele acceptă doar tokenul contului IAP al serviciului `line_counter`. Tokenurile altor servicii IAP (SMS, autocomplete etc.) sunt respinse, comparația se face în timp constant, iar tokenul nu se scrie în log la o încercare eșuată.
- Limitare cunoscută (LINECOUNT-001, deschisă): markerii de comentariu din interiorul șirurilor de caractere (ex. `"/*"` în JS) pot face ca liniile următoare să fie excluse, deci totalurile pot fi subestimate.

#### 3. Dependențe

- `terrabit_iap`

#### 4. Componente Cheie

**Modele**

- `ir.module.module` (extins): `_iap_count_lines` parcurge sursa fiecărui modul de pe disc și numără liniile de cod; `_iap_module_in_submodule` stabilește dacă modulul se află într-un submodul git (pe baza `.git` și `.gitmodules`).

**Vizualizări**

- Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- `iap_service_line_counter` (înregistrare `iap.service`, `noupdate`): serviciul „Module Line Counter” cu `technical_name` `line_counter`, sold întreg.
- `post_init_hook`: creează un `iap.account` pentru fiecare companie, dacă nu există deja.
- Controller `LineCounterIapController` (`controllers/main.py`): rutele `/iap/line_counter/modules` și `/iap/line_counter/count`, cu `auth="none"` și validare prin token IAP.

#### 5. Conexiuni

- `terrabit_iap`: oferă infrastructura IAP pe care se înregistrează serviciul și conturile.
- Serverul IAP Terrabit (în afara acestui modul) interoghează rutele expuse; nu există alte legături funcționale verificate în cod.
