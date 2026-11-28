# eCommerce Store Selector - Click & Collect

- **Nume Tehnic:** `deltatech_website_store_selector_collect`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_website_store_selector_collect
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_store_selector_collect`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul de legătură între [eCommerce Store Selector](../deltatech_website_store_selector/index.md) și *Click & Collect* (`website_sale_collect`). Se instalează automat când sunt instalate ambele și face ca magazinul ales pe site să fie magazinul de ridicare propus la finalizarea comenzii.

#### 2. Funcționalități Cheie

- Magazinul ales pe site este magazinul de ridicare propus la checkout pentru metoda *Pick up in store*, chiar dacă metoda deservește mai multe magazine.
- Alegerea altui magazin de ridicare la checkout devine magazinul vizitatorului (antetul, stocul și depozitul comenzii îl urmează).
- Schimbarea magazinului din antet mută ridicarea comenzii „în magazin” la noul magazin sau o șterge dacă metoda de ridicare nu deservește magazinul respectiv.
- Stocul afișat și verificat este cel al magazinului ales, nu cel mai bun stoc dintre magazinele de ridicare; astfel se evită și calculul stocului tuturor magazinelor pe paginile de produs.
- Listarea magazinelor de ridicare (harta de la checkout) nu mai lasă pe liniile coșului avertizările magazinelor fără stoc: decide doar magazinul ales.
- Pagina produsului afișează blocul de magazin al selectorului în locul blocului Click & Collect, care ignoră magazinul vizitatorului.

#### 3. Dependențe

- [deltatech_website_store_selector](../deltatech_website_store_selector/index.md)
- `website_sale_collect`

#### 4. Componente Cheie

**Modele**

- Extensii ale modelelor din Click & Collect (`website`, `sale.order`, `delivery.carrier`) care folosesc magazinul ales; fără modele noi. Modulul este `auto_install`.

**Vizualizări**

- Nu are vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `website_sale_collect`: sursa metodei de livrare *Pick up in store*.
