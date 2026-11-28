# Romania - Taxare inversă art. 331 în punctul de vânzare (localizat la `l10n_ro_reverse_charge_331_pos/index.md`)

- **Nume Tehnic:** `l10n_ro_reverse_charge_331_pos`
- **Versiune:** `20.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_reverse_charge_331_pos
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reverse_charge_331_pos`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține poziția fiscală de la art. 331 în afara selecției din Punctul de vânzare cât timp cumpărătorul nu este înregistrat în scopuri de TVA. Butonul de poziție fiscală al casierului listează tot ce e configurat pe casă și permite alegerea oricărei poziții, indiferent de client; acesta este drumul prin care taxarea inversă ajunge pe o vânzare la care nu se cuvine. În plus, o comandă cu taxare inversă trebuie facturată, fiindcă bonul fiscal nu documentează o livrare cu taxare inversă. Se instalează automat când sunt prezente `l10n_ro_reverse_charge_331` și `point_of_sale`.

#### 2. Funcționalități Cheie

- Poziția art. 331 dispare din lista butonului **Taxă** cât timp comanda nu are un client înregistrat conform art. 316; se filtrează lista, deci casierul nu trebuie să știe cine e plătitor de TVA.
- Un client neplătitor care are totuși pe fișă poziția plătitorilor nu o aduce pe comandă; linia păstrează taxa domestică, cu TVA la cota standard.
- Cu un client plătitor, poziția clientului se preia, iar linia cu bunul din lista art. 331 primește `0% R331`, fără TVA în total.
- Pe ecranul **Plată**, opțiunea **Factură** este bifată și nu poate fi debifată pentru comenzile cu taxare inversă; serverul facturează singur comenzile sincronizate fără bifă, dacă au client.
- O comandă cu taxare inversă ajunsă pe server fără client nu poate fi facturată: rămâne pe bon și primește o notă în chatter, ca TVA-ul să fie regularizat de contabil.
- Returul unei vânzări facturate cu taxare inversă se face tot cu factură de stornare; returul unei vânzări nefacturate rămâne pe bon.
- Configurare pe casă (**Punct de vânzare → Configurare → Setări**, secțiunea **Contabilitate**): **Taxe flexibile** activate, poziția plătitorilor adăugată la **Permis**; poziția art. 331 nu se pune la **Implicit** și nici pe o presetare.
- Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md)
- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `account.fiscal.position` (extindere): încarcă în POS câmpul `l10n_ro_reverse_charge_331`, ca marcajul art. 331 să însoțească poziția fiscală pe fiecare casă.
- `account.tax` (extindere): încarcă în POS câmpurile taxei necesare marcajului art. 331.
- `res.partner` (extindere): încarcă în POS statutul de TVA (`l10n_ro_vat_subjected`), ca filtrarea să nu depindă de o alegere manuală.
- `pos.order`: `_l10n_ro_requires_invoice_331` stabilește dacă o comandă trebuie facturată, iar `_process_saved_order` o facturează la sincronizare sau o notează în chatter când lipsește clientul.

**Cod JavaScript (frontend POS)**

- `pos_order.esm.js`: `isVatRegistered(partner)` (oglinda verificării Python) și corectarea `PosOrder.updatePricelistAndFiscalPosition`, care anulează poziția art. 331 dacă noul client nu e înregistrat.
- `control_buttons.esm.js`: corectează `ControlButtons.clickFiscalPosition`, construind dialogul de selecție fără regimurile art. 331 cât timp clientul nu e înregistrat.
- `payment_screen.esm.js`: bifează și blochează opțiunea **Factură** pentru comenzile cu taxare inversă și afișează mesajul de refuz la încercarea de debifare.

**Vizualizări**

- Nu adaugă vizualizări XML.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md): sursa marcajului art. 331 și a gărzii de pe facturi; acest modul extinde protecția în ecranul POS.
- [l10n_ro_reverse_charge_331_sale](../l10n_ro_reverse_charge_331_sale/index.md): același regim pe comenzile de vânzare.
- [l10n_ro_reverse_charge_331_purchase](../l10n_ro_reverse_charge_331_purchase/index.md): garda art. 331 pe achiziții.
- [deltatech_pos_fix](../deltatech_pos_fix/index.md): motivul pentru care filtrarea se face la nivelul listei de poziții disponibile, nu la calculul taxelor; cele două module patch-uiesc metode diferite din fluxul POS.
