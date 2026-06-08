# Romania - Send E-Factura - legacy (localizat la `l10n_ro_account_edi_ubl/index.md`)

- **Nume Tehnic:** `l10n_ro_account_edi_ubl`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_account_edi_ubl`
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_account_edi_ubl`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Acest modul este o punte tehnică (bridge) păstrată pentru compatibilitate retroactivă în jurul trimiterii facturilor electronice românești (E-Factura) către SPV-ul ANAF. Practic, el nu mai conține logică proprie: rolul său este să marcheze numele tehnic vechi `l10n_ro_account_edi_ubl` ca fiind în continuare instalabil și să atragă automat modulul curent de E-Factura (`l10n_ro_edi`), unde se află toată funcționalitatea reală. Existența lui asigură o tranziție lină pentru bazele de date mai vechi care îl aveau deja instalat, fără a-l pierde la upgrade și fără a cere reconfigurare din partea utilizatorului.

#### 2. Funcționalități Cheie

- Asigură continuitatea numelui tehnic `l10n_ro_account_edi_ubl` pentru bazele de date existente (modul legacy/bridge).
- Se instalează automat (`auto_install = True`) atunci când dependența sa este prezentă, redirecționând trimiterea E-Factura către modulul curent.
- Trage după sine modulul de E-Factura propriu-zis (`l10n_ro_edi`), care conține logica de generare UBL și de comunicare cu SPV-ul ANAF.
- Nu adaugă modele, vizualizări sau date proprii — întreaga funcționalitate este moștenită din dependență.

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

Modulul nu definește componente tehnice proprii. Este un pachet de tip bridge/legacy, fără cod Python funcțional și fără fișiere de date.

**Modele**

- Niciun model definit sau extins. Fișierul `__init__.py` este gol, iar manifestul nu declară nicio sursă Python suplimentară.

**Vizualizări**

- Nicio vizualizare. Cheia `data` din `__manifest__.py` este o listă goală.

**Acțiuni Automate / Acțiuni Server**

- Nicio sarcină `ir.cron`, regulă `base.automation` sau înregistrare `ir.actions.server`. Singurul comportament automat este `auto_install = True` la nivel de manifest, care declanșează instalarea automată a modulului împreună cu dependența sa.

#### 5. Conexiuni

- `l10n_ro_edi`: modulul de E-Factura curent către care această punte redirecționează; conține logica reală de generare UBL și de transmitere la SPV-ul ANAF.
