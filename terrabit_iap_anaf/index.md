# ANAF IAP Client (localizat la `terrabit_iap_anaf/index.md`)

- **Nume Tehnic:** `terrabit_iap_anaf`
- **Versiune:** `19.0.1.4.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_anaf
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_anaf`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Conectează Odoo la SPV ANAF (Spațiul Privat Virtual) pentru e-Factura, fără a instala certificatul digital pe fiecare server. Autorizarea se face o singură dată prin serviciul Terrabit IAP, care păstrează token-ul de acces valid și îl trimite bazei de date a clientului.

#### 2. Funcționalități Cheie

- **Autorizare din setări:** butonul **Generate Token IAP**, lângă setările standard e-Factura (*Setări > Facturare/Contabilitate*, secțiunea **Romanian E-Factura**), pornește autorizarea ANAF prin Terrabit IAP; butonul standard din `l10n_ro_edi` este ascuns. În producție se debifează **Use Test Environment**; la mai multe companii se păstrează activă doar compania autorizată.
- **Token completat automat:** Client ID, Client Secret, token-urile de acces și de reîmprospătare și datele lor de expirare se scriu pe companie, în câmpurile standard `l10n_ro_edi`.
- **Reînnoire într-un singur loc:** serverul Terrabit IAP reînnoiește token-ul (ANAF invalidează token-ul anterior la fiecare reînnoire). Cronul local de reînnoire din `l10n_ro_edi` rămâne activ la instalare și este oprit de server abia după ce acesta deține un token valid.
- **Token expirat semnalat:** când token-ul a expirat, butonul reapare, cu avertismentul că e nevoie de o nouă autorizare cu certificatul digital.
- **Apeluri ale serverului protejate cu secret (nou în 1.4.0):** după ce serverul confirmă secretul de callback al contului IAP, baza de date acceptă rutele apeluri doar cu acest secret, nu doar cu `account_token`. Baze mai vechi (server neconfirmat) merg ca înainte.
- **Înregistrare automată a secretului:** acțiunea programată zilnică **IAP ANAF: Register Callback Secret** înregistrează secretul pentru conturile care au deja token, fără reautorizare; câmpul **Callback Secret Registered** din contul IAP arată starea.
- **Token-urile nu ajung în jurnale:** se scriu doar numele câmpurilor și datele de expirare.
- **Instalare:** pentru fiecare companie se creează un cont IAP pentru serviciul **ANAF SPV Token** (`anaf_token`), cu endpoint `https://terrabit.odoo.com`, fără cod de activare (vizibil în modul dezvoltator: *Setări > Tehnic > IAP > IAP Accounts*). În lucrul de zi cu zi e-Factura funcționează ca în Odoo standard.
- **Serviciu extern:** modulul schimbă token-ul ANAF cu serverul Terrabit IAP, care îl trimite bazei după autorizare și îl cere înapoi (recuperare) când are nevoie.

#### 3. Dependențe

- `iap`
- [terrabit_iap](../terrabit_iap/index.md)
- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `iap.account` (extins): metodele `anaf_token_response` (scrie token-ul primit pe companie), `anaf_token_export` (întoarce serverului token-ul curent, pentru recuperare), `anaf_disable_local_refresh` (oprește cronul local de reînnoire la cererea serverului), `_cron_anaf_register_callback_secret` (înregistrează secretul de callback pe server); `_cron_refresh_tokens` doar loghează, pentru compatibilitate.
- `res.config.settings` (extins): câmpul calculat `l10n_ro_edi_token_expired` și acțiunea `button_l10n_ro_edi_generate_token_iap`, care leagă contul IAP de companie, îl înregistrează pe server și deschide URL-ul de autorizare.
- `iap.service` (date): serviciul `anaf_token` („ANAF SPV Token”).

**Controllere** (`auth="none"`, protejate cu `account_token` și, după confirmarea serverului, cu secretul de callback)

- `/iap/anaf_token_response`: primește token-ul ANAF de la serverul IAP (rulează pe cursor read/write, `readonly=False`).
- `/iap/anaf_token_export`: trimite serverului token-ul curent al bazei.
- `/iap/anaf_disable_local_refresh`: oprește reînnoirea locală (idempotent).
- Cont inexistent și secret greșit dau același mesaj („Account not found”).

**Vizualizări**

- `res_config_settings_form_inherit_l10n_ro_edi`: ascunde butonul standard și adaugă **Generate Token IAP**, vizibil când nu există token sau acesta a expirat, cu avertisment.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_anaf_register_callback_secret` (**IAP ANAF: Register Callback Secret**): zilnic; înregistrează secretul de callback al conturilor `anaf_token` încă neconfirmate, până când serverul confirmă.
- Cronul standard `l10n_ro_edi` de reînnoire a token-ului nu mai este dezactivat la instalare sau prin migrare; îl oprește doar serverul IAP prin `/iap/anaf_disable_local_refresh`.

#### 5. Conexiuni

- [terrabit_iap](../terrabit_iap/index.md): infrastructura IAP Terrabit (conturi IAP, secret de callback) de care depinde modulul.
- `l10n_ro_edi`: modulul standard e-Factura, ale cărui câmpuri de token sunt completate și al cărui cron de reînnoire este oprit de server.
- `iap`: conturile și serviciile IAP extinse de modul.
