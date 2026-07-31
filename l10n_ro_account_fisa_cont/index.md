

# `l10n_ro_account_fisa_cont`

- **Nume Prietenesc:** Romania - Fișă de Cont
- **Nume Tehnic:** `l10n_ro_account_fisa_cont`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_fisa_cont
- **Ultima Ingestie:** 2026-05-31
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul oferă un raport nativ "Fișă de Cont" integrat în framework-ul `account_reports` Enterprise, conform **OMFP 1802/2014**. Acesta afișează pentru fiecare cont: sold inițial, mișcări cu cont corespondent, sold progresiv și sold final.

## 2. Funcționalități Cheie

- Sold inițial calculat automat de framework (tranzacții anterioare perioadei selectate).
- Coloana **Cont Corespondent**: cont unic → cod cont; conturi multiple → „Diverși”.
- Sold progresiv acumulat per linie (running balance).
- Export **PDF** landscape și **XLSX** nativ.
- Drill-down la nota contabilă (opțiuni moștenite din Grand Livre).
- Filtre: perioadă, jurnale, analitic, căutare cont/partener.
- Suport multi-companie cu selector de companie.
- Vizibil automat doar pentru companiile cu **Țara = România**.

## 3. Dependențe

- `account_reports`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- `l10n_ro_fisa_cont_handler`: Un model handler dedicat pentru generarea raportului Fișă de Cont.

### Vizualizări / Date

- `data/l10n_ro_fisa_cont_report.xml`: Definește acțiunea raportului și structura sa în sistemul de raportare Odoo.

### Acțiuni Automate / Acțiuni Server

*Nu au fost identificate explicit în `__manifest__.py` sau `readme/DESCRIPTION.md`.*

## 5. Conexiuni

- [[l10n_ro_account_chart/|l10n_ro_account_chart]]: Legat de configurarea contabilă de bază pentru România.
