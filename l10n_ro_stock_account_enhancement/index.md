# Romania - Stock Accounting Enhancement (localizat la `l10n_ro_stock_account_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_account_enhancement`
- **Versiune:** `19.0.0.0.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_account_enhancement
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_account_enhancement`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Acest modul aduce verificări suplimentare pentru evidența contabilă a stocurilor în contextul localizării românești. Pe de o parte, se asigură că mișcările de stoc nu se înregistrează cu un preț de cost egal cu zero, evitând astfel valorizări incorecte. Pe de altă parte, introduce o restricție la postarea facturilor de vânzare sau de achiziție care conțin produse stocabile, dar nu sunt legate de o comandă de vânzare (SO) sau de achiziție (PO). Restricția poate fi activată sau dezactivată din setările de configurare, oferind flexibilitate în funcție de practicile fiecărei companii.

#### 2. Funcționalități Cheie

- Verificare ca prețul de cost să fie diferit de zero la mișcările de stoc.
- Restricție la postarea facturilor (vânzare/achiziție) care conțin produse stocabile fără referință la o comandă de vânzare (SO) sau de achiziție (PO).
- Posibilitatea de a activa/dezactiva această restricție din setările de configurare (Accounting -> România).

#### 3. Dependențe

- `l10n_ro_stock_account`
- `l10n_ro_config`

#### 4. Componente Cheie

Secțiune omisă: fișierul `readme/DESCRIPTION.md` este prezent și nu solicită explicit analiza codului pentru componente (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server), conform fluxului de ingestie din schemă.

#### 5. Conexiuni

- `l10n_ro_stock_account`: modulul de bază pentru contabilitatea stocurilor în localizarea românească, pe care acest modul îl extinde cu verificări suplimentare.
- `l10n_ro_config`: oferă cadrul de configurare al localizării românești unde este expusă opțiunea de activare/dezactivare a restricției.
