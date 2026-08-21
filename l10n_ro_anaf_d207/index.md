# Romania - ANAF Declarația 207 (WHT PJ Nerezidente) (localizat la `l10n_ro_anaf_d207/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d207`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d207
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d207`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru întocmirea și exportul Declarației 207 — declarația informativă privind impozitul reținut la sursă pe veniturile plătite persoanelor juridice nerezidente, depusă anual la ANAF (termen: ultima zi din februarie a anului următor).

#### 2. Funcționalități Cheie

- Import automat al beneficiarilor PJ nerezidenți din conturile 446x, cu filtrare după flag-ul `l10n_ro_wht_applicable` de pe partener
- Grupare automată pe tipuri de venit (sect_II, 25 coduri) conform XSD ANAF
- Suport CEDI: câmp `Act_N` (act normativ / declarație proprie) și `is_exempt` per beneficiar
- Validare XML față de schema XSD `d207_20025020.xsd` (namespace v2) înainte de export
- Export fișier XML semnat, gata de depus în Soft J ANAF
- Workflow ciornă → confirmată, cu posibilitate de rectificativă (`d_rec`)
- Raport de previzualizare live (din jurnal) cu buton „Generează ciornă D207"
- Integrare cu fluxul `account.return`: verificare automată „ciornă generată" și „beneficiari cu NIF completat"; termen scadență calculat automat

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d207`: declarația D207 persistentă (ciornă/confirmată), cu liniile de beneficiari PJ nerezidenți, tipuri de venit (01–25) și export XML validat XSD.
- `l10n_ro_anaf_d207.report.handler`: handler de raport de previzualizare (proiecție live peste conturile 446x), fără date proprii persistate; oferă butonul „Generează ciornă D207".
- `account.return` (extindere): calculează termenul legal de depunere (ultima zi din februarie a anului următor) și adaugă verificările automate specifice D207 (ciornă generată, beneficiari fără NIF).

**Vizualizări**

- `views/l10n_ro_anaf_d207_view.xml`: formularele și listele pentru gestionarea declarației D207 (identificare, grilă beneficiari, workflow).

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); importul, generarea ciornei și exportul se declanșează manual din interfață.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează registrul profilurilor de declarații ANAF (`anaf_declaration_profile`) și meniul comun al declarațiilor ANAF.
- [l10n_ro_anaf_d205](../l10n_ro_anaf_d205/index.md): declarație ANAF înrudită (impozit reținut la sursă, PF), aceeași familie de declarații WHT.
- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): declarație ANAF înrudită din aceeași suită de raportare fiscală.
- `l10n_ro_reports`: sursa mixin-ului `account.return` peste care se integrează fluxul de verificări și termene D207.
