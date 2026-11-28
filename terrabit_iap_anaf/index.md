# ANAF IAP Client (localizat la `terrabit_iap_anaf/index.md`)

- **Nume Tehnic:** `terrabit_iap_anaf`
- **Versiune:** `20.0.1.4.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_iap_anaf
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_anaf`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Conectează Odoo la ANAF SPV, sistemul online al fiscului, pentru e-Factura, fără să fie nevoie să instalați certificatul digital pe fiecare server. Autorizarea se face o singură dată prin serviciul Terrabit IAP, care păstrează tokenul de acces valid și îl trimite în baza dvs. de date.

#### 2. Funcționalități Cheie

- **Autorizare din setări**: butonul **Generate Token IAP**, lângă setările standard e-Factura, pornește autorizarea ANAF prin Terrabit IAP (în locul butonului standard **Generate Token**).
- **Token completat automat**: Client ID, Client Secret, tokenurile de acces și de reîmprospătare și datele de expirare se scriu pe companie, în câmpurile standard din `l10n_ro_edi`.
- **Reînnoire într-un singur loc**: serverul Terrabit IAP reînnoiește tokenul, iar jobul local standard de reînnoire este oprit (ANAF invalidează tokenul anterior la fiecare reînnoire).
- **Token expirat semnalat**: când tokenul a expirat, butonul reapare cu un avertisment că este necesară o nouă autorizare cu certificatul digital.
- **Fără tokenuri în loguri**: se înregistrează doar numele câmpurilor și datele de expirare.
- **Cont IAP per companie**: la instalare se creează contul IAP pentru serviciul **ANAF SPV Token** (endpoint `https://terrabit.odoo.com`); **Callback Secret Registered** arată că serverul a confirmat secretul bazei, iar apelurile serverului sunt acceptate doar cu acest secret. Bazele cu token existent sunt înregistrate de acțiunea programată **IAP ANAF: Register Callback Secret**.
- **Înainte de autorizare**: în producție se debifează **Use Test Environment**, iar la mai multe companii rămâne selectată în comutator doar compania autorizată.
- **Serviciu extern**: modulul schimbă tokenul ANAF cu serverul Terrabit IAP, care îl trimite în baza dvs. după autorizare și îl cere înapoi când are nevoie.

Fluxul pas-cu-pas, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `iap`
- [terrabit_iap](../terrabit_iap/index.md)
- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `iap.account` (extins): contul IAP al serviciului ANAF, cu înregistrarea secretului de callback și primirea tokenului.
- `res.config.settings` (extins): butonul **Generate Token IAP** și starea tokenului în setările e-Factura.

**Vizualizări**

- `views/res_config_settings_views.xml`: butonul de generare și avertismentul de token expirat în secțiunea **Romanian E-Factura**.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_anaf_register_callback_secret` (**IAP ANAF: Register Callback Secret**): înregistrează pe server secretul de callback pentru bazele care aveau deja token.

Controller: ruta `/iap/anaf_token_response` primește tokenul trimis de server.

#### 5. Conexiuni

- [terrabit_iap](../terrabit_iap/index.md): clientul IAP de bază, pe care se sprijină contul ANAF.
- [terrabit_iap_server_anaf](../terrabit_iap_server_anaf/index.md): partea de server care obține, reînnoiește și trimite tokenul.
