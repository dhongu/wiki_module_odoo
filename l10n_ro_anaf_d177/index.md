# Romania - Cerere de redirecționare a impozitului (D177) (localizat la `l10n_ro_anaf_d177/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d177`
- **Versiune:** `20.0.1.1.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d177
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d177`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Cererea 177 permite redirecționarea unei părți din impozitul pe profit sau pe veniturile microîntreprinderilor către beneficiari (art. 25 alin. (4) lit. i) din Codul fiscal). Se depune separat de D107: D107 raportează sponsorizările acordate, iar D177 cere virarea impozitului către beneficiari, în limita sumei rămase.

#### 2. Funcționalități Cheie

- Cerere cu linii de beneficiari: denumire, cod fiscal, tip, IBAN, sumă și acord obținut.
- Plafonul de redirecționare, suma redirecționată anterior și restul disponibil, calculat automat.
- Completarea liniei din partener, inclusiv IBAN-ul din conturile bancare (IBAN-ul e obligatoriu).
- Tipuri de beneficiar: entitate nonprofit, UNICEF, bursă privată, întreprindere socială sau alt caz legal.
- Export XML validat cu schema oficială `d177_20260309.xsd`; exportul e blocat dacă totalul cerut depășește restul disponibil.
- Meniu: *Contabilitate → Raportare → Declarații ANAF → D177 Redirecționare impozit*; fluxul pas-cu-pas este în fișa consultantului.
- Versiune formular: structura v1.0.8 din 09.03.2026, verificată cu DUKIntegrator la 12.09.2026.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d177`: cererea (an fiscal, plafon, redirecționat anterior, rest), cu `mail.thread`, activități și mixinul de export.
- `l10n.ro.anaf.d177.line`: linia de beneficiar.

**Vizualizări**

- `view_l10n_ro_anaf_d177_list` și `view_l10n_ro_anaf_d177_form`: lista și formularul cererii.
- `action_l10n_ro_anaf_d177`: acțiunea de meniu.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): D107 raportează sponsorizările; D177 cere virarea impozitului, separat.
