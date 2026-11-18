# Product Chatter Protection (localizat la `deltatech_product_chatter/index.md`)

- **Nume Tehnic:** `deltatech_product_chatter`
- **Versiune:** `19.0.1.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_chatter
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_chatter`
- **Ultima Ingestie:** `2026-11-18`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul restricționează ștergerea, editarea și golirea mesajelor din chatter-ul produselor (șabloane de produs și variante), permițând aceste acțiuni doar utilizatorilor care fac parte dintr-un grup de securitate dedicat. Astfel se păstrează istoricul complet al comunicării și al modificărilor legate de produse, evitând ștergerea accidentală sau abuzivă a urmelor de audit.

#### 2. Funcționalități Cheie

- Blochează acțiunea de ștergere a mesajelor din chatter pentru produse (șablon și variantă), direct din interfața Odoo, inclusiv „ștergerea" prin golirea conținutului mesajului.
- Blochează ștergerile directe ale înregistrărilor `mail.message` legate de produse (ORM/RPC, scripturi, module terțe) pentru utilizatorii fără grup.
- Blochează editarea directă (ORM/RPC) a conținutului sau a atașamentelor mesajelor legate de produse pentru utilizatorii fără grup.
- Introduce grupul de securitate „Delete Product Chatter Messages", care trebuie acordat doar utilizatorilor de încredere: **Settings → Users & Companies → Users → Access Rights**.
- Fără grup, ștergerea/editarea unui mesaj dă eroare; cu grup, comportamentul este cel obișnuit.
- Restricția se aplică exclusiv mesajelor de pe `product.template` și `product.product`; celelalte modele nu sunt afectate, iar datele nu sunt modificate.

#### 3. Dependențe

- `product`
- `mail`

#### 4. Componente Cheie

**Modele**

- `product.template`: suprascrie `_check_can_update_message_content`, pentru a cere grupul de securitate înainte de a permite editarea/golirea conținutului mesajelor din chatter.
- `product.product`: aceeași restricție, pentru variantele de produs.
- `mail.message` (extindere): suprascrie `write()` și `unlink()` pentru a bloca editările și ștergerile directe ale mesajelor legate de produse, fără grup.

**Vizualizări**

- Modulul nu adaugă vizualizări; funcționează exclusiv la nivel de logică de acces pe chatter.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

**Securitate**

- `deltatech_product_chatter.group_delete_product_chatter` (grup „Delete Product Chatter Messages"): singurul grup ai cărui membri pot șterge sau edita mesaje din chatter-ul produselor; la instalare este acordat automat utilizatorilor `base.user_root` și `base.user_admin`.

#### 5. Conexiuni

- `mail`: modulul extinde mecanismul standard de chatter prin suprascrierea verificării de actualizare a conținutului mesajelor.
- `product`: restricția se aplică pe modelele de produs (`product.template`, `product.product`).
