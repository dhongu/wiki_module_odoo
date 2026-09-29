# Romania - Declarația 307 (ajustări de TVA) (localizat la `l10n_ro_anaf_d307/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d307`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d307
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d307`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite întocmirea Declarației 307 (formularul ANAF privind sumele rezultate din ajustarea, corecția ajustărilor sau regularizarea taxei pe valoarea adăugată). Se depune de persoana impozabilă care a ajustat TVA-ul în urma transferului de active, a transferului proprietății asupra activelor fixe din leasing sau a anulării codului de TVA. Operațiunile se introduc pe rânduri, totalurile se calculează automat, iar declarația se exportă în XML acceptat de ANAF.

#### 2. Funcționalități Cheie

- Declarația se creează din **Contabilitate → Raportare → Declarații ANAF → D307 Ajustări de TVA** (acces pentru grupul contabil) și are stările Ciornă / Confirmată.
- Trei tipuri de operațiuni: **A** (transfer de active), **L** (transferul dreptului de proprietate asupra activelor corporale fixe din leasing) și **C** (anularea codului de TVA conform art. 316 alin. (11) lit. a)–e), g) sau h) din Codul fiscal).
- Fiecare operațiune are operatorul implicat (cedent, finanțator sau beneficiar) și TVA-ul aferent; codul fiscal și denumirea se preiau de pe partener cu un singur clic, fără prefixul RO.
- Totalurile pe cele trei tipuri și suma de control se calculează automat, cu sume întregi (lei), conform regulilor ANAF; TVA-ul poate fi negativ.
- Suport pentru declarație rectificativă și pentru declarația depusă după anularea rezervei verificării ulterioare, caz în care temeiul legal este obligatoriu (art. 105 alin. (6) lit. a) sau b) din Legea 207/2015).
- Semnatarul (nume, funcție) intră în antetul XML.
- Validări la export: CUI-ul companiei, numele semnatarului, cel puțin o operațiune și unicitatea perechii (tip, cod operator) — un operator nu poate apărea de două ori pe același tip.
- Export XML conform schemei `d307_20171205.xsd` (OPANAF 793/2016, validator J1.1.0).
- Modulul nu generează note contabile; raportează sumele deja ajustate în contabilitate. Fluxul pas cu pas este în fișa consultant.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d307`: declarația (perioadă, stare, rectificativă, temei legal, semnatar, totaluri, fișier XML); moștenește `mail.thread`, `mail.activity.mixin` și `l10n_ro_anaf.report.handler.mixin`.
- `l10n.ro.anaf.d307.line`: o operațiune declarată (tip, partener/operator, cod, denumire, TVA); generează elementul `<operatie>` din XML.

**Vizualizări**

- `view_l10n_ro_anaf_d307_list`: lista declarațiilor, cu perioadă, totaluri și stare.
- `view_l10n_ro_anaf_d307_form`: formularul declarației, cu antet, operațiuni, totaluri și export XML.

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_anaf_d307`: acțiunea de fereastră (listă/formular) și meniul `menu_l10n_ro_anaf_d307`. Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): decontul de TVA al perioadei, unde ajustarea își are corespondentul contabil (corelație manuală, nu există legătură tehnică).
