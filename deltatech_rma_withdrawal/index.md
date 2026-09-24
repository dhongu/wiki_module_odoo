# RMA Withdrawal (localizat la `deltatech_rma_withdrawal/index.md`)

- **Nume Tehnic:** `deltatech_rma_withdrawal`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_rma_withdrawal
- **Cale Locală:** `odoo-addons/bitshop/deltatech_rma_withdrawal`
- **Ultima Ingestie:** 2026-09-24
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Retragerea din contract și returul comercial rămân înregistrări diferite: [deltatech_sale_withdrawal](../deltatech_sale_withdrawal/index.md) ține declarația consumatorului, [deltatech_rma](../deltatech_rma/index.md) ține coletul. Puntea le leagă, ca un consumator care se retrage să primească aceeași fișă de retur cu cod de bare și coletul lui să treacă prin aceeași recepție prin scanare ca orice retur, fără ca retragerea să capete vreodată o stare de aprobare pe care, conform art. 11a din Directiva 2011/83/UE, nu are voie s-o aibă.

#### 2. Funcționalități Cheie

- Mod de execuție nou, `rma_parcel` (*Așteptăm coletul înapoi, cu fișă de retur*), ales în **Vânzări → Configurare → Setări → Retragere din contract → Execuția retragerii**.
- La confirmarea retragerii se creează, ca superuser, o cerere de retur direct în **Așteptăm coletul**, de tip *Retur*, cu rezolvarea *Returnăm banii*: nu trece prin *Ciornă* sau *Trimis*, din care ar putea fi aprobată. Executarea de două ori nu deschide un al doilea colet.
- Taxa de manipulare e zero (art. 14): motivul rezervat, **Retragere în termenul legal**, are intervalul 0–0, e *Doar pentru colegi* (nu apare în portal) și spune că transportul de întoarcere e pe cheltuiala clientului.
- Fișa pleacă pe mail cu un șablon propriu, fără nicio formulare de aprobare; spune că banii se returnează după ce produsele ajung sau după dovada expedierii (art. 13 alin. (3)).
- Coletul urmează apoi fluxul obișnuit: recepție prin scanare, verdicte, repunere în stoc. Nota de credit se pregătește din cererea de retur, iar retragerea se marchează rambursată; câmpul *Notă credit* de pe retragere nu e completat de punte.
- Pe formularul retragerii, butonul și câmpul **Colet de retur**. Câmpul *Mod de execuție* al retragerii afișează codul tehnic (`rma_parcel`).

#### 3. Dependențe

- [deltatech_rma](../deltatech_rma/index.md)
- [deltatech_sale_withdrawal](../deltatech_sale_withdrawal/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.sale.withdrawal` (extins): `deltatech_rma_id` și `_execute_withdrawal_rma_parcel`, punctul de extindere al modului de execuție.
- `res.company` (extins): valoarea `rma_parcel` adăugată prin `selection_add` pe `deltatech_withdrawal_execution_mode`.

**Vizualizări**

- `view_deltatech_sale_withdrawal_form_rma`: butonul și câmpul *Colet de retur* pe retragere.

**Date**

- `reason_statutory_withdrawal` (`noupdate`): motivul rezervat retragerii, cu taxa 0–0.
- `mail_template_withdrawal_slip`: mailul cu fișa, fără formulare de aprobare.

Fluxul operațional pas-cu-pas, cu capturi, e în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 5. Conexiuni

- [deltatech_sale_withdrawal](../deltatech_sale_withdrawal/index.md): declarația de retragere, confirmarea de primire, rambursarea.
- [deltatech_sale_withdrawal_stock](../deltatech_sale_withdrawal_stock/index.md): celălalt mod de execuție, prin anularea livrării sau returul direct de stoc.
- [deltatech_rma](../deltatech_rma/index.md): fișa cu cod de bare, recepția prin scanare, transferul de retur.
