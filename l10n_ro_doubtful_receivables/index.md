# Romania - Doubtful Receivables and Impairment Adjustments (491) (localizat la `l10n_ro_doubtful_receivables/index.md`)

- **Nume Tehnic:** `l10n_ro_doubtful_receivables`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_doubtful_receivables
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_doubtful_receivables`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul acoperă tratamentul contabil și fiscal al creanțelor comerciale devenite incerte, conform OMFP 1802/2014 (principiul prudenței) și art. 26 alin. (1) lit. c) din Codul fiscal. Odoo standard urmărește vechimea creanțelor, dar nu le reclasifică în clienți incerți, nu constituie ajustarea pentru depreciere și nu separă partea deductibilă fiscal de cea nedeductibilă. Modulul introduce un dosar de creanță incertă, cu un flux în patru momente contabile, iar diferența permanentă nedeductibilă devine o cifră vizibilă pe fiecare dosar. Este în stadiul de dezvoltare Alpha.

#### 2. Funcționalități Cheie

- **Dosar de creanță incertă** (numerotat `CI/AAAA/nnnnn`, cu chatter și activități) cu flux în momente distincte, fiecare cu nota lui contabilă: reclasificare, ajustare, apoi reluare sau scoatere din evidență.
- **Reclasificare** `Dr 4118 = Cr 4111`, cu reconcilierea automată a liniei de creanță din factură, pentru ca soldul să nu apară dublu (pe 4111 și pe 4118).
- **Ajustare pentru depreciere** `Dr 6814 = Cr 491`, pe o sumă propusă din politica de vechime sau introdusă manual.
- **Limita fiscală de 30%** ca parametru de companie: fiecare dosar arată partea deductibilă și diferența permanentă nedeductibilă. Procentul se îngheață pe dosar la creare, deci o modificare ulterioară a setării nu rescrie istoricul. Cota rămâne editabilă pe dosar (ex. 100% pentru faliment). Condițiile cumulative de deductibilitate (peste 270 de zile de la scadență, negarantată, debitor neafiliat) sunt modelate ca bife pe dosar; detaliile sunt în fișa consultantului.
- **Reluarea ajustării** `Dr 491 = Cr 7814` la încasarea creanței (buton Recovered) și la scoaterea din evidență.
- **Scoatere din evidență** `Dr 654 = Cr 4118` pentru pierderea definitivă, cu reluarea prealabilă a ajustării.
- **Politici de ajustare pe vechime**: tranșe configurabile (ex. 90 zile → 20%, 180 → 50%, 365 → 100%); se aplică tranșa cu pragul cel mai mare atins de vechime.
- **Wizard „Propose from Overdue Invoices”**: propune în bloc facturile restante peste un prag de zile (implicit 270), sare facturile deja marcate și nu postează nimic, propunerile rămânând ciorne.
- **Semnalarea ajustărilor orfane**: filtrul „Needs Reversal” și un cron zilnic care creează activități pe dosarele cu factura încasată și ajustarea rămasă în sold. Reluarea o face manual contabilul.
- **Totaluri în listă**: coloanele Tax Deductible și Non-Deductible, utile pentru registrul fiscal și D101.
- **Configurare** în Contabilitate → Configurare → Setări, secțiunea „Doubtful Receivables (RO)” (vizibilă doar pentru companii cu țara fiscală România): conturile 4118, 491, 6814, 7814, 654, jurnalul notelor și procentul deductibil. Dacă un cont lipsește, acțiunea se oprește cu mesaj explicit, fără nota incompletă.
- **Meniuri**: Contabilitate → Tranzacții → Doubtful Receivables (dosare și wizardul de propunere); Contabilitate → Configurare → Contabilitate → Doubtful Receivable Policies.
- **Acces**: managerul contabil (`account.group_account_manager`) are drepturi complete; utilizatorul contabil (`account.group_account_user`) doar citire.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `mail`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.doubtful.receivable`: dosarul de creanță incertă (`mail.thread` + `mail.activity.mixin`), cu client, factură, sume, procent deductibil înghețat, stare și legături către notele contabile (reclasificare, ajustare, reluare, scoatere din evidență); conține cron-ul `_cron_flag_collected_receivables`.
- `l10n.ro.doubtful.policy` / `l10n.ro.doubtful.policy.line`: politica de ajustare pe vechime și tranșele ei (zile restanță → procent).
- `l10n.ro.doubtful.propose.wizard` (tranzitoriu): propunerea în bloc a dosarelor din facturile restante.
- `res.company` (extins): conturile 4118, 491, 6814, 7814, 654, jurnalul și procentul deductibil.
- `res.config.settings` (extins): câmpurile de configurare aferente, afișate doar pentru companii cu țara fiscală România.

**Vizualizări**

- `view_doubtful_receivable_list`, `view_doubtful_receivable_form`, `view_doubtful_receivable_search`: lista (cu totaluri deductibil / nedeductibil), formularul cu butoanele fluxului și filtrele (inclusiv Needs Reversal).
- `view_doubtful_policy_form`, `view_doubtful_policy_list`: politicile de ajustare.
- `view_doubtful_propose_wizard_form`: wizardul de propunere.
- `res_config_settings_view_form_doubtful`: secțiunea din Setări contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `cron_flag_collected_receivables`: rulează zilnic și creează activitate pe dosarele unde factura a fost încasată dar ajustarea a rămas în sold.
- `seq_doubtful_receivable`: secvența `CI/%(year)s/` (ir.sequence) pentru numerotarea dosarelor.

#### 5. Conexiuni

Nu există legături funcționale cu alte module din monorepo verificate în cod (modulul depinde doar de `account`, `l10n_ro` și `mail`). Conturile 4118, 491, 6814, 7814 și 654 sunt preluate din planul de conturi al `l10n_ro`. Legăturile cu declarațiile (registrul fiscal, D101) sunt descrise doar în fișa consultantului, fără dependență în cod.
