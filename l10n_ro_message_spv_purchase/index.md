# SPV Messages to Purchase Orders (localizat la `l10n_ro_message_spv_purchase/index.md`)

- **Nume Tehnic:** `l10n_ro_message_spv_purchase`
- **Versiune:** `19.0.0.0.14`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_message_spv_purchase
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_message_spv_purchase`
- **Ultima Ingestie:** `2026-11-23`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul extinde mecanismul de mesaje SPV (Spațiul Privat Virtual ANAF) din România pentru fluxul de aprovizionare. Când o factură electronică de la furnizor sosește prin SPV, modulul ajută utilizatorul să găsească rapid comanda de achiziție corespunzătoare sau să creeze una nouă, atașează pe comandă o copie a fișierului XML al facturii și leagă liniile facturii de liniile comenzii, astfel încât comanda să nu fie facturată de două ori.

#### 2. Funcționalități Cheie

- Câmpuri noi pe mesajul SPV:
  - `Purchase Reference` (`purchase_ref`) – extras automat din XML, de la `OrderReference/ID`, atunci când este disponibil.
  - `Purchase Order` (`purchase_order_id`) – comanda de achiziție legată, dacă există.
- Două butoane în antetul formularului SPV, vizibile doar pe mesajele de achiziție (facturi și chitanțe de la furnizor):
  - **Găsește Comanda**: caută comenzi de achiziție după referință (`purchase_ref` sau, ca alternativă, `ref`) în referința furnizorului, documentul sursă sau numărul comenzii, restrânse la partenerul și compania mesajului și la comenzile care nu sunt complet facturate. Dacă găsește o singură comandă, o leagă și continuă importul; dacă sunt mai multe, deschide lista filtrată; dacă nu găsește nimic, afișează o eroare.
  - **Creează Comanda**: face aceeași căutare; dacă nu există nicio comandă, creează o cerere de ofertă în stare ciornă pentru partenerul mesajului (partenerul este obligatoriu), cu referința drept referință furnizor, și o leagă.
- Dacă referința aparține doar unei comenzi deja complet facturate, **Găsește Comanda** nu o mai leagă, iar eroarea numește comanda și facturile ei.
- Un al doilea clic pe un mesaj deja legat de comanda găsită este blocat, pentru ca documentul să nu fie procesat de două ori.
- La găsirea sau crearea comenzii se postează o notă în chatter-ul ei, cu o copie a XML-ului SPV atașată (`ir.attachment` pe `purchase.order`, fără dubluri după checksum sau după nume și mimetype). Dacă factura de furnizor nu există încă, XML-ul se extrage din arhiva ZIP descărcată de la ANAF.
- Factura creată din mesajul SPV se leagă de liniile comenzii (potrivirea standard din `purchase`): cantitatea facturată se actualizează, iar „Create Bill" standard nu mai produce o a doua factură. Liniile care nu sunt pe comandă (transport, ambalaje) rămân pe factură.
- Cu `deltatech_purchase_ubl` instalat, liniile facturii se importă pe comandă: direct, cu o notificare, când toate liniile se potrivesc după cod furnizor sau cod de bare și totalurile coincid; altfel se deschide asistentul de import în previzualizare, iar utilizatorul decide pentru fiecare linie (folosește un produs, creează un produs nou sau ignoră). Opțiunea de factură de furnizor este dezactivată dacă factura SPV există deja.
- Avertismente de duplicat, nebloante, în chatter: comandă care are deja altă factură, „Create Bill" pe o comandă legată de o factură SPV și factură cu aceeași cheie de deduplicare, când modulul care furnizează cheia este instalat.
- Nu necesită configurări speciale; instalarea `deltatech_purchase_ubl` este recomandată pentru importul liniilor din XML.

#### 3. Dependențe

- `l10n_ro_message_spv`
- `purchase`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.message.spv` (extins): adaugă `purchase_ref` și `purchase_order_id`, metodele de căutare/creare a comenzii (`action_find_purchase`, `action_create_purchase`) și postarea XML-ului pe comandă.
- `purchase.order` (extins): la `action_create_invoice` postează în chatter un avertisment de duplicat dacă există deja o factură din SPV legată de comandă.
- `account.move` (extins): `_l10n_ro_link_spv_purchase_order` leagă factura de liniile comenzii prin potrivirea standard și semnalează duplicatele; `_l10n_ro_flag_cross_stack_duplicate` marchează o posibilă duplicare față de cealaltă stivă SPV, doar dacă există câmpul `l10n_ro_edi_dedup_key`.

**Vizualizări**

- `view_l10n_ro_message_spv_form_inherit_purchase`: extinde formularul mesajului SPV cu câmpurile noi și butoanele **Găsește Comanda** și **Creează Comanda**.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau acțiuni server; acțiunile se declanșează manual din butoanele antetului formularului SPV.

#### 5. Conexiuni

- `l10n_ro_message_spv`: modulul de bază care gestionează mesajele SPV ANAF; acest addon îl extinde pentru fluxul de achiziții.
- `purchase`: modulul standard Odoo de comenzi de achiziție, ținta legării și a postării notelor/atașamentelor.
- [deltatech_purchase_ubl](../deltatech_purchase_ubl/index.md): opțional; importă liniile facturii pe comandă din XML-ul UBL, direct sau prin asistent de previzualizare.
- [l10n_ro_efactura_dedup](../l10n_ro_efactura_dedup/index.md): opțional; furnizează cheia de deduplicare folosită la semnalarea duplicatelor cross-stack.
