# Romania - Cash Register (localizat la `l10n_ro_cash_register/index.md`)

- **Nume Tehnic:** `l10n_ro_cash_register`
- **Versiune:** `20.0.1.4.4`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_cash_register
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_cash_register`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă registrul de casă ca document numerotat (formularul cod 14-4-7A, OMFP 2634/2015): câte un document pentru fiecare casierie și zi, cu sold inițial preluat din ziua precedentă și sold final calculat din notele contabile postate pe contul casei. Include închiderea zilei și monetarul (numărarea numerarului pe cupiuri), astfel că evidența de casă poate fi păstrată, tipărită și prezentată la control.

#### 2. Funcționalități Cheie

- Un document per (casierie, zi), cu numerotare proprie prin secvență, unic pe dată și jurnal.
- Sold inițial preluat automat din ziua precedentă și sold final calculat; soldurile și mișcările se citesc din notele contabile postate pe contul casei jurnalului (`default_account_id`, ex. 5311).
- Mișcările zilei: încasări, plăți, explicația operațiunii și partenerul; chatter și activități pe document pentru urmărire și responsabil.
- Tipărire în forma cerută de formular.
- **Închiderea zilei**: soldul se îngheață, iar contul casei nu mai primește înregistrări în ziua închisă sau înaintea ei până la redeschiderea explicită; corecțiile se fac prin stornare sau notă de corecție datată în ziua curentă. Nu se închide o zi din viitor sau cu sold negativ.
- **Monetarul**: butonul **Numără numerarul** adaugă un rând pentru fiecare cupiură activă a monedei casieriei (leu și euro livrate cu modulul; alte valute se adaugă din *Contabilitate > Configurare > Cupiuri numerar*). Diferența față de soldul scriptic apare ca plus sau lipsă și se tipărește în „Monetar – situația numerarului pe cupiuri”.
- **Înregistrează diferența** deschide operațiunea de casă precompletată (sens, sumă, cont implicit: 7588 pentru plus, 65882 pentru lipsă, dacă jurnalul nu are conturi proprii); contabilul poate alege alt cont (473, 4282). Lipsa nu este imputată automat.
- Bifa **Monetar obligatoriu la închiderea zilei** pe jurnalul de casă: ziua se închide doar după numărare și doar dacă numerarul numărat este egal cu soldul contului casei.
- La o casierie în valută (5314) se numără cupiurile valutei; diferența în valută se înregistrează printr-o notă contabilă, nu din operațiunea de casă.
- Alegerea variantei: acest modul produce **documentul** numerotat (Community); `l10n_ro_cash_register_report` produce **raportul** pe interval, fără numerotare (Enterprise). Cele două pot fi instalate împreună.

Fluxul complet de configurare și utilizare este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- [l10n_ro_account_sequence](../l10n_ro_account_sequence/index.md)

#### 4. Componente Cheie

Secțiune omisă: `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit analiza componentelor tehnice.

#### 5. Conexiuni

- [l10n_ro_account_sequence](../l10n_ro_account_sequence/index.md): numerotarea separată a documentelor din jurnalul de casă.
- `account`: jurnale, plăți și note contabile pe care se bazează registrul.
- [l10n_ro_cash_register_report](../l10n_ro_cash_register_report/index.md): același registru ca raport pe interval, cu export PDF/XLSX; complementar, nu numerotează.
- [l10n_ro_cash_bank_enhanced](../l10n_ro_cash_bank_enhanced/index.md): completări pe fluxul de casă/bancă, adiacente registrului de casă.
- [l10n_ro_bank_register_report](../l10n_ro_bank_register_report/index.md): echivalentul de partea de bancă al registrului de casă.
