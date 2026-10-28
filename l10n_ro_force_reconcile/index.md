# Romania - Reconciliere forțată între conturi diferite (localizat la `l10n_ro_force_reconcile/index.md`)

- **Nume Tehnic:** `l10n_ro_force_reconcile`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_force_reconcile
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_force_reconcile`
- **Ultima Ingestie:** `2026-10-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un asistent pentru reconcilierea a două elemente de jurnal din conturi diferite, deși Odoo standard permite reconcilierea doar între linii din același cont. Asistentul generează o notă de compensare cu câte o linie pe fiecare cont și reconciliază liniile originale cu liniile corespunzătoare. Acoperă cazuri frecvente în contabilitatea românească, precum avansul furnizor față de factură sau compensarea client-furnizor.

#### 2. Funcționalități Cheie

- **Cazuri de utilizare:** avans furnizor ↔ factură furnizor (409 ↔ 401), avans client ↔ factură client (419 ↔ 411), compensare client-furnizor pentru același partener (411 ↔ 401), decontare avans angajat ↔ furnizor (542 ↔ 401).
- **Lansare:** din lista **Elemente jurnal** (de exemplu **Contabilitate → Examinare → Control → Elemente jurnal**), cu exact 2 linii bifate, din **Acțiuni → Reconciliere forțată (conturi diferite)**. Acțiunea este disponibilă doar utilizatorilor din grupul **Contabilitate / Manager** (`account.group_account_manager`).
- **Verificări la deschidere:** ambele linii trebuie să fie postate, nereconciliate complet, din aceeași companie, iar conturile lor să aibă bifat **Permite reconcilierea** (de activat doar pe conturile de terți 4xx/5xx).
- **Câmpuri completate automat în asistent:** conturile și reziduurile celor două linii, **Sumă compensată** (minimul celor două reziduuri), partenerul comun, **Jurnal** (primul jurnal de tip *Diverse* al companiei), **Data notei** (azi) și **Etichetă** (`COMPENSARE`). Suma, jurnalul, data și eticheta se pot modifica.
- **Reconciliere parțială:** dacă suma compensată este mai mică decât rezidualul, linia rămâne parțial reconciliată; asistentul poate fi relansat pe aceleași linii.
- **Rezultat:** la **Reconciliază** se creează și se postează nota de compensare, iar fiecare linie originală este reconciliată cu linia de pe același cont din notă; se deschide nota generată.
- **Limitare:** asistentul lucrează în moneda companiei; diferențele de curs nu se gestionează automat și se tratează separat, prin reevaluarea valutară.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.force.reconcile` (wizard): preia cele două linii din context, validează condițiile, propune suma și jurnalul și creează nota de compensare în `action_force_reconcile`, apoi reconciliază liniile.

**Vizualizări**

- `wizard/account_force_reconcile_views.xml`: formularul asistentului de reconciliere forțată (acțiunea `action_account_force_reconcile`).

**Acțiuni Automate / Acțiuni Server**

- `action_server_force_reconcile`: acțiune server „Forced Reconciliation (Different Accounts)”, legată de lista `account.move.line`, restricționată la `account.group_account_manager`; deschide asistentul cu liniile selectate. Nu sunt definite sarcini `ir.cron`.

#### 5. Conexiuni

- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): diferențele de curs valutar nu sunt gestionate de acest modul și se înregistrează prin reevaluarea valutară.
- [l10n_ro_expense_currency](../l10n_ro_expense_currency/index.md): avansurile angajaților în valută (cont 542), care pot fi compensate cu furnizorii (542 ↔ 401).
