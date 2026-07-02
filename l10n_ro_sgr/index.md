# Sistem Garanție-Returnare (SGR) România (localizat la `l10n_ro_sgr/index.md`)

- **Nume Tehnic:** `l10n_ro_sgr`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_sgr
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_sgr`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul implementează suportul contabil complet pentru **Sistemul Garanție-Returnare (SGR)**, instituit prin OUG 74/2022 și H.G. 1050/2022. Gestionează garanția de 0,50 RON per ambalaj pe facturi și comenzi de achiziție, conturile dedicate 461.SGR și 462.SGR, taxa specială de 0% pentru e-Factura (categoria UBL „O"), raportul de sold SGR și wizardurile de returnare ambalaje și decontare cu administratorul RetuRO.

## 2. Funcționalități Cheie

- **Configurare automată la instalare:** produs „Garanție SGR ambalaj" (0,50 RON), conturi 461.SGR și 462.SGR, taxă SGR 0% cu categoria UBL `O` și codul `VATEX-EU-O`.
- **Vânzări:** linia SGR apare automat pe facturile de vânzare, fără TVA (Art. 286 alin. 4 Cod Fiscal), cu marcare corectă în XML CIUS-RO.
- **Achiziții (PO):** inserare automată a liniei SGR pe comenzile de cumpărare, cu cascade delete la ștergerea liniei-părinte.
- **Raport sold SGR:** sold 461.SGR / 462.SGR per partener, cu filtre dată/companie și numărul de ambalaje în circulație.
- **Wizard returnare ambalaje:** generează credit note (`out_refund`) pentru ambalajele returnate de client.
- **Wizard decontare RetuRO:** creează și postează înregistrarea de decontare periodică a contului 461.SGR.

## 3. Dependențe

- `deltatech_sale_add_extra_line`
- `deltatech_purchase_add_extra_line`
- `account`
- `l10n_ro`
- `purchase`

## 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

### Vizualizări / Date

- `data/account_sgr_data.xml`: Date de configurare (produs SGR, conturi 461/462, taxa SGR).
- `views/account_move_views.xml`, `views/purchase_order_views.xml`: Liniile SGR pe facturi și comenzi.
- `views/sgr_report_views.xml`: Raportul de sold SGR.
- `views/sgr_wizard_views.xml`: Wizardurile de returnare și decontare RetuRO.
- `views/res_config_settings_views.xml`: Setările SGR.

### Acțiuni Automate / Acțiuni Server

- `post_init_hook`: Pregătește configurarea SGR (produs, conturi, taxă) la instalarea modulului.

## 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
