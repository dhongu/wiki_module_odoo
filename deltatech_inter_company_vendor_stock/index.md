# Stoc Inter-Company (localizat la `deltatech_inter_company_vendor_stock/index.md`)

- **Nume Tehnic:** `deltatech_inter_company_vendor_stock`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_inter_company_vendor_stock
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_inter_company_vendor_stock`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul afișează stocul liber al unei companii din grup în compania care vinde produsele acesteia. Când compania furnizoare rezervă sau validează mișcări de stoc, modulul scrie stocul liber al produsului pe linia de furnizor (**Quantity Available**) pe care compania vânzătoare o ține pentru acel furnizor, iar vânzătorii pot promite livrări pe baza stocului real al grupului.

#### 2. Funcționalități Cheie

- Scenariul: două companii din același grup, în aceeași bază de date, cu regulile inter-company Enterprise; compania furnizoare ține stocul, cea vânzătoare cumpără de la ea și vinde clienților proprii.
- La **Validate** sau la rezervare în compania furnizoare, stocul liber al produsului se recalculează și se scrie pe linia de furnizor (în fișă: din 20 de unități, după livrarea a 5 rămân 15, iar după rezervarea altor 3 rămân 12).
- Valoarea se vede în **Purchase → Configuration → Vendor Pricelists**, ca coloană opțională în lista de furnizori de pe produs (fila *Purchase*) și în coloana opțională *Vendor Quantity Available* de pe liniile comenzii de vânzare.
- Rezervarea și validarea se fac cu compania furnizoare activă în selectorul de companii: se caută liniile de furnizor ale partenerului companiei active și se numără doar stocul ei, chiar dacă sunt selectate mai multe companii.
- O linie setată pe o variantă primește stocul variantei; o linie fără variantă (cazul uzual) primește stocul tuturor variantelor produsului.

#### 3. Dependențe

- `sale_purchase_inter_company_rules`
- [deltatech_vendor_stock](../deltatech_vendor_stock/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.move`: la rezervare și validare actualizează cantitatea disponibilă pe linia de furnizor.

**Vizualizări**

- Fără vizualizări proprii; folosește câmpurile din [deltatech_vendor_stock](../deltatech_vendor_stock/index.md).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_vendor_stock](../deltatech_vendor_stock/index.md): oferă câmpul de stoc la furnizor, alimentat aici din companiile grupului.
