# Terrabit Pro (localizat la `terrabit_pro/index.md`)

- **Nume Tehnic:** `terrabit_pro`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_pro
- **Cale Locală:** `odoo-addons/terrabit/terrabit_pro`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Terrabit Pro este un modul-pachet (meta-modul) care instalează dintr-o singură mișcare setul extins de aplicații folosit în implementările Terrabit. Se adaugă peste pachetul de bază `terrabit_base` și aduce resurse umane, concedii, documente, comerț electronic, CRM și proiecte, plus integrarea cu SAGA și completarea orașelor în website. Modulul nu are cod propriu (modele, vizualizări sau automatizări) și nu adaugă funcționalități noi: rolul său este să grupeze dependențele esențiale, astfel încât un client să primească o configurare coerentă și ușor de reprodus.

#### 2. Funcționalități Cheie

- Instalează într-un singur pas pachetul de bază Terrabit (vânzări, achiziții, stocuri, contabilitate și localizarea pentru România) prin `terrabit_base`.
- Adaugă aplicațiile standard Odoo pentru resurse umane (`hr`), concedii (`hr_holidays`), documente (`documents`), comerț electronic (`website_sale`), CRM (`crm`) și proiecte (`project`).
- Include integrarea cu SAGA (export de date contabile) prin `deltatech_saga`.
- Include selecția orașului la adresele din website prin `deltatech_website_city`.
- Este marcat ca aplicație (`application`) și nu se instalează automat; versiunea curentă are pictogramă proprie în locul celei generice.

#### 3. Dependențe

- [terrabit_base](../terrabit_base/index.md)
- `hr`
- `documents`
- `website_sale`
- `crm`
- `project`
- `hr_holidays`
- [deltatech_website_city](../deltatech_website_city/index.md)
- [deltatech_saga](../deltatech_saga/index.md)

#### 4. Componente Cheie

**Modele**

Modulul nu definește și nu extinde modele.

**Vizualizări**

Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

Nu există acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [terrabit_base](../terrabit_base/index.md): pachetul de bază peste care se așază acest modul.
- [deltatech_saga](../deltatech_saga/index.md): exportul către SAGA, inclus ca dependență.
- [deltatech_website_city](../deltatech_website_city/index.md): orașe în adresele din website.
