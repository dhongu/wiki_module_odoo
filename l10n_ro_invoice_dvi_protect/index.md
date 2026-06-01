# Protecție resetare facturi furnizor și DVI (localizat la `l10n_ro_invoice_dvi_protect/index.md`)

- **Nume Tehnic:** `l10n_ro_invoice_dvi_protect`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_invoice_dvi_protect
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_invoice_dvi_protect`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Modulul protejează integritatea contabilă a stocurilor evaluate FIFO, blocând resetarea la ciornă a facturilor furnizor și anularea documentelor DVI (costuri de aterizare) atunci când stocul recepționat a fost deja parțial consumat. În Odoo, costul de achiziție FIFO se propagă către ieșirile de stoc; dacă factura de intrare ar fi resetată după consum, costul aplicat ieșirilor ar deveni orfan, generând inconsistențe. Modulul previne acest scenariu.

#### 2. Funcționalități Cheie

- Blochează butonul **Resetare la ciornă** pe facturile furnizor (`in_invoice`, `in_refund`) dacă vreo mișcare de stoc asociată comenzii de achiziție are `remaining_qty < quantity` (stoc deja parțial consumat).
- Mesaj de eroare explicit care indică produsul și cantitățile implicate.
- Blochează butonul **Anulare** pe documentele DVI / costuri de aterizare (`stock.landed.cost`) când factura furnizor asociată (`vendor_bill_id`) nu trece verificarea de consum.
- Protecție automată, fără configurare, integrată în fluxul standard de achiziție și recepție.

#### 3. Dependențe

- `purchase_stock`
- `stock_landed_costs`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): Adaugă verificarea care blochează resetarea la ciornă a facturilor furnizor cu stoc consumat.
- `stock.landed.cost` (extins): Adaugă verificarea care blochează anularea DVI legate de o factură protejată.

**Vizualizări / Date**

*Modulul nu adaugă vizualizări sau date noi; intervine exclusiv asupra logicii butoanelor existente.*

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate; protecția este declanșată sincron la acțiunile utilizatorului.*

#### 5. Conexiuni

- `[[l10n_ro]]`
