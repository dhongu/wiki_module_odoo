# MRP Concentration (localizat la `deltatech_mrp_concentration/index.md`)

- **Nume Tehnic:** `deltatech_mrp_concentration`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_concentration
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_concentration`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Acest modul introduce o funcționalitate specializată de gestionare a concentrației pentru procesele de producție din Odoo. Este conceput pentru industrii (precum cea chimică, alimentară sau farmaceutică) unde concentrația reală a unui ingredient activ dintr-o componentă poate varia, necesitând ajustarea cantităților de producție pentru a menține calitatea produsului finit.

#### 2. Funcționalități Cheie

- **Urmărirea concentrației componentelor**: adaugă un câmp **Concentrație** direct pe liniile listei de materiale (BoM), permițând inginerilor de producție să specifice concentrația necesară pentru fiecare materie primă sau ingredient.
- **Ajustări dinamice ale producției**: se integrează cu modulul de bază de Producție (MRP) din Odoo pentru a se asigura că, în timpul producției, cantitățile efectiv consumate țin cont de concentrația specificată, compensând variațiile de concentrație ale componentelor pentru calitate și potență consecvente ale produselor finite.
- **Trasabilitate și documentare**: include datele de concentrație atât pe lista de materiale (BoM), cât și pe comenzile de producție (MO) individuale, pentru o mai bună auditabilitate și control al calității.

#### 3. Dependențe

- `base`
- `mrp`
- `stock`
- `sale`
- `product`

#### 4. Componente Cheie

Documentația pentru Sumar și Funcționalități Cheie a fost preluată din `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune este omisă, deoarece Readme-ul nu o solicită explicit.

#### 5. Conexiuni

- [deltatech_mrp](../deltatech_mrp/index.md): suită de extensii personalizate pentru modulul de Producție (MRP), cu care acest modul împărtășește aria funcțională a listelor de materiale și a comenzilor de producție.
