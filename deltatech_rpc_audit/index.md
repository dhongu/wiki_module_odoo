# RPC Audit Log (localizat la `deltatech_rpc_audit/index.md`)

- **Nume Tehnic:** `deltatech_rpc_audit`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_rpc_audit
- **Cale Locală:** `odoo-addons/deltatech/deltatech_rpc_audit`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul înregistrează într-un jurnal (log) apelurile RPC externe primite
de server, astfel încât administratorii pot audita ce integrare apelează ce
model și ce metodă, și de la ce adresă IP anume. Acoperă atât endpoint-urile
vechi — **XML-RPC** (`/xmlrpc`, `/xmlrpc/2`) și **JSON-RPC** (`/jsonrpc`) —
cât și endpoint-ul modern **`/json/2/<model>/<method>`**, ceea ce contează
pentru că cele vechi sunt marcate ca deprecate în Odoo 19: pe măsură ce
integrările trec pe cel nou, un audit care ar urmări doar endpoint-urile vechi
ar deveni tăcut fără să semnaleze nimic. Este util pentru depanare, securitate
și investigarea integrărilor terțe (de exemplu conectori de e-commerce,
aplicații mobile sau scripturi externe) fără a afecta clientul web standard.

#### 2. Funcționalități Cheie

- Loghează fiecare apel către serviciul `object` (apelurile ORM reale prin
  XML-RPC/JSON-RPC clasic) cu IP client, bază de date, utilizator, model,
  metodă și o reprezentare trunchiată a argumentelor, sub logger-ul
  `odoo.rpc.audit`; parolele/credențialele nu sunt niciodată logate.
- Loghează și apelurile pe endpoint-ul modern `/json/2/<model>/<method>`, cu
  aceleași câmpuri, plus marcajul `via=json2` care permite distingerea celor
  două căi în timpul unei migrări, păstrând totuși un singur grep pentru toate
  apelurile.
- Sare peste apelurile `/json/2/ir.cron/acquire_job`: pe Odoo.sh acesta este
  motorul planificatorului care rulează într-o buclă strânsă, iar logarea lor
  ar îneca puținele linii pentru care există audit-ul.
- Determină adresa IP reală a clientului din antetul `X-Forwarded-For`, astfel
  încât apelurile din spatele unui reverse proxy (nginx, edge-ul Odoo.sh) nu
  sunt toate atribuite IP-ului proxy-ului (ex. `10.0.0.2`), indiferent de
  opțiunea de server `proxy_mode`.
- Poate fi activat/dezactivat fără a dezinstala modulul, fie din cheia de
  configurare `rpc_audit_enabled` (pentru instalări self-hosted), fie din
  Parametrul de Sistem `rpc_audit.enabled` (funcționează și pe Odoo.sh, fără
  rebuild). Dacă logger-ul `odoo.rpc.audit` este dezactivat peste nivelul
  INFO, modulul nu face nicio muncă suplimentară.
- Permite excluderea IP-urilor „zgomotoase" (health check-uri, monitorizare)
  prin cheia de configurare `rpc_audit_ignore_ips` sau prin Parametrul de
  Sistem `rpc_audit.ignore_ips` (separate prin virgulă, valorile din ambele
  surse se combină).

#### 3. Dependențe

- `rpc`

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări sau acțiuni automate — este un modul
strict tehnic, bazat pe controllere HTTP care extind controllerele native ale
modulului `rpc`.

**Controllere**

- `AuditJson2` (extinde `WebJson2Controller` din `rpc`): suprascrie
  `web_json_2_rpc`, ruta modernă `/json/2/<model>/<method>`, pentru a loga
  apelul (model, metodă, ids, argumente) înainte de a-l delega
  implementării native; ruta e moștenită fără redeclarare, ca să păstreze
  auth-ul și rezoluția „readonly" din core.
- `AuditXMLRPC` (extinde `XMLRPC` din `rpc`): suprascrie `_xmlrpc`, helper-ul
  comun folosit de rutele `/xmlrpc/<service>` și `/xmlrpc/2/<service>`, pentru
  a loga apelul înainte de a-l dispecera prin `dispatch_rpc`.
- `AuditJSONRPC` (extinde `JSONRPC` din `rpc`): re-declară ruta `/jsonrpc` ca
  să intercepteze și să logheze apelul, păstrând inclusiv avertismentul de
  deprecare emis nativ de controllerul core.
- `RPC` (moștenește din `AuditXMLRPC` și `AuditJSONRPC`): controller compozit
  care oglindește clasa `rpc.RPC` din modulul de bază; `AuditJson2` rămâne
  separat intenționat, la fel cum core ține `/json/2` într-un controller
  propriu.
- Funcții helper: `_client_ip()` (citește `X-Forwarded-For`), `_settings()` /
  `_settings_from_config()` / `_settings_from_param()` (setări efective
  combinate din fișierul de configurare și System Parameters, cu cache de 60
  secunde per bază de date), `_log_rpc_call()` (formatează și scrie linia de
  log pentru XML-RPC/JSON-RPC clasic), `_log_json2_call()` (echivalentul
  pentru endpoint-ul modern, cu filtrul `_JSON2_SKIP`).

#### 5. Conexiuni

- `rpc`: dependință directă — modulul suprascrie controllerele XML-RPC,
  JSON-RPC și `/json/2` definite acolo (fără pagină wiki proprie la data
  acestei ingestii).
