# Vendor Products Storage (localizat la `deltatech_vendor_products_storage/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_storage`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_vendor/tree/19.0/deltatech_vendor_products_storage
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products_storage`
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Prototip (stadiu Alpha) care permite păstrarea pozelor și a fișierelor PDF ale articolelor din catalogul furnizorilor (`vendor.product`) într-un spațiu de stocare în cloud, prin mecanismul standard `cloud_storage`. Fișierele se trimit direct de pe telefon sau din browser către bucket, fără să treacă prin serverul Odoo, iar modulul funcționează cu orice furnizor de stocare compatibil (Google sau Cloudflare R2), ales din Setări.

#### 2. Funcționalități Cheie

- Chatter pe formularul articolului din catalogul furnizorului, ca fișierele să poată fi atașate din Odoo.
- Articol provizoriu: o etichetă tipărită încă nedescrisă se poate crea doar cu codul; denumirea preia codul, iar prețul de vânzare este 0 (importurile din feed-uri nu sunt afectate, ele trimit ambele câmpuri).
- Endpoint `POST /vendor_product_storage/upload_info` (JSON-RPC, utilizator autentificat cu drept de scriere): creează atașamentul unui articol, identificat după id sau cod, și întoarce URL-ul semnat pentru încărcarea directă în bucket. Se acceptă doar imagini raster (SVG este refuzat) și PDF, până la dimensiunea maximă.
- Endpoint `POST /vendor_product_storage/confirm_upload`: verifică fișierul încărcat, înregistrează dimensiunea reală în atașament și șterge atașamentul dacă încărcarea lipsește, blob-ul este gol sau fișierul depășește limita.
- Miniatura primei pagini pentru PDF-urile din cloud funcționează (cea standard cere conținutul fișierului în baza de date).
- Dimensiunea maximă: parametrul de sistem `deltatech_vendor_products_storage.max_file_size` (octeți, implicit 25 MB).
- Curățare zilnică a atașamentelor neconfirmate în 24 de ore (parametrul `deltatech_vendor_products_storage.unconfirmed_hours`), deoarece limita de dimensiune se impune prin `confirm_upload`.
- Fișierul rămâne în bucket la ștergerea articolului sau a atașamentului; fișierele nefolosite se curăță cu scriptul de curățare al modulului de stocare cloud.

#### 3. Dependențe

- [deltatech_vendor_products](../deltatech_vendor_products/index.md)
- `cloud_storage`

#### 4. Componente Cheie

**Modele**

- `vendor.product` (extins): adaugă `mail.thread`, prețul de vânzare implicit 0 și completarea denumirii din cod la creare.
- `ir.attachment` (extins): dimensiunea maximă permisă, citirea dimensiunii reale a blob-ului din cloud (cerere cu `Range`), descărcarea limitată a conținutului pentru miniatură, înregistrarea `file_size` și curățarea atașamentelor neconfirmate.

**Vizualizări**

- `view_vendor_product_form_storage`: moștenește formularul articolului din catalogul furnizorului și adaugă chatter-ul.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_vendor_product_storage_clean_unconfirmed`: rulează zilnic și șterge atașamentele cloud ale articolelor (`vendor.product`) cu dimensiune neînregistrată, mai vechi decât pragul configurat.

**Controllere**

- `VendorProductStorage`: rutele `upload_info` și `confirm_upload`.
- `VendorProductAttachmentController`: suprascrie miniatura primei pagini PDF pentru fișierele din cloud.

#### 5. Conexiuni

- [deltatech_vendor_products_site](../deltatech_vendor_products_site/index.md): modul înrudit al aceleiași suite de catalog al furnizorilor.
- [deltatech_cloud_storage_r2](../deltatech_cloud_storage_r2/index.md): furnizor de stocare (Cloudflare R2) care se poate alege pentru `cloud_storage`.
