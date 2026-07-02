# Rambursare TVA (D300 Sold Negativ) România (localizat la `l10n_ro_vat_refund/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_refund`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_vat_refund
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_vat_refund`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul urmărește cererile de rambursare TVA rezultate din soldul negativ al decontului D300. Oferă o mașină de stări pentru ciclul de viață al cererii, monitorizează termenul legal de 45 de zile, calculează dobânzile de întârziere (0,02%/zi) și sprijină monografia contabilă specifică (conturile 4424/4426/5121) pentru evidențierea TVA de recuperat și a încasării rambursării.

## 2. Funcționalități Cheie

- **State machine cerere rambursare:** urmărirea statusului cererii de la depunere până la soluționare.
- **Termen legal 45 de zile:** monitorizarea termenului de soluționare și semnalarea depășirilor.
- **Calcul dobânzi de întârziere:** 0,02% pe zi pentru rambursările întârziate.
- **Monografie contabilă:** suport pentru conturile 4424 (TVA de recuperat), 4426 (TVA deductibil) și 5121 (banca) la încasarea rambursării.
- **Wizard de creare cerere** pornind de la soldul negativ D300, cu secvență dedicată.

## 3. Dependențe

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md)
- `mail`

## 4. Componente Cheie

### Modele

- `l10n.ro.vat.refund`: Cererea de rambursare TVA, cu state machine, termen, dobânzi și legături contabile.
- `l10n.ro.vat.refund.wizard`: Wizard pentru crearea cererii pe baza soldului negativ D300.
- `account.return`: Extins pentru integrarea cu fluxul de declarații/decont TVA.

### Vizualizări / Date

- `views/l10n_ro_vat_refund_views.xml`: Interfața de gestionare a cererilor de rambursare.
- `wizard/l10n_ro_vat_refund_wizard_views.xml`: Wizardul de creare cerere.
- `data/ir_sequence.xml`: Secvența pentru numerotarea cererilor.
- `data/ir_cron.xml`: Cron-ul de monitorizare termene/dobânzi.
- `data/return_checks.xml`: Verificări asociate decontului de TVA.

### Acțiuni Automate / Acțiuni Server

- **Monitorizare cereri rambursare:** cron pentru urmărirea termenului de 45 de zile și calculul dobânzilor de întârziere.

## 5. Conexiuni

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): sursa soldului negativ TVA care declanșează cererea de rambursare.
- [l10n_ro_vat_regularization](../l10n_ro_vat_regularization/index.md): regularizarea contabilă 4426/4427/4424.
- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): checklist de închidere și urmărirea documentelor ANAF.
