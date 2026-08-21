# Terrabit Delivery Staff (localizat la `terrabit_delivery_staff/index.md`)

- **Nume Tehnic:** `terrabit_delivery_staff`
- **Versiune:** `19.0.0.0.10`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_delivery_staff`
- **Cale Locală:** `odoo-addons/bitshop/terrabit_delivery_staff`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul permite distribuirea livrărilor către personalul propriu de livrare (curieri/șoferi interni). Fiecare livrare poate fi atribuită unui angajat care face parte din grupul „Delivery staff", iar acești utilizatori văd și gestionează doar propriile livrări, fără a putea modifica livrările atribuite altor colegi. În plus, modulul oferă un raport PDF dedicat personalului de livrare, util la organizarea traseelor și a predării coletelor.

#### 2. Funcționalități Cheie

- Distribuirea livrărilor pe angajați (personal de livrare propriu).
- Restricționarea accesului: utilizatorii din grupul „Delivery staff" nu pot modifica livrările altor utilizatori.
- Raport PDF pe livrare, dedicat personalului de livrare (pickup list).
- Parametru de sistem `delivery_staff.allow_change_responsible` care controlează dacă personalul de livrare poate schimba utilizatorul responsabil de pe livrare (implicit `False`).

#### 3. Dependențe

- `sale`
- `stock`
- [deltatech_delivery](../deltatech_delivery/index.md)
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)
- [deltatech_logistic_docs](../deltatech_logistic_docs/index.md)

#### 4. Componente Cheie

Documentația pentru 'Sumar' și 'Funcționalități Cheie' a fost preluată din fișierul `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a componentelor (Modele, Vizualizări, Acțiuni) din cod este omisă, deoarece nu este menționată explicit în Readme.

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): completează gestionarea livrărilor prin stări/etape, util alături de distribuirea livrărilor pe personalul propriu.
