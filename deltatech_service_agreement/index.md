# Contracte de Servicii (localizat la `deltatech_service_agreement/index.md`)

- **Nume Tehnic:** `deltatech_service_agreement`
- **Versiune:** `19.0.2.0.20`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_agreement
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_agreement`
- **Ultima Ingestie:** `2026-11-21`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite definirea și gestionarea contractelor de servicii cu facturare recurentă. Pentru fiecare perioadă, sistemul pregătește consumurile planificate ale contractelor active, care pot fi corectate (cantitate, preț, data facturii) înainte de facturare, iar apoi generează facturile către clienți. Astfel, facturile reflectă serviciile prestate real, iar legătura dintre factură și contract rămâne păstrată.

#### 2. Funcționalități Cheie

- Definirea contractelor de servicii pentru fiecare partener și companie, cu monedă, ciclu de facturare (lunar, trimestrial, anual sau personalizat), ziua facturii, termen de plată și linii de servicii.
  - Liniile au cantitate, preț unitar, cantitate gratuită și cicluri gratuite.
  - Doar contractele *În derulare* se facturează; data următoarei facturi se calculează din ultima factură confirmată (sau data contractului), ciclu și ziua facturii (`-1` = ultima zi a lunii, `0` = fără zi fixă).
- Pregătirea facturării pentru o perioadă (acțiunea *Pregătire facturare*, doar pentru manageri): se creează câte un consum *Fără factură* pentru fiecare linie de contract.
- Corectarea consumurilor înainte de facturare: modificare în masă a prețului (actualizează și prețul de listă al produsului), distribuirea unei cantități sau a unei valori (modurile *Fix* și *Împarte*) și schimbarea datei facturii.
- Generarea facturilor de client din consumuri, grupate pe contract, pe partener sau pe linie de contract (opțional și pe serviciu).
  - Un consum cu cantitate negativă devine o corecție cu trimitere la factura inițială (notă de credit dacă valoarea netă este negativă).
  - Consumurile care nu depășesc cantitatea gratuită devin *Neaplicabil*.
  - Anularea sau ștergerea facturii readuce consumurile în starea *Fără factură*.
- Configurare necesară: bifa *Factură servicii* pe jurnalul de vânzări folosit, tip de contract cu jurnal asociat, cicluri de facturare și perioade de serviciu (intervale de date) pentru luna facturată.
- O acțiune programată zilnică pregătește și facturează (ciornă) contractele setate pe facturare automată (setare tehnică, nu apare în formular; implicit contractele sunt *Manual*).
- Drepturi de acces (19.0): toți utilizatorii interni pot citi contractele, liniile, tipurile, grupurile și consumurile; modificarea rămâne la utilizatorii și managerii de service (crearea contractelor doar manageri). Utilizatorii portal nu au acces.
- Un contract poate fi șters doar în starea *Ciornă*, iar un consum facturat nu poate fi șters.

#### 3. Dependențe

- `base`
- `product`
- `account`
- [deltatech_service_base](../deltatech_service_base/index.md)

#### 4. Componente Cheie

Secțiune omisă: fișierul `readme/DESCRIPTION.md` este prezent și nu solicită explicit analiza codului pentru componente (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server), conform fluxului de ingestie din `schema.md`.

#### 5. Conexiuni

- [deltatech_service_base](../deltatech_service_base/index.md): modul de bază al suitei de servicii, pe care se construiește gestiunea contractelor de servicii.
