# Romania - Obiecte de inventar pe salariat

- **Nume Tehnic:** `l10n_ro_inventory_items_hr`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_inventory_items_hr
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_inventory_items_hr`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde Obiectele de inventar cu darea în folosință pe salariat (`hr.employee`), nu doar pe un utilizator Odoo, deci și salariații fără cont pot primi obiecte. Bonul de dare în folosință, PV-ul de scoatere din gestiune și registrul arată salariatul. Modulul se instalează explicit, ca aplicația Angajați să nu fie instalată la firmele care nu o folosesc.

#### 2. Funcționalități Cheie

- Câmpul Salariat pe fișa obiectului, în listă și în căutare (Inventar → Obiecte de Inventar → Registru OI), cu grupare după salariat.
- Câmpul Salariat în wizardul Dare în Folosință (batch); dacă salariatul are utilizator, acesta devine responsabil. Salariatul rămâne modificabil după darea în folosință, cu urmă în chatter; o mutare nu generează bon nou, ci se retipărește bonul din fișă.
- Bonul de Dare în Folosință arată salariatul în coloana Responsabil; Registrul OI grupează pe salariat, cu subtotal.
- Lipsă imputată: la Scoate din Gestiune cu tipul Pierdută / Lipsă și Imputat pe Salariat (4282), persoana căreia i se impută se completează cu contactul salariatului; suma 0 înseamnă valoarea de înregistrare.
- Modulul nu postează note proprii; rămân notele din baza (603 = 303 și 8035, 4282 = 7588, stornarea lui 8035).
- Fluxul pas cu pas stă în fișa consultantului.

#### 3. Dependențe

- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md)
- `hr`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.inventory.item`: extins cu câmpul Salariat.
- `l10n.ro.inventory.item.use.wizard`: wizardul de dare în folosință, cu Salariat.
- `l10n.ro.inventory.item.dispose.wizard`: wizardul de scoatere din gestiune, cu imputare pe salariat.

**Vizualizări**

- `l10n_ro_inventory_item_views.xml`: formular, listă și căutare cu Salariat.
- `inventory_item_use_wizard_views.xml`: wizardul de dare în folosință.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md): modulul de bază, cu notele 303 / 603 / 8035.
