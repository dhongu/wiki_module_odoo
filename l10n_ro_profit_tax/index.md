# Romania - Impozit pe profit (D100/D101) (localizat la `l10n_ro_profit_tax/index.md`)

- **Nume Tehnic:** `l10n_ro_profit_tax`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_profit_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_profit_tax`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul calculează automat impozitul pe profit conform Legii 227/2015 Titlul II, cu sprijin pentru D100 trimestrial (cumulat de la 1 ianuarie) și D101 anual. Pornind de la profitul contabil (venituri clasa 7 − cheltuieli clasa 6), aplică ajustări fiscale configurabile per cont, gestionează pierderea fiscală reportată (deducere FIFO, limita 70%) și creditul fiscal pentru sponsorizări, generând nota contabilă Dr 691 = Cr 441 la postare. Include și un Registru de evidență fiscală, pe modelul din OMF 808/2026, care listează ajustările pe rânduri, cu temei legal, și se reconciliază cu calculul anual. Se adresează companiilor plătitoare de impozit pe profit la cota de 16%.

#### 2. Funcționalități Cheie

- **Calcul pe perioadă**, la **Contabilitate → Contabilitate → Impozit pe Profit**: se aleg anul fiscal, perioada (T1, T2, T3 pentru D100, cu scadențe 25 apr / 25 iul / 25 oct, sau anual pentru D101, scadent 25 martie anul următor) și jurnalul de operațiuni diverse. Fiecare perioadă este cumulată de la 1 ianuarie; calculul anual este independent de cele trimestriale. La trecerea de la micro la profit în cursul anului se modifică manual **Data de la**.
- **Butonul Calculează din contabilitate** preia din rulajele perioadei, fără notele de închidere pe contul 121: venituri și cheltuieli (partea financiară separată pe prefixe de cont configurabile în setări, implicit 761–768, 786 și 663–668, 686), ajustările fiscale, sponsorizarea și cifra de afaceri netă (701–708 minus 709). Toate câmpurile de ajustare pot fi suprascrise manual.
- **Rânduri calculate direct din conturi:** impozitul pe profit (691, 692, 694, 697; nedeductibil, D101 rd. 23), protocolul (6231) peste limita de 2% din profitul contabil majorat cu impozitul și protocolul (rd. 26), sponsorizarea (6582), integral nedeductibilă (rd. 27), și amortizarea contabilă (6811) cu amortizarea fiscală editabilă. Regulile de ajustare pe aceste conturi sunt ignorate, ca să nu se numere de două ori.
- **Ajustări fiscale configurabile per cont**, la **Configurare → Impozit Profit → Ajustări fiscale**: cheltuieli nedeductibile (+, de exemplu amenzi pe 6581), venituri neimpozabile (−, dividende pe 761) și deduceri suplimentare (−, de exemplu cercetare-dezvoltare), cu procent per regulă.
- **Pierdere fiscală reportată** (art. 31 CF), la **Configurare → Impozit Profit → Pierderi reportate**: 5 ani pentru pierderile din 2024 încoace și 7 ani pentru cele de până în 2023, cu starea Activă / Epuizată / Expirată. **Sugerează deducere pierdere** aplică FIFO și limita de 70% din profitul impozabil; câmpul **(-) Pierdere dedusă efectiv** se poate modifica în limita impusă. Anularea calculului eliberează utilizările de pierdere.
- **Credit fiscal sponsorizări** (art. 25 alin. (4) lit. i) CF): cel mai mic dintre cheltuiala efectivă, 0,75% din cifra de afaceri netă și 20% din impozitul calculat, rotunjit în jos la leu.
- **Rotunjire:** impozitul se rotunjește la leu (0,50 în sus), iar nota are aceeași sumă ca declarația. **Cotă impozit (%)** se poate modifica pe calculul curent (de exemplu cotă redusă prin tratat). **De plată** scade creditul de sponsorizare și impozitul datorat pentru trimestrele anterioare, introdus manual cu valoarea declarată prin D100 (afișat 0 dacă rezultatul ar fi negativ).
- **Postare:** **Postează nota Dr 691 = Cr 441** (în practică pe 4411), datată în ultima zi a perioadei, cu verificări (stare ciornă, impozit de plată pozitiv, conturi existente, limita de 70% respectată); calculul devine doar pentru citire, iar **Vezi nota contabilă** deschide nota. Cu bază zero sau negativă postarea este refuzată („Impozitul de plată este zero"). Rectificare: **Anulează**, **Resetează la ciornă**, corectare și repostare (într-o perioadă blocată fiscal este nevoie de deblocare prealabilă).
- **Registru de evidență fiscală** (OMF 808/2026, care a abrogat OMFP 870/2005), la **Contabilitate → Contabilitate → Registru de evidență fiscală**: se creează pentru un an fiscal, se alege calculul anual și se apasă **Generează din calculul D101**; se reconciliază automat cu calculul. **Tipărește registrul** dă documentul cu Nr. crt., Explicații, Valoarea (lei), iar **Situație analitică a ajustărilor fiscale** este raportul detaliat pe coloane. **Închide anul** face registrul imutabil, **Redeschide** îl readuce în lucru. Deocamdată doar registrul anual; cel trimestral nu este acoperit.
- **Limitări:** impozitul minim pe cifra de afaceri (OUG 115/2023) nu e calculat automat (ajustare manuală a sumei **De plată**); pierderea fiscală a exercițiului se înregistrează manual în **Pierderi reportate**.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.profit.tax.compute`: calculul pe perioadă, cu mașina de stări `draft → posted → cancelled` și generarea notei Dr 691 = Cr 441.
- `l10n.ro.tax.adjustment`: ajustări fiscale per cont contabil (tip nedeductibil / neimpozabil / deducere și procent).
- `l10n.ro.tax.loss`: registrul pierderilor fiscale reportate, cu deducere FIFO și expirare la 5 sau 7 ani.
- `l10n.ro.tax.loss.usage`: utilizările de pierdere per calcul (suma dedusă).
- `l10n.ro.tax.register`: registrul de evidență fiscală, reconciliat cu calculul anual.
- `l10n.ro.tax.register.line`: rândurile registrului (ajustare, temei legal, valori).
- `res.company` / `res.config.settings` (extinse): conturile financiare D101 și parametrii de calcul.

**Vizualizări**

- `views/l10n_ro_profit_tax_views.xml`: interfața de calcul, ajustări fiscale și pierderi reportate.
- `views/l10n_ro_tax_register_views.xml`: interfața registrului de evidență fiscală.
- `views/res_config_settings_views.xml`: opțiunile de configurare (**Setări → Impozit pe profit (RO)**).
- `action_report_tax_register`, `action_report_tax_register_detail` (`ir.actions.report`): registrul tipărit și situația analitică a ajustărilor.
- `data/ir_sequence.xml`: secvența registrului de evidență fiscală.

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate; calculul, postarea, sugerarea deducerii pierderii și generarea registrului se declanșează manual.*

#### 5. Conexiuni

- [l10n_ro_micro_tax](../l10n_ro_micro_tax/index.md): regimul alternativ (micro); la depășirea plafonului compania trece la impozit pe profit, iar trimestrele următoare se calculează aici.
- [l10n_ro_account_return_pl_closing](../l10n_ro_account_return_pl_closing/index.md): închiderea de cont de profit și pierdere, sursă a rezultatului contabil (notele de închidere pe 121 sunt excluse din calcul).
- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): declararea impozitului trimestral; linia 103 se citește din notele postate de acest modul.
- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): raportarea creditului fiscal pentru sponsorizări.
- [l10n_ro_financial_statements](../l10n_ro_financial_statements/index.md): corelarea rezultatului fiscal cu cel contabil.
