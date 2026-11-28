# Sale Feedback (localizat la `deltatech_sale_feedback/index.md`)

- **Nume Tehnic:** `deltatech_sale_feedback`
- **Versiune:** `20.0.1.0.9`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_feedback
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_feedback`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul cere clienților, prin e-mail, să evalueze produsele cumpărate, la câteva zile după emiterea facturii. E-mailul listează fiecare produs din factură cu imagine, link către pagina produsului și trei linkuri de evaluare, iar răspunsul clientului este înregistrat pe produs. Astfel firma primește feedback despre produse fără muncă manuală.

#### 2. Funcționalități Cheie

- Șablonul de e-mail **Invoice: request feedback** listează liniile facturii clientului (imagine, link către produs, cantitate, trei linkuri de evaluare: *Satisfied*, *Not satisfied*, *Highly Dissatisfied*); secțiunile și notele apar ca titluri. E-mailul este postat în chatter-ul facturii și trimis imediat.
- Fiecare linie de produs are propria evaluare pe șablonul de produs, înregistrată prin pagina standard `/rate` din Odoo.
- Acțiunea programată **Request Feedback** (inactivă la instalare) rulează zilnic și trimite e-mailul pentru facturile clienților postate cu un număr de zile în urmă (implicit 3), la companiile cu opțiunea **Email feedback after sale** activă.
- Întârzierea se citește din parametrul de sistem `sale.days_request_feedback` (`Setări > Tehnic > Parametri > Parametri de sistem`); nu are câmp în setări.
- Trimitere manuală: pe facturile clienților, `Acțiuni > Request feedback`, indiferent de opțiunea companiei.
- Șablon per companie: în `Vânzări > Configurare > Setări`, câmpul **Email Template Request Feedback**; fără el se folosește șablonul modulului.
- Dacă compania facturii are adresă de website, linkurile din e-mail se construiesc pe acea adresă, nu pe `web.base.url`.
- Fluxul pas cu pas și capturile sunt în fișa consultantului.

#### 3. Dependențe

- `sale`
- `account`
- `portal_rating`
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `account.move`: `cron_request_feedback` și `request_feedback`, trimiterea e-mailului; `get_base_url` alege adresa website-ului companiei.
- `account.move.line`: `rating_get_access_token`, token pentru linkurile de evaluare pe linie.
- `res.company`: `sale_feedback` și `sale_feedback_template_id`.
- `res.config.settings`: expune opțiunea, șablonul și parametrul `sale.days_request_feedback`.

**Vizualizări**

- `res_config_settings_view_form`: opțiunea și șablonul în setările de vânzări.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_feedback`: acțiunea programată zilnică **Request Feedback** (inactivă la instalare).
- `action_request_feedback`: acțiune server pe facturi, trimitere manuală.
- `mail_template_sale_feedback`: șablonul de e-mail al cererii de feedback.

#### 5. Conexiuni

- Niciuna documentată suplimentar față de dependențe.
