# Terrabit IAP Server Params

- **Nume Tehnic:** `terrabit_iap_server_params`
- **Versiune:** `19.0.1.3.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_params
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_params`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modul pentru serverul IAP Terrabit, care permite administratorului să trimită parametri de sistem către instanțele Odoo ale clienților și să le anunțe din timp despre mentenanță. Din același loc se poate programa și îmbinarea (merge) automată a codului pe repository-ul GitHub al clientului, iar sistemul confirmă ulterior că actualizarea a fost aplicată. Modulul are statut Beta și categoria „Hidden”.

#### 2. Funcționalități Cheie

- Serviciu nou „System Parameters Sync” (`params_sync`) adăugat la conturile IAP ale clienților; pe contul clientului apare o pagină cu lista de parametri (cheie, valoare, activ, dată de expirare) și butonul de trimitere către client.
- Trimiterea parametrilor către `<base_url>/iap/update_params`; rezultatul real este raportat ca `success`, `partial` (chei respinse de lista albă a clientului), `failed` sau `skipped` (nimic de trimis). Clientul acceptă doar `database_notification_banner` și cheile cu prefixul `terrabit.` / `terrabit_`.
- Expirare automată: un parametru cu „Expire At” depășit este dezactivat și configurația este retrimisă clientului (verificare la 10 minute).
- Asistent „Maintenance Notification”: se aleg conturile clientului, ora mentenanței, întârzierea de ștergere a bannerului (implicit 1 oră) și mesajul (precompletat cu ora locală). Bannerul `database_notification_banner` este trimis la client și retras automat după expirare.
- Programare opțională de Git Merge la ora mentenanței (ramura head implicit `staging`, base implicit `main`), pentru conturile cu „GitHub Repository” completat; conturile fără repository sunt semnalate în asistent.
- Meniu „Scheduled Merges” (sub meniul rădăcină IAP) cu starea fiecărui merge: Scheduled, Merged, Deployed & Verified, Nothing to Merge, Failed; se poate reprograma.
- Merge-ul se execută prin API-ul GitHub, cu tokenul din parametrul de sistem `terrabit_iap.github_token`; la lipsa tokenului operația eșuează cu mesaj explicit.
- Confirmarea deploy-ului: se interoghează `/iap/system_info` de pe client; dacă `server_start` este posterior merge-ului, starea devine „Deployed & Verified” și bannerul de mentenanță este retras și retrimis.
- Rută `/iap/params/sync_all` (JSON-RPC) pentru sincronizarea tuturor conturilor `params_sync`; rezervată administratorilor (`base.group_system`), răspunsul nu conține tokenuri.
- Probleme cunoscute deschise (readme/bugs.md): PARAMS-003 (modelul de parametri este accesibil oricărui utilizator intern, P1) și PARAMS-004 (expirările eșuate nu sunt reîncercate, P2).

#### 3. Dependențe

- `terrabit_iap_server`

#### 4. Componente Cheie

**Modele**

- `iap.server.account` (extins): adaugă `param_ids`, `github_repo` și metodele de trimitere a parametrilor către client.
- `iap.server.service` (extins): adaugă codul de serviciu `params_sync`.
- `iap.server.account.param`: parametru cheie/valoare asociat unui cont, cu indicator „activ” și dată de expirare.
- `iap.git.merge`: merge programat head → base pe un repository GitHub, cu stare, SHA-ul commit-ului și datele de execuție/deploy.
- `iap.maintenance.notification` (tranzitoriu): asistentul de notificare de mentenanță și programare merge.

**Vizualizări**

- `iap_server_account_view_form_inherit_params`: pagina „System Parameters Sync” pe contul IAP.
- `view_iap_maintenance_notification_form` / `action_iap_maintenance_notification`: asistentul de notificare.
- `view_iap_git_merge_list`, `view_iap_git_merge_form`, `action_iap_git_merge`, `menu_iap_git_merge`: merge-urile programate.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_expire_params`: la 10 minute, dezactivează parametrii expirați și retrimite configurația.
- `ir_cron_run_scheduled_merges`: la 5 minute, rulează merge-urile scadente și verifică deploy-ul celor îmbinate.

#### 5. Conexiuni

- [terrabit_iap_params](../terrabit_iap_params/index.md): partea de client, care primește parametrii și aplică doar cheile din lista albă.
- `deltatech_test_system`: afișează pe instanța clientului bannerul `database_notification_banner`.
