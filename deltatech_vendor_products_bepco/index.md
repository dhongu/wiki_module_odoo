# Vendor Products Bepco (localizat la `deltatech_vendor_products_bepco/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_bepco`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop_vendor/tree/20.0/deltatech_vendor_products_bepco
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products_bepco`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul conectează catalogul de produse al furnizorilor la Bepco, prin API-ul TVH, astfel încât prețurile Bepco să poată fi verificate direct din Odoo, fără copiere manuală. Este util echipelor care cumpără piese și vor să cunoască prețul de achiziție actual înainte de a emite o comandă sau o ofertă.

#### 2. Funcționalități Cheie

- Tip de conexiune nou, **Bepco**, pe fluxul furnizorului (`vendor.feed`).
- Căutare online: la căutarea unui cod de piesă, se interoghează API-ul TVH și se cere o cotație de preț, care întoarce prețul de achiziție.
- Coduri, descrieri și prețuri preluate direct de la Bepco, deci mai puține erori de tastare.
- Verificarea unei piese înainte de adăugarea ei într-o comandă de achiziție sau într-o ofertă pentru client.
- Limitări: caută câte un singur cod pe rând; nu importă catalogul Bepco, nu creează variante, iar butoanele *Load Price* de pe flux nu actualizează prețurile pentru acest tip de conexiune.
- Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md)

#### 4. Componente Cheie

**Modele**

- `vendor.feed` (extins): adaugă tipul de conexiune `bepco` și interogarea API-ului TVH.
- `vendor.product` (extins): preluarea datelor piesei găsite.

**Vizualizări**

- Fără vizualizări proprii (`data` gol în manifest).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_vendor_products](../deltatech_vendor_products/index.md): catalogul furnizorilor în care ajung datele Bepco.
