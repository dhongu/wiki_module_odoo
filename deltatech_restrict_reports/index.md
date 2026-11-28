# Restrict Reports Access (localizat la `deltatech_restrict_reports/index.md`)

- **Nume Tehnic:** `deltatech_restrict_reports`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_restrict_reports
- **Cale Locală:** `odoo-addons/deltatech/deltatech_restrict_reports`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul limitează cine vede datele rapoartelor Analiză Vânzări (Vânzări > Raportare) și Analiză Facturi (Contabilitate/Facturare > Raportare), independent de celelalte drepturi ale utilizatorului (Vânzător, Facturare, Contabilitate etc.). Este util când anumiți utilizatori trebuie să vadă doar propriile vânzări și facturi, iar alții pe toate, fără a umbla la drepturile standard pe documentele de bază.

#### 2. Funcționalități Cheie

- Două grupuri noi: **Rapoarte Vânzări/Facturi: doar propriile înregistrări** (comenzile/facturile unde utilizatorul este vânzător) și **Rapoarte Vânzări/Facturi: toate înregistrările**.
- Un utilizator fără niciunul dintre grupuri vede cele două rapoarte goale, fără eroare de acces.
- Nimeni nu primește automat vreun grup: după instalare, toți utilizatorii, administratorii inclusiv, văd rapoartele goale până la atribuire. Atribuirea se face manual, din Setări > Utilizatori, fila Drepturi de acces, secțiunea **Restrict Reports**.
- Sunt filtrate cele două rapoarte de analiză și butonul **Sold** de pe produse (calculat din Analiză Vânzări); comenzile, facturile, butonul **Invoiced** de pe clienți și rapoartele contabile nu sunt filtrate.
- Meniul Vânzări > Raportare cere în continuare dreptul standard de administrator Vânzări; modulul nu schimbă accesul la meniuri.
- Fluxul pas-cu-pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `sale`
- `account`

#### 4. Componente Cheie

Modulul nu definește modele Python noi; funcționalitatea se implementează prin securitate declarativă.

**Modele**

- Sunt vizate modelele existente `sale.report` și `account.invoice.report`, fără modificarea structurii lor.

**Vizualizări**

- Nu sunt adăugate vizualizări; se reutilizează ecranele standard de raportare din `sale` și `account`.

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron`, `base.automation` sau `ir.actions.server`. Modulul definește:

- `group_restrict_reports_own` / `group_restrict_reports_all`: cele două grupuri, al doilea îl implică pe primul, grupate sub privilegiul `res_groups_privilege_restrict_reports`.
- `sale_report_restrict_rule` și `account_invoice_report_restrict_rule` (în `security/ir.access.csv`): restricții globale, fără grup, pe operația de citire. Domeniul se filtrează după `user_id` (`sale.report`) și `invoice_user_id` (`account.invoice.report`) pentru grupul „propriile”, nu filtrează pentru grupul „toate”, iar fără grup nu returnează niciun rând.
- Suprascrieri pe acțiunile standard de raportare din `sale` și `account`, care limitează meniurile la grupul „propriile”; control doar la nivel de interfață, datele fiind protejate de restricțiile de mai sus.

#### 5. Conexiuni

- `sale`: restricționează raportul standard Analiză Vânzări (`sale.report`).
- `account`: restricționează raportul standard Analiză Facturi (`account.invoice.report`).
