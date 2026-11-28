# Romania - Creanțe incerte și ajustări pentru depreciere (491)

- **Nume Tehnic:** `l10n_ro_doubtful_receivables`
- **Versiune:** `20.0.1.0.8`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_doubtful_receivables
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_doubtful_receivables`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Tratamentul contabil și fiscal al creanțelor comerciale devenite incerte, conform OMFP 1802/2014 și art. 26 alin. (1) lit. c) din Codul fiscal. Odoo standard urmărește vechimea creanțelor, dar nu are reclasificarea în clienți incerți, ajustarea pentru depreciere și separarea părții deductibile de cea nedeductibilă. Modulul le adaugă, cu notă contabilă distinctă pe fiecare moment.

#### 2. Funcționalități Cheie

- Dosar de creanță incertă, cu flux în patru momente: reclasificare, ajustare, reluare sau scoatere din evidență.
- Reclasificare `Dr 4118 = Cr 4111`, cu reconcilierea automată a liniei de creanță din factură.
- Ajustare pentru depreciere `Dr 6814 = Cr 491`, pe sumă propusă din politică sau introdusă manual.
- Limita fiscală de deducere (implicit 30%, parametru de companie): fiecare dosar arată partea deductibilă și diferența permanentă nedeductibilă; procentul se îngheață pe dosar la creare.
- Reluarea ajustării `Dr 491 = Cr 7814` la încasare sau scoatere din evidență; scoatere din evidență `Dr 654 = Cr 4118`.
- Politici de ajustare pe vechime, cu tranșe configurabile (ex. 90 zile - 20%, 180 - 50%, 365 - 100%).
- Wizard „Propune din facturi restante” (restanță minimă implicită 270 de zile): creează dosare în ciornă, nu postează nimic și sare facturile care au deja dosar.
- Cron zilnic care creează activitate pe dosarele cu factura încasată și ajustarea rămasă în sold; filtrul „Necesită reluare”.
- Configurare în Contabilitate → Configurare → Setări (conturi 4118, 491, 6814, 7814, 654, jurnal, cotă deductibilă); meniu în Contabilitate → Tranzacții → Creanțe incerte.
- Rolul Contabil creează și modifică dosarele; Utilizator contabil are doar citire.
- Fluxul complet este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`
- `mail`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.doubtful.receivable`: dosarul de creanță incertă (cu `mail.thread` și activități).
- `l10n.ro.doubtful.policy` / `l10n.ro.doubtful.policy.line`: politica de ajustare și tranșele ei de vechime.
- `l10n.ro.doubtful.propose.wizard`: wizardul de propunere din facturi restante.
- `res.company` / `res.config.settings` (extinse): conturi, jurnal și cota deductibilă.

**Vizualizări**

- `views/l10n_ro_doubtful_receivable_views.xml`: formular și listă cu totaluri deductibil / nedeductibil.
- `views/l10n_ro_doubtful_policy_views.xml`: politicile și tranșele.
- `views/res_config_settings_views.xml`: setările modulului.
- `wizard/l10n_ro_doubtful_propose_wizard_views.xml`: wizardul de propunere.

**Acțiuni Automate / Acțiuni Server**

- `cron_flag_collected_receivables` (`ir.cron`): zilnic, semnalează ajustările rămase pe creanțe încasate.
- `seq_doubtful_receivable` (`ir.sequence`): numerotarea dosarelor.

#### 5. Conexiuni

- [l10n_ro_doubtful_receivables_profit_tax](../l10n_ro_doubtful_receivables_profit_tax/index.md): preia diferența permanentă în registrul de evidență fiscală și în D101.
