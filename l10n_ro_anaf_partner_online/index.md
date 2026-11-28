# Romania - ANAF Partner Data for Odoo Online

- **Nume Tehnic:** `l10n_ro_anaf_partner_online`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_anaf_partner_online
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_anaf_partner_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Completează partenerii români din ANAF după CUI, inclusiv pe **Odoo Online**: modulul nu are cod Python și se importă ca arhivă zip (Aplicații > Importați modulul). Căutarea rulează pe serviciul Terrabit, care interoghează ANAF și trimite datele în baza dumneavoastră.

#### 2. Funcționalități Cheie

- **Buton ANAF pe formularul partenerului**, lângă codul fiscal: completează denumirea, adresa sediului (județ, oraș, cod poștal), codul fiscal cu `RO` doar pentru plătitorii de TVA și telefonul, înainte de salvare. Butonul este ascuns pe contactele unei companii.
- **Actualizare în masă**: *Acțiuni > Actualizare din ANAF* pe o selecție de parteneri; răspunsul vine în câteva secunde, cu o notă în chatter pe fiecare partener găsit. Partenerii fără cod fiscal sunt săriți.
- **Starea ANAF pe tab-ul ANAF**: plătitor de TVA, inactiv fiscal, radiat, nr. registrul comerțului (J…), data ultimei verificări.
- **Activare dintr-un clic**: *Contacte > Configurare > ANAF > Serviciu ANAF*, **Activează**; tokenul serviciului se scrie automat, cu căutări de probă gratuite. **Cumpără credite** și **Reîmprospătează credite** sunt pe același ecran. Se consumă un credit per răspuns ANAF (găsit sau negăsit); CUI invalid sau ANAF indisponibil sunt gratuite.
- **Cine ce vede**: utilizatorii care editează parteneri pot folosi butonul și acțiunea; doar administratorii activează serviciul, cumpără credite și văd *Cereri ANAF*.
- **Cereri ANAF**: lista cererilor cu tip, CUI, stare și eroare; o cerere fără răspuns după 10 minute se retrimite o dată.
- **Ce iese din baza de date**: CUI-ul căutat, tokenurile, id-ul cererii, UUID-ul și adresa bazei; la activare, și denumirea și codul fiscal al firmei.
- Pașii cu capturi sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_iap_online](../deltatech_iap_online/index.md)
- `contacts`

Exclude `l10n_ro_partner_create_by_vat` și `l10n_ro_partner_autocomplete` (nu se instalează împreună).

#### 4. Componente Cheie

**Modele**

- `res.partner` (câmpuri adăugate prin date): `x_anaf_vat_payer`, `x_anaf_inactive`, `x_anaf_struck_off`, `x_anaf_trade_register`, `x_anaf_last_check`.
- `x_iap_online_service`: serviciul ANAF (cod `anaf_partner_online`), din `deltatech_iap_online`.

**Vizualizări**

- `view_partner_form`: butonul ANAF (widget JS `anaf_lookup_widget`) și tab-ul ANAF.
- Acțiunile de meniu *Serviciu ANAF* și *Cereri ANAF*, sub *Contacte > Configurare > ANAF*.

**Acțiuni Automate / Acțiuni Server**

- `action_anaf_lookup_partners`: *Actualizare din ANAF*, pe selecție.
- `action_anaf_apply`: scrie răspunsul ANAF pe partener, doar dacă utilizatorul poate edita partenerul și CUI-ul e neschimbat.

#### 5. Conexiuni

- [deltatech_iap_online](../deltatech_iap_online/index.md): serviciile, creditele și cererile Terrabit.
- [l10n_ro_anaf_token_online](../l10n_ro_anaf_token_online/index.md): același mecanism Terrabit, pentru tokenul SPV.
- [l10n_ro_anaf_partner_lookup](../l10n_ro_anaf_partner_lookup/index.md): aceeași căutare ANAF, dar în Python, pe server propriu.
