# Registrul Inventar (FR-50) (localizat la `l10n_ro_inventory_register/index.md`)

- **Nume Tehnic:** `l10n_ro_inventory_register`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_inventory_register
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_inventory_register`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Modulul generează Registrul Inventar anual pentru companiile din România, conform formularului cod 14-1-2 (OMFP 2634/2015). Creează un registru pe companie și an fiscal și produce linii recapitulative pe categoriile patrimoniale principale, pornind de la soldurile contabile postate la data raportului. Permite completarea valorii de inventar și a cauzelor diferențelor față de valoarea contabilă, acoperind cerința legală a registrului recapitulativ anual.

#### 2. Funcționalități Cheie

- Registru pe companie și an fiscal, cu generare automată a liniilor recapitulative pe categorii patrimoniale.
- Calcul al valorilor contabile pe solduri nete acolo unde natura categoriei o cere: imobilizările se diminuează cu amortizările și ajustările aferente, iar stocurile cu ajustările pentru depreciere din clasa 39.
- Completarea valorii de inventar și a cauzelor diferențelor față de valoarea contabilă.
- Preluarea valorii de inventar pentru categoria Stocuri din listele validate de inventariere fizică, atunci când este instalat `l10n_ro_inventory_closing`.
- Raport tipăribil conform formularului cod 14-1-2.

#### 3. Dependențe

- `account`
- `[[l10n_ro]]`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.inventory.register`: Registrul anual pe companie și an fiscal, cu liniile recapitulative pe categorii patrimoniale.

**Vizualizări / Date**

- `views/l10n_ro_inventory_register_views.xml`: Interfața de gestionare a registrelor de inventar.
- `report/report_inventory_register.xml` și `report/report_actions.xml`: Raportul tipăribil conform formularului cod 14-1-2.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate dedicate; generarea liniilor se face la cerere din interfața registrului.*

#### 5. Conexiuni

- `[[l10n_ro_inventory_closing]]`
- `[[l10n_ro_period_close_enhanced]]`
