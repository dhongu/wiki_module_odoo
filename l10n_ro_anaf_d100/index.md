# Romania - ANAF D100 Declaration (localizat la `l10n_ro_anaf_d100/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d100`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d100
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d100`
- **Ultima Ingestie:** 2026-06-09

#### 1. Sumar

Acest modul permite companiilor românești să genereze și să exporte **Declarația 100 — Declarația privind obligațiile de plată la bugetul de stat** direct din Odoo Enterprise, eliminând introducerea manuală a datelor în DUKIntegrator sau în formularul PDF ANAF. Se adresează plătitorilor de impozit pe profit, impozit pe veniturile microîntreprinderilor, impozit pe dividende și altor obligații fiscale raportate lunar sau trimestrial la ANAF, conform nomenclatorului de coduri bugetare.

#### 2. Funcționalități Cheie

- **Raport interactiv D100** integrat în rapoartele contabile Enterprise, cu linii predefinite pe coduri ANAF (102 impozit pe profit, 121 impozit micro, 150/604 impozit pe dividende) și filtrare pe perioadă (lunar sau trimestrial).
- **Coloane dedicate:** Suma datorată, Suma de plată și Cod bugetar, sumele fiind citite automat din soldurile conturilor de obligații fiscale (ex. 4411/691).
- **Export XML (Soft J)** — fișier XML conform schemei oficiale ANAF, validat automat față de XSD înainte de descărcare, gata pentru import în DUKIntegrator.
- **Export XDP (Soft A)** — fișier XDP pentru formularul PDF inteligent ANAF, importabil direct în Adobe Acrobat Reader.
- **Calcul automat scadență** — data de 25 a lunii următoare perioadei de raportare, derivată din filtrul de dată al raportului.
- **Preluare automată date companie** — CUI (cu eliminarea automată a prefixului „RO"), denumire, adresă, telefon, e-mail și datele declarantului din contul utilizatorului curent.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf_d100.report.handler`: handlerul custom al raportului, care moștenește `account.report.custom.handler` și `l10n_ro_anaf.report.handler.mixin`; alimentează liniile prin motorul custom și implementează exporturile XML și XDP.

**Vizualizări / Date**

- `l10n_ro_anaf_d100_report` (`account.report`): definiția raportului D100, cu coloanele Suma datorată / Suma de plată / Cod bugetar și liniile pe obligații fiscale (102, 121, 150/604), legat de handlerul custom.
- `views/d100_xml_export.xml`: butonul de export XML (Soft J), vizibil permanent în antetul raportului.
- `views/d100_xdp_export.xml`: butonul de export XDP (Soft A), vizibil permanent în antetul raportului.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate sarcini `ir.cron`; exportul se declanșează manual din butoanele raportului.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună ANAF (mixin handler, utilitare de export și date declarant).
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): declarație ANAF construită pe același cadru de raport contabil.
- [l10n_ro_anaf_d120](../l10n_ro_anaf_d120/index.md): declarație ANAF înrudită din aceeași suită.
- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md): sursă pentru obligația de impozit pe profit (linia 102).
- [l10n_ro_micro_tax](../l10n_ro_micro_tax/index.md): sursă pentru obligația de impozit micro (linia 121).
- [l10n_ro_dividends](../l10n_ro_dividends/index.md): sursă pentru obligația de impozit pe dividende (liniile 150/604).
