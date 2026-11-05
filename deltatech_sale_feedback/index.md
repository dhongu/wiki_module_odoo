# Sale Feedback (localizat la `deltatech_sale_feedback/index.md`)

- **Nume Tehnic:** `deltatech_sale_feedback`
- **Versiune:** `19.0.1.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_feedback
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_feedback`
- **Ultima Ingestie:** `2026-11-05`

#### 1. Sumar

Modulul cere clienților, prin email, să evalueze produsele cumpărate, la câteva zile după emiterea facturii. Fiecare linie de factură apare în email cu imaginea produsului, un link către pagina lui și trei legături de evaluare, astfel încât compania adună opinii fără efort manual. **Atenție:** pe 19.0 trimiterea nu funcționează în starea actuală a codului (vezi limitările de mai jos).

#### 2. Funcționalități Cheie

- **Email de feedback pe factură**: șablonul *Invoice: request feedback* listează liniile facturii de client, fiecare cu imaginea produsului, link către pagina produsului, cantitatea și trei legături de evaluare (*Satisfied*, *Not satisfied*, *Highly Dissatisfied*). Liniile de secțiune și de notă apar ca titluri.
- **Evaluare pe produs**: fiecare linie de produs are propria înregistrare de rating pe șablonul de produs, iar un clic pe o legătură de evaluare înregistrează ratingul clientului pentru acel produs prin pagina standard `/rate` din Odoo.
- **Trimitere programată**: acțiunea programată *Request Feedback* (inactivă la instalare) rulează zilnic și trimite emailul pentru facturile de client datate cu un număr de zile în urmă, implicit 3. Întârzierea se citește din parametrul de sistem `sale.days_request_feedback` (*Settings > Technical > Parameters > System Parameters*).
- **Trimitere manuală**: pe facturile de client, *Actions > Request feedback* trimite emailul pentru facturile selectate.
- **Legături pe site-ul companiei**: când compania facturii are adresă de site, modulul încearcă să construiască legăturile din email pe acea adresă, în locul lui `web.base.url` al bazei de date.
- **Limitări**:
  - pe 19.0 trimiterea nu funcționează: codul apelează încă `xmlid_to_res_id` și `message_post_with_template`, care nu mai există în Odoo, deci atât acțiunea programată, cât și *Request feedback* se opresc cu eroare; subiectul, expeditorul, destinatarul și limba șablonului folosesc încă sintaxa veche `${...}`, care nu mai este randată;
  - opțiunea *Email feedback after sale* și șablonul ei din *Sales > Configuration > Settings* se salvează, dar nu sunt folosite: emailul folosește mereu șablonul propriu al modulului;
  - acțiunea programată ia toate facturile de client de la acea dată, postate sau nu.

#### 3. Dependențe

- `sale`
- `account`
- `portal_rating`
- `website_sale`

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`; apelurile învechite menționate în limitări au fost confirmate în `models/account_invoice.py`.

**Modele**

- `account.move` (extins): `cron_request_feedback()` și `request_feedback()`, trimiterea emailului de feedback.
- `account.move.line` (extins): `rating_get_access_token()`, pentru legăturile de evaluare.
- `mail.template`, `res.company`, `res.config.settings` (câmpul `days_request_feedback`, parametrul `sale.days_request_feedback`) și `ir.config_parameter`: extinderi pentru șablon, companie și setări.

**Vizualizări**

- `views/account_move_view.xml`: acțiunea *Request feedback* pe facturi.
- `views/res_config_settings_views.xml`: opțiunile din setările de vânzări.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_feedback` (*Request Feedback*, `ir.cron`): inactivă la instalare, rulează zilnic și apelează `cron_request_feedback()`.
- Șablonul de email *Invoice: request feedback* (`data/mail_data.xml`).

#### 5. Conexiuni

- Nicio conexiune suplimentară documentată în afara dependențelor declarate.
