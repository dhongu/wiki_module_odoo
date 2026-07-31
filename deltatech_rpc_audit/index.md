# RPC Audit Log (localizat la `deltatech_rpc_audit/index.md`)

- **Nume Tehnic:** `deltatech_rpc_audit`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_rpc_audit
- **Cale Locală:** `odoo-addons/deltatech/deltatech_rpc_audit`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul înregistrează într-un jurnal (log) toate apelurile externe XML-RPC
și JSON-RPC primite de server, astfel încât administratorii pot audita ce
integrare apelează ce model și ce metodă, și de la ce adresă IP anume. Este
util pentru depanare, securitate și investigarea integrărilor terțe (de
exemplu conectori de e-commerce, aplicații mobile sau scripturi externe) fără
a afecta clientul web standard.

#### 2. Funcționalități Cheie

- Loghează fiecare apel către serviciul `object` (apelurile ORM reale) cu IP
  client, bază de date, utilizator, model, metodă și o reprezentare trunchiată
  a argumentelor, sub logger-ul `odoo.rpc.audit`; parolele/credențialele nu
  sunt niciodată logate.
- Determină adresa IP reală a clientului din antetul `X-Forwarded-For`, astfel
  încât apelurile din spatele unui reverse proxy (nginx, edge-ul Odoo.sh) nu
  sunt toate atribuite IP-ului proxy-ului, indiferent de opțiunea de server
  `proxy_mode`.
- Poate fi activat/dezactivat fără a dezinstala modulul, fie din cheia de
  configurare `rpc_audit_enabled` (pentru instalări self-hosted), fie din
  Parametrul de Sistem `rpc_audit.enabled` (funcționează și pe Odoo.sh, fără
  rebuild).
- Permite excluderea IP-urilor „zgomotoase" (health check-uri, monitorizare)
  prin cheia de configurare `rpc_audit_ignore_ips` sau prin Parametrul de
  Sistem `rpc_audit.ignore_ips` (separate prin virgulă, valorile din ambele
  surse se combină).
- Dacă logger-ul `odoo.rpc.audit` este dezactivat peste nivelul INFO, modulul
  nu face nicio muncă suplimentară (verificare ieftină înainte de orice
  procesare).

#### 3. Dependențe

- `rpc`

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări sau acțiuni automate — este un modul
strict tehnic, bazat pe controllere HTTP care extind controllerele native ale
modulului `rpc`.

**Controllere**

- `AuditXMLRPC` (extinde `XMLRPC` din `rpc`): suprascrie `_xmlrpc`, helper-ul
  comun folosit de rutele `/xmlrpc/<service>` și `/xmlrpc/2/<service>`, pentru
  a loga apelul înainte de a-l dispecera prin `dispatch_rpc`.
- `AuditJSONRPC` (extinde `JSONRPC` din `rpc`): re-declară ruta `/jsonrpc` ca
  să intercepteze și să logheze apelul, păstrând inclusiv avertismentul de
  deprecare emis nativ de controllerul core.
- `RPC` (moștenește din `AuditXMLRPC` și `AuditJSONRPC`): controller compozit
  care oglindește clasa `rpc.RPC` din modulul de bază.
- Funcții helper: `_client_ip()` (citește `X-Forwarded-For`), `_settings()`
  (setări efective combinate din fișierul de configurare și System
  Parameters, cu cache de 60 secunde per bază de date), `_log_rpc_call()`
  (formatează și scrie linia de log).

#### 5. Conexiuni

- `rpc`: dependință directă — modulul suprascrie controllerele XML-RPC/JSON-RPC
  definite acolo (fără pagină wiki proprie la data acestei ingestii).
