# Romania - Declarația D100 ANAF (localizat la `l10n_ro_anaf_d100/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d100`
- **Versiune:** `19.0.0.0.12`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d100
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d100`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul permite companiilor românești să genereze și să exporte **Declarația 100 — Declarația privind obligațiile de plată la bugetul de stat** direct din Odoo Enterprise, eliminând introducerea manuală a datelor în DUKIntegrator sau în formularul PDF ANAF. Se adresează plătitorilor de impozit pe profit, impozit pe veniturile microîntreprinderilor, impozit pe dividende și altor obligații fiscale raportate lunar sau trimestrial la ANAF.

#### 2. Funcționalități Cheie

- **Raport interactiv D100** integrat în rapoartele contabile Enterprise (**Contabilitate → Raportare → Declarații ANAF → Declarație 100**), cu linii predefinite pe coduri ANAF (102, 103, 121, 150, 604) și filtrare pe perioadă (lunar sau trimestrial). Liniile cu suma zero sunt ascunse.
- **Coloane dedicate:** Suma datorată (lei), Suma de plată (lei) și Cod bugetar.
- **Surse ale sumelor:** linia 103 (impozit pe profit) se calculează automat din conturile 44111 / 44112, iar linia 121 (impozit micro) din conturile 44118 / 44182, pe baza notelor postate. Liniile 102 (plăți anticipate, specific instituțiilor de credit), 150 (dividende persoane juridice) și 604 (dividende persoane fizice) nu au sursă automată și rămân la zero până când administratorul configurează domeniul lor pe conturile folosite de firmă.
- **Export XML (Soft J)** — fișier XML conform schemei oficiale ANAF (`d100_24022022.xsd`), validat automat față de XSD înainte de descărcare, gata pentru import în DUKIntegrator.
- **Export XDP (Soft A)** — fișier XDP pentru formularul PDF inteligent ANAF (`D100_710_XML_0126_191026.pdf`, din 19.10.2026), importabil prin funcția *Importă date* din Adobe Acrobat Reader.
- **Versiune de formular acceptată:** OPANAF 57/19.01.2026; fișierul XML trece validarea cu DUKIntegrator fără erori.
- **Calcul automat scadență** — data de 25 a lunii următoare perioadei de raportare, derivată din filtrul de dată al raportului.
- **Preluare automată date companie** — CUI (cu eliminarea prefixului „RO"), denumire, adresă, telefon, e-mail și datele declarantului (nume și funcție) din contul utilizatorului care exportă. Pentru obligația 121 se raportează și cota de impozit micro (1% sau 3%) setată în **Setări → Contabilitate**.
- **Creanțe trimestriale:** obligațiile 102, 103 și 121 se declară doar pentru martie, iunie, septembrie sau decembrie.
- **Opriri cu mesaj explicit:** nu există nicio obligație de declarat pentru perioadă, o obligație trimestrială este exportată pentru o lună care nu e de final de trimestru, sau o linie a raportului nu figurează în nomenclatorul obligațiilor. Exportul se oprește și pentru o companie cu datele de identificare incomplete.
- **Declarație inițială:** exportul generează întotdeauna o declarație inițială; pentru anulare sau rectificare se urmează procedura ANAF în DUKIntegrator, modulul neavând buton dedicat.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf_d100.report.handler`: handlerul custom al raportului, care moștenește `account.report.custom.handler` și `l10n_ro_anaf.report.handler.mixin`; alimentează liniile prin motorul custom și implementează exporturile XML și XDP.
- `res.company` / `res.config.settings` (extinse): câmpul `l10n_ro_micro_tax_rate` (cota de impozit micro), raportat pe obligația 121.

**Vizualizări / Date**

- `l10n_ro_anaf_d100_report` (`account.report`): definiția raportului D100, cu coloanele Suma datorată / Suma de plată / Cod bugetar și liniile pe obligații fiscale (102, 103, 121, 150, 604), legat de handlerul custom.
- `l10n_ro_anaf_d100_report_action` (`ir.actions.client`): acțiunea care deschide raportul.
- `views/d100_xml_export.xml`: șablonul exportului XML (Soft J).
- `views/d100_xdp_export.xml`: șablonul exportului XDP (Soft A).
- `res_config_settings_view_form`: câmpul cotei de impozit micro în setările de contabilitate.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate sarcini `ir.cron`; exportul se declanșează manual din butoanele raportului.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună ANAF (mixin handler, utilitare de export și date declarant).
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): declarație ANAF construită pe același cadru de raport contabil.
- [l10n_ro_anaf_d120](../l10n_ro_anaf_d120/index.md): declarație ANAF înrudită din aceeași suită.
- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md): calculul impozitului pe profit, ale cărui note postate alimentează linia 103.
- [l10n_ro_micro_tax](../l10n_ro_micro_tax/index.md): calculul impozitului micro, ale cărui note postate alimentează linia 121.
- [l10n_ro_dividends](../l10n_ro_dividends/index.md): impozitul pe dividende (liniile 150/604, fără sursă automată în raport).
