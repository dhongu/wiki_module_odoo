# Vizualizator Linii Listă de Prețuri (localizat la `deltatech_pricelist_line_viewer/index.md`)

- **Nume Tehnic:** `deltatech_pricelist_line_viewer`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pricelist_line_viewer
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pricelist_line_viewer`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul îmbunătățește gestionarea listelor de prețuri din Odoo punând la dispoziție o vizualizare dedicată de tip listă pentru articolele (liniile) listei de prețuri. Astfel devine mult mai simplu să cauți, să filtrezi și să administrezi reguli de prețuri complexe, distribuite pe mai multe produse și categorii. Pe lângă confortul de utilizare, modulul introduce și un control de acces mai fin, permițând anumitor utilizatori să modifice listele de prețuri fără a avea drepturi complete de administrator de vânzări.

#### 2. Funcționalități Cheie

- **Vizualizare centralizată a liniilor listei de prețuri**: adaugă un buton de tip „stat button” în partea de sus a formularului listei de prețuri; la apăsare se deschide o vizualizare de tip arbore (tree) pe tot ecranul, cu toate regulile de prețuri ale acelei liste.
- **Căutare și filtrare avansată**: activează capabilitățile standard Odoo de căutare și filtrare la nivelul liniilor listei de prețuri, ușurând accesul și administrarea listelor cu un număr mare de reguli.
- **Control de securitate rafinat**: introduce un grup tehnic nou, **Permit pricelist editing**, care permite utilizatorilor desemnați să modifice listele de prețuri și liniile acestora fără a necesita privilegii complete de Administrator Vânzări.

#### 3. Dependențe

- `sale_management`
- `product`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea de Componente Cheie nu este detaliată din cod, întrucât fișierul `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie. Pe baza datelor declarate în `__manifest__.py`, modulul aduce:

**Vizualizări**

- `views/product_pricelist_view.xml`: extinde formularul listei de prețuri cu butonul de acces către vizualizarea de tip listă a liniilor.

**Acțiuni Automate / Acțiuni Server**

- `data/security_groups.xml`: definește grupul tehnic **Permit pricelist editing** pentru editarea listelor de prețuri fără drepturi de administrator complet.

#### 5. Conexiuni

- Nicio conexiune suplimentară documentată în afara dependențelor declarate.
