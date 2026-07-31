# Romania - Blocare storno TVA la încasare declarat (FR-16) (localizat la `l10n_ro_vat_on_payment_lock/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_on_payment_lock`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_vat_on_payment_lock`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_vat_on_payment_lock`
- **Ultima Ingestie:** `2026-07-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul blochează desfacerea reconcilierii unei încasări atunci când TVA la încasare aferentă (exigibilitate amânată pe contul 4428, mecanismul cash-basis) este deja inclusă într-un decont D300 declarat. Conform FR-16 / art. 282 Cod Fiscal, exigibilitatea TVA la încasare devine definitivă odată raportată într-un D300 validat, iar desfacerea ulterioară a reconcilierii ar storna retroactiv TVA-ul deja declarat — ceea ce nu este permis. Astfel, modulul protejează integritatea declarațiilor fiscale deja depuse la ANAF.

#### 2. Funcționalități Cheie

- Blochează desfacerea reconcilierii (`account.partial.reconcile`) — fie prin reset plată la ciornă, fie prin desfacere manuală din widgetul de reconciliere — atunci când aceasta a generat o notă de exigibilitate TVA cash-basis (cont 4428).
- Verifică dacă nota de exigibilitate TVA are dată mai mică sau egală decât data de blocare fiscală a companiei (`tax_lock_date`), setată la validarea D300.
- Afișează un mesaj de eroare explicit, cu referință la nota contabilă, data acesteia și data blocării fiscale.
- Perioadele nedeclarate (ulterioare datei de blocare) rămân editabile — controlul nu restricționează fluxul normal de lucru.
- Se aplică exclusiv companiilor cu țara fiscală România.
- Completează regimul de TVA la încasare furnizat de `l10n_ro_vat_on_payment` (OCA) și mecanismul nativ Odoo de exigibilitate pe încasare, fără a-l dubla.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.partial.reconcile`: extins cu metoda `unlink()` suprascrisă, care rulează controlul `_l10n_ro_check_caba_in_locked_period()` înainte de a permite desfacerea reconcilierii. Dacă reconcilierea a generat o mișcare contabilă postată cu `tax_cash_basis_rec_id` egal cu reconcilierea curentă, iar data acelei mișcări este mai mică sau egală cu `tax_lock_date` al companiei, operația este blocată cu `UserError`.

**Vizualizări**

Modulul nu adaugă vizualizări proprii; nu are fișiere de date (`data: []` în manifest).

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` — logica se aplică direct la nivel de model, la apelul `unlink()`.

#### 5. Conexiuni

- `l10n_ro_vat_on_payment`: modulul OCA care implementează regimul de TVA la încasare pentru România; acest modul completează controlul de blocare fiscală fără a duplica logica de exigibilitate.
