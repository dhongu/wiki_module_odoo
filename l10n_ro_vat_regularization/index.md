# Romania - Regularizare TVA (localizat la `l10n_ro_vat_regularization/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_regularization`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_vat_regularization
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_vat_regularization
- **Ultima Ingestie:** `2026-10-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul automatizează regularizarea TVA la finele perioadei fiscale (lună sau trimestru), conform OMFP 1802/2014. Calculează soldurile conturilor de TVA deductibilă (4426) și colectată (4427) din înregistrările postate și generează cu un singur clic nota contabilă de închidere, stabilind dacă firma are TVA de plată (4423) sau TVA de recuperat (4424). Rezultatul trebuie să corespundă decontului D300 al perioadei; regularizarea îl pregătește contabil, dar nu înlocuiește depunerea declarației.

#### 2. Funcționalități Cheie

- **Creare regularizare:** **Contabilitate → Contabilitate → Regularizare TVA → Nou**, cu perioada (De la / Până la), data notei (de obicei ultima zi a perioadei), conturile și jurnalul de operațiuni diverse; se pot crea mai multe regularizări, pentru perioade diferite, fiecare cu nota ei.
- **Calcul solduri:** „Calculează solduri" afișează TVA deductibilă (4426), TVA colectată (4427), TVA net și rezultatul (TVA de plată, de recuperat sau zero), cu un banner explicativ; la TVA net zero nu se generează notă.
- **TVA de plată:** când 4427 depășește 4426, nota închide 4427 în 4426 și trece diferența în 4423 (implicit 44231, TVA de plată curentă); pentru scadență peste un an, contul 44231 se înlocuiește manual cu 44232, înainte de postare.
- **TVA de recuperat:** când 4426 depășește 4427, nota închide ambele conturi, iar diferența rămâne de recuperat în 4424.
- **Preluare automată din planul de conturi:** conturile 4426, 4427, 44231 și 4424 și primul jurnal de tip General se precompletează la creare; pot fi schimbate cât timp regularizarea este în ciornă.
- **Anulare și resetare:** o regularizare postată se poate anula (se anulează și nota contabilă) și apoi reseta la ciornă.
- **Acces:** meniul este vizibil pentru Contabilitate / Utilizator sau superior; crearea și postarea cer rolul Contabilitate / Manager.
- **Integrare cu închiderea perioadei:** dacă este instalat `l10n_ro_period_close_enhanced`, checklistul semnalează lipsa regularizării pentru perioadă.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.vat.regularization`: regularizarea TVA pe perioadă, cu conturile 442x, soldurile calculate prin SQL doar din note postate, rezultatul și nota contabilă generată; stări Ciornă / Postată / Anulată.

**Vizualizări**

- `l10n_ro_vat_regularization_list` / `l10n_ro_vat_regularization_form`: lista și formularul regularizărilor (meniu `menu_l10n_ro_vat_regularization`).
- `l10n_ro_vat_regularization_search`: filtrarea regularizărilor.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește cron-uri sau acțiuni server; regularizarea se generează manual la finele perioadei.

#### 5. Conexiuni

- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): checklistul de închidere verifică existența regularizării.
