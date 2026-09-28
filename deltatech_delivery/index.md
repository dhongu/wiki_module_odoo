# Deltatech Delivery Base (localizat la `deltatech_delivery/index.md`)

- **Nume Tehnic:** `deltatech_delivery`
- **Versiune:** `19.0.6.8.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery`
- **Ultima Ingestie:** `2026-09-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul „Deltatech Delivery Base” este o extensie cuprinzătoare pentru Odoo care îmbunătățește și optimizează capacitățile de gestionare a livrărilor din ecosistemul Odoo. Modulul servește drept fundație pentru diverse integrări specifice fiecărui curier și oferă un cadru robust pentru gestionarea expedierilor către mai mulți furnizori de servicii de livrare. Modulul de bază pune la dispoziție și un cadru partajat de opțiuni de livrare pentru serviciile legate de AWB: opțiuni standard precum livrarea sâmbăta, deschiderea coletului, returul coletului, livrarea personală și notificarea prin SMS sunt definite centralizat și pot fi expuse per curier, în funcție de capabilitățile conectorului. Operatorul selectează doar opțiunile permise de curierul ales, în timp ce structura existentă `shipment_info` rămâne neschimbată pentru compatibilitate retroactivă. Pentru volume mari de comenzi, modulul oferă acum și trei acțiuni în masă direct din lista de comenzi de vânzare: validarea rapidă a livrărilor deja pregătite, trimiterea la curier cu urmărire vizuală a progresului și afișarea facturilor comenzilor selectate. O livrare **amânată** — de operator, de regula de plată sau de verificarea comenzii — este acum respectată peste tot: nu poate pleca la curier prin niciun buton și nicio acțiune în masă, ci este raportată ca reținută, cu motivul.

#### 2. Funcționalități Cheie

- **Gestionare îmbunătățită a livrărilor**:
  - Opțiuni îmbunătățite de configurare a curierului de livrare
  - Catalog partajat de opțiuni de livrare pentru serviciile AWB
  - Selectarea opțiunilor de livrare specifice curierului cu `many2many_tags`
  - Capabilități de curier calculate automat (doar citire) din `delivery_type`
  - Metode de expediere și tipuri de livrare extinse
  - Mecanisme flexibile de calcul al costului de livrare
  - Capabilități avansate de gestionare a coletelor

- **Suport pentru mai mulți curieri**:
  - Cadru de bază pentru integrarea mai multor curieri de expediere
  - Interfață unificată pentru gestionarea diferitelor servicii de curierat
  - API standardizat pentru extensiile specifice curierilor
  - Structuri de date comune pentru informațiile de expediere
  - Modulele de curier definesc opțiunile de livrare suportate pentru propriul conector

- **Procesarea expedierilor**:
  - Flux de lucru simplificat pentru crearea și procesarea expedierilor
  - Generarea automată a documentelor de expediere
  - Capabilități de procesare în lot pentru expedieri multiple
  - Urmărirea și sincronizarea stării livrării
  - Opțiunile de livrare sunt stocate compatibil în structura JSON existentă `shipment_info`
  - Wizard-ul de AWB avertizează când greutatea sau dimensiunile unui colet par aberante — peste pragurile per curier (implicit 31,5 kg, 150 cm pe latură, 0,5 m³; `0` dezactivează un prag) sau când dimensiunile par introduse în milimetri în loc de centimetri; e doar avertisment, coletul poate fi trimis oricum

- **Acțiuni în masă pe comenzile de vânzare**:
  - **Validate Deliveries** — din meniul Acțiuni al listei de comenzi de vânzare, validează în masă livrările deja pregătite (rezervare stoc + `button_validate`) pentru comenzile selectate; fiecare comandă e procesată izolat, printr-un wizard de confirmare urmat de o notificare cu numărul de succese și lista comenzilor cu probleme (motiv inclus)
  - **Send to Carrier** — din același meniu, deschide un dialog OWL care trimite comenzile selectate la curier secvențial (una câte una), cu progres live per linie: succes (cu numărul AWB), eroare clară, rezultat „incert" (când răspunsul curierului s-a pierdut și nu se reîncearcă automat, ca să nu apară un AWB dublu) sau **reținut** (livrare amânată, fără apel la curier); cât rulează, un banner cu rotiță animată arată că acțiunea e în curs, iar „Închide” e dezactivat până la final. Pentru o livrare la care operatorul n-a apăsat încă **Carrier Details → Aplică**, dialogul calculează și aplică detaliile automat, chiar înainte de trimitere, din datele curente ale livrării — livrările deja aplicate manual sunt trimise neatinse; butonul **Send to Shipper** de pe o livrare individuală cere în continuare aplicarea întâi
  - Din același dialog, **Print AWBs** combină într-un singur PDF etichetele deja generate pentru comenzile trimise cu succes, fără să genereze nimic nou
  - **View Invoices** (Afișează facturile) — deschide lista facturilor comenzilor selectate (sau direct factura, dacă e una), de unde se folosește tipărirea standard Odoo în masă

- **Reținerea livrărilor amânate** *(19.0.6.6.x)*:
  - o livrare cu bifa **Amânată** (`postponed` pe transfer, din `deltatech_delivery_status`) nu poate primi AWB până nu este eliberată, indiferent de calea folosită
  - **Trimite la curier** de pe transfer refuză cu mesajul de reținere în loc să încerce expedierea
  - **Validate Deliveries** listează comanda cu mesajul de reținere, în locul erorii seci „transfer is postponed"
  - **Send to Carrier** raportează rândul ca reținut (`held`, distinct de eroare și de rezultat incert), fără apel la curier
  - un singur hook central, `stock.picking._delivery_hold_message()`, întoarce textul de reținere (sau nimic) și e consultat de toate cele trei căi de mai sus; modulele care cunosc motivele (ex. [deltatech_delivery_review](../deltatech_delivery_review/index.md)) completează textul cu motivul concret (ex. ramburs peste prag)

- **Ramburs refuzat cu factura încă deschisă** *(nou, 19.0.6.8.0)*:
  - `delivery.awb` are acum un câmp stocat `cod_amount` (suma de încasat ramburs, preluată din `shipment_info["value_to_collect"]` al livrării), plus indicatorul căutabil `cod_unpaid_refused` și `cod_open_amount` (soldul deschis al facturilor)
  - lista **„Refused COD - Invoice Open”** (meniurile *Inventar > Delivery AWB* și *Contabilitate > Clienți*), grupată pe curier, arată coletele ramburs refuzate de client a căror factură de vânzare e încă neîncasată — curierul nu mai încasează nimic pe un colet refuzat, deci niciun decont de ramburs nu va închide vreodată acea factură; lista doar semnalează, nu creează notă de credit sau ajustare
  - un buton **„View Open Invoices”** pe lista de AWB-uri deschide direct facturile deschise ale rândurilor selectate

- **Fix multi-companie pe AWB** *(19.0.6.8.1)*:
  - `delivery.awb.company_id` se calculează acum din compania livrării (sau, în lipsa ei, din compania comenzii de vânzare) în loc să rămână necompletat; cron-ul de stare crea AWB-uri fără companie, iar regula multi-companie lasă să treacă o companie goală, așa că orice companie vedea toate AWB-urile. Câmpul rămâne editabil pentru un importator care setează explicit compania; la upgrade, AWB-urile existente sunt aliniate pe livrarea lor prin SQL

- **Gestionarea coletelor**:
  - Suport pentru mai multe colete într-o singură expediere
  - Gestionarea dimensiunilor și greutății coletelor
  - Configurarea și validarea tipurilor de ambalare
  - Gruparea și optimizarea coletelor

- **Gestionarea adreselor**:
  - Capabilități îmbunătățite de validare a adreselor
  - Suport pentru diferite formate de adrese în funcție de țară
  - Normalizarea adreselor pentru cerințele de expediere
  - Tratarea specială a locațiilor de livrare

- **Funcționalități de integrare**:
  - Integrare cu gestionarea stocurilor Odoo
  - Conexiune fără cusur cu procesarea comenzilor de vânzare
  - Crearea automată a livrărilor din vânzări sau transferuri
  - Sincronizare cu operațiunile de facturare

- **Experiența utilizatorului**:
  - Interfețe intuitive pentru operațiunile de expediere
  - Vizibilitate clară asupra informațiilor de expediere
  - Proces simplificat de selectare a curierului
  - Selectarea opțiunilor AWB pe bază de etichete (tags), în locul valorilor booleene fixe din wizard
  - Istoric și urmărire cuprinzătoare a expedierilor

Modulul reprezintă fundația pentru integrările specifice ale curierilor precum Fan Courier, TNT, DHL și alții, oferind un cadru consecvent pentru gestionarea livrărilor indiferent de curierul utilizat. Opțiunile de livrare sunt împărțite intenționat între modulul de bază și submodulele specifice fiecărui curier: modulul de bază definește înregistrările comune de opțiuni și interfața generică, fiecare modul `deltatech_delivery_*` definește ce opțiuni sunt suportate pentru propriul `delivery_type`, iar dacă un modul de curier nu definește un subset specific, toate opțiunile standard rămân disponibile.

Funcționalități care pot fi adăugate în submodule: generarea AWB în format PDF / HTML / ZPL, ștergerea AWB, obținerea tarifelor pentru o expediere, listele de orașe / județe / lockere / puncte de ridicare, istoricul de stare al unei expedieri, lista de AWB-uri, expediere cu mai multe colete, cu valoare declarată (asigurare), cu ramburs, cu id de oraș și județ, ridicare doar din punctul de ridicare indicat, trimiterea id-ului de locker în AWB, notă de restituire în AWB, expediere cu dimensiuni, precum și opțiunile de livrare sâmbăta, colet deschis, retur colet și livrare personală în lockere.

Fluxul pas-cu-pas al acțiunilor în masă și al reținerii livrărilor amânate (inclusiv capturile și mesajele de eroare frecvente) este documentat integral în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `delivery`
- `payment`
- `base_address_extended`
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)
- `stock`
- `purchase`
- `purchase_stock`

#### 4. Componente Cheie

Conform fluxului de ingestie din schema wiki, secțiunea „Sumar” și „Funcționalități Cheie” provin din `readme/DESCRIPTION.md` (îmbogățit cu esențialul din `readme/USAGE.md` și din `readme/FISA_CONSULTANT.md` pentru cele două acțiuni în masă, pentru reținerea livrărilor amânate și pentru lista de ramburs refuzat), care nu solicită explicit analiza codului pentru componente. Prin urmare, această secțiune nu este detaliată din cod; ca reper minim: hook-ul central al reținerii — `stock.picking._delivery_hold_message()` — este consultat de `send_to_shipper()`, `action_send_to_carrier_one()` și `action_bulk_validate_deliveries()`; iar `delivery.awb` are acum câmpurile `cod_amount`, `cod_unpaid_refused`, `cod_open_amount` și `company_id` (calculat din livrare/comandă); tabloul de bord [deltatech_delivery_dashboard](../deltatech_delivery_dashboard/index.md) numără pe `cod_amount`, `company_id` și `poll_abandoned`.

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): furnizează stările de livrare folosite de cadrul de urmărire a expedierilor din acest modul, inclusiv câmpul `postponed` și butoanele Amână/Eliberează pe comandă.
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): extinde fluxul de livrare și plată în site-ul web, valorificând cadrul de curieri din acest modul.
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md) + [deltatech_delivery_review](../deltatech_delivery_review/index.md) (bitshop): verificarea comenzii amână livrarea pe poarta „Înainte de livrare"; puntea completează mesajul de reținere din `_delivery_hold_message()` cu motivele concrete (ex. ramburs peste prag, adresă incompletă) — extindere opțională, fără pagină wiki proprie încă.
- [deltatech_delivery_dashboard](../deltatech_delivery_dashboard/index.md): tabloul de urmărire livrări, cu carduri KPI peste lista de AWB-uri; numără pe `cod_amount` și `company_id` de pe `delivery.awb` (introduse aici în 19.0.6.8.0/19.0.6.8.1) și pe `poll_abandoned`.
