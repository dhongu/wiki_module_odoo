# Romania - Stock Accounting Controls (localizat la `l10n_ro_stock_account_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_account_enhancement`
- **Versiune:** `19.0.0.0.7`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_account_enhancement
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_account_enhancement`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul aduce verificări suplimentare pentru evidența contabilă a stocurilor în contextul localizării românești. Pe de o parte, se asigură că mișcările de stoc nu se înregistrează cu un preț de cost egal cu zero, evitând astfel valorizări incorecte. Pe de altă parte, introduce o restricție la confirmarea facturilor de vânzare sau de achiziție care conțin produse stocabile, dar nu sunt legate de o comandă de vânzare (SO) sau de achiziție (PO). Restricția poate fi activată sau dezactivată din setările de configurare, oferind flexibilitate în funcție de practicile fiecărei companii.

#### 2. Funcționalități Cheie

- Verificare ca prețul unitar să fie diferit de zero la mișcările reale de stoc (de exemplu, livrarea unei mărfi fără cost): operația se oprește cu mesajul „Price unit is not set for product ...", iar livrarea rămâne în starea „Ready". Verificarea este mereu activă; nu se aplică calculelor pe un set gol de mișcări (de exemplu, retururile unei livrări care nu are). Poate fi oprită temporar (de exemplu, pentru un stoc inițial la cost zero) prin parametrul de sistem `l10n_ro_stock_account.skip_price_unit_check`.
- Restricție la confirmarea facturilor și a notelor de credit (vânzare/achiziție) care conțin produse stocabile fără referință la o comandă de vânzare (SO) sau de achiziție (PO). Liniile cu servicii sau consumabile nu sunt verificate.
- Posibilitatea de a activa/dezactiva restricția din Facturare → Configurare → Setări, secțiunea România, opțiunea „Check storable product line source" (se aplică la nivel de bază de date; valoarea este salvată în parametrul de sistem `l10n_ro_stock_account.check_storable_line_source`).
- Fluxul pas-cu-pas, cu capturi de ecran, se găsește în [Fișa Consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro_stock_account`
- `l10n_ro_config`

#### 4. Componente Cheie

Secțiune omisă: fișierul `readme/DESCRIPTION.md` este prezent și nu solicită explicit analiza codului pentru componente (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server), conform fluxului de ingestie din schemă.

#### 5. Conexiuni

- `l10n_ro_stock_account`: modulul de bază pentru contabilitatea stocurilor în localizarea românească, pe care acest modul îl extinde cu verificări suplimentare.
- `l10n_ro_config`: oferă cadrul de configurare al localizării românești unde este expusă opțiunea de activare/dezactivare a restricției.
