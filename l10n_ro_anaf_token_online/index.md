# Romania - ANAF SPV Token for Odoo Online

- **Nume Tehnic:** `l10n_ro_anaf_token_online`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_anaf_token_online
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_anaf_token_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Tokenul SPV ANAF pentru e-Factura, și pe **Odoo Online**: modulul nu are cod Python și se importă ca arhivă zip. Autorizarea cu certificatul digital se face o singură dată, pe serverul Terrabit, care ține tokenul valabil și îl trimite în baza dumneavoastră. Nu înregistrați o aplicație proprie la ANAF și nu reînnoiți tokenul manual.

#### 2. Funcționalități Cheie

- **Generează token (Terrabit)**, în *Setări > Facturare > E-Factura România*: deschide autorizarea ANAF pe serverul Terrabit. Primul clic activează serviciul; apăsați din nou după câteva secunde.
- **Tokenul se completează singur**: Client ID, Client Secret, tokenul de acces, cel de reînnoire și expirările se scriu pe firmă (găsită după CUI), în câmpurile standard e-Factura, după autorizare și după fiecare reînnoire.
- **Reînnoire într-un singur loc**: când sosește tokenul, acțiunea programată standard de reînnoire e-Factura se oprește; într-o bază cu mai multe firme se oprește doar când toate firmele cu token ANAF îl primesc de la Terrabit.
- **Cost**: o autorizare costă 1 credit (1 credit = 1 EUR), reînnoirile sunt gratuite; consumul apare în *Setări > Credite Terrabit > Consum credite*.
- **Butonul standard Generează token este ascuns**, pentru că ar invalida tokenul reînnoit de Terrabit.
- Tokenul vine prin HTTPS pe un URL de webhook secret; din bază pleacă adresa și UUID-ul bazei, denumirea și CUI-ul firmei.
- Nu se instalează împreună cu `terrabit_iap_anaf` (același token, alt canal).
- La dezinstalare, reporniți acțiunea programată de reînnoire sau generați un token cu butonul standard. Pașii cu capturi sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro_edi`
- [deltatech_iap_online](../deltatech_iap_online/index.md)

Exclude `terrabit_iap_anaf`.

#### 4. Componente Cheie

**Modele**

- `res.company` (câmp adăugat prin date): `x_l10n_ro_anaf_token_terrabit`.
- `x_iap_online_service`: serviciul *ANAF SPV Token* (cod `anaf_token`).

**Vizualizări**

- `res_config_settings_view_form`: butonul *Generează token (Terrabit)* și ascunderea celui standard.

**Acțiuni Automate / Acțiuni Server**

- `automation_anaf_token_receive` (`base.automation`, declanșator pe webhook): primește tokenul de la Terrabit.
- `action_anaf_token_receive`: scrie tokenul SPV pe firmă și oprește cron-ul de reînnoire.
- `action_anaf_token_authorize`: *Generează token (Terrabit)*.

#### 5. Conexiuni

- [deltatech_iap_online](../deltatech_iap_online/index.md): servicii, credite și consum.
- [l10n_ro_anaf_partner_online](../l10n_ro_anaf_partner_online/index.md): același mecanism Terrabit, pentru datele partenerilor.
- `terrabit_iap_anaf`: canal alternativ pentru același token (incompatibil).
