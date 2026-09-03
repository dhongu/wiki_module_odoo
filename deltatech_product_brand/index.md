# Manager Mărci Produse (Product Brand Manager)

- **Nume Tehnic:** `deltatech_product_brand`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_product_brand
- **Cale Locală:** `odoo-addons/bitshop/deltatech_product_brand`
- **Ultima Ingestie:** `2026-09-03`

#### 1. Sumar

Acest modul oferă un sistem robust și centralizat de gestionare a mărcilor de produse în Odoo, ajutând companiile să-și organizeze și să-și categorisească întregul catalog de produse în funcție de marcă. Din perspectivă de business, această extensie este esențială pentru menținerea unei baze de date de produse structurate și ușor de căutat, ceea ce conduce la îmbunătățirea performanței de marketing și vânzări.

#### 2. Funcționalități Cheie

- Identitate de marcă unificată: creare și gestionare a unei ierarhii consistente de mărci pentru toate produsele din Odoo.
- Căutare și descoperire îmbunătățite: experiență mai bună pentru utilizator și client prin filtrare și căutare facilă după marcă.
- Marketing țintit: dezvoltarea și execuția de campanii de marketing și strategii de vânzări specifice pe marcă.
- Analize detaliate pe marcă: generarea și analizarea rapoartelor de performanță a vânzărilor și de inventar pe marcă de produs.
- Gestionare scalabilă a catalogului: organizarea și administrarea eficientă a unui număr mare de produse și mărci într-o singură interfață Odoo integrată.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

*Notă: Conform fluxului de ingestie, Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`. Componentele de mai jos sunt incluse din `readme/USAGE.md` și din manifest, ca reper de orientare pentru utilizator.*

**Modele**

- `product.brand`: marca de produs, cu logo, partener asociat și descriere.
- `product.template`: extins cu un câmp de marcă, disponibil în formularul de produs.

**Vizualizări**

- Mărcile de produse se administrează din **Vânzări > Configurare > Produse > Mărci de produse**.
- Câmpul de marcă apare în formularul produsului, sub numele acestuia.

**Rapoarte**

- Raportul de vânzări (**Vânzări > Raportare > Vânzări**) permite gruparea/dimensionarea după marcă în vizualizarea pivot.
- Raportul de facturi (**Facturare > Raportare > Management > Analiză facturi**) permite gruparea/dimensionarea după marcă.

#### 5. Conexiuni

- [deltatech_brand_field](../deltatech_brand_field/index.md): adaugă/gestionează câmpul de marcă pe produs, complementar cu modelul `product.brand` definit aici.
- [deltatech_marketplace_brand](../deltatech_marketplace_brand/index.md): depinde de acest modul și extinde mărcile de produse în contextul marketplace.
