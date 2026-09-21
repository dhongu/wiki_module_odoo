# eTransport Enhancement (localizat la `l10n_ro_etransport_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_etransport_enhancement`
- **Versiune:** `19.0.0.9.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_etransport_enhancement
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_etransport_enhancement`
- **Ultima Ingestie:** `2026-09-21`

#### 1. Sumar

Modulul `l10n_ro_etransport_enhancement` extinde funcționalitatea standard de e-Transport din Odoo pentru piața românească, adăugând îmbunătățiri și opțiuni suplimentare. Scopul său este să facă integrarea cu sistemul e-Transport (SPV) mai flexibilă și mai fiabilă, acoperind atât livrările/recepțiile clasice printr-un depozit, cât și transporturile dropship (furnizor → client, fără mișcare de stoc intermediară), simplificând conformitatea fiscală pentru transporturile de mărfuri și reducând efortul administrativ al departamentelor de logistică și contabilitate.

#### 2. Funcționalități Cheie

- Trimiterea documentelor e-Transport direct din livrările/recepțiile de stoc (stock pickings), cu suport pentru diferite tipuri de trimitere prin parametri de context.
- **Timeout configurabil** pentru API-ul ANAF (implicit 60 s, per companie) — standardul Odoo are 10 s fix, insuficient la ore de vârf.
- Căderile de rețea către ANAF nu mai aruncă eroare tehnică în interfață: transferul rămâne cu un document eșuat și un mesaj clar care avertizează să se verifice în SPV înainte de retrimitere, ca să nu se emită un al doilea UIT pentru aceleași bunuri.
- Reîncercare automată doar pentru interogările de stare (GET, idempotent); încărcarea documentului (POST) nu se reîncearcă niciodată automat.
- Traseu rutier complet punct de trecere a frontierei ↔ birou vamal la import (operațiune 40) și export (50): standardul Odoo permite biroul vamal doar la un singur capăt al traseului, ceea ce face imposibilă declararea tronsonului aflat sub supraveghere vamală (PTF → birou vamal interior la import, birou vamal → PTF la export).
- Data transportului nu mai cade cu eroare când utilizatorul care trimite nu are fus orar setat (cazul tipic al trimiterilor automate rulate ca OdooBot); se folosește implicit fusul României (`Europe/Bucharest`).
- Liniile pe care standardul le trimite cu valoare 0 nu mai ajung la ANAF ca zero: prețul unitar se calculează din valoarea de stoc a mișcării, apoi din costul standard al produsului, apoi din prețul de vânzare; dacă niciunul nu poate fi determinat, trimiterea se oprește cu o eroare explicită în loc să depună o declarație invalidă.
- Liniile fără cantitate sunt eliminate din declarație, iar o greutate netă sau brută lipsă e aproximată cu cealaltă — șablonul QWeb standard scapă tăcut un atribut cu valoare zero, dar schema ANAF le cere pe toate.
- **Unitate de măsură aliniată cu cantitatea declarată** (`codUnitateMasura`): standardul ia cantitatea din UoM-ul de bază al produsului dar codul unității din UoM-ul liniei; când linia e într-o UoM secundară (cutie, bax, palet), perechea devine incoerentă și declarația e greșită fără nicio eroare vizibilă. Modulul aliniază codul pe unitatea în care e efectiv exprimată cantitatea.
- Opțiunea de companie **„UIT: get price from order"** convertește corect prețul de pe linia de comandă la UoM-ul de bază al produsului, evitând supraevaluarea valorii declarate cu factorul de conversie al UoM-ului secundar.
- „Get lines" (calculul liniilor de greutate) recalculează de la zero, nu adaugă — o a doua apăsare nu mai dublează greutățile trimise la ANAF; un avertisment pe transfer semnalează mișcările fără linie de greutate calculată.
- Greutăți totale (netă/brută) cântărite la rampă, cu buton **„Distribute weights"** care ajustează liniile individuale proporțional (sau egal, când toate pornesc de la zero) ca să însumeze greutatea reală cântărită.
- **Locație de start specifică** (`Specific Start Location`): permite alegerea manuală a unui partener a cărui adresă înlocuiește adresa calculată automat (depozit) pentru capătul de plecare al traseului — util când transportul național pleacă efectiv dintr-un alt loc (ex. birou vamal interior, după vămuire). Vizibil doar pe livrări, doar pentru operațiunea „Transport pe teritoriul național" și doar când locația e de tip adresă.
- **Documente însoțitoare** configurabile pe transfer (CMR, factură, aviz, altele), trimise ca listă la ANAF — standardul trimite un singur document, hardcodat ca aviz cu numărul transferului. Butonul de completare automată adaugă avizul (numărul transferului) și facturile emise deja legate de livrare; observațiile lipsă/goale sunt omise din XML în loc să fie trimise ca șir vid (respins de ANAF).
- **Partener de transport dedicat** (`Transport Partner`) pe transfer, populat automat din curierul livrării dacă are partener e-Transport configurat; folosit ca declarant al transportatorului fără să mai fie obligatoriu `carrier_id`.
- UIT-ul nu se mai scrie în `carrier_tracking_ref` la preluarea stării — acel câmp e referința reală de urmărire a curierului (AWB), nu un cod ANAF; UIT-ul rămâne disponibil în tab-ul eTransport.
- **Suport dropship** (furnizor → client direct, fără mișcare de stoc intermediară): trimiterea eTransport funcționează pe transferul dropship nativ, pentru operațiunile 10 (AIC), 20 (LIC), 30 (național), 40 (import) și 50 (export), fără depozit fictiv.
- Coloana mișcării din lista de linii de greutate poate afișa denumirea produsului (nu doar codul intern), pentru a distinge vizual liniile pe transferuri cu mai multe produse.

**Dropship — detalii operaționale** (vezi și `readme/USAGE.md`):

- Traseul fizic și tranzacția declarată se rezolvă din comenzile legate (vânzare + achiziție), nu din depozit: nu există locație de plecare/sosire reală în stoc.
- Partenerul comercial declarat (`partenerComercial`) e clientul pe operațiunile de livrare (20, 30, 50) și furnizorul pe operațiunile de achiziție (10, 40); adresa de încărcare implicită e cea a furnizorului (poate fi înlocuită cu `Specific Start Location`), iar adresa de livrare vine din comanda legată.
- Valoarea declarată folosește prețul din comanda legată (achiziție pentru 10/40, vânzare pentru 20/30/50), fără TVA, cu conversia UoM și valutară nativă la RON — dropship folosește mereu valoarea din comandă, indiferent de setarea „UIT: get price from order" a depozitului.
- Fiecare linie de marfă trebuie legată atât de o comandă de vânzare cât și de o comandă de achiziție ale companiei declarante; o declarație are un singur furnizor, un singur client comercial și o singură adresă de livrare. Nepotrivirile de țară față de operațiunea selectată, datele de adresă românești lipsă, operațiunile nesuportate, retururile și dropship-urile în lot/mixte sunt blocate cu eroare explicită.
- Documentele însoțitoare implicite (buton) adaugă numărul transferului și facturile de vânzare emise; pentru AIC/import, documentul furnizorului trebuie introdus manual.
- **Fix 19.0.0.9.2:** Odoo 19 a primit ulterior suport nativ pentru dropship în `l10n_ro_edi_stock`, iar metoda nucleului care pregătește datele declarației ignoră de atunci `data["partner_id"]` când tipul de operațiune e `dropship` și derivă întotdeauna partenerul din comanda de achiziție (furnizorul) — indiferent de sensul operațiunii. Fără corecție, o livrare dropship (operațiunile 20/30/50) ar pleca la ANAF cu furnizorul în locul clientului, fără nicio eroare vizibilă. Modulul rescrie acum `partenerComercial` (denumire, cod fiscal, cod de țară) după apelul metodei nucleului, cu partenerul corect ales de modul.

**Alte reguli tehnice**

- Codul de țară al Greciei se declară `EL`, nu `GR` (conform standardului ANAF), atât pentru partenerul comercial cât și pentru organizatorul transportului — aplicat consecvent și pe calea dropship.
- Câmpurile `l10n_ro_transport_partner_id` și `l10n_ro_etransport_start_address` sunt indexate (chei străine către `res.partner`, tabelă mare) — fără index, ștergerea/unificarea unui partener declanșa scanări secvențiale costisitoare.

#### 3. Dependențe

- `l10n_ro_edi`
- `l10n_ro_edi_stock`

#### 4. Componente Cheie

Secțiunea „Componente Cheie" clasică (Modele/Vizualizări/Acțiuni) e omisă în mare parte conform priorității `readme/DESCRIPTION.md`, dar re-ingestia curentă adaugă componentele apărute după publicarea inițială a Readme-ului, absente din pagina veche.

**Modele**

- `stock.picking` (extindere): găzduiește toate câmpurile și metodele de îmbunătățire — greutăți personalizate, partener de transport, adresă de start specifică, documente însoțitoare, gestionarea erorilor de rețea, alinierea UoM/cantitate, corecția prețurilor zero.
- `stock.picking` (extindere separată în `stock_picking_dropship.py`, menținută intenționat distinctă de extinderea principală pentru a controla ordinea `super()`): rezolvă traseul fizic și partenerul comercial pentru transferurile dropship, pornind de la comenzile de vânzare/achiziție legate, în loc de depozit.
- `l10n.ro.etransport.document`: documentele însoțitoare declarate pe transfer (CMR, factură, aviz, altele), cu tip, număr, dată și observații opționale.
- `l10n.ro.stock.picking.weight.line`: liniile de greutate (netă/brută) per mișcare de stoc, folosite la calculul și distribuirea greutăților cântărite.
- `stock.move` (extindere): afișare opțională a denumirii produsului în locul `display_name`-ului standard, în lista de linii de greutate.
- `res.company` / `res.config.settings` (extindere): setările „UIT: get price from order" și timeout-ul API-ului ANAF.
- Patch pe `ETransportAPI._make_etransport_request` (nu un model ORM): forțează timeout-ul configurat pe sesiunea `requests` și montează reîncercări automate doar pentru cererile GET.

**Vizualizări**

- `view_picking_form` (extindere formular `stock.picking`): expune câmpurile de îmbunătățire (greutăți, partener transport, adresă de start, documente însoțitoare) și butoanele „Get lines" / „Distribute weights" / completare documente implicite.
- `res_config_settings_view_form` (extindere): secțiunea „UIT" din Setări Inventar, cu opțiunea de preluare a prețului din comandă și timeout-ul API ANAF.

**Acțiuni Automate / Acțiuni Server**

Niciuna definită direct de modul; comportamentul se declanșează din acțiunea nativă „Send eTransport" (inclusă în `l10n_ro_edi_stock`) și din butoanele adăugate pe formularul de transfer.

#### 5. Conexiuni

- `l10n_ro_edi`: modulul de bază pentru integrarea EDI/e-Transport în localizarea românească, pe care acest modul îl extinde.
- `l10n_ro_edi_stock`: integrarea EDI la nivel de stoc, baza pe care se adaugă îmbunătățirile pentru trimiterea documentelor e-Transport din livrări/recepții și, mai nou, din transferuri dropship.
- `stock_dropshipping` (fără pagină wiki, dependență opțională la nivel funcțional, nu declarată în manifest): calea de dropship se activează doar acolo unde fluxul nativ de dropship al Odoo e deja instalat; modulul nu adaugă un depozit sau un tip de operațiune fictiv.
- `deltatech_uom_unece` (fără pagină wiki, suită separată, licență proprietară): dacă e instalată, face configurabil codul UNECE per unitate de măsură; modulul NU depinde de ea — codul unității folosit la declarație rămâne cel al produsului (`uom.uom._get_unece_code()`), nu cel al liniei, chiar dacă `deltatech_uom_unece` e prezentă.
