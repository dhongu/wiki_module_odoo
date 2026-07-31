# Leasing Financiar și Operațional (167/21x) (localizat la `l10n_ro_leasing/index.md`)

- **Nume Tehnic:** `l10n_ro_leasing`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_leasing
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_leasing`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează contractele de leasing financiar și operațional conform OMFP 1802/2014. Pentru fiecare contract generează un grafic de rambursare cu defalcare pe capital, dobândă și TVA și produce automat notele contabile aferente activării și ratelor lunare. Include un cron opțional pentru postarea automată a ratelor scadente și o mașină de stări pentru ciclul de viață al contractului.

#### 2. Funcționalități Cheie

- Leasing financiar (art. 360 OMFP 1802/2014): activare contract Dr 21x = Cr 167, cu contul de imobilizări 21x selectabil per contract (2131 echipamente, 212 construcții, 2133 mijloace de transport etc.).
- Notă lunară per rată pentru leasing financiar: Dr 167 + Dr 666 + Dr 4426 = Cr 401.
- Leasing operațional: notă lunară per rată Dr 612 + Dr 4426 = Cr 401.
- Generare automată a graficului de rambursare prin formula anuității constante (dobândă fixă), cu defalcare capital / dobândă / TVA per rată.
- Editare manuală a graficului (import grafic din contract).
- Postare individuală sau în batch a ratelor scadente, cu cron opțional pentru automatizare.
- Mașină de stări contract: Ciornă → Activ → Finalizat (sau Anulat).

#### 3. Dependențe

- `account`
- `[[l10n_ro]]`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.leasing.contract`: Contractul de leasing cu graficul de rate și logica de generare a notelor contabile.

**Vizualizări / Date**

- `views/l10n_ro_leasing_contract_views.xml`: Interfața de gestionare a contractelor și a graficelor de rambursare.
- `data/ir_cron.xml`: Definește cron-ul de postare a ratelor scadente.
- `security/ir.model.access.csv`: Drepturile de acces.

**Acțiuni Automate / Acțiuni Server**

- Cron scadențar leasing: postează automat ratele scadente ale contractelor active.

#### 5. Conexiuni

- `[[l10n_ro_payment_instruments]]`
