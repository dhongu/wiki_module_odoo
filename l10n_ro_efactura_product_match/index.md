# Romania - Potrivire articol la import e-Factura (localizat la `l10n_ro_efactura_product_match/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_product_match`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_efactura_product_match
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_product_match`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

La importul facturilor de cumpărare din SPV (e-Factura), Odoo standard nu caută niciodată codul propriu de articol dacă furnizorul trimite și codul lui. Linia rămâne fără articol, fără nicio eroare, deci nu intră în stoc și nu moștenește contul și taxele articolului. Modulul închide acest gol: adaugă în planul de căutare o treaptă nouă, care folosește codul nostru retrimis de furnizor în factură, astfel încât liniile să fie legate corect de nomenclatorul de articole.

#### 2. Funcționalități Cheie

- Căutare suplimentară a articolului după codul propriu din `BuyersItemIdentification` (BT-156), comparat cu **Referința internă** (`default_code`) a articolului.
- Treaptă nouă cu prioritatea 16, între căutarea după cod intern (15) și cea după denumire (20), astfel încât o potrivire exactă pe cod câștigă în fața celei aproximative pe denumire.
- Fără efecte secundare: rulează doar dacă treptele anterioare au eșuat și doar când BT-156 diferă de codul deja căutat; prioritatea codului de furnizor (`product.supplierinfo`) rămâne neschimbată.
- Ordinea completă de căutare: cod furnizor (`supplierinfo`, 5) → cod de bare (BT-157, 10) → cod intern (15) → **codul nostru din BT-156 (16)** → denumire (20) → predicție din facturile anterioare.
- Nu are meniuri, câmpuri sau setări proprii; este suficient să fie instalat. Verificarea se face pe factura importată (Contabilitate → Furnizori → Facturi), unde coloana opțională **Produs** trebuie să fie completată.
- Limită: dacă furnizorul nu trimite deloc BT-156, potrivirea rămâne în sarcina treptelor standard; se completează codul furnizorului în fila *Achiziții* a articolului. Facturile importate înainte de instalare nu se corectează retroactiv.
- Acoperă doar fluxul UBL (CIUS-RO); fluxul CII / Factur-X nu este tratat.
- Fluxul detaliat, verificările și erorile frecvente sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `product.product`: extins cu `_import_retrieve_product_from_buyers_item_id` (căutare după `default_code = buyers_item_id`) și cu suprascrierea `_get_retrieval_product_search_plan`, care adaugă treapta cu prioritatea 16.

**Vizualizări**

- Nu are vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_efactura_dedup](../l10n_ro_efactura_dedup/index.md): complementar în același flux de import din SPV (evită importul dublu); fără dependență în cod.
- [l10n_ro_efactura_import_assist](../l10n_ro_efactura_import_assist/index.md): complementar în același flux de import (controlul diferențelor față de comanda de achiziție); fără dependență în cod.
- `account_edi_ubl_cii`: parserul UBL standard care citește BT-155/BT-156 și apelează planul de căutare extins de acest modul.
