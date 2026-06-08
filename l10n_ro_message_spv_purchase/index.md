# Purchase Message SPV (localizat la `l10n_ro_message_spv_purchase/index.md`)

- **Nume Tehnic:** `l10n_ro_message_spv_purchase`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_message_spv_purchase
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_message_spv_purchase`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Acest modul extinde mecanismul de mesaje SPV (Spațiul Privat Virtual ANAF) din România pentru a sprijini fluxul de aprovizionare (procure-to-pay). El leagă mesajele SPV primite de comenzile de achiziție (Purchase Orders) și menține sincronizate jurnalul de discuții (chatter) și atașamentele comenzii. Practic, atunci când o factură electronică sosește prin SPV, modulul ajută utilizatorul să identifice rapid comanda de achiziție corespunzătoare sau să creeze una nouă, atașând automat fișierul XML al facturii direct pe comandă.

#### 2. Funcționalități Cheie

- Câmpuri noi pe mesajul SPV:
  - `Purchase Reference` (`purchase_ref`) – extras automat din XML, de la `OrderReference/ID`, atunci când este disponibil.
  - `Purchase Order` (`purchase_order_id`) – comanda de achiziție legată, dacă există.
- Două acțiuni dedicate pe formularul SPV:
  - **Find Purchase** (Caută Comandă): caută comenzi de achiziție după referință (folosind `purchase_ref` sau, ca alternativă, `ref`) în câmpurile `partner_ref`, `origin` sau `name`, restrânse după partener/companie când acestea sunt disponibile.
  - **Create Purchase** (Creează Comandă): execută aceeași căutare; dacă nu găsește nimic și un partener este setat, creează o comandă de achiziție în stare ciornă și o leagă.
- Când o comandă este găsită sau creată, se postează o notă în chatter-ul comenzii cu un mesaj contextual și cu XML-ul SPV atașat.
- XML-ul SPV nu este doar referențiat; se creează o copie a atașamentului XML pe comandă (`ir.attachment` cu `res_model='purchase.order'`), evitând legarea încrucișată la fișierul original al mesajului.
- Prevenirea duplicatelor pentru atașamentele de pe comandă, pe baza checksum-ului (cu alternativă la nume și mimetype).

#### 3. Dependențe

- `l10n_ro_message_spv`
- `purchase`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, modulul aduce următoarele componente principale.

**Modele**

- `l10n.ro.message.spv` (extins): model de mesaj SPV căruia i se adaugă câmpurile `purchase_ref` (referința de achiziție extrasă din XML) și `purchase_order_id` (legătura către comanda de achiziție).
- `purchase.order` (vizat): pe comanda găsită sau creată se postează o notă în chatter și se atașează o copie clonată a XML-ului SPV (`ir.attachment` cu `res_model='purchase.order'`).

**Vizualizări**

- `views/message_spv_view.xml`: extinde formularul mesajului SPV pentru a afișa câmpurile noi și butoanele de antet **Find Purchase** și **Create Purchase**.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt documentate acțiuni automate (`ir.cron` / `base.automation`) în Readme. Acțiunile sunt declanșate manual prin butoanele din antetul formularului SPV.

#### 5. Conexiuni

- `l10n_ro_message_spv`: modulul de bază care gestionează mesajele SPV ANAF; acest addon îl extinde pentru fluxul de achiziții.
- `purchase`: modulul standard Odoo de comenzi de achiziție, ținta legării și a postării notelor/atașamentelor.
