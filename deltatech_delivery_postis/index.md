# Postis Shipping (localizat la `deltatech_delivery_postis/index.md`)

- **Nume Tehnic:** `deltatech_delivery_postis`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_postis
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_postis`
- **Ultima Ingestie:** `2026-09-03`

#### 1. Sumar

Modulul conectează Odoo la Postis, platforma românească de management al livrărilor care stă în fața mai multor curieri deodată (Cargus, GLS, DPD, Sameday, Nemo, DHL, FAN). În loc de o integrare separată pentru fiecare curier, expedierea este predată către Postis cu numele unui serviciu, iar Postis o rutează, întoarce AWB-ul și raportează starea înapoi — tarifare, generare AWB, etichete, anulare și tracking, toate în fluxul standard de livrare din Odoo, fără un portal separat de ținut sincronizat.

#### 2. Funcționalități Cheie

- O singură conexiune (credențiale Postis) acoperă toți curierii disponibili pe cont; curierul se alege per metodă de livrare, din lista de servicii importată
- Cotare la cel mai bun preț între curierii pe care Postis îi are disponibili pentru client
- Autentificare securizată pe gateway-ul Postis, cu credențialele mascate în logul tehnic
- Generarea AWB-ului și a etichetei PDF direct din comanda de livrare (picking); AWB-ul este salvat înainte de a fi preluată eticheta, astfel încât un eșec la etichetă nu pierde niciodată AWB-ul
- Reobținerea etichetei unui AWB existent, dacă atașamentul a fost șters
- Anularea unei expedieri pentru o comandă respinsă sau modificată
- Calcul de tarif în timp real pentru o comandă de vânzare, interogat prin Postis, integrat cu prețuirea de livrare din Odoo; suportă și preț fix cu un prag opțional peste care este interogat curierul
- Import automat al catalogului de județe și localități Postis pentru România; localitățile sunt înregistrate ca mapări peste nomenclatorul Odoo (nu ca duplicate), iar localitățile nepotrivite rămân vizibile ca „de mapat" în loc să fie ghicite; expedierile sunt adresate după id-ul de localitate/județ Postis, nu doar după nume
- Istoricul stărilor expedierii, preluat de la Postis și scris pe comanda de livrare; o singură expediere inaccesibilă nu mai oprește interogarea de status pentru restul lotului
- Opțiuni avansate de expediere: ramburs (COD, cu comutarea automată a tipului de plată Postis), valoare declarată (asigurare) per colet, expediere cu mai multe colete (greutatea repartizată pe colete), plătitor expeditor sau destinatar, ridicare de la o adresă înregistrată la Postis (trimisă prin referința ei Postis)
- Reîncercări sigure: un răspuns pierdut la crearea sau anularea AWB-ului este raportat ca rezultat incert, nu ca eroare simplă, astfel încât apăsarea repetată a butonului nu poate rezerva un al doilea AWB pentru același colet
- Ce NU acoperă integrarea (declarat explicit ca lipsă, nu ca bug): generare AWB în format ZPL sau HTML, listă de lockere sau puncte de ridicare, raport de decontare ramburs (COD settlement), expediere cu dimensiuni, opțiune livrare sâmbăta, opțiune „colet deschis", notă de restituire în AWB, trimitere id de locker în AWB
- Postis publică un singur gateway — nu există un host de test separat; contul demo este accesat la aceeași adresă, cu credențiale demo. Debifarea „Production Environment" pe metoda de livrare NU ține un apel departe de contul live — doar credențialele fac asta

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins): metode de dispecerizare Postis — `postis_login`, `postis_rate_shipment`, `postis_send_shipping`, `postis_get_label`, `postis_get_label_filename`, `postis_get_tracking_link`, `postis_cancel_shipment`, `postis_get_status_history`, `postis_import_carrier_city`, `_postis_api_capabilities` (declară ce operații suportă integrarea, astfel încât butoanele pentru operații pe care Postis nu le poate face nu mai sunt oferite)
- `delivery.carrier.service` (extins): serviciile de curierat Postis (Cargus, GLS, DPD, Sameday, Nemo, DHL, FUN) importate ca înregistrări cu `delivery_type = "postis"`
- `res.country` / `res.country.state` / `res.city` (extinse): câmpul `postis_id` pentru mapare pe nomenclatorul Postis; `res.city` primește și `postis_name`
- `stock.package.type` (extins): opțiunea `postis` adăugată la `package_carrier_type`
- `res.config.settings` (extins): comutatorul `module_deltatech_delivery_postis`
- `PostisProvider` (clasă Python, `models/postis_request.py`): client al API-ului REST Postis — login, tarifare, expediere, etichetă, anulare, istoric de status; `PostisUncertainResult` marchează un răspuns pierdut în tranzit ca rezultat incert, nu ca eroare simplă

**Vizualizări**

- `view_delivery_carrier_form_with_provider_postis`: adaugă pagina „Postis Configuration" pe formularul `delivery.carrier` (utilizator/parolă, `postis_client_id`, partener companie, metode de plată la livrare, plătitor expediere, serviciul Postis), vizibilă doar când `delivery_type = postis`
- `res_config_settings_views.xml`: comutatorul modulului în Setări

**Acțiuni Automate / Acțiuni Server**

- Nu definește `ir.cron`, `base.automation` sau `ir.actions.server`
- `uninstall_hook`: rulează la dezinstalare
- Migrare `19.0.1.0.0/post-migration.py`: mută la instalare o bază venită de pe 17.0 (unde modulul rămăsese blocat la pasul 18.0) — credențialele Postis sunt reportate pe câmpurile comune `username`/`password` de pe curier, ca la orice alt curier din suită

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): furnizează infrastructura comună a suitei de curierat (metode partajate pe `delivery.carrier`) peste care se construiește integrarea Postis
- [deltatech_delivery_postis_locker](../deltatech_delivery_postis_locker/index.md): extinde acest modul cu suport pentru puncte de tip locker/easybox pe curierii Postis (rescris pe 19.0 în PR #132)
- `delivery`: modulul standard Odoo de livrare, ale cărui modele (`delivery.carrier`, `delivery.carrier.service`) sunt extinse
- `mail`: folosit pentru mesageria/urmărirea pe documentele de livrare

---

**Notă corecție:** `readme/HISTORY.md` menționează că modulul a rămas „blocat la pasul 18.0" pe branch-ul 17.0 înainte de migrarea curentă pe 19.0.1.0.0 — nu este o eroare de versiune de corectat, ci un istoric real al migrării, păstrat ca atare.
