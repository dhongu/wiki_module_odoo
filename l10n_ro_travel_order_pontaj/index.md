# Romania - Ordin de deplasare în pontaj (localizat la `l10n_ro_travel_order_pontaj/index.md`)

- **Nume Tehnic:** `l10n_ro_travel_order_pontaj`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_travel_order_pontaj
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_travel_order_pontaj`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Leagă ordinul de deplasare de pontaj: zilele de delegație ale angajatului se scriu singure în foaia colectivă de prezență, cu codul **D**, la aprobarea ordinului. Contabilul nu mai trebuie să treacă manual delegațiile în pontaj, iar zilele se actualizează dacă se schimbă perioada sau angajatul.

#### 2. Funcționalități Cheie

- La aprobarea ordinului, fiecare zi lucrătoare a deplasării primește în pontaj codul **D** (delegație), ca o corecție pe zi. Zilele libere din program și sărbătorile legale rămân cum le propune pontajul.
- Zilele se iau din perioada efectivă, dacă e completată, altfel din cea planificată, de la plecarea până la întoarcerea în localitate (inclusiv pentru deplasările în străinătate), în fusul orar al angajatului.
- La schimbarea perioadei sau a angajatului, zilele se refac; la anularea ordinului sau la întoarcerea în ciornă, zilele scrise de ordin se șterg.
- O corecție scrisă de mână pe una din zile (concediu, zi lucrată în sărbătoare) nu este înlocuită și nici ștearsă.
- Pe ordin apare butonul **Pontaj (D)**, care listează zilele scrise în pontaj.
- Dacă luna de pontaj e închisă, modificarea ordinului care atinge zilele ei e refuzată; luna trebuie redeschisă din pontaj.
- Flux de utilizare: ordinul se creează și se aprobă ca de obicei (**Contabilitate → Furnizori → Ordine de deplasare**); dacă angajatul se întoarce mai devreme sau mai târziu, se completează sosirea efectivă.
- Se instalează automat când sunt instalate ambele module de care depinde (`auto_install`). Stadiu: Beta; licență OPL-1.

#### 3. Dependențe

- `l10n_ro_travel_order`
- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.travel.order` (extins): adaugă `pontaj_override_ids` și `pontaj_day_count`, calculul zilelor lucrătoare (`_get_pontaj_dates`), sincronizarea cu pontajul (`_sync_pontaj`), suprascrie `action_approve`, `action_cancel`, `action_draft` și `write` (reface zilele la schimbarea angajatului sau a datelor de plecare/întoarcere) și `action_view_pontaj_days`.
- `l10n.ro.hr.pontaj.override` (extins): câmpul `l10n_ro_travel_order_id` (ștergere în cascadă) marchează corecțiile create de ordin, pentru a le distinge de cele manuale.

**Vizualizări**

- `view_l10n_ro_travel_order_form_pontaj`: moștenește formularul ordinului de deplasare și adaugă în `button_box` butonul statistic **Pontaj (D)**, vizibil doar când există zile scrise.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md): oferă foaia de pontaj, codul D și corecțiile pe zi în care scrie acest modul.
