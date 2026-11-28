# Romania - Import DVI from the SNI PDF

- **Nume Tehnic:** `l10n_ro_customs_dvi_import`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_customs_dvi_import
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_customs_dvi_import`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Preia declarația vamală de import (DVI) direct din PDF-ul tipărit de Sistemul Național de Import (SNI) și completează cu ea wizardul DVI de pe factura furnizorului, din [l10n_ro_customs_dvi](../l10n_ro_customs_dvi/index.md). Se evită transcrierea manuală a valorilor vamale.

#### 2. Funcționalități Cheie

- Din PDF se citesc: **MRN** și data acceptării (numărul și data DVI), **regimul vamal** (4000 sau 4200), **taxa vamală A00** (intră în costul mărfii prin landed cost), **baza și TVA B00** (transcrise, nu recalculate; la 4200 devine TVA reținut ca garanție, importul rămâne scutit) și cota de TVA, după care se propune taxa de achiziție.
- Pentru control se afișează: LRN, data liberului de vamă, moneda și cursul vamal, facturile din documentele justificative (N380) și metoda de plată.
- Verificări înainte de completare: documentul e o declarație SNI, importatorul e compania curentă, declarația nu e deja pe alt DVI, numărul de articole e cel din antet, iar sumele A00 și B00 de pe articole dau totalurile. Dacă una pică, nu se completează nimic.
- Avertisment în wizard dacă factura furnizorului nu apare printre facturile declarației.
- Flux: factura furnizorului confirmată, butonul **DVI**, câmpul **DVI PDF (SNI)**, verificarea taxei propuse (la TVA amânat se alege taxa de import cu taxare inversă), apoi **Apply**.
- PDF-ul se atașează pe DVI, cu un rezumat al valorilor citite în istoric.
- Necesită biblioteca Python `pdfminer.six`; pe servere cu `cryptography` veche se instalează păstrând versiunea existentă. Pașii cu capturi sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_customs_dvi](../l10n_ro_customs_dvi/index.md)
- Python: `pdfminer.six`

#### 4. Componente Cheie

**Modele**

- `account.invoice.dvi` (extins, wizard): câmpul de încărcare a PDF-ului, parsarea și verificările.

**Vizualizări**

- `view_account_invoice_dvi_form`: câmpul **DVI PDF (SNI)** și valorile citite, în wizardul DVI.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_customs_dvi](../l10n_ro_customs_dvi/index.md): wizardul DVI completat de acest modul.
