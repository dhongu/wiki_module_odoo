# Instrumente de Plată (Cecuri, Bilete la Ordin) (localizat la `l10n_ro_payment_instruments/index.md`)

- **Nume Tehnic:** `l10n_ro_payment_instruments`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payment_instruments
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payment_instruments`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează instrumentele de plată specifice (cecuri, bilete la ordin, cambii) conform Legii 58/1934 și Legii 59/1934. Urmărește fiecare instrument printr-o mașină de stări de la emitere/primire până la onorare sau refuz, generează automat notele contabile aferente fiecărei etape și oferă un scadențar cu alerte. Conturile contabile sunt auto-detectate din planul de conturi RO și pot fi suprascrise manual.

#### 2. Funcționalități Cheie

- Tipuri suportate: cec primit (5113), cec emis, bilet la ordin de primit (413) / de plătit (403), cambie de primit (413) / de plătit (403).
- Mașină de stări: Ciornă → În portofoliu → Remis la bancă → Onorat, cu ramuri Refuzat / Protestat și Andosat (pentru BO/cambii primite).
- Note contabile automate per etapă (ex.: cec primit Dr 5113 = Cr 4111 → onorare Dr 5121 = Cr 5113; BO emis Dr 401 = Cr 403 → plată Dr 403 = Cr 5121; andosare BO Dr 401 = Cr 413).
- Gestionarea refuzului: reactivarea creanței/datoriei și activitate de avertizare.
- Scadențar cu coloane "Zile până la scadență" și coduri de culoare în listă.
- Cron zilnic opțional de alertă cu X zile înainte de scadență (parametru `l10n_ro_payment_instruments.alert_days_before_due`, implicit 5 zile).
- Auto-detectare conturi 5113, 413, 403, 4111, 401, 5121 din planul RO, cu suprascriere manuală per instrument.

#### 3. Dependențe

- `account`
- `[[l10n_ro]]`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payment.instrument`: Instrumentul de plată cu mașina de stări, conturile asociate și generarea notelor contabile.

**Vizualizări / Date**

- `views/l10n_ro_payment_instrument_views.xml`: Interfața de gestionare și scadențarul instrumentelor.
- `data/ir_cron.xml`: Cron-ul zilnic de alertă scadență.
- `security/ir.model.access.csv`: Drepturile de acces.

**Acțiuni Automate / Acțiuni Server**

- Cron zilnic de alertă scadență: creează activități de avertizare cu un număr configurabil de zile înainte de scadența instrumentelor.

#### 5. Conexiuni

- `[[l10n_ro_leasing]]`
