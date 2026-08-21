# Sistem Garanție-Returnare (SGR) România (localizat la `l10n_ro_sgr/index.md`)

- **Nume Tehnic:** `l10n_ro_sgr`
- **Versiune:** `19.0.1.3.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_sgr
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_sgr`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează suportul contabil complet pentru **Sistemul Garanție-Returnare (SGR)**, stabilit prin H.G. 1074/2021, republicată, și administrat de RetuRO Sistem Garanție-Returnare SA. Este destinat companiilor care comercializează produse cu ambalaje primare din sticlă, PET sau aluminiu și care au obligația legală de a colecta garanția de 0,50 RON/ambalaj de la clienți și de a o transfera periodic către RetuRO.

#### 2. Funcționalități Cheie

- **Configurare automată la instalare** — produs SGR, conturile 461001 și 462101, taxă 0% cu categoria UBL `O` și codul `VATEX-EU-O` pentru export e-Factura CIUS-RO.
- **Vânzări** — linia SGR pe facturile de vânzare: 0,50 RON/ambalaj, în afara sferei TVA (art. 315^5 alin. 2 Cod fiscal); nota contabilă Dr 4111 = Cr 461001. Linia SGR **nu** se inserează automat pe factură, ci trebuie adăugată manual de operator.
- **Achiziții (PO)** — linie SGR inserată automat pe comenzile de cumpărare pentru produsele cu `extra_product_id` = articol SGR; cascade delete la ștergerea liniei-părinte.
- **Raport sold SGR** — sold 461001 / 462101 per partener, cu numărul de ambalaje în circulație; accesibil din Contabilitate → Rapoarte → Sold SGR.
- **Wizard returnare ambalaje** — generează credit note (`out_refund`) cu linia SGR pentru ambalajele returnate de client.
- **Wizard decontare RetuRO** — creează și postează înregistrarea contabilă de decontare periodică (Dr 5121 = Cr 461001).
- **Integrare e-Factura CIUS-RO** — taxa SGR 0% primește automat `TaxCategory = O` și `TaxExemptionReasonCode = VATEX-EU-O` în XML-ul CIUS-RO.

#### 3. Dependențe

- [deltatech_sale_add_extra_line](../deltatech_sale_add_extra_line/index.md)
- [deltatech_purchase_add_extra_line](../deltatech_purchase_add_extra_line/index.md)
- `account`
- `l10n_ro`
- `purchase`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md` și `readme/USAGE.md`:

**Modele**

- `res.company`: câmpuri de configurare `l10n_ro_sgr_product_id`, `l10n_ro_sgr_sale_account_id`, `l10n_ro_sgr_purchase_account_id`, `l10n_ro_sgr_tax_id`.
- `res.config.settings`: expune setările SGR la nivel de companie.
- `account.move`: gestionează linia SGR pe facturile de vânzare/achiziție.
- `purchase.order`: inserare/eliminare automată a liniei SGR pe baza `extra_product_id`/`extra_qty` de pe produs.
- `product.template`: marcarea produselor cu ambalaj SGR.
- `l10n_ro_sgr_report` (wizard raport): calculează soldul 461001/462101 și numărul de ambalaje în circulație per partener.

**Wizard-uri**

- `sgr_return_wizard` (`wizard/sgr_return_wizard.py`): generează credit note de returnare ambalaje.
- `sgr_settlement_wizard` (`wizard/sgr_settlement_wizard.py`): generează nota de decontare periodică cu RetuRO.

**Vizualizări / Date**

- `data/account_sgr_data.xml`: fișier rezervat pentru date de referință statice (conturile, produsul și taxa SGR se creează prin `post_init_hook`, nu prin date XML).
- `views/account_move_views.xml`, `views/purchase_order_views.xml`: liniile SGR pe facturi și comenzi.
- `views/sgr_report_views.xml`: raportul de sold SGR.
- `views/sgr_wizard_views.xml`: wizardurile de returnare și decontare RetuRO.
- `views/res_config_settings_views.xml`: setările SGR.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): la instalare, pentru fiecare companie din România (sau, în lipsă, pentru toate companiile), creează produsul SGR, conturile 461001/462101 (doar dacă grupele 461/462 există deja în planul de conturi) și taxa SGR 0% cu categoria UBL `O`.

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): taxa SGR generată de modul folosește câmpurile UBL (`ubl_cii_tax_category_code`, `ubl_cii_tax_exemption_reason_code`) pentru exportul corect în XML CIUS-RO al e-Facturii.
