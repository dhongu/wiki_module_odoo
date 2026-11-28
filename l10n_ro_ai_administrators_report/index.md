# Romania - Raportul administratorilor cu Plutus (AI) (localizat la `l10n_ro_ai_administrators_report/index.md`)

- **Nume Tehnic:** `l10n_ro_ai_administrators_report`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_ai_administrators_report
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_ai_administrators_report`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Plutus, agentul AI de analiză financiară, scrie draftul textelor din raportul administratorilor cerut de OMFP 1802/2014 (pct. 489–491), pornind de la indicatorii F10/F20/F30 și de la analiza anuală. Administratorul citește, corectează și confirmă; agentul nu confirmă niciodată raportul.

#### 2. Funcționalități Cheie

- Butonul *Draft cu Plutus* pe raportul în ciornă: trimite agentului indicatorii raportului (exercițiul curent și precedent) și, dacă există, analiza anuală a aceluiași exercițiu, cu abaterile și cauzele lor.
- Scrie doar în secțiunile goale: dezvoltarea și performanța (pct. 489), riscurile, indicatorii-cheie și evoluția previzibilă cu riscul financiar (pct. 491). Ce a scris administratorul rămâne neatins.
- Nu inventează: cercetarea-dezvoltarea, sucursalele, acțiunile proprii și resursele necorporale nu se trimit agentului și se completează manual.
- Fiecare cifră din text e verificată în datele trimise; cifrele negăsite se evidențiază în text și se listează pe formular.
- Confirmarea raportului așteaptă revizuirea (*Texte revizuite*); la revizuire evidențierile se scot, ca să nu ajungă în PDF.
- Un eșec AI nu strică raportul: eroarea se afișează, iar textele rămân cum erau.
- Flux: *Contabilitate → Raportare → Rapoarte de extras → Raportul administratorilor* → *Calculează indicatorii* → *Draft cu Plutus* → *Texte revizuite* → *Confirmă*. Pașii detaliați sunt în fișa consultantului.
- Agentul și anonimizarea partenerilor se configurează în setările analizei financiare.

#### 3. Dependențe

- [l10n_ro_financial_statements](../l10n_ro_financial_statements/index.md)
- [deltatech_ai_financial_analysis](../deltatech_ai_financial_analysis/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.fs.administrators.report` (extins): adaugă acțiunile de draft AI (`action_ai_draft`), marcarea ca revizuit (`action_ai_mark_reviewed`), verificarea cifrelor și blocarea confirmării până la revizuire.

**Vizualizări**

- `view_l10n_ro_fs_administrators_report_form`: extinde formularul raportului cu butonul *Draft cu Plutus*, banda cu secțiunile scrise, cifrele negăsite și *Texte revizuite*.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_partner_financials](../l10n_ro_partner_financials/index.md): aceeași familie de extensii pentru analiza financiară (bonitatea partenerilor), fără dependență directă.
