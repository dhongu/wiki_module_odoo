# Romania - Vector fiscal și Fișa pe rol (SPV ANAF) (localizat la `l10n_ro_anaf_fiscal_status/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_fiscal_status`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_fiscal_status](https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_fiscal_status)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_fiscal_status`
- **Ultima Ingestie:** `2026-07-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul descarcă automat, din Spațiul Privat Virtual (SPV) al ANAF, pentru fiecare companie și punct de lucru, două evidențe esențiale: vectorul fiscal (ce obligații declarative are contribuabilul și cu ce periodicitate) și fișa pe rol (ce sume are de plătit, restanțe și accesorii). Datele sunt păstrate cu istoric, oferind echipei financiare o imagine clară și la zi asupra situației fiscale a companiei, fără a mai fi nevoie de verificări manuale în portalul ANAF.

#### 2. Funcționalități Cheie

- Descărcare automată din SPV a **vectorului fiscal** (`l10n.ro.fiscal.vector`) — obligațiile declarative active: TVA lunar/trimestrial, impozit pe profit vs. micro, salarii (D112), accize, dividende, nerezidenți.
- Arhivare automată a obligațiilor ieșite din vigoare (prin D700), cu păstrarea istoricului (`active=False`).
- Descărcare automată a **fișei pe rol** (`l10n.ro.fiscal.ledger`) — sume de plată, restanțe și accesorii pe fiecare cod de creanță bugetară, ca snapshot append-only cu istoric pe ani.
- Păstrarea documentului-sursă ANAF (PDF/registru) atașat la fiecare snapshot, pentru audit.
- Transport prin infrastructura existentă Terrabit Connect (mTLS la SPVWS2, fără OAuth2 Bearer) și coada de joburi din `l10n_ro_anaf_agent` (tip job `fiscal_status`) — modulul nu reinventează transportul, adaugă doar tipul de cerere și cele două modele de evidență.
- Cron zilnic de descărcare (dezactivat implicit) și cron zilnic de remindere pentru termenele de depunere apropiate (activitate `mail.activity`), pe baza mapării categorie fiscală → declarație Odoo (D300, D112, D101, D100, D103, D390).
- Alimentează calendarul real de declarații (FR-60) și auditul de corelare a declarațiilor (FR-65).

#### 3. Dependențe

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md)
- [l10n_ro_anaf_messages](../l10n_ro_anaf_messages/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.fiscal.vector`: obligație declarativă activă din vectorul fiscal al companiei; reține categoria fiscală, periodicitatea, declarația Odoo asociată și intervalul de valabilitate; obligațiile ieșite din vigoare sunt arhivate (`active=False`), păstrând istoricul.
- `l10n.ro.fiscal.ledger`: snapshot append-only al fișei pe rol la o dată (`snapshot_date`) — sumă de plată, restanță, accesorii per cod de creanță bugetară, cu document-sursă ANAF atașat; unicitate pe (companie, dată, cod creanță).
- `res.company` (extins): orchestrează descărcarea (cale on-prem prin agent local sau cale cloud prin job) și aplică rezultatul normalizat peste vectorul fiscal și fișa pe rol (`_l10n_ro_apply_fiscal_status`, `_l10n_ro_apply_fiscal_vector`, `_l10n_ro_apply_fiscal_ledger`).
- `deltatech.tc.station` (extins din `l10n_ro_anaf_agent`): adaugă acțiunea `action_enqueue_fiscal_status` pentru a pune în coadă un job de tip `fiscal_status`.
- `deltatech.tc.job` (extins din `l10n_ro_anaf_agent`): adaugă valoarea de selecție `fiscal_status` și procesează rezultatul jobului, apelând `_l10n_ro_apply_fiscal_status` pe companie.

**Vizualizări**

- `view_l10n_ro_fiscal_vector_list` / `view_l10n_ro_fiscal_vector_form`: listă și formular pentru vectorul fiscal, cu evidențierea vizuală a liniilor arhivate (`decoration-muted`) și ribbon „Arhivat”.
- `view_l10n_ro_fiscal_ledger_list` / `view_l10n_ro_fiscal_ledger_form`: listă și formular pentru fișa pe rol, cu evidențierea restanțelor (`decoration-danger`) și totaluri pe coloane (sumă de plată, restanță, accesorii, total datorat).
- `menu_l10n_ro_fiscal_vector` / `menu_l10n_ro_fiscal_ledger`: intrări de meniu „Vector fiscal” și „Fișa pe rol”, subordonate meniului de declarații ANAF din `l10n_ro_anaf_base`.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_download_fiscal_status` (inactiv implicit): cron zilnic care pune în coadă câte un job `fiscal_status` pentru fiecare agent (stație Terrabit Connect) activ.
- `ir_cron_fiscal_deadline_reminders` (inactiv implicit): cron zilnic care emite activități de reminder pentru obligațiile fiscale din vector aflate aproape de termenul de depunere (implicit cu 7 zile înainte).

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează meniul de declarații ANAF în care se integrează „Vector fiscal” și „Fișa pe rol”.
- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md): furnizează infrastructura de agent (stații, joburi) folosită pentru transportul cererilor către SPV.
- [l10n_ro_anaf_messages](../l10n_ro_anaf_messages/index.md): furnizează clientul SPV (`anaf_spv_client.make_spv_request`) folosit pentru calea on-prem de descărcare.
