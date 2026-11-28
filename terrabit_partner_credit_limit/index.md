# Partner Credit Limit (localizat la `terrabit_partner_credit_limit/index.md`)

- **Nume Tehnic:** `terrabit_partner_credit_limit`
- **Versiune:** `20.0.1.6.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/terrabit_partner_credit_limit
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_credit_limit`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Gestionează limitele de credit ale clienților: blochează confirmarea comenzilor de vânzare când datoria clientului (plus comanda curentă) ar depăși limita stabilită sau când clientul are facturi restante. Derogarea se face controlat, prin roluri, iar excepțiile se pot da pe echipă de vânzări, pe partener sau pe tranzacție de plată. Reduce riscul financiar și ajută la controlul creanțelor pentru firmele care acordă termene de plată.

#### 2. Funcționalități Cheie

- **Limită pe firmă:** se folosește limita standard Odoo (*Facturare > Limite de credit*, activată la instalare prin opțiunea „Sales Credit Limit"); verificarea citește limita, datoria și restanța partenerului comercial (firma), nu ale contactului de pe comandă.
- **Blocaj la confirmare:** comanda e refuzată dacă datoria + comanda depășesc limita cu mai mult decât toleranța; clientul cu facturi scadente (peste **Zile de grație**) este considerat restant.
- **Derogări:** „Allow Over Credit?" pe partener (tab *Vânzări & Achiziții*) sau pe comandă (aprobare pe o sumă precisă, care cade dacă comanda crește peste ea); echipele de vânzări pot ignora limitele („Ignore credit limits").
- **Grupuri de acces:** „Manage credit limits" (editează limita, „Allow Over Credit?" și zilele de grație) și „Can approve sale order over credit limit" (ocolește verificarea la confirmare). Utilizatorii fără acest drept văd butonul „Req. confirm", care creează o activitate către responsabilul echipei.
- **Setări globale** (*Vânzări > Configurare > Setări*, secțiunea Limită de credit): toleranța, telefonul contabilității, tratarea termenului de plată „imediat" (verificat / scutit de limită / scutit de orice verificare), calculul datoriei din facturi în loc de soldul contabil, tipul de tranzacție de plată care scutește comanda, conturi suplimentare incluse în datorie (ex. `4118,413,418`), includerea comenzilor confirmate nefacturate și regula pentru clienții fără limită (nimic / doar restanțe / tot ce e deschis).
- **Protecție după confirmare:** schimbarea termenului de plată din „imediat" pe o comandă confirmată este permisă doar aprobatorilor.
- **Parametri de sistem fără câmp în Setări:** `credit_limit_check_supplier_invoices` și `terrabit_partner_credit_limit.skip_only_card`.

Fluxul pas-cu-pas, cu capturi și mesajele de eroare, este în [Fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account_payment`
- `sale_management`
- [terrabit_partner_payable_receivable](../terrabit_partner_payable_receivable/index.md)

#### 4. Componente Cheie

**Modele**

- `res.partner`: câmpurile de limită de credit, „Allow Over Credit?" și zilele de grație.
- `sale.order`: verificarea limitei și a restanței la confirmare, aprobarea pe sumă și solicitarea de aprobare.
- `sale.order.line`: ajustări pentru calculul comenzilor nefacturate.
- `crm.team`: opțiunea „Ignore credit limits".
- `mail.activity`: tip de activitate implicit pentru solicitarea de aprobare (suprascriere globală, pentru toate modelele).
- `res.company` / `res.config.settings`: setările globale de limită de credit.

**Vizualizări**

- `views/partner_view.xml`: câmpurile modulului pe formularul partenerului.
- `views/sale_order_view.xml`: „Allow Over Credit?", butonul „Req. confirm" și avertismentele pe comandă.
- `views/sale_team.xml`: opțiunea pe echipa de vânzări.
- `views/res_config_settings_views.xml`: setările globale.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`. La instalare, `data/ir.config_parameter.xml` creează parametrii implicit (toleranță 1, telefon `n/a`, termen imediat scutit) și `post_init_hook` activează limita standard pe companii.

#### 5. Conexiuni

- [terrabit_partner_payable_receivable](../terrabit_partner_payable_receivable/index.md) (dependență): afișează soldul clientului pe comandă, unde apare și avertizarea de depășire.
- [terrabit_partner_credit_limit_website](../terrabit_partner_credit_limit_website/index.md): aplică aceeași verificare la checkout-ul website-ului.
- [terrabit_partner_credit_limit_review](../terrabit_partner_credit_limit_review/index.md): punte opțională cu regulile de revizuire a comenzilor (limită depășită, facturi restante), mutate acolo.
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md): motorul de revizuire a comenzilor folosit de puntea de mai sus.
- `sales_team` (`crm.team`) și `mail`: echipa de vânzări cu excepția „Ignore credit limits" și activitatea „Req. confirm".
