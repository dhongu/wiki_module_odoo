# Romania - Point of Sale (localizat la `l10n_ro_pos/index.md`)

- **Nume Tehnic:** `l10n_ro_pos`
- **Versiune:** `20.0.1.9.1`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_pos
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_pos`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Adaptează Punctul de Vânzare (POS) la cerințele din România: ieșirile din gestiune sunt contabilizate la fiecare mișcare de stoc, iar casierul este avertizat la vânzările în numerar care depășesc plafoanele legale.

#### 2. Funcționalități Cheie

- Dacă este instalat `l10n_ro_stock_account`, se generează note contabile la fiecare mișcare de ieșire din stoc; nota contabilă de închidere a sesiunii POS nu mai conține liniile de ieșire din gestiune.
- Avertisment pe ecranul de plată la vânzare în numerar de minimum 5000 lei („doar către persoane fizice”) și mesaj de eroare la depășirea a 10.000 lei.
- Raportul „Detalii vânzări” afișează și coloanele de cost de stoc, inclusiv pe rândurile de retur.
- Date suplimentare la pregătirea facturii din comanda POS.

#### 3. Dependențe

- `point_of_sale`
- `pos_stock`
- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

**Modele**

- `pos.order`: completări la valorile facturii (`_prepare_invoice_vals`).
- `pos.session`: conturi și linii de închidere pentru stoc.
- Clasa de raport `pos_order` (raportul de detalii vânzări).

**Vizualizări**

- `report_saledetails.xml`: șablonul raportului „Detalii vânzări” extins.
- Șablon OWL `PaymentScreenStatus` (extins) și `PaymentScreenStatus.esm.js`: avertismentele de plafon.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_config](../l10n_ro_config/index.md): configurarea localizării române.
- `l10n_ro_stock_account`: contabilitatea mișcărilor de stoc, folosită la închiderea sesiunii.
