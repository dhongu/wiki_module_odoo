# Romania - e-Sigiliu (Electronic Seals) (localizat la `l10n_ro_esigiliu/index.md`)

- **Nume Tehnic:** `l10n_ro_esigiliu`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_esigiliu
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_esigiliu`
- **Ultima Ingestie:** `2026-07-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează sigiliile electronice e-Sigiliu aplicate de autorități (ANAF/Vamă) pe transporturile rutiere de bunuri monitorizate, conform reglementărilor românești privind supravegherea fiscală a mărfurilor în tranzit.

#### 2. Funcționalități Cheie

- Înregistrarea sigiliului electronic cu număr unic per companie, validat printr-o constrângere SQL.
- Asocierea sigiliului la un transfer de stoc (`stock.picking`): transportator, număr de înmatriculare, rută monitorizată și UIT e-Transport.
- Ciclu de viață complet: **Ciornă → Aplicat → Eliminat**, cu înregistrarea automată a datei de aplicare și de eliminare.
- Buton statistic **e-Sigiliu** pe formularul de transfer, cu numărul de sigilii asociate.
- Meniu dedicat **Inventar → Raportare → e-Sigiliu Seals** pentru vizualizarea centralizată a tuturor sigiliilor.
- Acces bazat pe grupurile standard Inventar (utilizator/manager).

> **Notă (faza 1):** modulul acoperă evidența locală a sigiliilor. Integrarea directă cu API-ul ANAF e-Sigiliu (sincronizare automată a statusului) este planificată pentru faza 2, pe același mecanism OAuth2 folosit de `l10n_ro_edi`.

#### 3. Dependențe

- `stock`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.esigiliu`: modelul principal — evidența unui sigiliu electronic (număr unic per companie, transportator, vehicul, rută monitorizată, UIT e-Transport, date de aplicare/eliminare, stare draft/applied/removed) și acțiunile `action_apply` / `action_remove` pentru tranziția de stare.
- `stock.picking` (extindere): adaugă `l10n_ro_esigiliu_ids` (One2many către sigilii) și `l10n_ro_esigiliu_count`, plus acțiunea `action_view_l10n_ro_esigiliu` pentru afișarea sigiliilor asociate transferului.

**Vizualizări**

- `view_l10n_ro_esigiliu_list`: listă cu numărul sigiliului, transferul, transportatorul, vehiculul, UIT-ul, datele de aplicare/eliminare și starea (badge colorat).
- `view_l10n_ro_esigiliu_form`: formular cu butoane de acțiune **Apply Seal** / **Remove Seal** în antet și statusbar draft/applied/removed.
- `view_picking_form_esigiliu`: extinde formularul de transfer de stoc (`stock.view_picking_form`) cu un buton statistic (pictogramă lacăt) care afișează numărul de sigilii asociate.
- `menu_l10n_ro_esigiliu`: meniu **Inventar → Raportare → e-Sigiliu Seals**.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

Nu au fost identificate module conexe cu legătură funcțională verificată în cod (câmpul `uit` este text liber, fără referință directă la modulele de e-Transport).
