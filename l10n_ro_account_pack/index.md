# Romania - Pachet contabilitate de bază (localizat la `l10n_ro_account_pack/index.md`)

- **Nume Tehnic:** `l10n_ro_account_pack`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_pack
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_pack`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modul-pălărie (bundle) care instalează dintr-o singură mișcare modulele de bază pentru contabilitatea românească: corecțiile aduse localizării standard Odoo și completările planului de conturi (OMFP 1802/2014). Clientul bifează un singur modul în loc să le caute și să le instaleze pe rând. Modulul nu are cod propriu, iar configurările rămân cele din documentația fiecărui modul inclus.

#### 2. Funcționalități Cheie

- Instalare unică, din **Aplicații** sau din **Setări → România Enterprise**; modulele incluse se instalează automat, împreună cu dependențele lor.
- Corecții la balanța de verificare RO (4 și 5 coloane): solduri finale pe conturi active/pasive, subtotaluri fără compensare între conturi, opțiunile „Raw trial balance" și „Hide off-balance accounts" (`l10n_ro_reports_fix`).
- Coduri SAF-T corecte pentru cotele de TVA 21%/11% și taxe fără nume împiedicate (`l10n_ro_saft_fix`).
- Export SAF-T (D406) fără secțiunile goale respinse de ANAF, cu raportarea plăților care nu provin dintr-un extras bancar (`l10n_ro_saft_export_fix`).
- Conturi lipsă din nomenclatorul SAF-T, blocarea notelor pe conturi sintetice, analitic obligatoriu pe cont și gardă la dezactivarea conturilor cu rulaj; mecanismele de blocare sunt opt-in per companie, din **Setări → Contabilitate** (`l10n_ro_account_chart`).
- Cont corespondent calculat pe fiecare poziție contabilă (`l10n_ro_account_correspondence`).
- Dezinstalarea pachetului nu dezinstalează modulele incluse.

#### 3. Dependențe

- [l10n_ro_reports_fix](../l10n_ro_reports_fix/index.md)
- [l10n_ro_saft_fix](../l10n_ro_saft_fix/index.md)
- [l10n_ro_saft_export_fix](../l10n_ro_saft_export_fix/index.md)
- [l10n_ro_account_chart](../l10n_ro_account_chart/index.md)
- [l10n_ro_account_correspondence](../l10n_ro_account_correspondence/index.md)

#### 4. Componente Cheie

**Modele**

Modulul nu definește și nu extinde modele proprii.

**Vizualizări**

Fără vizualizări proprii (`data` este gol).

**Acțiuni Automate / Acțiuni Server**

Nu există.

#### 5. Conexiuni

Modulul nu are conexiuni suplimentare în afara dependențelor de mai sus, care sunt toate incluse prin manifest.
