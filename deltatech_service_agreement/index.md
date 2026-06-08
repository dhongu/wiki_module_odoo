# Contracte de Servicii (localizat la `deltatech_service_agreement/index.md`)

- **Nume Tehnic:** `deltatech_service_agreement`
- **Versiune:** `19.0.2.0.9`
- **Cale:** `https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_agreement`
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_agreement`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul oferă posibilitatea de a defini și gestiona contracte de servicii cu facturare recurentă. Pe baza acestor contracte, sistemul generează periodic facturi către clienți, ținând cont de moneda, data de facturare și recurența stabilite în fiecare contract. Înainte de facturare, consumurile de servicii planificate pot fi actualizate cu cele efective, astfel încât facturile reflectă serviciile prestate real.

#### 2. Funcționalități Cheie

- Definirea contractelor de servicii, cu precizarea monedei, a datei de facturare și a recurenței.
- Generarea periodică, automată, a facturilor pe baza contractelor definite.
- Actualizarea consumurilor de servicii planificate cu cele efective, înainte de facturare.

#### 3. Dependențe

- `base`
- `product`
- `account`
- `deltatech_service_base`

#### 4. Componente Cheie

Secțiune omisă: fișierul `readme/DESCRIPTION.md` este prezent și nu solicită explicit analiza codului pentru componente (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server), conform fluxului de ingestie din `schema.md`.

#### 5. Conexiuni

- `deltatech_service_base`: modul de bază al suitei de servicii, pe care se construiește gestiunea contractelor de servicii.
