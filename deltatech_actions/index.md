# Deltatech Actions (localizat la `deltatech_actions/index.md`)

- **Nume Tehnic:** `deltatech_actions`
- **Versiune:** `19.0.0.0.9`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_actions
- **Cale Locală:** `odoo-addons/deltatech/deltatech_actions`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul Deltatech Actions este un set de instrumente de mentenanță și curățare pentru baza de date Odoo. Acesta oferă acțiuni programate (cron) și funcții de service care ajută la menținerea unei baze de date curate și ordonate: eliminarea atașamentelor duplicate, ștergerea PDF-urilor vechi de pe comenzile de vânzare sau crearea regulilor de reaprovizionare lipsă. Toate sarcinile sunt gândite să fie sigure: vin dezactivate implicit și rulează în mod „dry run” (fără modificări reale în baza de date) până când administratorul le activează conștient.

#### 2. Funcționalități Cheie

- Căutarea și ștergerea fișierelor XML ANAF duplicate (cron: „Delete duplicate xml attachments”).
- Crearea regulilor de reaprovizionare a stocului lipsă (cron: „Create missing reordering rules (0/0)”).
- Căutarea și ștergerea atașamentelor PDF vechi de pe comenzile de vânzare (cron: „Delete pdf sale order attachments”).
- Toate sarcinile cron sunt dezactivate implicit și rulează în mod „dry” (fără modificări în baza de date).
- Funcție de anulare a tuturor mișcărilor de stoc și contabile de pe o comandă de vânzare (`force_cancel_order_and_moves`). Aceasta trebuie apelată printr-o acțiune de server creată manual, din motive de securitate.

#### 3. Dependențe

- `account_edi`
- `sale`
- `product`
- `stock`

#### 4. Componente Cheie

**Acțiuni Automate / Acțiuni Server**

(Conform `readme/DESCRIPTION.md`, modulul este construit în jurul sarcinilor cron de mentenanță definite în `data/ir_cron_data.xml`. Toate sunt dezactivate implicit și rulează în mod „dry run”.)

- `Delete duplicate xml attachments`: caută și șterge fișierele XML ANAF duplicate.
- `Create missing reordering rules (0/0)`: creează regulile de reaprovizionare a stocului care lipsesc.
- `Delete pdf sale order attachments`: caută și șterge atașamentele PDF vechi ale comenzilor de vânzare.
- `force_cancel_order_and_moves`: funcție de service care anulează toate mișcările de stoc și contabile de pe o comandă de vânzare; din motive de securitate nu este expusă automat, ci trebuie legată manual de o acțiune de server (`ir.actions.server`).

#### 5. Conexiuni

Modulul nu are conexiuni funcționale documentate cu alte module care au pagină în acest wiki.
