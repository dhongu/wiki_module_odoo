# Romania - Confirmarea datelor ANAF ale partenerilor

- **Nume Tehnic:** `l10n_ro_anaf_partner_confirm`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_partner_confirm
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_partner_confirm`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adresa unui partener preluată din ANAF rămâne „de confirmat” până o verifică un om. Datele din registrul ANAF sunt adesea incomplete (stradă fără număr, localitate în afara județului), e-Factura le respinge abia după emitere, iar sincronizarea periodică rescrie corecturile făcute de mână. Modulul marchează adresa, avertizează și, opțional, blochează validarea facturii către client până la confirmare.

#### 2. Funcționalități Cheie

- Marcaj „Date ANAF de confirmat” pe partener, pus automat când sincronizarea ANAF scrie sau schimbă adresa (stradă, localitate, cod poștal, județ), inclusiv la un partener confirmat anterior.
- Bandă de avertizare pe fișa partenerului: date lipsă pentru e-Factura, București fără sector, stradă fără număr, localitate în afara județului.
- Butonul „Confirmă adresa” refuză confirmarea cât timp lipsesc datele cerute de e-Factura; cine și când a confirmat rămâne în istoric.
- Filtrul „Date ANAF de confirmat” în lista de parteneri.
- La validarea facturii către client: notă de avertizare în chatter sau, dacă e bifată setarea „Block Partners with Unconfirmed ANAF Data” (Setări → Contabilitate, secțiunea „ANAF Partner Monitoring (RO)”), blocarea validării. Stornările nu sunt blocate.
- Modificările din afara adresei (denumire, CAEN, statut TVA, inactiv) nu pun marcajul; ele rămân în jurnalul de monitorizare ANAF.
- Fluxul pas-cu-pas este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md)

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): marcajul de confirmare, problemele adresei și acțiunea de confirmare.
- `account.move` (extins): avertizare sau blocare la validarea facturii către client.
- `res.company` / `res.config.settings` (extinse): setarea de blocare a partenerilor neconfirmați.

**Vizualizări**

- `views/res_partner_views.xml`: banda de avertizare, butonul „Confirmă adresa” și filtrul din lista de parteneri.
- `views/res_config_settings_views.xml`: setarea de blocare.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): sincronizarea ANAF care scrie adresa și declanșează marcajul.
- `l10n_ro_edi`: e-Factura (SPV), motivul pentru care adresa trebuie să fie corectă.
