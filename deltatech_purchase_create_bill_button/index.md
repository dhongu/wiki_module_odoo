# Purchase Create Bill Button (localizat la `deltatech_purchase_create_bill_button/index.md`)

- **Nume Tehnic:** `deltatech_purchase_create_bill_button`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_create_bill_button`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_create_bill_button`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

În Odoo 19, butonul clasic „Create Bill" de pe formularul comenzii de achiziție a fost înlocuit cu un widget „Upload Bill" care obligă utilizatorul să atașeze un fișier înainte de a putea genera factura. Acest modul restabilește butonul clasic, cu un singur clic, lângă widget-ul de încărcare, astfel încât comenzile de achiziție să poată fi facturate direct, fără a fi nevoie de un fișier atașat — exact ca în Odoo 18. Modulul restaurează totodată și copierea automată a „Referinței Furnizorului" de pe comanda de achiziție în câmpurile „Referință" și „Referință Plată" ale facturii de furnizor generate, comportament eliminat în Odoo 19.

#### 2. Funcționalități Cheie

- Restabilește butonul „Create Bill" (facturare cu un singur clic) pe formularul comenzii de achiziție, alături de widget-ul „Upload Bill"
- Permite crearea facturii de furnizor direct din comanda de achiziție, fără a fi necesară atașarea unui fișier
- Restaurează copierea automată a „Referinței Furnizorului" din comanda de achiziție în câmpurile „Referință" și „Referință Plată" ale facturii generate, replicând comportamentul din Odoo 18

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe fișierul `readme/DESCRIPTION.md`, care nu detaliază componentele tehnice individuale. Conform fluxului de ingestie, analiza codului pentru modele, vizualizări și acțiuni automate a fost omisă, deoarece Readme-ul este prezent și nu solicită explicit această analiză.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale documentate către alte module cu pagină în wiki.
