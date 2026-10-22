# Deltatech Services Maintenance Agreement

- **Nume Tehnic:** `deltatech_service_maintenance_agreement`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_maintenance_agreement
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_maintenance_agreement`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Leagă fluxul de mentenanță de contractul de service al echipamentului: fiecare notificare și fiecare comandă de service știe ce contract acoperă echipamentul vizat, astfel încât echipa de service vede contractul în timp ce tratează solicitarea. Livrările nefacturabile sunt oferite doar atunci când tipul de contract le permite.

#### 2. Funcționalități Cheie

- **Contract pe notificare:** notificarea afișează contractul de service al echipamentului, preluat automat din echipament, în formular și ca coloană opțională în listă.
- **Contract pe comanda de service:** comanda de service poartă contractul, completat la crearea din echipament sau din notificare (coloană opțională în listă).
- **Livrări permise de tipul de contract:** butonul *Livrare nouă* de pe o notificare din categoria *Livrare* apare doar dacă tipul de contract permite livrări nefacturabile și nu a fost creată încă nicio livrare. Opțiunea *Permite livrări nefacturabile* se bifează în *Servicii > Configurare > Tipuri de contract de service*, pe tipurile ale căror contracte acoperă livrări de consumabile.
- **Valori implicite din echipament:** documentele deschise din echipament primesc contractul, adresa și persoana de contact ca valori implicite.

#### 3. Dependențe

- [deltatech_service_maintenance](../deltatech_service_maintenance/index.md)
- [deltatech_service_equipment](../deltatech_service_equipment/index.md)
- [deltatech_service_agreement](../deltatech_service_agreement/index.md)

#### 4. Componente Cheie

**Modele**

- `service.notification` (extins): `agreement_id` (related din echipament), `can_create_delivery` (din tipul contractului), completarea contractului la creare și transmiterea lui în contextul implicit.
- `service.order` (extins): câmpul `agreement_id` (Contract de service).
- `service.equipment` (extins): `get_context_default` adaugă contractul, adresa și contactul.

**Vizualizări**

- `view_service_notification_form` / `view_service_notification_tree`: contractul pe notificare și butonul *Livrare nouă* condiționat de `can_create_delivery`.
- `view_service_order_form`: câmpul contract pe comanda de service.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- Nu există legături funcționale suplimentare față de dependențele de mai sus.
