# Romania - Raportul administratorilor cu Plutus (AI)

- **Nume Tehnic:** `l10n_ro_ai_administrators_report`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_ai_administrators_report
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_ai_administrators_report`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Plutus, agentul AI de analiză financiară, scrie draftul textelor din raportul administratorilor cerut de OMFP 1802/2014 (pct. 489–491), pornind de la indicatorii din situațiile financiare și, dacă există, de la analiza anuală a aceluiași exercițiu. Administratorul citește, corectează și confirmă textele: agentul nu confirmă niciodată raportul. Modulul economisește timp la redactare, fără a risca cifre inventate.

#### 2. Funcționalități Cheie

- Butonul *Draft cu Plutus* pe raportul aflat în ciornă: trimite agentului indicatorii din rândurile F10, F20 și F30 (exercițiul curent și cel precedent) și, dacă există, analiza anuală a exercițiului, cu abaterile și cauzele lor.
- Scrie doar în secțiunile goale: dezvoltarea și performanța (pct. 489), riscurile, indicatorii-cheie (pct. 491 alin. 1), evoluția previzibilă și riscul financiar (pct. 491 alin. 2). Textul precompletat cu cifre al dezvoltării se înlocuiește; ce a scris administratorul rămâne neatins. Pentru a recere draftul unei secțiuni, aceasta se golește și se apasă din nou butonul.
- Nu inventează: cercetarea-dezvoltarea, sucursalele, acțiunile proprii și resursele necorporale nu se trimit agentului și rămân de scris de administrator.
- Fiecare cifră din text este verificată în datele trimise; cifrele negăsite se evidențiază în text și se listează într-o bandă galbenă pe formular, alături de secțiunile scrise.
- Confirmarea așteaptă revizuirea: cât timp draftul nu e marcat *Texte revizuite*, raportul nu se poate confirma. La revizuire, evidențierile se scot, ca să nu ajungă în PDF.
- Un eșec AI nu strică raportul: eroarea apare într-o bandă roșie, iar textele rămân cum erau.
- Cale de lucru: *Contabilitate → Raportare → Rapoarte de extras → Raportul administratorilor*; indicatorii se calculează cu *Calculează indicatorii* (sau automat la draft). Agentul și anonimizarea partenerilor se configurează în setările analizei financiare.
- Starea draftului (`Plutus Draft`): Fără draft, Draft de revizuit, Draft cu cifre de verificat, Revizuit, Eșuat. Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- [l10n_ro_financial_statements](../l10n_ro_financial_statements/index.md)
- [deltatech_ai_financial_analysis](../deltatech_ai_financial_analysis/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.fs.administrators.report` (extins): adaugă starea draftului AI, secțiunile scrise, cifrele neverificate, eroarea, datele trimise agentului și data draftului; metodele `action_ai_draft`, `action_ai_mark_reviewed`, iar `action_confirm` este blocat până la revizuire.

**Vizualizări**

- `view_l10n_ro_fs_administrators_report_form`: moștenește formularul raportului; adaugă butoanele *Draft cu Plutus* și *Texte revizuite*, banda galbenă (secțiuni scrise, cifre de verificat), banda roșie de eroare și o filă cu datele trimise agentului.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_financial_statements](../l10n_ro_financial_statements/index.md): raportul administratorilor și documentul de depunere F10/F20/F30 din care provin indicatorii.
- [deltatech_ai_financial_analysis](../deltatech_ai_financial_analysis/index.md): agentul Plutus, analiza anuală și verificarea cifrelor.
