# Raport PRN - Zebra (Browser Print / Terrabit Connect) (localizat la `deltatech_report_prn_zebra_sdk/index.md`)

- **Nume Tehnic:** `deltatech_report_prn_zebra_sdk`
- **Versiune:** `19.0.1.3.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_report_prn_zebra_sdk`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_report_prn_zebra_sdk`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul adaugă tipărirea directă a etichetelor Zebra (format PRN/ZPL) generate de modulul [deltatech_report_prn](../deltatech_report_prn/index.md), fără a mai trece prin descărcarea manuală a fișierului `.prn`. Eticheta este trimisă automat la imprimantă prin agentul local Terrabit Connect sau, opțional, prin serviciul clasic Zebra Browser Print — astfel, operatorul de la depozit apasă „Print” și eticheta iese direct din imprimantă, fără pași suplimentari.

#### 2. Funcționalități Cheie

- Un „shim" JavaScript (`terrabit_browserprint.js`) care expune interfața globală `window.BrowserPrint` (`getLocalDevices` / `getDefaultDevice` / `device.send`), susținută de agentul Terrabit Connect (`http://127.0.0.1:8765/zebra/*`) — trimite ZPL la imprimantă prin rețea (TCP :9100) sau USB (spooler-ul sistemului), fără a necesita SDK-ul Zebra sau serviciul Zebra Browser Print.
- Comutator de activare și un selector de „Transport” în *Setări → Setări Generale → Integrări → Zebra* (dezactivat implicit). Transportul alege backend-ul: doar agentul Terrabit Connect, doar SDK-ul Zebra Browser Print, sau Auto (preferă agentul și trece pe SDK-ul Zebra dacă agentul nu raportează nicio imprimantă).
- Un handler de raport (înregistrat cu o secvență mai mică decât cel implicit) care, atunci când este activat, trimite ZPL-ul generat direct la imprimanta de pe stația de lucru (USB sau rețea), cu notificări de succes/eroare. Imprimanta este rezolvată per stație de lucru (localStorage → dispozitiv implicit al mașinii → imprimantă unică → dialog de selecție).
- Revenire automată (fallback) la descărcarea clasică a fișierului `.prn` (gestionată de `deltatech_report_prn`) atunci când comutatorul este oprit, modulul nu e instalat, transportul ales nu e accesibil sau nu se poate rezolva nicio imprimantă.

#### 3. Dependențe

- [deltatech_report_prn](../deltatech_report_prn/index.md)
- `base_setup`

#### 4. Componente Cheie

**Modele**

- `ir.http` (extins): în `session_info()` expune către clientul web comutatorul global „Browser Print" (`deltatech_report_prn.browser_print_enabled`) și transportul ales (`deltatech_report_prn.zebra_transport`), citite prin `sudo()` din `ir.config_parameter`, pentru ca handler-ul de raport PRN să aleagă între tipărirea directă și descărcarea clasică fără un apel RPC suplimentar.
- `res.config.settings` (extins): adaugă câmpurile `deltatech_browser_print_enabled` (boolean, comutator) și `deltatech_zebra_transport` (selecție: `auto` / `agent` / `sdk`), ambele salvate ca parametri de sistem (`config_parameter`).

**Vizualizări**

- `res_config_settings_view_form` (extindere prin xpath în blocul `integration`): adaugă secțiunea „Label printing (local agent)" cu comutatorul de activare și selectorul de transport (vizibil doar când comutatorul e activat).

**Active (assets) — `web.assets_backend`**

- `static/zebra/BrowserPrint.min.js`, `static/zebra/BrowserPrint-Zebra.min.js`: biblioteca oficială Zebra Browser Print SDK (folosită doar ca opțiune de transport, nu ca dependență obligatorie).
- `static/src/js/terrabit_browserprint.js`: shim-ul care expune `window.BrowserPrint` peste agentul Terrabit Connect.
- `static/src/js/zebra_printer_dialog.esm.js` + `static/src/xml/zebra_printer_dialog.xml`: dialogul de selecție a imprimantei, afișat când există mai multe dispozitive disponibile.
- `static/src/js/zebra_browser_print.esm.js`: handler-ul de raport care interceptează tipărirea PRN și trimite ZPL-ul către transportul ales.

#### 5. Conexiuni

- [deltatech_report_prn](../deltatech_report_prn/index.md): modulul care randează efectiv etichetele PRN/ZPL și gestionează descărcarea `.prn` de rezervă; `deltatech_report_prn_zebra_sdk` înlocuiește doar canalul de livrare către imprimantă (tipărire directă în loc de descărcare manuală).
