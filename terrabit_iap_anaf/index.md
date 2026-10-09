# ANAF IAP Client (localizat la `terrabit_iap_anaf/index.md`)

- **Nume Tehnic:** `terrabit_iap_anaf`
- **Versiune:** `19.0.1.3.3`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_anaf
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_anaf`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Conectează Odoo la SPV ANAF (Spațiul Privat Virtual) pentru e-Factura, fără a instala certificatul digital pe fiecare server. Autorizarea se face o singură dată prin serviciul Terrabit IAP, care păstrează token-ul de acces valid și îl trimite bazei de date a clientului.

#### 2. Funcționalități Cheie

- **Autorizare din setări:** butonul **Generate Token IAP**, lângă setările standard e-Factura (*Setări > Contabilitate*), pornește autorizarea ANAF prin Terrabit IAP; butonul standard din `l10n_ro_edi` este ascuns.
- **Token completat automat:** Client ID, Client Secret, token-urile de acces și de reîmprospătare și datele lor de expirare se scriu pe companie, în câmpurile standard `l10n_ro_edi`.
- **Reînnoire într-un singur loc:** serverul Terrabit IAP reînnoiește token-ul, iar cronul local de reînnoire din `l10n_ro_edi` este oprit (ANAF invalidează token-ul anterior la fiecare reînnoire).
- **Token expirat semnalat:** când token-ul a expirat, butonul reapare, cu avertismentul că e nevoie de o nouă autorizare cu certificatul digital.
- **Token-urile nu ajung în jurnale:** se scriu doar numele câmpurilor și datele de expirare.
- **Instalare:** pentru fiecare companie se creează un cont IAP pentru serviciul **ANAF SPV Token** (`anaf_token`); în lucrul de zi cu zi e-Factura funcționează ca în Odoo standard.
- **Serviciu extern:** modulul schimbă token-ul ANAF cu serverul Terrabit IAP, care îl trimite bazei după autorizare și îl cere înapoi (recuperare) când are nevoie.

#### 3. Dependențe

- `iap`
- `terrabit_iap`
- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `iap.account` (extins): metodele `anaf_token_response` (scrie token-ul primit pe companie), `anaf_token_export` (întoarce serverului token-ul curent, pentru recuperare), `anaf_disable_local_refresh` (oprește cronul local de reînnoire la cererea serverului); `_cron_refresh_tokens` doar loghează, pentru compatibilitate.
- `res.config.settings` (extins): câmpul calculat `l10n_ro_edi_token_expired` și acțiunea `button_l10n_ro_edi_generate_token_iap`, care leagă contul IAP de companie, îl înregistrează pe server și deschide URL-ul de autorizare.
- `iap.service` (date): serviciul `anaf_token` („ANAF SPV Token”).

**Controllere** (`auth="none"`, protejate cu secretul partajat `account_token`)

- `/iap/anaf_token_response`: primește token-ul ANAF de la serverul IAP.
- `/iap/anaf_token_export`: trimite serverului token-ul curent al bazei.
- `/iap/anaf_disable_local_refresh`: oprește reînnoirea locală (idempotent).

**Vizualizări**

- `res_config_settings_form_inherit_l10n_ro_edi`: ascunde butonul standard și adaugă **Generate Token IAP**, vizibil când nu există token sau acesta a expirat, cu avertisment.

**Acțiuni Automate / Acțiuni Server**

- Niciuna activă; cronul `l10n_ro_edi.ir_cron_l10n_ro_edi_refresh_access_token` este dezactivat la instalare (`post_init_hook`) și prin migrare pe bazele existente.

#### 5. Conexiuni

- `terrabit_iap`: infrastructura IAP Terrabit de care depinde modulul.
- `l10n_ro_edi`: modulul standard e-Factura, ale cărui câmpuri de token sunt completate.
- `terrabit_iap_server_anaf`: partea de server (în afara acestui wiki) care reînnoiește token-ul și îl trimite clienților.
