# Romania - Rambursare TVA (sold negativ D300) (localizat la `l10n_ro_vat_refund/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_refund`
- **Versiune:** `20.0.1.0.8`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_vat_refund
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_vat_refund`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul urmărește cererile de rambursare a TVA rezultate din soldul negativ al decontului D300, conform Codului Fiscal art. 303 (termen ANAF de 45 de zile, cu dobânzi de 0,02% pe zi la depășire). Gestionează ciclul cererii printr-o mașină de stări (cerere, inspecție, rambursată sau compensată) și generează monografia contabilă aferentă. Depunerea documentației și comunicarea cu ANAF rămân pași manuali.

#### 2. Funcționalități Cheie

- Mașină de stări pentru cererea de rambursare: Ciornă, Depusă la ANAF, În inspecție fiscală, Aprobată (integral sau parțial), Respinsă, Virată de ANAF, Compensată.
- Asistent de alegere între reportarea soldului negativ și rambursare, deschis din verificarea **TVA de recuperat — alegere opțiune** de pe închiderea de TVA; alegerea „rambursare” creează cererea și bifează rambursarea în D300 (`solicit_ramb = D`, cu primul cont bancar al companiei).
- Calcul automat al termenului (+45 de zile de la depunere) și al dobânzilor: suma solicitată × 0,02% × zilele de depășire.
- Notă contabilă la virament (Dr 5121 = Cr 4424, cu linie separată pentru dobânzi, venit în 7588) și notă de compensare care stinge 4424.
- Secvență dedicată pentru numerotarea cererilor și sarcină programată (săptămânală) care creează activități de avertizare pe cererile cu termenul depășit.
- Meniu: **Contabilitate → Raportare → Declarații ANAF → Rambursare TVA**; vizualizări listă, formular, grafic și pivot.
- Fluxul detaliat pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md)
- `mail`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.vat.refund`: Cererea de rambursare TVA, cu mașină de stări, termen, dobânzi și note contabile (moștenește `mail.thread` și `mail.activity.mixin`).
- `l10n.ro.vat.refund.wizard`: Asistentul de alegere între reportare și rambursare.
- `account.return`: Extins pentru integrarea cu fluxul de declarații/decont TVA.

**Vizualizări**

- `l10n_ro_vat_refund_form`, `l10n_ro_vat_refund_list`, `l10n_ro_vat_refund_graph`, `l10n_ro_vat_refund_pivot`, `l10n_ro_vat_refund_search`: interfața de gestionare a cererilor.
- `wizard/l10n_ro_vat_refund_wizard_views.xml`: asistentul de alegere a opțiunii.

**Acțiuni Automate / Acțiuni Server**

- `RO: Check VAT Refund Deadlines`: `ir.cron` săptămânal (`_cron_check_refund_deadlines`) care semnalează cererile cu termenul de 45 de zile depășit.
- `TVA de recuperat — alegere opțiune`: verificare (return check) pe tipul de declarație românesc.

#### 5. Conexiuni

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): sursa soldului negativ de TVA care declanșează cererea de rambursare.
- [l10n_ro_vat_regularization](../l10n_ro_vat_regularization/index.md): regularizarea contabilă 4426/4427/4424.
- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): checklist de închidere și urmărirea documentelor ANAF.
