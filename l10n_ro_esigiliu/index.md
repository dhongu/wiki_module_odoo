# Romania - e-Sigiliu (sigilii electronice) (localizat la `l10n_ro_esigiliu/index.md`)

- **Nume Tehnic:** `l10n_ro_esigiliu`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_esigiliu
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_esigiliu`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține evidența sigiliilor electronice e-Sigiliu aplicate de autorități (ANAF/Vamă) pe transporturile rutiere de bunuri monitorizate, conform reglementărilor românești privind supravegherea fiscală a mărfurilor în tranzit. Nu necesită configurare și nu generează note contabile.

#### 2. Funcționalități Cheie

- Înregistrarea sigiliului cu număr unic per companie (constrângere SQL).
- Asocierea la un transfer de stoc: transportator, număr de înmatriculare, rută monitorizată și UIT e-Transport.
- Ciclu de viață **Ciornă → Aplicat → Eliminat**, prin **Aplică sigiliul** și **Elimină sigiliul**, cu data aplicării și a eliminării completate automat.
- Buton statistic **e-Sigiliu** (lacăt) pe formularul transferului, din **Inventar → Transferuri**, cu numărul de sigilii asociate.
- Listă centralizată în **Inventar → Raportare → Sigilii e-Sigiliu**, utilă pentru găsirea sigiliilor aplicate dar neeliminate.
- Acces prin grupurile standard Inventar (utilizator/manager).
- Faza 1: doar evidență locală; integrarea cu API-ul ANAF e-Sigiliu (sincronizare automată a statusului) este planificată pentru faza 2. Fluxul cu capturi este în fișa consultantului.

#### 3. Dependențe

- `stock`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.esigiliu`: sigiliul (număr unic per companie, transportator, vehicul, rută, UIT, date de aplicare/eliminare, stare) cu acțiunile `action_apply` / `action_remove`.
- `stock.picking` (extindere): `l10n_ro_esigiliu_ids`, contorul și acțiunea de afișare a sigiliilor transferului.

**Vizualizări**

- `views/l10n_ro_esigiliu_views.xml`: lista, formularul cu bara de stare și meniul din Inventar → Raportare.
- `views/stock_picking_views.xml`: butonul statistic pe transfer.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [l10n_ro_etransport_block](../l10n_ro_etransport_block/index.md): gestionează UIT-ul e-Transport al transferurilor; în e-Sigiliu câmpul UIT este text liber, fără legătură directă în cod.
