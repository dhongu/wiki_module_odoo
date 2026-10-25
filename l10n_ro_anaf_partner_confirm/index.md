# Romania - Confirmarea datelor ANAF ale partenerilor

- **Nume Tehnic:** `l10n_ro_anaf_partner_confirm`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_partner_confirm
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_partner_confirm`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Adresa unui partener preluată din ANAF rămâne „de confirmat” până când o verifică un om. Datele din registrul ANAF sunt adesea incomplete sau neactualizate (stradă fără număr, localitate în afara județului), iar e-Factura respinge factura cu o adresă greșită abia după emitere. În plus, sincronizarea periodică ANAF rescrie adresa și o corectură făcută de mână se poate pierde. Modulul pune un marcaj de confirmare, avertizează utilizatorul și, opțional, blochează validarea facturilor către client până la confirmare.

#### 2. Funcționalități Cheie

- **Marcaj „Date ANAF de confirmat”** pus automat când sincronizarea ANAF scrie sau schimbă adresa (stradă, localitate, cod poștal, județ), inclusiv la un partener confirmat anterior dacă adresa s-a schimbat între timp.
- **Bandă de avertizare** pe fișa partenerului, cu problemele găsite: date lipsă pentru e-Factura, București fără sector, stradă fără număr, localitate în afara județului (unde există nomenclatorul de localități).
- **Butonul „Confirmă adresa”**: refuză confirmarea cât timp lipsesc datele cerute de e-Factura, iar mesajul spune ce lipsește; confirmarea (cine și când) rămâne în istoricul partenerului.
- **Filtrul „Date ANAF de confirmat”** în lista de parteneri.
- **La validarea facturii către client**: notă de avertizare în chatter (implicit) sau blocarea validării, dacă este bifată opțiunea din Setări → Contabilitate → „ANAF Partner Monitoring (RO)” → „Block Partners with Unconfirmed ANAF Data”. Stornările și documentele de intrare nu sunt blocate.
- Modificările din afara adresei (denumire, CAEN, statut TVA, inactiv) nu pun marcajul; ele rămân în jurnalul și alertele din monitorizarea modificărilor ANAF.
- Flux: sincronizare ANAF (automată sau butonul **Sync with ANAF** din fila Monitorizare ANAF) → bandă galbenă → verificare/corectare adresă → **Confirmă adresa**.

#### 3. Dependențe

- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md)

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): câmpurile `l10n_ro_anaf_to_confirm` și `l10n_ro_anaf_confirm_warnings`, verificarea datelor lipsă și a adresei, `action_l10n_ro_anaf_confirm`.
- `account.move` (extins): `action_post` verifică partenerul și avertizează sau blochează.
- `res.company` / `res.config.settings` (extinse): opțiunea `l10n_ro_anaf_block_unconfirmed`.

**Vizualizări**

- `view_partner_form_l10n_ro_anaf_confirm`: banda de avertizare și butonul „Confirmă adresa” pe partener.
- `view_res_partner_filter_l10n_ro_anaf_confirm`: filtrul „Date ANAF de confirmat”.
- `res_config_settings_view_form_anaf_partner_confirm`: opțiunea de blocare în Setări.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): sincronizarea și monitorizarea modificărilor datelor ANAF ale partenerilor, a cărei scriere de adresă declanșează marcajul.
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): baza integrării ANAF (dependență a modulului `l10n_ro_anaf_partner`).
- `account`: validarea facturilor către clienți.
