# Romania - Protecție la resetarea facturilor de furnizor și DVI (localizat la `l10n_ro_invoice_dvi_protect/index.md`)

- **Nume Tehnic:** `l10n_ro_invoice_dvi_protect`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_invoice_dvi_protect
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_invoice_dvi_protect`
- **Ultima Ingestie:** `2026-10-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul protejează costurile stocurilor evaluate FIFO, blocând resetarea la ciornă a facturilor de furnizor și anularea costurilor de aterizare (DVI) după ce stocul recepționat a fost deja parțial consumat. Costul de achiziție se propagă în costul ieșirilor de stoc; dacă documentul de intrare ar fi resetat după consum, costul aplicat ieșirilor ar rămâne fără legătură cu el. Modulul se adresează companiilor care importă mărfuri și își evaluează stocul prin FIFO.

#### 2. Funcționalități Cheie

- **Blocarea resetării facturii:** butonul **Resetare la ciornă** este blocat pe facturile și notele de credit de furnizor (`in_invoice`, `in_refund`) dacă vreo mișcare de intrare asociată liniilor de comandă de achiziție ale facturii are cantitatea rămasă mai mică decât cea recepționată.
- **Mesaj explicit:** eroarea numește produsul, cantitatea consumată și cea totală, de exemplu „cantitate consumată: 15,00 din 20,00 buc”; la mai multe produse se arată primul găsit.
- **Blocarea anulării DVI:** butonul **Anulează** de pe costul de aterizare (în ciornă) aplică aceeași verificare facturii asociate: fie `vendor_bill_id`, fie factura legată prin `dvi_id` (dacă este instalat `l10n_ro_customs_dvi`). Fără factură asociată, anularea este permisă, de aceea factura trebuie asociată mereu pe costul de aterizare.
- **Doar liniile legate de comandă:** serviciile sau cheltuielile adăugate manual pe factură sunt ignorate; la o factură mixtă cu stoc consumat, resetarea întregii facturi este blocată.
- **Fără configurare:** protecția este activă imediat după instalare. Se recomandă metoda de cost FIFO pe categoria produselor importate și bifarea **Este cost de aterizare** pe produsele de cost DVI.
- **Corecții după consum:** factură de stornare, cost de aterizare suplimentar (pozitiv sau negativ) sau ajustare de stoc prin inventariere, nu resetarea sau anularea documentului sursă.

#### 3. Dependențe

- `purchase_stock`
- `stock_landed_costs`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): `button_draft` apelează `_check_fifo_consumption` pentru facturile de furnizor; metoda verifică mișcările de intrare (`is_in`) ale liniilor de achiziție ale facturii și ridică `UserError` dacă `remaining_qty < quantity`.
- `stock.landed.cost` (extins): `button_cancel` aplică verificarea facturii asociate, găsită de `_dvi_protect_vendor_bill`.

**Vizualizări**

- Modulul nu adaugă vizualizări sau date; intervine doar asupra logicii butoanelor existente.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server; verificarea rulează sincron, la acțiunea utilizatorului.

#### 5. Conexiuni

- [l10n_ro_customs_dvi](../l10n_ro_customs_dvi/index.md): wizardul DVI scrie `dvi_id` pe factură, iar modulul folosește această legătură (verificată în cod, fără dependență) pentru a proteja anularea costului de aterizare.
