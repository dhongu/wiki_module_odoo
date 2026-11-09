# Romania - Impozit pe veniturile microîntreprinderilor (localizat la `l10n_ro_micro_tax/index.md`)

- **Nume Tehnic:** `l10n_ro_micro_tax`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_micro_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_micro_tax`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul calculează și înregistrează trimestrial impozitul pe veniturile microîntreprinderilor conform Legii 227/2015 Titlul III, actualizat prin OUG 115/2023 și OUG 21/2024. Se adresează companiilor cu cifra de afaceri sub 500.000 EUR/an care aplică cota de 1% (cu cel puțin un salariat) sau 3% (fără salariat). Determină automat baza impozabilă din veniturile din exploatare (cu excluderi configurabile), aplică cota corectă în funcție de numărul de salariați și generează nota contabilă aferentă. Include monitorizarea plafonului de 500.000 EUR, cu alertă și tranziție automată la impozitul pe profit la depășire.

#### 2. Funcționalități Cheie

- **Calcul trimestrial**, la **Contabilitate → Contabilitate → Impozit Micro-Întreprindere**: se aleg anul fiscal, trimestrul (T1–T4) și jurnalul de operațiuni diverse; datele de început și sfârșit se completează din trimestru. Model persistent `l10n.ro.micro.tax.compute` cu stările `draft → posted → cancelled`.
- **Butonul Calculează venituri** (doar în ciornă) citește notele postate în trimestru pe conturile de venituri (tip `income` / `income_other`) și completează veniturile totale, veniturile excluse, baza impozabilă (minimum 0), numărul de salariați (din aplicația Angajați dacă e instalată, altfel manual) și cota: 1% cu cel puțin un salariat, 3% fără salariați.
- **Formula:** impozit calculat = bază impozabilă × cotă; de plată = impozit calculat − **Plăți anterioare în an** (minimum 0). Plățile anterioare nu se completează automat, se introduc manual (la T1 rămân 0; la T2 impozitul achitat pentru T1).
- **Conturi excluse din bază**, configurabile pe companie (de exemplu 761 dividende, 7411 / 7584 subvenții, 765 diferențe de curs favorabile, 786 reluări de provizioane); lista e orientativă și se verifică cu consultantul fiscal (Cod Fiscal art. 53 alin. 1).
- **Postare:** **Postează nota** trece calculul în starea Postată și generează nota contabilă **Dr 698 = Cr 4418**, datată în ultima zi a trimestrului, accesibilă prin **Vezi nota contabilă**. Postarea e refuzată dacă impozitul de plată este zero sau dacă lipsesc conturile 698 / 4418.
- **Rectificare:** **Anulează** (anulează și nota postată, doar dacă perioada nu e blocată), apoi **Resetează la ciornă**, corectare și repostare.
- **Plata** impozitului (scadentă pe 25 ale lunii următoare trimestrului) se înregistrează separat prin jurnalul de bancă; nu o generează modulul. Impozitul din calcul alimentează declarația D100 trimestrială.
- **Monitorizarea plafonului:** job lunar, **dezactivat implicit** (se activează din **Setări → Tehnic → Automatizări**): la cifră de afaceri cumulată ≥ 80% din plafon postează o avertizare pe fișa companiei, iar la depășire trece regimul fiscal la impozit pe profit și înregistrează *Data ieșirii din regimul micro*. Conversia în EUR se face la cursul zilei. Dacă jobul nu e activ, regimul se schimbă manual în setări.
- **Configurare** în **Contabilitate → Configurare → Setări → Regim Fiscal Micro-Întreprindere (RO)**: **Regim fiscal RO** (Impozit micro-întreprindere 1%/3%), **Plafon micro (EUR)** (implicit 500.000) și **Conturi excluse micro**; este necesar și un jurnal de tip Operațiuni diverse pentru notele de impozit.
- Multicompanie: calculele sunt filtrate pe compania activă, iar jurnalul ales trebuie să îi aparțină. Modulul are 9 teste automate (TC-01 → TC-09).

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.micro.tax.compute`: calculul trimestrial al impozitului micro (1%/3% din venituri), cu mașina de stări, generarea notei contabile Dr 698 = Cr 4418 și metoda cron `_cron_check_micro_threshold`.
- `res.company` / `res.config.settings` (extinse): regimul fiscal, pragul în EUR, conturile excluse din baza de calcul și data ieșirii din regimul micro.

**Vizualizări / Date**

- `views/l10n_ro_micro_tax_views.xml`: lista și formularul pentru crearea, calculul și postarea calculelor de impozit micro.
- `views/res_config_settings_views.xml`: opțiunile regimului micro în Setări Contabilitate.
- `data/ir_cron.xml`: definiția jobului lunar de monitorizare a plafonului.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_check_micro_threshold` („RO: Check Micro-Enterprise Threshold"): rulează lunar, dar este creat inactiv; emite avertizare pe fișa companiei la 80% din plafon și declanșează tranziția la impozit pe profit la depășirea celor 500.000 EUR.

#### 5. Conexiuni

- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md): regimul în care tranzitează compania la depășirea plafonului micro; trimestrele următoare se calculează acolo.
- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): declararea obligației de impozit micro (linia 121), din notele postate de acest modul.
- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): scăzăminte din sponsorizări, acolo unde este cazul.
- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): checklist fiscal trimestrial.
