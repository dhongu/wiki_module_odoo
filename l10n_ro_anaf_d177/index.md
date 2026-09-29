# Romania - Cerere de redirecționare a impozitului (D177) (localizat la `l10n_ro_anaf_d177/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d177`
- **Versiune:** `19.0.1.1.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d177
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d177`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul pregătește Cererea 177, prin care o firmă care a acordat sponsorizări cere ca o parte din impozitul pe profit sau pe veniturile microîntreprinderilor să fie virată direct către beneficiari (art. 25 alin. (4) lit. i) din Codul fiscal). Cererea se depune separat de D107: D107 raportează sponsorizările acordate, iar D177 cere virarea impozitului. Modulul calculează restul disponibil de redirecționat și generează fișierul XML pentru ANAF, validat cu schema oficială.

#### 2. Funcționalități Cheie

- Cerere proprie (model cu linii de beneficiari): denumire, cod fiscal, adresă, tip beneficiar, contract de sponsorizare, IBAN, sumă redirecționată, acord obținut, telefon și e-mail.
- Antet cu anul fiscal, perioada, opțiunile de cerere rectificativă și numele semnatarului; meniul este în **Contabilitate → Raportare → Declarații ANAF → D177 Redirecționare impozit**.
- Plafon de redirecționare, sumă redirecționată anterior și **rest disponibil**, calculat automat; totalul cerut se însumează pe cerere.
- Alegerea partenerului completează automat denumirea, codul fiscal și IBAN-ul din conturile lui bancare.
- Flux cu stări: ciornă, confirmare, revenire în ciornă; apoi export XML.
- Validări la confirmare/export: beneficiarul are nevoie de cod fiscal, denumire, IBAN și sumă pozitivă; contractul de sponsorizare este obligatoriu pentru toate tipurile de beneficiar, cu excepția tipului 5 („alt beneficiar prevăzut de lege”), conform regulii ANAF R27.
- Export XML validat cu schema oficială `d177_20260309.xsd`; exportul este **blocat** dacă totalul cerut depășește restul disponibil.
- Modulul nu generează note contabile; este o cerere administrativă. Fluxul detaliat pas-cu-pas este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d177`: cererea D177 (moștenește `mail.thread`, `mail.activity.mixin` și `l10n_ro_anaf.report.handler.mixin`); conține antetul, plafonul, restul, starea și fișierul XML generat.
- `l10n.ro.anaf.d177.line`: linia de beneficiar (partener, tip, contract, IBAN, sumă, acord), cu completare automată din partener și export în XML.

**Vizualizări**

- `view_l10n_ro_anaf_d177_list`: lista cererilor.
- `view_l10n_ro_anaf_d177_form`: formularul cererii, cu tabul de beneficiari și butoanele Confirmă / Exportă XML.
- `action_l10n_ro_anaf_d177` și `menu_l10n_ro_anaf_d177`: acțiunea și meniul de acces.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): declarația pereche, care raportează sponsorizările acordate; corelație manuală, beneficiarii nu se preiau automat.
- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md): creditul fiscal de sponsorizare din care rezultă plafonul (completat manual).
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): depunerea electronică prin SPV, complementară.
