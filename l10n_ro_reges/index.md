# Integrare REGES-Online România (FR-45) (localizat la `l10n_ro_reges/index.md`)

- **Nume Tehnic:** `l10n_ro_reges`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_reges
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reges`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Acest modul integrează Odoo cu **REGES-Online** (Registrul Electronic General al Salariaților), sistemul Inspecției Muncii care înlocuiește REVISAL. Permite transmiterea electronică a angajaților și a contractelor de muncă (înregistrare, modificare, suspendare, radiere) conform obligațiilor legale, evitând amenzile de 5.000–8.000 RON per salariat neraportat. Transmiterea se face direct din fișa angajatului și a contractului, cu autentificare securizată și urmărire a rezultatelor.

## 2. Funcționalități Cheie

- **Autentificare OpenID Connect** cu refresh automat al token-ului JWT.
- **Transmitere angajați:** `InregistrareSalariat`, `ModificareSalariat`, `RadiereSalariat`.
- **Transmitere contracte:** `AdaugareContract`, `ModificareContract`, `SuspendareContract`, `RadiereContract`.
- **Polling asincron** al cozii de rezultate REGES (`/api/Status/PollMessage`).
- **Auto-tracking** al modificărilor pe câmpurile urmărite ale angajatului și contractului.
- **Jurnal de transmisii** cu posibilitate de retrimitere după corectarea erorilor.
- **Sincronizare nomenclator COR** din API-ul REGES.
- **Tab REGES** pe fișa angajatului și pe contract, plus meniu dedicat HR → REGES.
- **3 cron-uri:** polling la 30 min, contracte scadente zilnic, COR săptămânal.

## 3. Dependențe

- `hr_payroll`
- `l10n_ro`
- Python: `requests`

## 4. Componente Cheie

### Modele

- `hr.employee`: Extins cu CNP, nivel studii, tip act identitate, stare transmisie REGES și UUID angajat.
- `hr.contract`: Extins cu cod COR, tip durată/normă/loc muncă, temei încetare, stare contract REGES și UUID contract.
- Modele de configurare și jurnal de mesaje REGES, plus nomenclator COR.

### Vizualizări / Date

- `views/hr_employee_views.xml`, `views/hr_contract_views.xml`: Tab-uri REGES pe angajat și contract.
- `views/l10n_ro_reges_config_views.xml`, `views/l10n_ro_reges_message_views.xml`: Configurare și jurnal transmisii.
- `views/l10n_ro_reges_cor_views.xml`: Nomenclator COR.
- `data/l10n_ro_reges_cron.xml`: Cron-urile de polling, contracte scadente și sincronizare COR.

### Acțiuni Automate / Acțiuni Server

- **Polling rezultate REGES:** rulează la 30 de minute pentru preluarea rezultatelor cozii.
- **Contracte scadente:** rulează zilnic.
- **Sincronizare COR:** rulează săptămânal.

## 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
