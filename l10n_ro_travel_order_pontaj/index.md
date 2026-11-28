# Romania - Ordin de deplasare în pontaj (localizat la `l10n_ro_travel_order_pontaj/index.md`)

- **Nume Tehnic:** `l10n_ro_travel_order_pontaj`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_travel_order_pontaj
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_travel_order_pontaj`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Leagă ordinul de deplasare de pontaj: zilele de delegație se scriu singure în foaia colectivă de prezență, fără introducere manuală.

#### 2. Funcționalități Cheie

- La aprobarea ordinului, fiecare zi lucrătoare a deplasării primește în pontaj codul **D** (delegație), ca o corecție pe zi, cu numărul ordinului la *Motiv*. Zilele libere din program și sărbătorile legale rămân cum le propune pontajul.
- Zilele se iau din perioada efectivă, dacă e completată, altfel din cea planificată; la modificarea perioadei efective zilele se refac.
- La anularea ordinului sau la readucerea în ciornă, zilele scrise de ordin se șterg; corecțiile manuale existente nu sunt înlocuite și nici șterse.
- Butonul **Pontaj (D)** pe ordin arată zilele scrise; îl văd doar cei cu rolul Concediu „Responsabil: Gestionați toate cererile”.
- Dacă luna de pontaj e închisă, acțiunile care ating zilele ei sunt refuzate până la redeschiderea lunii din **Luni pontaj**.
- Se instalează automat când sunt instalate ambele module. Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `l10n_ro_travel_order`
- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.travel.order` (extins): zilele de pontaj scrise de ordin, contor și acțiunile de aprobare, anulare, ciornă.
- `l10n.ro.hr.pontaj.override` (extins): legătura corecției către ordinul de deplasare.

**Vizualizări**

- `view_l10n_ro_travel_order_form_pontaj`: butonul **Pontaj (D)** pe ordin.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- `l10n_ro_travel_order_fleet`: cealaltă punte a ordinului de deplasare (flotă).
