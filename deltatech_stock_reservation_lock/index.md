# Stock Reservation Lock

- **Nume Tehnic:** `deltatech_stock_reservation_lock`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_stock_reservation_lock
- **Cale Locală:** `odoo-addons/bitshop/deltatech_stock_reservation_lock`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

O rezervare este o promisiune făcută unui client, dar în Odoo standard orice utilizator de depozit o poate anula cu un singur clic. Modulul protejează stocul rezervat pe transferurile tipurilor de operațiune alese: rezervarea nu poate fi eliberată, depășită sau „furată” de alt transfer, iar orice eliberare autorizată este înregistrată.

#### 2. Funcționalități Cheie

Pe un transfer confirmat al unui tip de operațiune protejat:

- **Fără eliberare**: *Unreserve*, setarea cantității la 0 sau ștergerea ultimei operațiuni detaliate sunt refuzate. Doar utilizatorii din grupul *Release Protected Reservations* pot elibera stocul; ei nu sunt afectați nici de celelalte blocaje.
- **Fără livrare peste cerere**: cantitatea nu poate depăși cererea (demand).
- **Fără produse necomandate**: după confirmare nu se mai poate adăuga manual niciun produs (din formular, Barcode, import sau API). Liniile adăugate pe comanda de vânzare ajung în continuare pe transfer prin regulile de aprovizionare.
- **Livrarea parțială rămâne normală**: cantitatea poate fi scăzută atât timp cât rămâne peste zero; la validare, restanța rezervă din nou restul.
- **Fără „furt” de stoc**: validarea altui transfer care ar lua stocul rezervat este refuzată și numește transferul protejat. Ajustările de inventar și rebutul prevalează, fiindcă stocul a dispărut fizic.
- **Fiecare eliberare este înregistrată** pe transfer (produs, cantitate, locație).
- **Stocul eliberat merge la cine l-a cerut primul**: după o eliberare autorizată, transferurile în așteptare pentru acel produs se rezervă imediat, după prioritate și apoi după data programată.
- Verificările sunt pe date, nu pe butoane, deci Barcode, importurile și apelurile API respectă aceleași reguli. Anularea transferului sau a comenzii de vânzare funcționează ca de obicei.
- **Configurare**: în *Inventar > Configurare > Tipuri de operațiuni* se bifează **Protect Reservations** (opțiunea nu apare la recepții); în modul dezvoltator, grupul **Release Protected Reservations** (*Extra Rights*) se acordă utilizatorilor autorizați; administratorii de inventar îl au deja, deci operatorii se păstrează doar pe *Inventory / User*.
- Cu *Barcode*, ocolirea „setez cantitatea la 0 și număr prin scanare” nu mai funcționează pe tipurile protejate: se scanează față de cantitatea rezervată.
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking.type` (extins): câmpul boolean `protect_reservation` (**Protect Reservations**).
- `stock.move` (extins): blocarea adăugării de produse, a depășirii cererii și a „furtului” de rezervări, plus rezervarea imediată a transferurilor în așteptare după o eliberare.
- `stock.move.line` (extins): refuzul eliberării sau al ștergerii liniilor detaliate și jurnalizarea eliberărilor.

**Vizualizări**

- `view_picking_type_form`: opțiunea **Protect Reservations** pe tipul de operațiune.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni automate. Grupul `group_release_protected_reservation` (*Release Protected Reservations*) este acordat implicit administratorilor de inventar.

#### 5. Conexiuni

Nu există legături funcționale cu alte module wiki.
