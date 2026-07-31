# Marketplace Sales Order Stage addon (localizat la `deltatech_marketplace_sale_stage/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_sale_stage`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_marketplace_sale_stage
- **Cale Locală:** `odoo-addons/bitshop/deltatech_marketplace_sale_stage`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul oferă un sistem specializat de gestionare a etapelor (stages) pentru comenzile de vânzare provenite din marketplace-uri, îmbunătățind vizibilitatea și controlul pe parcursul întregului ciclu de procesare a comenzii. Din perspectivă de business, permite companiilor să definească și să urmărească etape personalizate pentru comenzile de marketplace, reflectând fluxurile de lucru și cerințele specifice fiecărui canal conectat. Astfel, echipele pot monitoriza exact statusul comenzilor, de la import până la livrare, pot impune pași obligatorii pentru conformitatea cu marketplace-ul și pot analiza performanța procesării prin urmărirea tranzițiilor între etape.

#### 2. Funcționalități Cheie

- Vizibilitate sporită a procesului: monitorizarea statusului exact al comenzilor de marketplace pe măsură ce avansează de la import către procesare și livrare.
- Control operațional: implementarea de fluxuri personalizate bazate pe etape, pentru a asigura parcurgerea tuturor pașilor necesari conformității cu marketplace-ul.
- Eficiență îmbunătățită: identificarea și rezolvarea rapidă a blocajelor din ciclul de procesare a comenzilor de marketplace.
- Integrare fără cusur: alinierea etapelor comenzilor de marketplace cu modulele integrate de vânzări și livrare din Odoo.
- Raportare mai bună: analiza performanței și a duratelor de procesare a vânzărilor de marketplace prin urmărirea tranzițiilor și a duratelor pe fiecare etapă.

#### 3. Dependențe

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- `deltatech_sale_stage`

#### 4. Componente Cheie

Modulul include un fișier `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune este omisă deoarece Readme-ul nu o solicită explicit.

#### 5. Conexiuni

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): modulul de bază pentru comenzile de vânzare din marketplace, peste care acest addon adaugă gestionarea etapelor.
- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul general de integrare marketplace din care face parte ecosistemul.
- [deltatech_marketplace_sale_type](../deltatech_marketplace_sale_type/index.md): modul soră, documentat în paralel, care adaugă tipuri pentru comenzile de marketplace.
