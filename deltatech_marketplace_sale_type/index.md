# Marketplace Order Types (localizat la `deltatech_marketplace_sale_type/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_sale_type`
- **Versiune:** `20.0.0.0.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_sale_type
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_sale_type`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul clasifică comenzile din marketplace după tip, pentru ca vânzările fiecărui canal să poată fi analizate separat de vânzările directe. Fiecărui backend de marketplace i se asociază un tip de comandă, aplicat automat pe comenzile importate. Este util pentru raportare pe canale și pentru a distinge clar comenzile de marketplace de celelalte categorii de comenzi.

#### 2. Funcționalități Cheie

- Tip de comandă implicit pe fiecare backend de marketplace (câmpul *Order Type*, din [deltatech_record_type](../deltatech_record_type/index.md)).
- Tipul se scrie automat pe comenzile importate din acel backend.
- Analiză și grupare a vânzărilor din marketplace după tip, pe fiecare platformă conectată.
- Modulul este gratuit. Fluxul de configurare se află în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_record_type](../deltatech_record_type/index.md)

#### 4. Componente Cheie

**Modele**

- `marketplace.backend` (extindere): câmpul `so_type_id` (`record.type`, urmărit în chatter).
- `marketplace.sale.order` (extindere): în `prepare_values()` scrie `so_type` din tipul backend-ului pe comanda importată.

**Vizualizări**

- `view_marketplace_backend_form` (`backend_views.xml`): extinde formularul backend-ului cu tipul de comandă.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): nucleul suitei de integrare cu marketplace-uri.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): comenzile din marketplace pe care acest modul le clasifică.
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): modul soră, care adaugă faze comenzilor.
