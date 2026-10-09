# Terrabit IAP AI (localizat la `terrabit_iap_ai/index.md`)

- **Nume Tehnic:** `terrabit_iap_ai`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_ai
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_ai`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Înregistrează serviciul **AI** pe platforma Terrabit IAP și pregătește contul IAP din care se consumă creditele de către modulele care apelează serviciile AI Terrabit. Este un modul tehnic, fără interfață proprie, instalat automat ca dependență de modulele consumatoare. Credențialele și endpoint-urile rămân în `terrabit_iap`.

#### 2. Funcționalități Cheie

- Declară serviciul IAP „AI” (nume tehnic `ai`, unitate `unit`) cu sold de credit întreg: consumul se numără în unități întregi, nu fracțiuni.
- La instalare creează, pentru fiecare companie existentă, un cont IAP propriu pentru serviciul AI. Creditele se cumpără și se consumă per companie, nu partajat într-o bază multi-company; fără cont, primul apel ar eșua.
- Dacă o companie are deja cont pentru serviciu, nu se creează un duplicat.
- Nu are meniuri sau ecrane proprii.

#### 3. Dependențe

- `terrabit_iap`

#### 4. Componente Cheie

**Modele**

- `iap.account` (extins): moștenit fără câmpuri sau logică suplimentară; conturile sunt create din `post_init_hook`.

**Vizualizări**

- Niciuna.

**Acțiuni Automate / Acțiuni Server**

- `iap_service_ai` (`data/iap_account_data.xml`): înregistrare `iap.service` pentru serviciul AI, cu `integer_balance` setat.
- `post_init_hook`: la instalare, creează contul IAP al serviciului pentru fiecare companie care nu are unul.

#### 5. Conexiuni

- `terrabit_iap`: platforma IAP Terrabit (credențiale, endpoint-uri), de care depinde acest modul.
- `iap`: modelele `iap.account` și `iap.service` extinse/populate de modul.
