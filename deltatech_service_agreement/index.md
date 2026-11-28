# Contracte de Servicii (localizat la `deltatech_service_agreement/index.md`)

- **Nume Tehnic:** `deltatech_service_agreement`
- **Versiune:** `20.0.2.0.18`
- **Cale:** `https://github.com/dhongu/deltatech_service/tree/20.0/deltatech_service_agreement`
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_agreement`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite definirea și gestionarea contractelor de servicii cu facturare recurentă. Pentru fiecare perioadă, sistemul pregătește consumurile planificate ale contractelor în curs, care pot fi corectate (cantitate, preț, dată) înainte de facturare, apoi generează facturile de client. Astfel, facturile reflectă serviciile prestate real, fără retastare manuală.

#### 2. Funcționalități Cheie

- Contracte de servicii pe partener și companie, cu monedă, ciclu de facturare (lunar, trimestrial, anual sau personalizat), ziua facturii (`-1` = ultima zi a lunii, `0` = fără zi fixă), termen de plată și linii de servicii cu cantitate, preț unitar, cantitate gratuită și cicluri gratuite.
- Pregătirea facturării (din lista de contracte, doar manageri): pentru perioada aleasă se creează câte un consum *Fără factură* pentru fiecare linie de contract în curs.
- Corectarea consumurilor înainte de facturare, inclusiv în masă: schimbare de preț (actualizează și prețul de listă al produsului), distribuție de cantitate sau valoare (Fix / Împarte) și schimbare a datei facturii.
- Facturare din consumuri (meniul *Serviciu → Contract → Facturare*), cu grupare pe partener, contract sau linie de contract; consumurile care nu depășesc cantitatea gratuită devin *Neaplicabil*.
- Un consum negativ devine corecție cu trimitere la factura inițială (notă de credit dacă valoarea netă este negativă).
- Jurnalul de vânzări folosit pentru servicii se marchează *Factură de servicii*; tipul de contract cere jurnalul și poate fi grupat pe *Grup de servicii*.
- Acțiune programată zilnică de facturare automată pentru contractele setate pe automat (setare tehnică, nu apare pe formular); implicit contractele sunt manuale.
- Fluxul pas-cu-pas, rolurile și verificările pentru consultant sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_service_base](../deltatech_service_base/index.md)
- `base`
- `product`
- `account`

#### 4. Componente Cheie

Secțiune omisă: pagina urmează `readme/DESCRIPTION.md` și fișa consultant, care nu solicită explicit analiza codului pentru Modele, Vizualizări și Acțiuni.

#### 5. Conexiuni

- [deltatech_service_base](../deltatech_service_base/index.md): modul de bază al suitei de servicii (meniu, grupuri, cicluri de facturare).
- [deltatech_service_equipment](../deltatech_service_equipment/index.md): leagă echipamentele și contoarele de liniile de contract și facturează pe baza citirilor.
- [deltatech_service_consumable](../deltatech_service_consumable/index.md): extinde contractele cu facturarea consumabilelor pe baza citirilor.
