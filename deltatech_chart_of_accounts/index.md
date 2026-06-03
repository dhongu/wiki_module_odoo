# Chart of Accounts (localizat la `deltatech_chart_of_accounts/index.md`)

- **Nume Tehnic:** `deltatech_chart_of_accounts`
- **Versiune:** `19.0.0.0.6`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_chart_of_accounts
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chart_of_accounts`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul extinde funcționalitatea de gestiune a planului de conturi din Odoo, fiind dedicat în special inițializării și corecției soldurilor inițiale la implementări noi și sincronizării lor cu sisteme externe (balanțe de verificare existente). Față de metoda standard Odoo (un singur articol contabil sau import de solduri de deschidere), modulul permite compararea soldurilor curente din Odoo cu soldurile externe și înregistrarea doar a diferențelor. Oferă un flux de lucru clar (ciornă / postat), trasabilitate completă între sesiunea de sincronizare și articolele contabile generate, sincronizare la nivel de partener pentru conturile de creanțe și datorii, precum și suport pentru contabilitatea storno conform standardelor românești, prin marcarea automată a valorilor negative de debit sau credit ca tranzacții storno.

#### 2. Funcționalități Cheie

- Sincronizare incrementală a soldurilor: compară soldurile curente din Odoo cu cele externe și postează doar diferențele.
- Import al planului de conturi printr-o acțiune dedicată (`action_import_chart_of_accounts`).
- Inițializare la nivel de partener: soldurile pot fi sincronizate detaliat pe parteneri, util pentru creanțe și datorii.
- Suport pentru contabilitate storno: valorile negative de debit/credit sunt marcate automat ca tranzacții storno, asigurând conformitatea cu standardele contabile românești.
- Flux de lucru cu stări „Ciornă" și „Postat": generare linii, revizuire, postare diferențe și revenire la ciornă (care șterge automat articolele contabile generate).
- Trasabilitate: legătură directă între înregistrarea de sincronizare și toate articolele contabile generate, pentru audit.
- Posibilitatea introducerii valorilor externe manual sau prin importul standard Odoo (CSV/Excel).

#### 3. Dependențe

- `base`
- `account`

#### 4. Componente Cheie

**Modele**

- `sync.chart.of.accounts`: model principal de sincronizare; generează liniile de comparație (debit/credit/sold) până la o dată dată, gestionează stările ciornă/postat și păstrează legătura cu articolele contabile generate.
- `import.chart.of.accounts`: linia de sincronizare/import care reține valorile Odoo alături de valorile externe (debit/credit extern) și postează diferențele, generând articolele contabile (inclusiv storno acolo unde este cazul).
- `account.move.line` (extins): implementează logica de storno — la setarea unei valori negative de debit sau credit, tranzacția este marcată automat ca storno.
- `account.move` (extins): articolul părinte este de asemenea marcat ca storno când conține linii storno.

**Vizualizări**

- `import_chart_of_accounts_view.xml`: vizualizările pentru liniile de import/sincronizare a planului de conturi (introducerea valorilor externe, postarea diferențelor).
- `sync_chart_of_accounts_view.xml`: vizualizarea formular/listă a sesiunii de sincronizare (generare linii, afișare, postare diferență, revenire la ciornă) accesibilă din Contabilitate > Configurare > Conturi > Sincronizare Plan de Conturi.

**Acțiuni Automate / Acțiuni Server**

- `action_import_chart_of_accounts`: acțiune de import al planului de conturi (referită în DESCRIPTION.md).

#### 5. Conexiuni

- `account`: modulul de contabilitate Odoo pe care îl extinde, prin articolele contabile și planul de conturi.
- `l10n_ro`: relevant pentru implementările pe localizarea românească, unde se folosesc inițializarea soldurilor și contabilitatea storno.
