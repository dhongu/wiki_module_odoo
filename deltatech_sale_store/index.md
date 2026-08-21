# Deltatech Sale from Store (localizat la `deltatech_sale_store/index.md`)

- **Nume Tehnic:** `deltatech_sale_store`
- **Versiune:** `19.0.2.4.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_store
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_store`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul facilitează vânzarea directă din magazin prin emiterea de bonuri fiscale. Permite generarea unui fișier destinat programului de tipărit bonuri fiscale și definirea unui client generic pentru care bonurile fiscale se emit automat. Prin marcarea jurnalelor cu opțiunea „Bon fiscal", modulul stabilește ce jurnale de vânzări produc bonuri fiscale și restricționează utilizarea jurnalelor de tip cash, oferind astfel un flux ordonat pentru încasările din magazin.

#### 2. Funcționalități Cheie

- Generarea unui fișier pentru programul de tipărit Bonuri Fiscale.
- Definirea unui client generic pentru care se emit automat bonurile fiscale.
- Opțiunea „Bon fiscal" în jurnal: la un jurnal de vânzări, marcajul definește jurnalul (jurnalele) pentru bonuri fiscale; la un jurnal de tip cash, marcajul restricționează folosirea jurnalului în alte plăți/încasări.
- Pregătire necesară: trebuie definit un jurnal de vânzări pentru Bonuri Fiscale cu codul `BF`.

#### 3. Dependențe

- `account`
- `web`
- `sale`
- `stock`
- `sales_team`
- [deltatech_partner_generic](../deltatech_partner_generic/index.md)
- [deltatech_record_type](../deltatech_record_type/index.md)
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md)

#### 4. Componente Cheie

> Documentația pentru această secțiune este preluată din `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului (modele, vizualizări, acțiuni automate) este omisă deoarece Readme-ul nu o solicită explicit.

#### 5. Conexiuni

- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): furnizează conectarea la casa de marcat (ECR) folosită pentru tipărirea bonurilor fiscale generate de acest modul.
- [deltatech_saga](../deltatech_saga/index.md): fluxul de documente (factură/bon fiscal/storno) al acestui modul alimentează coloana `TIP` din exportul SAGA (`f`/`B`/`C`), conform `readme/CONFIGURE.md`.
- `deltatech_payment_report`: definește conturile contabile (`data/account_data.xml`) reutilizate de fluxul de plăți/încasări asociat bonurilor fiscale (referit în comentariile manifestului).
