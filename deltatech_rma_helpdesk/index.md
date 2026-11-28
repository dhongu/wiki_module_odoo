# RMA - Helpdesk (localizat la `deltatech_rma_helpdesk/index.md`)

- **Nume Tehnic:** `deltatech_rma_helpdesk`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_rma_helpdesk
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_rma_helpdesk`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un tichet de Helpdesk este o conversație, un retur este un document: linii cu cantități, un motiv care poartă o politică, o fișă care călătorește în colet, un verdict pe fiecare produs și banii la final. Panoul After-Sales din Odoo îi dă tichetului wizardul standard de retur; acest modul îi dă în schimb o cerere de retur completă, din [deltatech_rma](../deltatech_rma/index.md), și le leagă pe cele două. Modul Enterprise, din suita bitshop_ent.

#### 2. Funcționalități Cheie

- Butonul **Cerere de retur** pe tichet, precompletat cu clientul, comanda de vânzare de pe tichet și liniile ei returnabile.
- Cererea se deschide ca formular nesalvat: un clic greșit nu consumă un număr RMA și nu lasă o cerere goală în registru.
- Contor și scurtătură pe tichet, legătură înapoi la tichet pe cerere.
- Rezultatul este scris pe tichet la aprobare, refuz și închidere, ca agentul de suport să-l citească fără să deschidă returul.
- Se activează per echipă, cu o bifă proprie lângă opțiunile After-Sales din Odoo (**Helpdesk > Configurare > Echipe Helpdesk**).

Fluxul operațional pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_rma](../deltatech_rma/index.md)
- `helpdesk_sale`

#### 4. Componente Cheie

**Modele**

- `helpdesk.team` (extins): bifa `use_deltatech_rma`.
- `helpdesk.ticket` (extins): `deltatech_rma_ids`, contorul și `action_create_deltatech_rma`.
- `deltatech.rma` (extins): `helpdesk_ticket_id` (`ondelete=set null`) și scrierea rezultatului pe tichet la `action_approve` / `action_refuse` / `action_close`.

**Vizualizări**

- `helpdesk_team_view_form_rma`: bifa pe echipă.
- `helpdesk_ticket_view_form_rma`: butonul și contorul pe tichet.
- `view_deltatech_rma_form_helpdesk` / `view_deltatech_rma_search_helpdesk`: legătura și căutarea după tichet pe cerere.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [deltatech_rma](../deltatech_rma/index.md): cererea de retur, fișa, recepția, verdictele, nota de credit.
- `helpdesk_sale`: comanda de vânzare de pe tichet, din care se precompletează liniile (`auto_install` pe orice bază cu Helpdesk și Vânzări).
