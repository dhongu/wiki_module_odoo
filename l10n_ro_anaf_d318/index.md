# Romania - Declarația D318 ANAF (localizat la `l10n_ro_anaf_d318/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d318`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d318
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d318`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru generarea **Declarației 318** — cererea de rambursare a TVA plătit în alt stat membru UE de persoane impozabile stabilite în România (Directiva 2008/9/CE). Este util firmelor cu achiziții în UE (combustibil, transport, cazare, taxe de drum, târguri) care vor să recupereze TVA-ul local. Raportul adună facturile eligibile, grupate pe statul de rambursare, și exportă XML-ul cererii. Necesită Odoo Enterprise.

#### 2. Funcționalități Cheie

- **Categorisire automată** a cheltuielilor pe codurile ANAF 1–10 (combustibil, transport, cazare, catering, târguri, altele), prin câmpul „Cod cheltuială D318" de pe cont; liniile fără cod primesc 10 — Altele.
- **Filtrare** a facturilor de furnizor din UE cu TVA plătit în statul respectiv; facturile cu TVA 0% nu sunt eligibile, iar notele de credit reduc totalurile.
- **Raport** în **Contabilitate → Raportare → Declarații (legal) → D318 - Rambursare TVA UE**, cu CIF furnizor, document, dată, cod cheltuială, bază, TVA și TVA deductibil.
- **Export XML (Soft J)**: un fișier pe stat de rambursare, livrat în ZIP dacă sunt mai multe state; validat cu schema `d318_20171107.xsd` înainte de descărcare.
- **Pro-rata**: cota de deducere se aplică din amonte (modul de deductibilitate sau manual); implicit TVA-ul e integral deductibil.
- **Setări** în **Setări → Contabilitate → Declarații ANAF România**: limba cererii, tipul titularului de cont și contul bancar de rambursare (implicit primul cont al companiei); adresa de e-mail a companiei este obligatorie.
- Termen de depunere: 30 septembrie a anului următor; praguri minime 50 EUR pe stat (cerere anuală) și 400 EUR (trimestrială).

Fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `account.account` (extins): câmpul „Cod cheltuială D318" (1–10) pe planul de conturi.
- `res.config.settings` / `res.company` (extinse): parametrii cererii D318 (limbă, tip titular, cont bancar).
- `l10n_ro_anaf_d318.tax.report.handler`: identifică facturile eligibile și generează exportul XML D318; folosește mixin-ul `l10n_ro_anaf.report.handler.mixin`.

**Vizualizări**

- `views/account_account_views.xml`: codul de cheltuială D318 pe fișa contului.
- `views/res_config_settings_views.xml`: setările D318 în Contabilitate.
- `data/d318_report.xml`: raportul D318.
- `report/d318_xml_template.xml`: șablonul QWeb al XML-ului ANAF.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul XML se declanșează manual din raport.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună de declarații ANAF (mixin handler, export, date declarant).
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): decontul de TVA, din același ecosistem de raportare fiscală RO.
- [l10n_ro_anaf_d398](../l10n_ro_anaf_d398/index.md): declarația privind TVA la încasare, din același ecosistem.
