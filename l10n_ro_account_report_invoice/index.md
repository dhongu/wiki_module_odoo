# Romania - Raport factură

- **Nume Tehnic:** `l10n_ro_account_report_invoice`
- **Versiune:** `20.0.0.4.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_account_report_invoice
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_account_report_invoice
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul adaptează factura tipărită la cerințele legale din România: adaugă mențiunea privind lipsa ștampilei și a semnăturii și, când factura este în altă monedă decât cea a companiei, afișează totalurile și în moneda companiei.

#### 2. Funcționalități Cheie

- Comentariu pe factură despre ștampilă și semnătură, conform legii; textul este configurabil pe companie (câmp traductibil, setat din Setări).
- Totaluri în moneda companiei pentru facturile în valută.
- În șabloanele de raport se afișează numărul de înregistrare la Registrul Comerțului (NRC) al partenerului și conturile bancare marcate pentru tipărire.
- Modificările se aplică doar înregistrărilor românești (`is_l10n_ro_record`).

#### 3. Dependențe

- [l10n_ro_config](../l10n_ro_config/index.md)
- `sale`

#### 4. Componente Cheie

**Modele**

- `res.company`: câmpul `l10n_ro_no_signature_text`.
- `res.config.settings`: expune textul în Setări.
- `account.move`, `sale.order`: extinse cu `l10n.ro.mixin`.

**Vizualizări**

- `views/invoice_report.xml`: extinde șabloanele raportului de factură.
- `views/account_invoice_view.xml`: ajustări în formularul facturii.
- `views/res_config_settings_view.xml`: setarea textului fără semnătură.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_config](../l10n_ro_config/index.md): configurarea de bază a localizării.
