# Registrul Inventar (FR-50) (localizat la `l10n_ro_inventory_register/index.md`)

- **Nume Tehnic:** `l10n_ro_inventory_register`
- **Versiune:** `19.0.1.3.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_inventory_register
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_inventory_register`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul generează Registrul Inventar anual pentru companiile din România, conform formularului cod 14-1-2 (OMFP 2634/2015). Creează un registru pe companie și an fiscal, calculează valorile contabile nete din soldurile postate și permite completarea valorii de inventar și a cauzelor diferențelor față de valoarea contabilă, acoperind cerința legală a registrului recapitulativ anual.

#### 2. Funcționalități Cheie

- Generare automată a celor 12 categorii patrimoniale standard (OMFP 2634/2015) din soldurile contabile postate la data raportului.
- Calcul net pentru imobilizări (minus amortizări și ajustări) și stocuri (minus ajustări pentru depreciere din clasa 39).
- Editare manuală a valorii de inventar și a cauzelor diferențelor per linie.
- Generare anexe analitice per cont, cu detaliere per partener pentru creanțe și datorii.
- Detaliere a mijloacelor fixe per bun din modulul de active (`account.asset`): nr. inventar, valoare de intrare, amortizare cumulată la data raportului și valoare contabilă netă, cu reconciliere față de soldul contabil al categoriei.
- Preluare opțională a valorii de inventar din listele validate de inventariere fizică, atunci când este instalat `l10n_ro_inventory_closing`.
- Confirmare cu blocare de editare; resetare la ciornă pentru corecții.
- Export PDF (formular 14-1-2 cu semnături) și export XLSX (cu foaie dedicată pentru detalierea mijloacelor fixe).
- Constrângere de unicitate companie + an fiscal.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `account_asset`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.inventory.register`: Registrul anual pe companie și an fiscal (mixin `mail.thread`/`mail.activity.mixin`), cu acțiunile de generare linii, calcul valori contabile, preluare valori din inventarul fizic, generare anexe analitice și de mijloace fixe, confirmare/resetare, tipărire PDF și export XLSX.
- `l10n.ro.inventory.register.line`: Liniile recapitulative pe categorie patrimonială (valoare contabilă, valoare inventar, diferențe, cauze).
- `l10n.ro.inventory.register.annex.line`: Anexa analitică per cont, cu detaliere per partener pentru creanțe și datorii.
- `l10n.ro.inventory.register.asset.line`: Anexa detaliată per mijloc fix (nr. inventar, cont, dată achiziție, valoare de intrare, amortizare cumulată, valoare netă), legată de `account.asset`.

**Vizualizări**

- `view_l10n_ro_inventory_register_form`: Formularul registrului, cu liniile recapitulative, anexele analitice și de mijloace fixe, și acțiunile de generare/confirmare/export.
- `view_l10n_ro_inventory_register_list`: Lista registrelor pe companie și an fiscal.
- `view_l10n_ro_inventory_register_search`: Filtrele de căutare a registrelor.
- `report/report_inventory_register.xml` și `report/report_actions.xml` (`action_report_inventory_register`): Raportul tipăribil conform formularului cod 14-1-2, cu spații de semnătură pentru administrator, contabil-șef și responsabil inventariere.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`) sau reguli `base.automation`; toate operațiile (generare linii, recalculare, anexe, export) se declanșează la cerere din interfața registrului.*

#### 5. Conexiuni

- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md): dacă este instalat, permite preluarea valorii de inventar pentru categoria Stocuri direct din ultimele liste validate de inventariere fizică.
- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): se integrează în fluxul de închidere de perioadă/an fiscal al companiei.
