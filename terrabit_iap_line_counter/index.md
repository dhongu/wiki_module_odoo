# Terrabit IAP Line Counter (localizat la `terrabit_iap_line_counter/index.md`)

- **Nume Tehnic:** `terrabit_iap_line_counter`
- **Versiune:** `20.0.2.0.4`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_iap_line_counter
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_line_counter`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Expune serverului Terrabit IAP numărul de linii de cod sursă ale modulelor instalate într-o bază de date client. Serverul poate astfel să afle ce module are instalate clientul și cât cod conțin. Modulul nu are readme de descriere; sumarul provine din manifest și cod.

#### 2. Funcționalități Cheie

- **Serviciu IAP „Module Line Counter”**: se înregistrează la instalare (cod tehnic `line_counter`, sold întreg).
- **Lista modulelor instalate**: ruta `/iap/line_counter/modules` returnează numele, denumirea, autorul și dacă modulul se află într-un submodul git.
- **Numărarea liniilor**: ruta `/iap/line_counter/count` numără liniile de cod (stil cloc, fără linii goale și comentarii) din fișierele `.py`, `.xml`, `.js`, `.css`, `.scss`; sunt excluse `tests`, `i18n`, `migrations` și `static/lib`. Fără listă de module se numără toate cele instalate.
- **Autentificare**: apelurile sunt acceptate doar cu tokenul contului IAP.
- **Bug cunoscut (LINECOUNT-001, P2, deschis)**: marcajele de comentariu din interiorul șirurilor de caractere pot face ca liniile următoare să nu fie numărate, deci totalurile pot fi subestimate.

#### 3. Dependențe

- [terrabit_iap](../terrabit_iap/index.md)

#### 4. Componente Cheie

**Modele**

- `ir.module.module` (extins): metodele de numărare a liniilor și de detectare a submodulelor git.

**Vizualizări**

- Nu are vizualizări; expune doar rute JSON-RPC.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [terrabit_iap](../terrabit_iap/index.md): clientul IAP de bază.
- [terrabit_iap_server](../terrabit_iap_server/index.md): serverul care consumă datele.
