# Deltatech - Restrict Reports Access (localizat la `deltatech_restrict_reports/index.md`)

- **Nume Tehnic:** `deltatech_restrict_reports`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_restrict_reports
- **Cale Locală:** `odoo-addons/deltatech/deltatech_restrict_reports`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul limitează accesul la rapoartele Analiză Vânzări (Vânzări > Raportare) și Analiză Facturi (Contabilitate/Facturare > Raportare), independent de orice alt drept pe care utilizatorul îl are deja (Vânzător, Facturare, Contabilitate etc.). Este util atunci când clientul dorește ca anumiți utilizatori să vadă doar propriile vânzări/facturi în rapoarte, iar alții să vadă toate înregistrările, fără să umble la drepturile de acces standard pe documentele de bază.

#### 2. Funcționalități Cheie

- Două grupuri noi controlează vizibilitatea rapoartelor de analiză: **Rapoarte Vânzări/Facturi: doar propriile înregistrări** (vede doar comenzile/facturile unde este Vânzător) și **Rapoarte Vânzări/Facturi: toate înregistrările** (vede toate înregistrările).
- Un utilizator care nu face parte din niciunul dintre cele două grupuri nu vede nicio dată în cele două rapoarte, iar intrările de meniu corespunzătoare îi sunt ascunse.
- Nimeni nu primește automat vreunul dintre grupuri — atribuirea se face manual, din Setări > Utilizatori, conform cerinței fiecărui client.

#### 3. Dependențe

- `sale`
- `account`

#### 4. Componente Cheie

Modulul nu definește modele Python noi; funcționalitatea se implementează integral prin securitate declarativă (grupuri, reguli de înregistrare și restricția acțiunilor de meniu existente).

**Modele**

Nu sunt definite sau extinse modele. Regulile de acces vizează modelele existente `sale.report` (Analiză Vânzări) și `account.invoice.report` (Analiză Facturi), fără a le modifica structura.

**Vizualizări**

Nu sunt adăugate vizualizări noi. Sunt reutilizate ecranele standard de raportare din `sale` și `account`.

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron`, `base.automation` sau `ir.actions.server`. Modulul folosește:

- `res.groups.privilege` (`res_groups_privilege_restrict_reports`) și `ir.module.category` (`module_category_restrict_reports`): grupează cele două grupuri de acces sub o categorie dedicată "Restrict Reports".
- `group_restrict_reports_own` / `group_restrict_reports_all`: cele două grupuri de acces; al doilea îl implică pe primul.
- `ir.rule` `sale_report_restrict_rule` și `account_invoice_report_restrict_rule`: reguli globale (fără câmp `groups`, deci se combină prin AND cu orice altă regulă a utilizatorului) care restricționează domeniul pe `sale.report` (după `user_id`) și `account.invoice.report` (după `invoice_user_id`) în funcție de grupul deținut; un utilizator fără niciun grup primește domeniul `[(0, '=', 1)]` (zero rânduri, fără eroare de acces).
- Suprascrieri de `ir.actions.act_window` pe acțiunile standard de raportare (`sale.action_order_report_all`, `sale.action_order_report_salesperson`, `sale.action_order_report_products`, `sale.action_order_report_customers`, `account.action_account_invoice_report_all`, `account.action_account_invoice_report_all_supp`): setează `group_ids` la grupul `group_restrict_reports_own`, ascunzând meniurile pentru utilizatorii fără drept — control doar la nivel de UX, vizibilitatea reală a datelor fiind impusă de regulile `ir.rule` de mai sus. Aceste înregistrări se reaplică la fiecare `-u` al modulului, nu doar la instalare.

#### 5. Conexiuni

- `sale`: extinde raportul standard Analiză Vânzări (`sale.report`) cu restricție de acces pe grup.
- `account`: extinde raportul standard Analiză Facturi (`account.invoice.report`) cu restricție de acces pe grup.
