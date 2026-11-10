# Website Image Watermark (localizat la `deltatech_website_watermark/index.md`)

- **Nume Tehnic:** `deltatech_website_watermark`
- **Versiune:** `19.0.1.0.13`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_watermark
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_watermark`
- **Ultima Ingestie:** `2026-11-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul adaugă automat o filigranare (watermark) pe imaginile produselor afișate pe site și pe celelalte dimensiuni de imagine calculate din `image.mixin`. Permite păstrarea imaginilor originale curate, aplicând dinamic filigranul companiei în momentul randării. Astfel, magazinul online beneficiază de protejarea vizuală a imaginilor de produs fără a modifica fișierele sursă încărcate.

#### 2. Funcționalități Cheie

- Aplică un filigran centrat și transparent (opacitate 20%, scalat la dimensiunea imaginii) pe imaginile de produs randate în magazinul online; miniaturile mici (coș, liste scurte) rămân curate, iar în back office rămâne imaginea originală.
- Filigranul companiei se încarcă în **Setări > Setări generale**, secțiunea **Companii**, câmpul **Watermark image**; fiecare companie are propriul filigran.
- Filigranul poate fi dezactivat pentru anumiți parteneri (câmpul **Use Watermark** din fila **Vânzări și achiziții**, bifat implicit pentru toți partenerii, angajați inclusiv) sau pentru anumite produse (câmpul **Has Watermark** din fila **Vânzări**, grupul **Ecommerce Shop**: magazinul trimite toate imaginile ca atare, inclusiv Ecommerce Media).
- O variantă cu imagine proprie afișează pe pagina de produs acea imagine, filigranată; o variantă fără imagine proprie afișează imaginea produsului.
- Suport complet pentru imaginile sursă WEBP; formatul de ieșire păstrează WEBP când originalul este WEBP, altfel se folosește JPEG (un PNG transparent își pierde transparența).
- Optimizat pentru performanță la procesarea unui număr mare de imagini (cache în memorie al filigranului și al dimensiunilor pregătite).
- Respectă dimensiunea de imagine solicitată din context (ex: `image_1024`, `image_512` etc.).

**Cerințe și note**

- Trebuie configurată o imagine de filigran la nivelul companiei; altfel filigranarea nu poate fi aplicată.
- Imaginea de filigran ar trebui să fie un PNG cu fundal transparent, într-o culoare închisă (recomandat).
- Când se așteaptă imagini filigranate, asigurați-vă că filigranul companiei este setat pentru a evita erorile de decodare.
- Pașii detaliați sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `website_sale`
- [deltatech_watermark](../deltatech_watermark/index.md)

#### 4. Componente Cheie

Documentația acestui modul se bazează pe fișierul `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului (Modele, Vizualizări, Acțiuni Automate) este omisă deoarece Readme-ul nu o solicită explicit.

Din manifest, modulul adaugă vizualizările `views/res_partner_view.xml` (câmpul **Use Watermark** pe partener) și `views/product_view.xml` (câmpul **Has Watermark** pe produs).

Notă tehnică (din Readme): decodare robustă a imaginilor cu fallback pentru intrări WEBP și data-URL; inițializarea pluginului WebP din Pillow (PIL) pentru a evita erorile de decodare; compoziție rapidă prin paste-with-mask pe RGBA, cu cache pentru straturile de filigran redimensionate și cu opacitate aplicată.

#### 5. Conexiuni

- [deltatech_watermark](../deltatech_watermark/index.md): modulul de bază care furnizează logica de filigranare a imaginilor, extinsă aici pentru magazinul online.
- `website_sale`: modulul eCommerce Odoo ale cărui imagini de produs sunt filigranate de acest modul.
