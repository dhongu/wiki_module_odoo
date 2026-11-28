# Vendor Products Storage (localizat la `deltatech_vendor_products_storage/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_storage`
- **Versiune:** `20.0.1.2.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_vendor/tree/20.0/deltatech_vendor_products_storage
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products_storage`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Prototip care păstrează pozele și fișierele PDF ale articolelor din catalogul furnizorilor (`vendor.product`) într-o stocare în cloud, prin mecanismul standard `cloud_storage`. Folosește doar API-ul generic, deci funcționează cu orice furnizor de stocare instalat și ales în Setări.

#### 2. Funcționalități Cheie

- Chatter pe formularul articolului din catalog: fișierele atașate ajung în cloud când depășesc *Minimum File Size* din setările stocării (implicit 20 MB); cele mai mici rămân în baza de date.
- Articol provizoriu (de exemplu o etichetă tipărită încă nedescrisă) creat doar cu cod: numele preia codul, prețul de vânzare este 0.
- `POST /vendor_product_storage/upload_info` (JSON-RPC, utilizator cu drept de scriere): creează atașamentul unui articol (după id sau cod) și întoarce URL-ul semnat pentru încărcare directă din telefon sau browser. Se acceptă doar imagini raster (SVG refuzat) și PDF, până la dimensiunea maximă.
- `POST /vendor_product_storage/confirm_upload`: verifică fișierul încărcat, înregistrează dimensiunea reală și șterge atașamentul dacă încărcarea lipsește sau e prea mare.
- Miniatura primei pagini din PDF funcționează pentru fișierele din cloud.
- Parametri de sistem: `deltatech_vendor_products_storage.max_file_size` (octeți, implicit 25 MB) și `deltatech_vendor_products_storage.unconfirmed_hours` (24 h).
- Fișierul rămâne în bucket la ștergerea articolului sau a atașamentului; curățarea se face cu scriptul modulului de stocare cloud.
- Pașii de configurare și testare sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_vendor_products](../deltatech_vendor_products/index.md)
- `cloud_storage`

#### 4. Componente Cheie

**Modele**

- `vendor.product` (extins, cu `mail.thread`): chatter și articole provizorii.
- `ir.attachment` (extins): curățarea încărcărilor neconfirmate și miniaturi PDF.

**Vizualizări**

- `view_vendor_product_form_storage`: chatter pe formularul articolului.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_vendor_product_storage_clean_unconfirmed`: zilnic, șterge atașamentele neconfirmate în 24 de ore.

#### 5. Conexiuni

- [deltatech_cloud_storage_r2](../deltatech_cloud_storage_r2/index.md): furnizor de stocare compatibil (Cloudflare R2).
- [deltatech_cloud_storage_s3](../deltatech_cloud_storage_s3/index.md): furnizor de stocare compatibil (S3).
- [deltatech_cloud_storage_b2](../deltatech_cloud_storage_b2/index.md): furnizor de stocare compatibil (Backblaze B2).
- [deltatech_cloud_storage_hetzner](../deltatech_cloud_storage_hetzner/index.md): furnizor de stocare compatibil (Hetzner).
