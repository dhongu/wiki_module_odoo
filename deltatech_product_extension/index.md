# Deltatech Products Extension (localizat la `deltatech_product_extension/index.md`)

- **Nume Tehnic:** `deltatech_product_extension`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_extension
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_extension`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Acest modul extinde modelul standard de produs din Odoo prin adăugarea unor câmpuri tehnice și logistice esențiale. Este destinat companiilor care au nevoie de o urmărire detaliată a atributelor produselor, cum ar fi termenul de valabilitate (durata de viață pe raft), informațiile despre producător și dimensiunile fizice. Astfel, devine mai ușor de gestionat stocul perisabil sau sensibil la timp, de planificat livrările și depozitarea și de organizat partenerii în funcție de calitatea de producător.

#### 2. Funcționalități Cheie

- **Urmărire logistică îmbunătățită**: adaugă pe șablonul de produs câmpurile **Termen de valabilitate (Shelf Life)** și **Unitate de măsură pentru termenul de valabilitate**, permițând o mai bună gestionare a stocului perisabil sau sensibil la timp.
- **Informații detaliate despre producător**: integrează direct pe fișa produsului o legătură către **Producător** (partener), oferind acces rapid la originea de fabricație și la datele de contact.
- **Dimensiuni fizice**: adaugă câmpuri pentru specificarea dimensiunilor produsului (Lungime, Lățime, Înălțime) direct pe înregistrarea produsului, utile pentru expediere, planificarea depozitării și afișarea în catalog.
- **Integrare cu partenerii**: extinde modelul de partener cu o bifă **Producător**, permițând categorizarea ușoară a vânzătorilor și furnizorilor și o filtrare mai bună în modulul Contacte.

#### 3. Dependențe

- `product`
- `account`

#### 4. Componente Cheie

Conform fluxului de ingestie (prioritizarea Readme), această secțiune nu este detaliată prin analiza codului, deoarece fișierul `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit documentarea Componentelor Cheie.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte pagini de module din wiki. Dependențele directe (`product`, `account`) sunt module standard Odoo și nu au încă pagină wiki.
