# No Negative Stock (localizat la `deltatech_stock_negative/index.md`)

- **Nume Tehnic:** `deltatech_stock_negative`
- **Versiune:** `20.0.2.1.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_negative
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_negative`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Implicit, Odoo permite validarea unui transfer chiar dacă stocul nu există, iar cantitatea din locație ajunge discret sub zero; eroarea iese la iveală abia la următoarea inventariere. Acest modul oprește mișcarea chiar la validare și îi spune utilizatorului ce a mai rămas efectiv în locație. Pentru situațiile speciale, regula se poate relaxa pe anumite locații (producție, tranzit).

#### 2. Funcționalități Cheie

- Blochează stocul negativ la validare: un transfer care ar duce o locație internă sub zero nu poate fi validat.
- Mesaj clar: utilizatorul vede produsul, locația și cantitatea care ar rămâne și este îndrumat să corecteze cantitățile sau stocul.
- Excepții pe locație: stocul negativ se poate permite pe locațiile dorite (producție, tranzit), din `Inventar > Configurare > Locații`.
- Verificare pe stocul fizic: cantitatea din locație, pe lot, pachet și proprietar, nu pe previziune.
- Sigur la transferuri cu mai multe linii: liniile aceluiași produs din aceeași validare se adună, deci nu pot depăși împreună stocul.
- Numere de serie, strict sau pe total: per locație, produsele cu serie se verifică pe seria liniei sau pe totalul locației (opțiunea *Verifică nr. de serie*).
- Compatibil cu Punctul de vânzare: bonurile din PoS trec implicit (marfa a ieșit deja din magazin); fiecare ocolire se înregistrează în jurnalul serverului, iar lipsa rămâne vizibilă ca stoc negativ de corectat. Se poate dezactiva din setări.
- Doar produse cu stoc urmărit: consumabilele fără *Urmărește inventarul* nu se verifică.
- Setare pe companie: regula se activează separat pe fiecare companie, din `Inventar > Configurare > Setări`, secțiunea *Trasabilitate*.
- Înainte de activare pe o bază existentă, se recomandă revizuirea pozițiilor negative (`Inventar > Raportare > Stoc pe locații`, filtrul *Stoc negativ*); fluxul complet este în fișa consultantului.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.move.line` (extins): verifică la validare stocul fizic al locației sursă și blochează cu eroare mișcarea care l-ar duce sub zero.
- `stock.quant` (extins): ajustează disponibilitatea pentru produsele cu serie, în locațiile unde verificarea numerelor de serie e dezactivată.
- `stock.location` (extins): câmpurile `allow_negative_stock` și `check_serial_no`.
- `res.company` (extins): câmpul `no_negative_stock` care activează regula pe companie.
- `res.config.settings` (extins): expune setările regulii (inclusiv ocolirea pentru Punctul de vânzare).

**Vizualizări**

- `res_config_view.xml`: opțiunile din Setări Inventar, secțiunea Trasabilitate.
- `stock_location_view.xml`: opțiunile pe formularul locației.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- Nu au fost identificate conexiuni către alte module cu pagină wiki.
