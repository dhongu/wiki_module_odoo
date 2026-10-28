# Romania - Închidere de inventar și note contabile (localizat la `l10n_ro_inventory_closing/index.md`)

- **Nume Tehnic:** `l10n_ro_inventory_closing`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_inventory_closing
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_inventory_closing`
- **Ultima Ingestie:** `2026-10-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul înregistrează contabil rezultatele inventarierii stocurilor conform legislației românești: OMFP 1802/2014 pentru tratamentul diferențelor și OMFP 2861/2009 pentru procesul-verbal de inventariere. Este destinat contabililor și gestionarilor care fac inventarierea periodică. După validarea inventarului, generează notele contabile pentru cele patru tipuri de diferențe (plus, minus neimputabil, minus imputabil cu TVA, casare) și tipărește documentele aferente: procesul-verbal, decizia de imputare și decizia de casare.

#### 2. Funcționalități Cheie

- **Flux:** în **Inventar → Operații → Ajustări → Documente inventariere** se pornește inventarul, se completează **Cantitate fizică** pe linii, se completează comisia, se validează inventarul (stocul se ajustează la cantitățile numărate), apoi **Generare note contabile**.
- **Tipul diferenței pe linie:** setat automat (fără diferență, plus inventar, minus neimputabil implicit la minus) și modificabil manual la minus în *minus imputabil* sau *casare*. Valoarea diferenței = |diferență| × prețul standard al produsului; liniile cu valoare zero nu generează note.
- **Note contabile pe tip:** plus inventar (Dr 3xx / Cr cont de plusuri, de regulă 607), minus neimputabil (Dr cont de minusuri, de regulă 607 / Cr 3xx), minus imputabil (scoatere din gestiune, plus o notă de imputare cu creanță pe 4282, venit pe 7588 și TVA pe 4427), casare (Dr 6583 / Cr 3xx). Contul de stoc 3xx se ia din categoria produsului; dacă lipsește, generarea se oprește cu un mesaj.
- **Imputare cu TVA:** pentru minusurile imputabile se completează **Persoană responsabilă** și **Valoare imputată**; TVA se calculează cu o cotă configurabilă pe companie (implicit 21%).
- **Fereastra de generare:** se alege jurnalul (tip *Operațiuni diverse*) și data notei, iar sumarul arată numărul de plusuri, minusuri neimputabile, minusuri imputabile și casări. Se creează câte o notă pe tip, postată imediat.
- **Stare contabilă a inventarului:** Necontabilizat → Parțial contabilizat → Complet contabilizat; la complet, câmpurile devin readonly, iar butonul **Note** rămâne link către notele generate. Notele se pot anula (resetare la ciornă și anulare), iar liniile revin la necontabilizat.
- **Comisia de inventariere:** președinte, membri, gestionar, număr și dată proces-verbal, locul inventarierii.
- **Rapoarte PDF:** Proces-Verbal Inventariere (OMFP 2861/2009), Decizie Imputare, Decizie Casare.
- **Configurare:** în **Setări → Companie** (tab *Inventariere RO*) sau **Contabilitate → Configurare → Setări** (secțiunea *Inventariere RO*): conturile de plusuri, minusuri neimputabile, imputare (4282), venituri imputare (7588), TVA colectată (4427), cheltuieli TVA (635), casare (6583) și cota TVA.

#### 3. Dependențe

- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)
- `stock_account`
- `l10n_ro`
- `account`

#### 4. Componente Cheie

**Modele**

- `stock.inventory` (extins): stare contabilă, notele generate (`l10n_ro_account_move_ids`), comisia, gestionarul și datele procesului-verbal.
- `stock.inventory.line` (extins): tipul diferenței (`l10n_ro_difference_type`), valoarea diferenței, persoana responsabilă, valorile de imputare și TVA și marcajul de contabilizare.
- `res.company` (extins): conturile de inventariere (`l10n_ro_inv_*`) și cota TVA de imputare `l10n_ro_inv_vat_rate`.
- `l10n.ro.inventory.accounting.wizard` (wizard): generează notele pe tipuri de diferențe; verifică obligatoriu conturile de plusuri și minusuri, iar conturile de imputare și de casare când sunt necesare.

**Vizualizări**

- `stock_inventory_form_inherit_l10n_ro`, `stock_inventory_line_tree_inherit_l10n_ro`, `stock_inventory_line_form_l10n_ro`: câmpurile și butoanele românești pe inventar și pe liniile lui.
- `view_company_form_inherit_l10n_ro_inventory`: configurarea conturilor pe companie.
- `view_inventory_accounting_wizard_form`: fereastra de generare a notelor.
- Rapoarte: `action_report_inventory_pv`, `action_report_inventory_imputare`, `action_report_inventory_casare`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server; notele se generează prin asistent, după validarea inventarului.

#### 5. Conexiuni

- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md): infrastructura de inventariere cantitativă, extinsă de acest modul cu partea contabilă și documentele legale.
