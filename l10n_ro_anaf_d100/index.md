# Romania - Declarația D100 ANAF (localizat la `l10n_ro_anaf_d100/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d100`
- **Versiune:** `20.0.0.0.10`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d100
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d100`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite companiilor românești să genereze și să exporte **Declarația 100 — Declarația privind obligațiile de plată la bugetul de stat** direct din Odoo Enterprise, eliminând introducerea manuală a datelor în DUKIntegrator sau în formularul PDF ANAF. Se adresează plătitorilor de impozit pe profit, impozit pe veniturile microîntreprinderilor, impozit pe dividende și altor obligații fiscale raportate lunar sau trimestrial la ANAF.

#### 2. Funcționalități Cheie

- **Raport interactiv D100** (*Contabilitate → Raportare → Declarații ANAF → Declarație 100*) integrat în rapoartele contabile Enterprise, cu coloanele **Suma datorată**, **Suma de plată** și **Cod bugetar**, linii pe coduri ANAF (102, 103, 121, 150, 604) și filtrare pe perioadă (lunar sau trimestrial). Liniile cu suma zero sunt ascunse.
- **Surse automate:** 103 (impozit pe profit, conturile 44111/44112) și 121 (impozit micro, conturile 44118/44182); liniile 102, 150 și 604 nu au sursă automată și rămân la zero până când domeniul lor este configurat pe conturile firmei. Obligațiile trimestriale (102, 103, 121) se declară doar pentru martie, iunie, septembrie sau decembrie.
- **Export XML (Soft J)** — fișier XML conform schemei oficiale ANAF, validat automat față de XSD înainte de descărcare, gata pentru import în DUKIntegrator.
- **Export XDP (Soft A)** — fișier XDP pentru formularul PDF inteligent ANAF, importabil în Adobe Acrobat Reader.
- **Calcul automat scadență** — data de 25 a lunii următoare perioadei de raportare.
- **Preluare automată date companie** — CUI (fără prefixul „RO"), denumire, adresă, telefon, e-mail și datele declarantului din contul utilizatorului curent; pentru obligația 121 se raportează cota de impozit micro din setări (1% sau 3%).
- Exportul se oprește cu mesaj explicit dacă nu există nicio obligație de declarat, dacă o obligație trimestrială e exportată pentru o lună care nu e de final de trimestru sau dacă o linie nu figurează în nomenclator. Se generează întotdeauna o declarație inițială.
- **Versiune formular acceptată:** OPANAF 57/19.01.2026, schemă `d100_24022022.xsd`; verificat cu DUKIntegrator la 13.09.2026.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf_d100.report.handler`: handlerul custom al raportului (moștenește `account.report.custom.handler` și `l10n_ro_anaf.report.handler.mixin`); alimentează liniile și implementează exporturile XML și XDP.
- `res.company` / `res.config.settings` (extinse): cota de impozit pe veniturile microîntreprinderilor, setată în *Setări → Contabilitate*.

**Vizualizări**

- `l10n_ro_anaf_d100_report` (`account.report`, în `data/d100_report.xml`): definiția raportului, cu coloanele și liniile pe obligații fiscale.
- `views/d100_xml_export.xml` și `views/d100_xdp_export.xml`: butoanele de export XML (Soft J) și XDP (Soft A).
- `res_config_settings_views.xml`: setarea cotei de impozit micro.

**Acțiuni Automate / Acțiuni Server**

Nu au fost identificate sarcini `ir.cron`; exportul se declanșează manual din butoanele raportului.

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună ANAF (mixin handler, utilitare de export și date declarant).
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): declarație ANAF construită pe același cadru de raport contabil.
- [l10n_ro_anaf_d120](../l10n_ro_anaf_d120/index.md): declarație ANAF înrudită din aceeași suită.
- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md): calculul impozitului pe profit citit de linia 103.
- [l10n_ro_micro_tax](../l10n_ro_micro_tax/index.md): calculul impozitului micro citit de linia 121.
- [l10n_ro_dividends](../l10n_ro_dividends/index.md): sursă pentru obligațiile de impozit pe dividende (liniile 150/604).
