# Romania - Închidere de inventar și note contabile

- **Nume Tehnic:** `l10n_ro_inventory_closing`
- **Versiune:** `20.0.1.2.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_inventory_closing
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_inventory_closing`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul înregistrează contabil rezultatul inventarierii stocurilor, conform legislației românești: OMFP 1802/2014 pentru tratamentul diferențelor de inventar și OMFP 2861/2009 pentru procesul-verbal de inventariere. Contabilul și gestionarul clasifică plusurile și lipsurile, generează notele contabile dintr-un singur wizard și tipăresc documentele cerute (proces-verbal, decizie de imputare, decizie de casare).

#### 2. Funcționalități Cheie

- **Cele patru tipuri de diferențe:** plus de inventar, minus neimputabil, minus imputabil și casare, plus minusul justificat (perisabilități în limită, furt dovedit), tratat fără ajustarea TVA.
- **Nota de stoc o singură dată pe linie**, la valoarea postată de mișcarea de inventar (FIFO / cost mediu): plusul se contabilizează Dr 3xx / Cr 607, minusurile și casările Dr 607 / Cr 3xx. Dacă mișcarea a postat deja nota la validare, wizardul nu o repetă.
- **Ajustarea TVA deduse** la lipsuri (Cod fiscal art. 304): Dr 635 / Cr 4426, la cota de la achiziție (editabilă pe linie); nu se aplică la minusul justificat și la casarea cu dovada distrugerii.
- **Imputarea minusurilor imputabile:** Dr 4282 (salariat) sau 461 (terț) / Cr 7581, la valoarea de înlocuire stabilită de comisie, fără TVA colectată.
- **Wizard „Generare note contabile”** (după validarea inventarului): alegerea jurnalului de operațiuni diverse, data notei (implicit data inventarului) și un sumar pe tipuri de diferențe.
- **Stare contabilă a inventarului** urmărită automat: Necontabilizat, Parțial contabilizat, Complet contabilizat; la complet, câmpurile devin doar pentru citire, iar butonul „Note” trimite la documentele generate.
- **Comisia de inventariere** (președinte, membri, gestionar, nr. și data PV, locul inventarierii) completată pe inventar.
- **Configurarea conturilor pe companie** (Setări → Companie → tab „Inventariere RO”): conturile de rezervă 607, 4282, 461, 7581, 635, 4426, plătitor de TVA și cota curentă de TVA.
- **Rapoarte PDF:** Proces-Verbal de Inventariere, Decizie de Imputare, Decizie de Casare. Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)
- `stock_account`
- `l10n_ro`
- `account`

#### 4. Componente Cheie

**Modele**

- `stock.inventory`: extins cu starea contabilă, notele generate, comisia de inventariere, gestionarul și datele procesului-verbal.
- `stock.inventory.line`: extins cu tipul diferenței, valoarea, persoana responsabilă, valoarea imputată, cota de TVA la achiziție, dovada distrugerii și marcajul de contabilizare.
- `stock.move`: extins pentru recunoașterea notei de stoc deja postate la validarea inventarului.
- `res.company`: extins cu conturile și parametrii de inventariere.
- `l10n.ro.inventory.accounting.wizard`: wizardul care generează și postează notele contabile.

**Vizualizări**

- `stock_inventory_form_inherit_l10n_ro`: câmpurile românești pe documentul de inventariere.
- `stock_inventory_line_tree_inherit_l10n_ro`, `stock_inventory_line_form_l10n_ro`: tipul diferenței, valorile și imputarea pe linii.
- `view_company_form_inherit_l10n_ro_inventory`: conturile de inventariere pe companie.
- `wizard/inventory_accounting_wizard_views.xml`: fereastra de generare a notelor contabile.
- `report/report_inventory_pv.xml`, `report/report_inventory_imputare.xml`, `report/report_inventory_casare.xml`: rapoartele PDF.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate; notele contabile se generează la cerere, prin wizard, după validarea inventarului.

#### 5. Conexiuni

- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md): obiectele de inventar (303/603/8035), tratate separat de stocurile inventariate aici.
- [l10n_ro_inventory_register](../l10n_ro_inventory_register/index.md): Registrul inventar poate prelua valoarea de inventar din listele validate aici.
- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): inventarierea mijloacelor fixe.
