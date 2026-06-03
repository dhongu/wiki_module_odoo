# Sale Feedback (localizat la `deltatech_sale_feedback/index.md`)

- **Nume Tehnic:** `deltatech_sale_feedback`
- **Versiune:** `19.0.1.0.5`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_feedback`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_feedback`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul automatizează colectarea de feedback de la clienți după vânzarea produselor. Pe baza facturilor emise, sistemul trimite automat clientului un e-mail prin care îi solicită părerea despre produsele cumpărate. Astfel, compania poate aduna opinii și evaluări de la clienți fără efort manual, ajutând la îmbunătățirea calității serviciilor și a relației cu clienții.

#### 2. Funcționalități Cheie

- Trimite automat clientului un e-mail pentru a-i cere feedback referitor la produsele vândute, pe baza facturilor emise.
- Trimiterea se face printr-o sarcină programată (cron job), inactivă la instalare, care expediază e-mailurile implicit la 3 zile după data facturii.
- Intervalul de trimitere poate fi configurat printr-un alt număr de zile, folosind parametrul de sistem `sale.days_request_feedback`.
- Utilizează un șablon de e-mail dedicat: „Invoice: request feedback".

#### 3. Dependențe

- `sale`
- `account`
- `portal_rating`
- `website_sale`

#### 4. Componente Cheie

**Acțiuni Automate / Acțiuni Server**

- Sarcină programată (`ir.cron`) — inactivă la instalare; trimite e-mailurile de solicitare feedback, implicit la 3 zile după data facturii (interval configurabil prin parametrul de sistem `sale.days_request_feedback`).

**Date / Șabloane**

- Șablonul de e-mail „Invoice: request feedback" (definit în `data/mail_data.xml`) — corpul mesajului trimis clientului pentru a solicita feedback.

#### 5. Conexiuni

- Niciuna documentată suplimentar față de dependențe.
