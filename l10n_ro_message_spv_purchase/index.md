# SPV Messages to Purchase Orders (localizat la `l10n_ro_message_spv_purchase/index.md`)

- **Nume Tehnic:** `l10n_ro_message_spv_purchase`
- **Versiune:** `20.0.0.0.13`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_message_spv_purchase
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_message_spv_purchase`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde mesajele SPV (e-Factura, ANAF) din România pentru a lega facturile de furnizor primite prin SPV de comenzile de achiziție. Copiază XML-ul facturii pe comandă și leagă liniile facturii de liniile comenzii, astfel încât comanda să nu fie facturată de două ori. Contabilul furnizori găsește sau creează comanda direct din mesajul SPV.

#### 2. Funcționalități Cheie

- Câmpuri noi pe mesajul SPV: `Purchase Reference` (extrasă automat din XML, `OrderReference/ID`) și `Purchase Order` (comanda legată).
- Două butoane în antetul mesajului SPV, vizibile doar pe mesajele de achiziție (facturi și chitanțe de furnizor):
  - *Găsește Comanda*: caută comenzi după referință (`purchase_ref` sau, ca alternativă, `ref`) în referința furnizorului, documentul sursă sau numărul comenzii, pentru partenerul și compania mesajului și doar printre comenzile nefacturate complet. Dacă referința aparține unei comenzi deja facturate complet, nu o mai leagă, iar eroarea numește comanda și facturile ei.
  - *Creează Comanda*: face aceeași căutare; dacă nu găsește nimic, creează o cerere de ofertă în ciornă pentru partenerul mesajului (partenerul este obligatoriu) și o leagă.
- Un al doilea clic pe un mesaj deja legat de comanda găsită este blocat, ca documentul să nu fie procesat de două ori.
- La găsirea sau crearea comenzii se postează o notă în chatter cu o copie a XML-ului SPV atașată (`ir.attachment` pe `purchase.order`, fără duplicate după checksum sau nume și mimetype). Dacă factura nu există încă, XML-ul se ia din arhiva ZIP descărcată de la ANAF.
- Factura de furnizor creată din mesajul SPV este legată de liniile comenzii (potrivire standard de achiziții): cantitatea facturată se actualizează, iar „Creează factură” standard nu produce o a doua factură. Liniile care nu sunt pe comandă (transport, ambalaj) rămân pe factură.
- Cu *Purchase UBL* instalat, liniile facturii se importă pe comandă: direct, cu notificare, când toate liniile se potrivesc după cod furnizor sau cod de bare și totalurile coincid; altfel se deschide previzualizarea, unde operatorul decide pentru fiecare linie (folosește un produs, creează un produs nou sau ignoră).
- Avertismente neblocante în chatter pentru dubluri: o comandă care are deja altă factură, „Creează factură” pe o comandă legată de o factură SPV și o factură cu aceeași cheie de deduplicare, când modulul care furnizează cheia este instalat.
- Nu necesită configurare specială; se recomandă `deltatech_purchase_ubl` pentru importul liniilor din XML. Fluxul pas-cu-pas și capturile sunt în fișa consultant.

#### 3. Dependențe

- [l10n_ro_message_spv](../l10n_ro_message_spv/index.md)
- `purchase`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.message.spv` (extins): câmpurile `purchase_ref` și `purchase_order_id`, butoanele de căutare/creare a comenzii, copierea XML-ului pe comandă.
- `purchase.order` (extins): avertismente de dublare în chatter și legarea cu mesajul SPV.
- `account.move` (extins): legarea liniilor facturii de linii de comandă și avertismente de deduplicare.

**Vizualizări**

- `views/message_spv_view.xml`: extinde formularul mesajului SPV cu câmpurile noi și butoanele *Găsește Comanda* / *Creează Comanda*.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate; acțiunile se declanșează manual din butoanele mesajului SPV.

#### 5. Conexiuni

- [deltatech_purchase_ubl](../deltatech_purchase_ubl/index.md): opțional, importă liniile facturii pe comandă (direct sau cu previzualizare).
- [l10n_ro_message_spv](../l10n_ro_message_spv/index.md): modulul de bază care descarcă și procesează mesajele e-Factura din SPV.
- `purchase`: comenzile de achiziție la care se leagă facturile.
