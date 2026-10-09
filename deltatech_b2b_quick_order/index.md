# B2B Quick Order (localizat la `deltatech_b2b_quick_order/index.md`)

- **Nume Tehnic:** `deltatech_b2b_quick_order`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_b2b_quick_order
- **Cale Locală:** `odoo-addons/bitshop/deltatech_b2b_quick_order`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Comandă rapidă după codul produsului pentru clienții companie din portalul B2B. Cumpărătorul care știe codurile nu mai navighează prin magazin: lipește lista (un cod pe rând, opțional cu cantitatea), o verifică și adaugă totul în coș dintr-un singur clic, la prețul din lista de prețuri a clientului.

#### 2. Funcționalități Cheie

- Intrare în portal la **Contul meu ▸ Comandă rapidă** (`/b2b/quick`), vizibilă pentru clienții B2B activi (și pe pagina `/my`).
- Formate acceptate pe rând: `ABC-123 x 3`, `ABC-123, 3` sau doar `ABC-123` (cantitate 1).
- Căutarea codului: întâi potrivire exactă pe referința internă, apoi o singură potrivire parțială, apoi codul de bare. Un cod care se potrivește cu mai multe produse nu este ghicit: clientul primește candidații și introduce codul complet.
- Același cod scris de două ori își adună cantitățile.
- Fluxul: lipire coduri, **Verifică codurile**, corectarea cantităților în tabel (rândurile necitite sunt listate cu motivul), apoi **Adaugă în coș**.
- Prețul afișat este cel din lista de prețuri a clientului, pentru cantitatea comandată (fără discount suplimentar peste lista de prețuri).
- Ajung în coș doar produsele vândute pe website, chiar și cu formular falsificat.
- Un contact cu drept doar de vizualizare sau un cont suspendat poate verifica codurile, dar nu le poate adăuga în coș.
- Modul în stadiul Beta; provine din comanda rapidă din `agroamat_b2b`.

#### 3. Dependențe

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md)

#### 4. Componente Cheie

**Modele**

- `product.product` (extins): metoda `_b2b_parse_quick_order(text, domain)` interpretează textul lipit și întoarce produsele cu cantități și lista erorilor.

**Vizualizări**

- `b2b_quick_order`: pagina QWeb cu formularul de coduri, tabelul de verificare și butonul de adăugare în coș.
- `portal_my_home_quick_order`: intrarea în pagina `/my` a portalului (moștenește `portal.portal_my_home`).

**Controllere**

- `/b2b/quick` (afișare), `/b2b/quick/check` (POST, verificare coduri și prețuri), `/b2b/quick/add` (POST, adăugare în coș și redirecționare la `/shop/cart`); extind `B2BPortal` din `deltatech_b2b_portal`.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md): portalul B2B pe care se construiește; oferă verificarea contului activ, dreptul de comandă și adăugarea în coș.
- `website_sale`: coșul și domeniul produselor vândute pe website, folosite la adăugare (prin portalul B2B).
