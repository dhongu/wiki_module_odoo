# Terrabit - DVI (localizat la `terrabit_dvi/index.md`)

- **Nume Tehnic:** `terrabit_dvi`
- **Versiune:** `19.0.1.1.0`
- **Cale:** `https://github.com/dhongu/l10n-romania/tree/19.0/terrabit_dvi`
- **Cale Locală:** `odoo-addons/l10n-romania/terrabit_dvi`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul gestionează Declarația Vamală de Import (DVI) pentru operațiunile de import de marfă din afara Uniunii Europene, făcând legătura între factura de achiziție externă și costurile vamale (landed cost). Pe baza datelor din DVI, modulul generează automat o înregistrare cu două linii (taxa vamală A00 și TVA-ul la import B00), respectând cadrul legal contabil românesc (Legea 82/1991, OMFP 1802/2014, Codul Fiscal și Regulamentul UE 2015/2447): factura furnizor se înregistrează la cursul BNR din data emiterii, cursul vamal lunar se folosește exclusiv pentru valoarea în vamă, taxe și TVA la import, iar toate înregistrările contabile rămân exclusiv în RON. Astfel, taxele vamale se capitalizează corect în costul de achiziție al mărfurilor, iar TVA-ul la import deductibil este evidențiat separat, cu trasabilitate completă de la comanda de achiziție până la stocul final.

#### 2. Funcționalități Cheie

- Face legătura între factura de achiziție externă și DVI (landed cost).
- Generează automat un DVI cu două linii și cu TVA (taxă vamală A00 și TVA la import B00).
- Suportă fluxul complet de import cu recepție în locație virtuală de tranzit („Transit/In-Coming") și vămuire prin DVI, în regim FOB.
- Capitalizează taxele vamale (A00) în costul de achiziție al mărfurilor prin repartizare ca landed cost (327 ← 371.tranzit).
- Evidențiază separat TVA-ul la import deductibil (B00) pe contul 4426.
- Înregistrează automat diferențele de curs valutar la plata facturii furnizor (conturile 665/765).
- Asigură toate înregistrările contabile exclusiv în RON, cu factura la cursul BNR și taxele/TVA la cursul vamal lunar.
- Asistă consultantul în alegerea Incoterm-ului (Incoterms® 2020) și impactul acestuia asupra momentului recepției și al landed costs.
- Necesită ca contul 447 să fie cont de reconciliere, pentru a putea fi închis prin bancă.

#### 3. Dependențe

- `stock_account`
- `account`
- `sale`
- `l10n_ro`
- `purchase_stock`
- `stock_landed_costs`

#### 4. Componente Cheie

Această secțiune a fost omisă deoarece fișierul `readme/DESCRIPTION.md` este prezent și nu solicită explicit analiza modelelor, vizualizărilor sau a acțiunilor automate. Conform schemei de ingestie, analiza codului pentru componente nu se efectuează în acest caz.

#### 5. Conexiuni

- `stock_landed_costs`: modulul Odoo de bază pentru repartizarea costurilor adiționale (landed costs) folosit la capitalizarea taxelor vamale.
- `l10n_ro`: localizarea contabilă românească, sursa pentru determinarea conturilor 446/447 utilizate la DVI.
- `l10n_ro_dvi`: modul cu funcționalitate similară, exclus prin manifest (`excludes`) — cele două nu pot coexista.
