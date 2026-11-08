# Romania - Blocare stornare TVA la încasare declarat (localizat la `l10n_ro_vat_on_payment_lock/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_on_payment_lock`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_vat_on_payment_lock
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_vat_on_payment_lock`
- **Ultima Ingestie:** `2026-11-08`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul blochează desfacerea reconcilierii unei încasări atunci când TVA la încasare aferentă (exigibilitate amânată pe contul 4428, mecanismul cash-basis) este deja inclusă într-un decont D300 declarat. Conform art. 282 Cod Fiscal, exigibilitatea TVA la încasare devine definitivă odată raportată într-un D300 validat, iar desfacerea ulterioară a reconcilierii ar storna retroactiv TVA-ul deja declarat, ceea ce nu este permis. Astfel, modulul protejează integritatea declarațiilor fiscale deja depuse la ANAF.

#### 2. Funcționalități Cheie

- Este un control de conformitate fără ecran propriu: nu adaugă meniuri sau vizualizări și acționează automat.
- Blochează desfacerea reconcilierii (`account.partial.reconcile`) dacă aceasta a generat o notă de exigibilitate TVA cash-basis (cont 4428), de exemplu:
  - pe factură, pictograma **ⓘ** de lângă „Plătit pe …" → **Anulare reconciliere**;
  - modificarea sumei sau ștergerea unei încasări readuse la ciornă.
- **Resetarea la ciornă** a încasării rămâne permisă: în Odoo 19 plata revine în ciornă păstrând reconcilierea, iar nota de exigibilitate rămâne postată.
- Verifică dacă nota de exigibilitate TVA are dată mai mică sau egală cu data de blocare fiscală a companiei (`tax_lock_date`), setată la validarea D300.
- Afișează dialogul **Operație invalidă**, cu mesaj în română, cu referință la nota contabilă, data acesteia și data blocării fiscale.
- Perioadele nedeclarate (ulterioare datei de blocare) rămân editabile.
- Se aplică exclusiv companiilor cu țara fiscală România.
- Completează regimul de TVA la încasare furnizat de `l10n_ro_vat_on_payment` (OCA) și mecanismul nativ Odoo de exigibilitate pe încasare, fără a-l dubla.
- Configurare necesară:
  - activarea **Contabilitate → Configurare → Setări → Taxe → Exigibilitate TVA la încasare** pe companie;
  - taxa de vânzare, pe fila **Opțiuni Avansate**, cu **Exigibilitatea taxei = Pe baza plății** și **Cont de tranziție a bazei de numerar** 4428;
  - contul de bază pentru notele cash-basis (câmpul „Base Tax Received Account") setat pe companie, în **Setări → Contabilitate**, secțiunea **Taxe**. Liniile de bază din nota de exigibilitate sunt o mișcare în oglindă (debit = credit, sold zero), folosită doar pentru raportarea bazei în grilele de TVA; se folosește un cont tehnic neutru (cu `l10n_ro_caba`, contul 442830 se setează automat). Dacă lipsește, baza rulează pe contul de venituri sau cheltuieli al facturii, ceea ce nu este corect;
  - utilizatorul are drepturi de Contabilitate.
- La încasare, nota de exigibilitate mută TVA-ul din 4428 în 4427 (la achiziții, din 4428 în 4426), proporțional cu suma încasată.
- Pentru o corecție legitimă, contabilul-șef mută mai întâi **Blochează declarația fiscală** înaintea lunii, din **Contabilitate → Contabilitate → Închidere → Blochează datele…** (resetarea D300 nu mută data de blocare TVA a companiei, iar o excepție de blocare nu ridică blocajul); apoi se depune un D300 rectificativ.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.partial.reconcile`: extins cu `unlink()` suprascris, care rulează controlul `_l10n_ro_check_caba_in_locked_period()` înainte de desfacerea reconcilierii. Dacă reconcilierea are o mișcare postată cu `tax_cash_basis_rec_id` egal cu ea, iar data mișcării este mai mică sau egală cu `tax_lock_date` al companiei (cu țara fiscală România), operația este blocată cu `UserError`.

**Vizualizări**

Modulul nu adaugă vizualizări proprii; nu are fișiere de date (`data: []` în manifest).

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`; logica se aplică direct la nivel de model, la apelul `unlink()`.

#### 5. Conexiuni

- `l10n_ro_vat_on_payment`: modulul OCA care implementează regimul de TVA la încasare pentru România; acest modul completează controlul de blocare fiscală fără a duplica logica de exigibilitate.
- [l10n_ro_caba](../l10n_ro_caba/index.md): setează automat contul tehnic 442830 pentru baza din notele de exigibilitate.
