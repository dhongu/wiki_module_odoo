# Picking Split (Împărțirea livrării)

- **Nume Tehnic:** `deltatech_picking_split`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_picking_split
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_split`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul permite operatorului din depozit să decidă manual ce cantități dintr-un transfer (livrare, recepție, transfer intern) pleacă acum și ce rămâne într-un transfer ulterior (backorder), în loc de comportamentul automat din Odoo. Astfel, o livrare se poate împărți controlat, produs cu produs, înainte de validare.

#### 2. Funcționalități Cheie

- Generarea manuală a unui backorder dintr-un transfer, printr-o acțiune disponibilă pe formularul transferului (meniul Acțiune), care deschide un wizard.
- Wizardul afișează pentru fiecare mișcare produsul, cererea (Demand) și cantitatea păstrată în transferul curent (Kept), preinițializată cu disponibilul prognozat.
- Linii cu cantitate păstrată 0 se mută integral în backorder; liniile cu cantitate parțială sunt împărțite, diferența ajungând într-o mișcare nouă din backorder.
- Se creează un transfer nou în stare ciornă, legat de original prin `backorder_id`, iar pe transferul original se postează un mesaj cu link către backorder. Dacă nicio cantitate nu e păstrată, nu se creează backorder.
- Validări la aplicare (din 19.0.1.0.2): cantitatea păstrată trebuie să fie între 0 și cererea curentă a mișcării, mișcarea trebuie să aparțină încă transferului, iar transferul nu poate fi finalizat sau anulat; la eroare nu se modifică nimic.
- Limitare cunoscută (PICKSPLIT-001, deschis): pentru mișcări cu o unitate de măsură diferită de cea de stoc, valoarea implicită a cantității păstrate nu este convertită; operatorul trebuie să o verifice manual.
- Acces pentru grupul Stoc / Utilizator (`stock.group_stock_user`).

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking.manual.backorder` (tranzitoriu): wizardul de împărțire; calculează liniile implicite din transferul activ, validează cantitățile (`_check_kept_quantities`) și creează backorder-ul (`do_create_backorder`).
- `stock.picking.manual.backorder.line` (tranzitoriu): o linie per mișcare de stoc, cu produs, cerere și cantitate păstrată; un onchange limitează cantitatea la cerere.

**Vizualizări**

- `view_manual_backorder_form`: formularul wizardului, cu listă editabilă (fără creare/ștergere de linii) și butoanele Apply / Cancel.
- `action_manual_backorder`: acțiune legată (binding) de `stock.picking`, vizibilă doar pe formular.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server; singura acțiune este cea de fereastră de mai sus.

#### 5. Conexiuni

- Nu există conexiuni funcționale verificate cu alte module care au pagină wiki.
