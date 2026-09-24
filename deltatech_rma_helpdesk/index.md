# RMA Helpdesk (localizat la `deltatech_rma_helpdesk/index.md`)

- **Nume Tehnic:** `deltatech_rma_helpdesk`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_rma_helpdesk
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_rma_helpdesk`
- **Ultima Ingestie:** 2026-09-24
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un tichet de Helpdesk e o conversație, un retur e un document: linii cu cantități, un motiv care poartă o politică, o fișă care călătorește în colet, un verdict pe fiecare produs și banii la final. Panoul After-Sales din Odoo îi dă tichetului wizardul standard de retur; puntea îi dă în schimb o cerere de retur completă, din [deltatech_rma](../deltatech_rma/index.md), și le leagă pe cele două. Modul Enterprise, din suita bitshop_ent.

#### 2. Funcționalități Cheie

- Bifă proprie pe echipă, **Cereri de retur**, în secțiunea *După Vânzare* (**Helpdesk → Configurare → Echipe HelpDesk**), separată de *Retururi* din Odoo, care instalează `helpdesk_stock`.
- Butonul **Cerere de retur** pe tichet (Alt+Shift+R), vizibil doar cu client pe tichet și pentru utilizatorii cu *Retururi / Utilizator*.
- Butonul deschide formularul cererii **nesalvat**, precompletat cu clientul, comanda de pe tichet, tichetul și liniile returnabile ale comenzii (cantitatea disponibilă, titlul tichetului ca descriere); cererea primește număr abia la salvare.
- Contorul **Retururi** pe tichet și legătura înapoi pe cerere (câmp și buton *Tichet*, căutare după tichet); ștergerea tichetului nu șterge cererea.
- Rezultatul e scris în istoricul tichetului la aprobare, refuz și rezolvare, ca agentul de suport să nu deschidă returul.

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

Fluxul operațional pas-cu-pas, cu capturi, e în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 5. Conexiuni

- [deltatech_rma](../deltatech_rma/index.md): cererea de retur, fișa, recepția, verdictele, nota de credit.
- `helpdesk_sale`: comanda de vânzare de pe tichet, din care se precompletează liniile.
