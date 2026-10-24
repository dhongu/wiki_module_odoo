# Romania - Import DVI din PDF-ul SNI (localizat la `l10n_ro_customs_dvi_import/index.md`)

- **Nume Tehnic:** `l10n_ro_customs_dvi_import`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_customs_dvi_import
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_customs_dvi_import`
- **Ultima Ingestie:** `2026-10-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul preia declarația vamală de import (DVI) direct din PDF-ul tipărit de Sistemul Național de Import (SNI) și completează automat wizardul DVI de pe factura furnizorului. Utilizatorul nu mai transcrie manual MRN-ul, regimul vamal, taxa vamală și TVA-ul de import, iar riscul de greșeli la introducere scade. Dacă documentul nu trece verificările, importul se oprește cu un mesaj și nu se completează nimic.

#### 2. Funcționalități Cheie

- Încărcarea PDF-ului în câmpul **DVI PDF (SNI)** din wizardul DVI, deschis cu butonul **DVI** de pe factura furnizorului confirmată.
- Din PDF se citesc: MRN-ul și data acceptării (devin numărul și data DVI), regimul vamal (4000 sau 4200), taxa vamală A00 (intră în costul mărfii prin landed cost), baza și TVA-ul B00 (transcrise din declarație, nu recalculate) și cota de TVA, după care se propune taxa de achiziție.
- La regimul 4200, B00 devine TVA-ul reținut ca garanție, iar importul rămâne scutit.
- Valori afișate pentru control sub câmp: LRN, data liberului de vamă, moneda și cursul vamal, facturile din documentele justificative (N380) și metoda de plată.
- Verificări înainte de completare: documentul e o declarație de import SNI; importatorul e compania curentă; declarația nu e deja înregistrată pe alt DVI; numărul de articole citite e cel din antet; sumele A00 și B00 de pe articole dau totalurile declarației.
- Avertisment dacă factura furnizorului nu apare printre facturile declarației.
- Declarația nu arată dacă TVA-ul s-a plătit în vamă sau e amânat: la amânare (certificat de amânare) se alege manual taxa de import cu taxare inversă.
- PDF-ul se atașează pe DVI, iar în istoric rămâne un rezumat al valorilor citite.
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_customs_dvi](../l10n_ro_customs_dvi/index.md)
- Bibliotecă Python externă: `pdfminer.six`

#### 4. Componente Cheie

**Modele**

- `account.invoice.dvi` (extins, model tranzitoriu): adaugă câmpurile `dvi_file`, `dvi_filename` și `dvi_import_info`, citirea PDF-ului la schimbarea fișierului (`_onchange_dvi_file`) și completarea DVI-ului la `do_create_dvi`.
- `tools/sni_dvi.py` (bibliotecă, nu model): parser al PDF-ului SNI bazat pe `pdfminer.six`, cu validarea totalurilor declarației.

**Vizualizări**

- `view_account_invoice_dvi_form` (moștenește `l10n_ro_customs_dvi.view_account_invoice_dvi_form`): adaugă câmpul de încărcare a PDF-ului și zona cu valorile citite.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_customs_dvi](../l10n_ro_customs_dvi/index.md): modulul de bază al DVI, al cărui wizard este completat din PDF.
