# Romania - Subvenții și Fonduri Nerambursabile (FR-38) (localizat la `l10n_ro_grants/index.md`)

- **Nume Tehnic:** `l10n_ro_grants`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_grants
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_grants`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

MVP pentru FR-38 — Subvenții și Fonduri Nerambursabile conform OMFP 1802/2014 și IAS 20. Modulul gestionează contractele de finanțare nerambursabilă cu state machine, bugetul pe categorii de cheltuieli eligibile, tranșele de plată cu generare automată de note contabile (475/131/132) și recunoașterea veniturilor (manuală sau prin cron lunar liniar). Acoperă surse precum PNRR, Fonduri Structurale UE, programe naționale și ajutoare de minimis.

## 2. Funcționalități Cheie

- **Contract de finanțare nerambursabilă** cu state machine (draft → contractat → activ → finalizat).
- **Buget pe categorii de cheltuieli eligibile** cu urmărire realizat vs. aprobat și alertă la procentul configurat din buget consumat.
- **Tranșe de plată primite** cu generare automată notă `Dr 5121 = Cr 475/131/132`.
- **Recunoaștere venituri** (`Dr 475/131 = Cr 7584/7411`) — manuală sau prin cron lunar liniar.
- **Calcul cheltuieli eligibile** per categorie din AML-uri cu distribuție analitică pe proiect.
- **Cron lunar opțional** pentru recunoașterea liniară a subvențiilor pentru active (inactiv implicit).

## 3. Dependențe

- `account`
- `analytic`
- `mail`
- `l10n_ro`
- `[[l10n_ro_anaf_base]]`

## 4. Componente Cheie

### Modele

- `l10n.ro.grant`: contractul de finanțare nerambursabilă cu state machine, buget, tranșe și recunoașterea veniturilor.
- Modele asociate pentru categoriile de buget și tranșele de plată.

### Vizualizări / Date

- `views/l10n_ro_grant_views.xml`: vizualizările contractului de finanțare.
- `data/ir_cron.xml`: jobul programat de recunoaștere liniară a subvențiilor pentru active.

### Acțiuni Automate / Acțiuni Server

- Cron lunar (inactiv implicit): recunoașterea liniară a subvențiilor pentru active.

## 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_financial_notes]]`
- `[[l10n_ro_fixed_assets]]`
