# Regularizare TVA România (localizat la `l10n_ro_vat_regularization/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_regularization`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_vat_regularization
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_vat_regularization`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul automatizează regularizarea TVA la finele perioadei contabile (lună sau trimestru), conform OMFP 1802/2014. Calculează automat soldurile conturilor de TVA deductibil (4426) și colectat (4427) și generează cu un singur clic nota contabilă de închidere, determinând dacă firma datorează TVA de plată (4423) sau are TVA de recuperat (4424). Operațiunea este obligatorie la depunerea decontului 300.

## 2. Funcționalități Cheie

- **Calcul automat al soldurilor TVA** pentru perioada selectată (4426 vs. 4427).
- **Generare notă de regularizare cu un clic:** închide 4426 și 4427 și determină netul.
- **TVA de plată (44231):** când 4427 > 4426, diferența se trece pe contul de TVA de plată.
- **TVA de recuperat (4424):** când 4426 > 4427, diferența se trece pe contul de TVA de recuperat.
- **Conformitate OMFP 1802/2014** art. 267–270 și Codul Fiscal.

## 3. Dependențe

- `account`
- `l10n_ro`

## 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

### Modele

- `l10n.ro.vat.regularization`: Gestionează calculul soldurilor TVA pe perioadă și generarea notei de regularizare.

### Vizualizări / Date

- `views/l10n_ro_vat_regularization_view.xml`: Interfața pentru lansarea și vizualizarea regularizării TVA.
- `security/ir.model.access.csv`: Drepturile de acces aferente.

### Acțiuni Automate / Acțiuni Server

*Nu sunt definite acțiuni automate; regularizarea se generează manual la finele perioadei.*

## 5. Conexiuni

- `l10n_ro_vat_refund`
- `l10n_ro_vat_group`
- `l10n_ro_vat_deductibility`
