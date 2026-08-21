# Deltatech Product Chatter (localizat la `deltatech_product_chatter/index.md`)

- **Nume Tehnic:** `deltatech_product_chatter`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_chatter
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_chatter`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul restricționează ștergerea (și golirea) mesajelor din chatter-ul produselor (șabloane de produs și variante), permițând această acțiune doar utilizatorilor care fac parte dintr-un grup de securitate dedicat. Astfel se păstrează istoricul complet al comunicării și modificărilor legate de produse, evitând ștergerea accidentală sau abuzivă a urmelor de audit.

#### 2. Funcționalități Cheie

- Blochează acțiunea de ștergere a mesajelor din chatter pentru produse (șablon și variantă), direct din interfața Odoo.
- Blochează și ștergerile/editările efectuate pe alte căi (ORM/RPC, scripturi, module terțe) asupra mesajelor `mail.message` legate de produse.
- Introduce grupul de securitate dedicat „Delete Product Chatter Messages”, care poate fi acordat doar utilizatorilor de încredere.
- Restricția se aplică exclusiv mesajelor de pe `product.template` și `product.product`; celelalte modele nu sunt afectate.

#### 3. Dependențe

- `product`
- `mail`

#### 4. Componente Cheie

**Modele**

- `product.template`: suprascrie `_check_can_update_message_content` pentru a impune verificarea grupului de securitate înainte de a permite editarea/golirea conținutului mesajelor din chatter.
- `product.product`: aplică aceeași restricție ca `product.template`, pentru variantele de produs.

**Vizualizări**

- Modulul nu adaugă vizualizări noi; funcționează exclusiv la nivel de logică de acces pe chatter.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`. Restricția este implementată prin suprascrierea metodei `_check_can_update_message_content` din modulul `mail`.

**Securitate**

- `deltatech_product_chatter.group_delete_product_chatter` (grup „Delete Product Chatter Messages”): singurul grup ai cărui membri pot șterge sau edita mesaje din chatter-ul produselor; la instalare este acordat automat utilizatorilor `base.user_root` și `base.user_admin`.

#### 5. Conexiuni

- `mail`: modulul extinde mecanismul standard de chatter (`mail.thread`) prin suprascrierea verificării de actualizare a conținutului mesajelor.
- `product`: restricția se aplică pe modelele de produs (`product.template`, `product.product`) furnizate de acest modul.
