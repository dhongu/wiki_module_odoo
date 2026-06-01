# Romania - D394 Point of Sale (localizat la `l10n_ro_anaf_d394_pos/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d394_pos`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d394_pos
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d394_pos`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Acest modul este o punte între declarația D394 și modulul Point of Sale, asigurând includerea corectă a bonurilor fiscale emise prin POS în declarație. Deoarece bonurile fiscale nu produc documente `out_receipt` în Odoo (comenzile nefacturate se agregă în nota contabilă a sesiunii), modulul reconstruiește contribuția POS direct din comenzile `pos.order`, evitând dubla numărare și păstrând jurnalul de TVA normal neatins. Se instalează automat când sunt prezente atât `l10n_ro_anaf_d394`, cât și `point_of_sale`.

#### 2. Funcționalități Cheie

- **Eliminarea notei de sesiune POS** din colectarea pe `account.move`, scopat doar la colectarea D394 (evită dubla numărare).
- **Construirea contribuției POS** la op1/op2 direct din comenzile `pos.order` nefacturate.
- **Numărători:** `nrBF` = numărul de bonuri (comenzi distincte), `nrAMEF` = jurnale POS distincte.
- **Tratarea retururilor (refund)** agregate cu semn negativ.
- **Rutare:** comandă nefacturată cu CUI → op1; fără CUI → op2; comandă facturată → deja în op1 prin `account.move`.
- **Instalare automată** (`auto_install`) când dependențele sunt prezente.

#### 3. Dependențe

- `[[l10n_ro_anaf_d394]]`
- `point_of_sale`

#### 4. Componente Cheie

**Vizualizări**

- `views/pos_config_views.xml`: opțiuni de configurare POS relevante pentru D394.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); colectarea POS se realizează în fluxul de generare D394.*

#### 5. Conexiuni

- `[[l10n_ro_anaf_d394]]`
- `[[l10n_ro_anaf_base]]`
