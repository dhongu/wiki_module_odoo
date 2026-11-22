# Romania - Declarația D318 ANAF (localizat la `l10n_ro_anaf_d318/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d318`
- **Versiune:** `19.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d318
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d318`
- **Ultima Ingestie:** `2026-11-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul permite generarea Declarației 318 (Cerere de rambursare a TVA de către persoanele impozabile stabilite în România, depusă în alt stat membru UE) direct din Odoo Enterprise. Modulul este esențial pentru companiile românești care efectuează achiziții în alte state membre UE (combustibil, transport, cazare etc.) și doresc să recupereze TVA-ul plătit local în acele țări, conform procedurii stabilite prin Directiva 2008/9/CE.

#### 2. Funcționalități Cheie

- **Categorisire automată:** maparea cheltuielilor pe codurile standard ANAF (1–10: combustibil, închirierea mijloacelor de transport, cheltuieli legate de ele, taxe de drum/pod/tunel, călătorie, cazare, catering, târguri și expoziții, lux/divertisment/reprezentare, altele) prin câmpul **Cod cheltuială D318** de pe conturile de cheltuieli. Liniile fără cod mapat primesc implicit codul 10 („Altele”).
- **Filtrare inteligentă:** identificarea facturilor de furnizor din UE care conțin TVA plătit în statul respectiv; furnizorul trebuie să aibă țara (și, ideal, codul de TVA) completate, iar facturile cu TVA 0% nu sunt eligibile. Raportul (**Contabilitate → Raportare → Declarații (legal) → D318 - Rambursare TVA UE**) grupează facturile pe statul de rambursare și arată CIF furnizor, document, dată, cod cheltuială, bază / TVA / TVA deductibil și totalul solicitat.
- **Setări** (**Setări → Contabilitate → Declarații ANAF România**): limba cererii, tipul titularului de cont (solicitant / reprezentant) și contul bancar de rambursare (implicit primul cont bancar al companiei); compania trebuie să aibă e-mail completat, altfel exportul este refuzat.
- **Export XML:** butonul **D318 file XML (Soft J)** din bara raportului generează un fișier pe stat de rambursare (ZIP dacă sunt mai multe state), validat intern față de schema oficială ANAF înainte de descărcare. Sumele sunt în moneda statului de rambursare (EUR, HUF, PLN, CZK, SEK, DKK); o factură în altă monedă sau o notă de credit pentru o factură cerută anterior apare marcată și oprește exportul. Nota de credit din aceeași cerere se scade din factură.
- **Pro-rata:** modulul nu aplică un procent de deducere propriu cererii; cota se aplică din amonte (modulul de deductibilitate sau manual), iar implicit TVA-ul se raportează integral deductibil.
- **Depunere:** fișierul se încarcă în SPV ANAF (Declarații și formulare → D318); termen 30 septembrie a anului următor, sume minime de 50 EUR pe stat (cerere anuală) și 400 EUR (trimestrială). Formularul acceptat este actualizat la 14.04.2026 (schemă `d318_20171107.xsd`), validat cu DUKIntegrator la 13.09.2026.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `account.account` (extins): câmpul `l10n_ro_d318_code` — codul de cheltuială D318 (1–10) pe contul contabil.
- `res.company` / `res.config.settings` (extinse): `l10n_ro_d318_language`, `l10n_ro_d318_owner_type` și `l10n_ro_d318_bank_id` (limba cererii, tipul titularului, contul bancar de rambursare).
- `l10n_ro_anaf_d318.tax.report.handler`: handler de raport personalizat (cu mixin-ul `l10n_ro_anaf.report.handler.mixin`) care colectează facturile UE eligibile, le grupează pe stat, verifică moneda și notele de credit și generează XML-ul D318 (`export_to_xml`).

**Vizualizări**

- `view_account_form_d318`: câmpul de cod de cheltuială D318 pe fișa contului contabil.
- `res_config_settings_view_form_d318`: setările D318 în ecranul de configurare Contabilitate.
- `l10n_ro_anaf_d318_report` (`data/d318_report.xml`, acțiunea client `action_l10n_ro_anaf_d318_report`): raportul cu coloanele CIF furnizor, referință, dată, cod, bază, TVA și TVA deductibil.
- `d318_report_xml_template` (`report/d318_xml_template.xml`): șablonul XML al cererii.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server; exportul XML se declanșează manual din raportul D318.

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează infrastructura comună de generare/depunere a declarațiilor ANAF (mixin-ul de handler, validare, export).
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): declarație conexă de decont TVA, parte din același ecosistem de raportare fiscală RO.
- [l10n_ro_anaf_d398](../l10n_ro_anaf_d398/index.md): declarație informativă privind TVA la încasare, parte din același ecosistem de raportare fiscală RO.
