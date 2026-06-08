# Romania - Storno Enhancements (localizat la `l10n_ro_account_storno/index.md`)

- **Nume Tehnic:** `l10n_ro_account_storno`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_account_storno
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_account_storno`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul implementează contabilitatea de tip **storno** (înregistrări în roșu / cu sumă negativă) conform standardelor contabile românești. În loc să anuleze o operațiune greșită printr-o înregistrare pe partea opusă a contului (care umflă artificial rulajele), storno-ul **inversează** suma chiar pe poziția inițială, cu valoare negativă, astfel încât soldurile și rulajele contabile rămân corecte. Comportamentul de storno se activează la nivel de companie, oferind flexibilitate între entitățile dintr-un grup.

#### 2. Funcționalități Cheie

- **Înregistrări negative (în roșu):** calculează automat valorile de debit și credit ca numere negative pentru liniile de storno, asigurând raportarea corectă în registrele contabile ale localizării românești.
- **Configurarea utilizării contului:** adaugă un câmp „Utilizare" (Debit, Credit sau Bivalent) pe conturile din planul de conturi, pentru redirecționarea automată a sumelor către coloana corectă conform regulilor contabile RO.
- **Logică de storno îmbunătățită:** extinde logica standard de stornare (reversare) din Odoo, marcând notele și liniile ca „storno", astfel încât soldurile să fie diminuate corect, nu majorate pe partea opusă.
- **Activare la nivel de companie:** comportamentul de storno este controlat de o setare pe companie, permițând flexibilitate între entități diferite.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

Sumarul și funcționalitățile cheie provin din `readme/DESCRIPTION.md`. Pentru context, componentele menționate explicit acolo se regăsesc în cod astfel:

**Modele**

- `account.move` / `account.move.line`: extind logica de reversare pentru a marca notele și liniile ca storno și a aplica sumele negative.
- `account.account`: adaugă câmpul de utilizare (Debit / Credit / Bivalent) pentru redirecționarea sumelor pe coloana corectă.
- `res.company`: setarea de activare a comportamentului de storno la nivel de companie.

**Hook**

- `post_init_hook`: inițializare la instalarea modulului (configurare implicită).

#### 5. Conexiuni

Modulul oferă mecanismul de bază pentru înregistrările negative (storno) din localizarea RO. Nu au fost adăugate aici conexiuni către alte pagini fără verificare în cod; alte module care menționează storno (de ex. închideri de perioadă sau gestiuni de stoc) îl pot folosi indirect prin logica de inversare a sumelor.
