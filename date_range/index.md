# Intervale de date

- **Nume Tehnic:** `date_range`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/others_addons/tree/20.0/date_range
- **Cale Locală:** `odoo-addons/others_addons/date_range`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Permite definirea unor intervale de date globale (luni, trimestre, exerciții financiare etc.), folosite la filtrarea valorilor în liste. Pentru dezvoltatori oferă și un mixin care adaugă în căutare un câmp de tip perioadă, utilizabil ca orice câmp relațional.

#### 2. Funcționalități Cheie

- Tipuri de intervale (**Setări > Tehnic > Date ranges > Date Range Types**) și intervale propriu-zise (**Date Ranges**).
- Wizard **Generate Date Ranges** pentru perioade recurente: se alege data de final sau numărul de intervale, iar durata, unitatea de timp, prefixul numelui și data de start vin din tipul de interval.
- Intervalele apar în filtrul personalizat pentru orice câmp date/datetime: tipul este oferit ca operator („in <tip>"), iar intervalul ca valoare.
- Pe tipul de interval, fila Generation permite valori implicite pentru wizard și generare automată, făcută de o sarcină programată zilnică.
- Pentru dezvoltatori: moștenirea `date.range.search.mixin` adaugă câmpul Period în căutare; implicit lucrează pe câmpul `date`, schimbabil prin `_date_range_search_field` (ex. `invoice_date`).

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- `date.range`: intervalul de date.
- `date.range.type`: tipul intervalului, cu setările de generare.
- `date.range.generator` (wizard): generează intervale recurente.
- `date.range.search.mixin` (abstract): mixin pentru câmpul de căutare pe perioadă.

**Vizualizări**

- `view_date_range_list`, `view_date_range_form_view`, `view_date_range_search`: intervalele.
- `view_date_range_type_list`, `view_date_range_type_form_view`, `view_date_range_type_search`: tipurile de intervale.
- `date_range_generator_view_form`: wizard-ul de generare.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_autocreate`: rulează zilnic și generează intervale noi pentru tipurile configurate cu generare automată.

#### 5. Conexiuni

- Folosit ca dependență de alte module care lucrează cu perioade (rapoarte, filtre pe luni/trimestre).
