# Protecție Chatter Produse (localizat la `deltatech_product_chatter/index.md`)

- **Nume Tehnic:** `deltatech_product_chatter`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_product_chatter
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_chatter`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul restricționează ștergerea (și golirea) mesajelor din chatter-ul produselor, șabloane și variante, doar utilizatorilor dintr-un grup de securitate dedicat. Astfel se păstrează istoricul comunicării și al modificărilor legate de produse.

#### 2. Funcționalități Cheie

- Blochează acțiunea **Delete** din chatter pentru `product.template` și `product.product`, inclusiv golirea conținutului mesajului.
- Blochează și ștergerile directe ale mesajelor `mail.message` legate de produse (ORM, RPC, scripturi, module terțe) pentru utilizatorii fără grup; ștergerile făcute de framework în sudo, de exemplu la ștergerea produsului, nu sunt blocate.
- Grupul **Delete Product Chatter Messages** (`deltatech_product_chatter.group_delete_product_chatter`), acordat implicit utilizatorilor `base.user_root` și `base.user_admin`; se atribuie din *Setări > Utilizatori și companii > Utilizatori*, fila **Access Rights**.
- Alte modele nu sunt afectate. Detaliile de utilizare sunt în fișa consultantului.

#### 3. Dependențe

- `product`
- `mail`

#### 4. Componente Cheie

**Modele**

- `product.template`: verificarea `_check_can_update_message_content` cere grupul de securitate.
- `product.product`: aceeași restricție pentru variante.
- `mail.message`: `unlink` suprascris, blochează ștergerea mesajelor de produs fără grup.

**Vizualizări**

- Nu sunt adăugate vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- `mail`: extinde mecanismul standard de chatter.
- `product`: se aplică pe modelele de produs.
