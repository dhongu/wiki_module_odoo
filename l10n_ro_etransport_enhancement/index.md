# e-Transport Enhancements (localizat la `l10n_ro_etransport_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_etransport_enhancement`
- **Versiune:** `20.0.0.10.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_etransport_enhancement
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_etransport_enhancement`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde funcționalitatea standard de e-Transport din Odoo pentru piața românească, făcând integrarea cu sistemul RO e-Transport (SPV) mai flexibilă și mai fiabilă. Acoperă atât livrările și recepțiile clasice, cât și transporturile dropship (furnizor direct la client), corectează situațiile în care declarația ar pleca la ANAF cu date incomplete sau greșite și reduce efortul echipelor de logistică și contabilitate.

#### 2. Funcționalități Cheie

- Trimiterea documentelor e-Transport direct din transferurile de stoc, cu tipuri de trimitere controlate prin parametri de context.
- **Timeout configurabil** pentru API-ul ANAF (standardul Odoo are 10 secunde fix, adesea prea puțin).
- Căderile de rețea către ANAF nu mai aruncă eroare tehnică: transferul păstrează un document eșuat cu un mesaj care cere verificarea în SPV înainte de retrimitere, ca să nu se emită un al doilea UIT.
- Reîncercare automată doar la interogările de stare (GET); încărcarea documentului nu se reîncearcă niciodată automat.
- **Traseu rutier punct de trecere a frontierei ↔ birou vamal** la import și export, ca să se poată declara tronsonul aflat sub supraveghere vamală.
- Data transportului nu mai cade când utilizatorul nu are fus orar (trimiteri automate ca OdooBot); se folosește fusul României.
- Liniile cu valoare zero primesc prețul din valoarea de stoc a mișcării, apoi din costul produsului, apoi din prețul de vânzare; dacă niciun preț nu se găsește, trimiterea se oprește cu eroare explicită.
- Liniile fără cantitate sunt eliminate, iar o greutate netă sau brută lipsă se aproximează cu cealaltă (ANAF cere ambele valori nenule).
- „Get lines" recalculează liniile de greutate în loc să le adauge; un avertisment semnalează mișcările fără linie de greutate.
- **Greutăți totale cântărite** (net și brut) cu butonul „Distribute weights", care ajustează liniile proporțional sau egal când toate pornesc de la zero.
- **Cod SH obligatoriu** pe produs: declarația se blochează la validare dacă lipsește (cu excepția operațiunilor 60/70); codul nu mai pleacă ca `00000000`.
- **Documente însoțitoare** configurabile pe transfer (CMR, factură, aviz, altele), trimise ca listă; butonul de completare adaugă avizul și facturile emise.
- **Transportator eTransport** dedicat pe transfer, completat din curierul livrării când acesta are partener configurat.
- **Locație de start specifică** pentru capătul de plecare al traseului național, înlocuind adresa calculată din depozit.
- **Corecția unei declarații** trimite UIT-ul corectat, deci nu se mai emite un UIT nou; bifa „Post-outage Declaration" trimite `declPostAvarie="D"`.
- Greutatea brută nu mai este dublată la colete; unitatea de măsură a liniei este aliniată cu cantitatea declarată.
- **Dropship** (furnizor → client, fără mișcare de stoc intermediară) prin acțiunea nativă „Send eTransport", pentru operațiunile 10 (AIC), 20 (LIC), 30 (național), 40 (import) și 50 (export). Partenerul comercial este clientul pe 20/30/50 și furnizorul pe 10/40; valoarea vine din comanda legată, fără TVA, convertită în RON; o declarație are un singur furnizor, un singur client și o adresă de livrare, iar retururile și dropship-urile în lot sau mixte sunt blocate. Corectează partenerul declarat, pe care nucleul îl derivă mereu din comanda de achiziție.
- Codul de țară al Greciei se declară `EL`, conform ANAF.
- Fluxul pas-cu-pas (setări UIT, cod SH, greutăți, documente, corecție) este în fișa de consultant.

#### 3. Dependențe

- `l10n_ro_edi`
- `l10n_ro_edi_stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins, în `stock_picking.py` și `stock_picking_dropship.py`): greutăți, transportator, adresă de start, documente însoțitoare, gestionarea erorilor de rețea, prețuri și unități, traseul dropship.
- `l10n.ro.etransport.document`: documentele însoțitoare declarate pe transfer.
- `l10n.ro.stock.picking.weight.line`: liniile de greutate (netă/brută) per mișcare.
- `stock.move` (extins): denumirea produsului în lista liniilor de greutate.
- `res.company` / `res.config.settings` (extinse): „UIT: get price from order" și timeout-ul API-ului ANAF.
- Patch pe `ETransportAPI._make_etransport_request` (nu model ORM): forțează timeout-ul și reîncercările pe GET.

**Vizualizări**

- `stock_picking_view.xml`: câmpurile și butoanele adăugate pe formularul transferului.
- `res_config_view.xml`: secțiunea „UIT" din setările de Inventar.

**Acțiuni Automate / Acțiuni Server**

Niciuna definită direct; comportamentul pornește din acțiunea nativă „Send eTransport" din `l10n_ro_edi_stock`.

#### 5. Conexiuni

- `l10n_ro_edi`: baza EDI/e-Transport pe care modulul o extinde.
- `l10n_ro_edi_stock`: integrarea la nivel de stoc, baza trimiterii din transferuri.
- `stock_dropshipping`: dependență funcțională opțională (nedeclarată); calea dropship se activează doar unde fluxul nativ e instalat.
- `deltatech_uom_unece`: suită separată; modulul nu depinde de ea, iar codul unității rămâne cel al produsului.
