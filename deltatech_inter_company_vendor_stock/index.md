# Deltatech Inter Company Stock (localizat la `deltatech_inter_company_vendor_stock/index.md`)

- **Nume Tehnic:** `deltatech_inter_company_vendor_stock`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_inter_company_vendor_stock
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_inter_company_vendor_stock`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul afișează stocul liber al unei companii din grup în compania care îi vinde produsele. Când compania furnizoare rezervă sau validează mișcări de stoc, modulul scrie stocul liber al produsului pe linia de furnizor (**Cantitate disponibilă**) pe care compania vânzătoare o ține pentru acel furnizor. Astfel, vânzătorii pot promite livrări pornind de la stocul real al grupului.

#### 2. Funcționalități Cheie

- Funcționează cu două companii ale aceluiași grup, în aceeași bază de date, folosind regulile inter-company din Enterprise: compania furnizoare ține stocul, cea vânzătoare cumpără de la ea și vinde clienților proprii. Pe produs, compania vânzătoare are o linie de furnizor al cărei furnizor este partenerul companiei furnizoare.
- Actualizare automată la rezervarea și la validarea mișcărilor de stoc din compania furnizoare.
- Câmpul **Cantitate disponibilă** se vede în **Achiziții → Configurare → Liste de prețuri furnizor**, precum și ca coloană opțională în lista de furnizori de pe fișa produsului (tabul **Achiziții**).
- Pe comanda de vânzare a companiei vânzătoare, coloana opțională **Cantitate disponibilă la furnizor** (din Vendor Stock) arată stocul liber al furnizorilor produsului.
- Rezervarea și validarea se fac în compania furnizoare, activă în selectorul de companii: se caută liniile de furnizor ale partenerului companiei active și se numără doar stocul acesteia, chiar dacă sunt selectate mai multe companii.
- Linia de furnizor pe o variantă primește stocul liber al variantei; linia fără variantă (cazul uzual, adăugată din fișa produsului) primește stocul liber însumat al tuturor variantelor.

#### 3. Dependențe

- `sale_purchase_inter_company_rules`
- [deltatech_vendor_stock](../deltatech_vendor_stock/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.move` (extins): după `_action_assign` și `_action_done` apelează `inter_company_stock_update()`, care scrie stocul liber (`free_qty`) al companiei active pe `qty_available` al liniilor `product.supplierinfo` unde partenerul companiei este furnizor.

**Vizualizări**

- Modulul nu adaugă vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_vendor_stock](../deltatech_vendor_stock/index.md): oferă câmpul `qty_available` pe linia de furnizor și coloana de pe comanda de vânzare, completate de acest modul.
