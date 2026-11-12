# Product Dimensions (localizat la `deltatech_product_dimension/index.md`)

- **Nume Tehnic:** `deltatech_product_dimension`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_dimension
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_dimension`
- **Ultima Ingestie:** `2026-11-06`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul extinde fișa produsului din Odoo cu dimensiunile fizice ale produsului: lungime, lățime și înălțime, exprimate în centimetri. Din aceste dimensiuni se calculează automat volumul produsului, în unitatea de volum aleasă în setări. Este util companiilor care au nevoie de aceste date pentru ambalare, depozitare sau transport.

#### 2. Funcționalități Cheie

- Câmpuri suplimentare pe produs: lungime (length), lățime (width) și înălțime (height), în cm, cu valoarea implicită 1 × 1 × 1.
- Rândul **Dimensiune** apare în fila **Inventar** a produsului, în grupul **Logistică**, deasupra rândului **Volum**.
- La modificarea oricărei dimensiuni, **Volum** se recalculează (lungime × lățime × înălțime / 1.000.000, în m³) și se convertește în unitatea de volum din **Setări → Configurări generale → Unități de măsură** (m³ sau ft³). Dacă o dimensiune este 0, volumul devine 0.
- Volumul poate fi corectat manual; la următoarea modificare a dimensiunilor se recalculează din nou. La importuri volumul nu se calculează din dimensiuni.
- Dimensiunile sunt ale produsului (șablonului), nu ale variantei: toate variantele aceluiași produs au aceleași dimensiuni.
- Fila **Inventar** și grupul **Logistică** apar doar la produsele de tip **Bunuri**.
- Modulul nu are efect fiscal sau contabil; dimensiunile pot fi folosite de alte module (transport, feed-uri pentru marketplace-uri).

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, modulul adaugă pe produs câmpuri de dimensiune (lungime, lățime, înălțime); calculul volumului este descris în `readme/HISTORY.md` și în fișa consultant. Detalierea tehnică a fost omisă conform fluxului de ingestie (prioritizarea Readme).

#### 5. Conexiuni

- `stock`, `delivery`: dacă sunt instalate, folosesc volumul produsului la transferuri și la transport.
