# Deltatech Customer Map

- **Nume Tehnic:** `deltatech_customer_map`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_customer_map
- **Cale Locală:** `odoo-addons/bitshop/deltatech_customer_map`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Harta 3D a clienților companiei, pe relieful real al țării: fiecare județ este colorat după vânzări, numărul de clienți sau numărul de facturi, orașele apar ca stâlpi luminoși, iar un click pe județ deschide orașele, principalii clienți și principalele produse din acel județ. Pentru firmele care vând și în afara țării, a doua hartă arată țările Europei, iar un click pe România deschide harta județelor. Directorul comercial vede rapid unde se vinde și unde nu, iar agentul de vânzări își vede doar propriii clienți.

#### 2. Funcționalități Cheie

- **Relief 3D real** (WebGL 2, three.js): munții, dealurile și câmpiile se văd dintr-o privire. Motorul 3D se încarcă doar la deschiderea hărții, nu odată cu restul Odoo. Fără WebGL 2, harta revine, fără eroare pentru utilizator, la o variantă 2.5D desenată pe canvas.
- **Două hărți**: județele României și țările Europei (55 de țări, proiecție Lambert). Pe harta Europei clienții sunt plasați după țară; un click pe România deschide harta pe județe (buton *Open the county map*). O companie din afara României primește direct harta Europei.
- **Trei metrici**: vânzări (fără taxe, în moneda companiei), clienți activi, facturi; perioade de 3, 6, 12 sau 24 de luni ori tot istoricul. Culorile, legenda și stâlpii orașelor urmează metrica aleasă.
- **Județe și orașe**: la hover se văd cifrele și clasamentul județului; click-ul zboară către județ și deschide panoul lateral cu orașele, top clienți (click deschide fișa clientului) și top produse; există și lista *Top counties*.
- **Fiecare client este plasat**: după județul din fișa clientului, apoi după înregistrarea de oraș (`res.city`, de ex. cu *l10n_ro_city*), apoi după numele orașului (sunt recunoscute variante precum „Mun. Cluj-Napoca" sau „SECTOR1"). Clienții care nu pot fi plasați și cei din străinătate sunt afișați separat (*Customers without county*), nu ascunși. Pe harta Europei, clientul fără țară e luat în țara companiei.
- **Aceleași vânzări ca în Segmentarea clienților**: liniile de produs de pe conturi de venit ale facturilor și notelor de credit postate, fără avansuri, limitate de setarea *Sales accounts* (70 pe planul românesc, ca penalitățile sau activele vândute să nu fie numărate ca vânzări).
- **Roluri preluate din Customer Segment**: *Own customers* vede doar clienții pentru care este vânzătorul (restricție aplicată pe server, indiferent ce trimite browserul); *All customers* vede toată compania și poate filtra după vânzător (*All salespersons*).
- **Navigare**: rotire/înclinare prin drag, zoom cu scroll sau pinch, dublu click sau butonul țintă pentru resetarea vederii, buton pentru legănarea automată. Harta, perioada, metrica și rotirea automată se rețin în browser.
- **Acces**: meniul *Sales > Customer Portfolio > Customer Map*; nu există rol propriu, rolul se acordă în *Settings > Users > Customer Portfolio*. Opțional, *base_address_extended* cu orașele țării (*l10n_ro_city* pentru România) permite plasarea clienților care au oraș, dar nu au județ.
- Hărțile României (41 de județe și București) și ale Europei sunt livrate cu modulul. Nu se adaugă câmpuri pe modele standard. Fluxul detaliat de configurare și utilizare este în [fișa consultantului](FISA_CONSULTANT.md).
- Surse de date: relief Mapzen / AWS Open Data terrain tiles, limitele județelor și țărilor și orașele Europei din Natural Earth (domeniu public), motor 3D three.js (MIT). Modul bazat pe modulul de hartă al MD Trade Concept SRL; licență OPL-1, stadiu Beta.

#### 3. Dependențe

- [deltatech_customer_segment](../deltatech_customer_segment/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.customer.map` (model abstract): calculează datele hărții (vânzări, clienți, facturi pe județ/țară și oraș, top clienți, top produse), plasează clienții după județ, oraș sau țară și aplică restricția pe rol.

**Vizualizări**

- `action_customer_map`: acțiune client (`tag` `deltatech_customer_map`) care deschide harta, implementată în OWL (`static/src/map/customer_map.esm.js`, `customer_map.xml`, `customer_map.scss`) cu motorul 3D în `map_engine.esm.js`.
- `menu_customer_map`: meniul *Customer Map* sub *Customer Portfolio*.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server.

#### 5. Conexiuni

- [deltatech_customer_segment](../deltatech_customer_segment/index.md): sursa rolurilor, a meniului *Customer Portfolio* și a setării *Sales accounts* (aceleași vânzări).
- [deltatech_customer_analysis](../deltatech_customer_analysis/index.md): analiza clienților din aceeași familie de portofoliu.
- [deltatech_sale_missions](../deltatech_sale_missions/index.md): misiunile de vânzare din aceeași familie de portofoliu clienți.
- `l10n_ro_city`: opțional, orașele României pentru plasarea clienților fără județ.
