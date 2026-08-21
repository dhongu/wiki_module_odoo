# POS Online Payment Safeguards (localizat la `deltatech_pos_online_payment/index.md`)

- **Nume Tehnic:** `deltatech_pos_online_payment`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_pos_online_payment
- **Cale Locală:** `odoo-addons/bitshop/deltatech_pos_online_payment`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul elimină posibilitatea ca un casier să marcheze manual, prin butonul "Force done", o plată online din Punctul de Vânzare ca fiind încasată înainte ca furnizorul de plăți să o confirme efectiv. Fără această siguranță, folosirea butonului pe o linie de plată online închide comanda și echilibrează sesiunea POS pe bani care nu au ajuns niciodată în cont, iar discrepanța iese la iveală abia la reconcilierea bancară.

#### 2. Funcționalități Cheie

- Ascunde butonul **Force done** pe liniile de plată care folosesc o metodă de plată online, păstrându-l disponibil pentru terminalele de plată fizice.
- Blochează și acțiunea din spatele butonului (nu doar afișarea lui), astfel încât linia nu poate fi forțată nici printr-un ecran neactualizat, nici printr-un scurtătură de tastatură.
- Afișează casierului o explicație și îl direcționează să reîncerce plata sau să schimbe metoda de plată.
- Funcționează independent de furnizorul de plăți — se aplică oricărui provider folosit ca metodă de plată online în POS (inclusiv cele Terrabit: ING WebPay, EuPlătesc, Monri, Libra Pay, BT iPay, Revolut, mobilPay), precum și oricărui alt provider suportat de Odoo.

#### 3. Dependențe

- `pos_online_payment`

#### 4. Componente Cheie

Modulul nu adaugă modele sau vizualizări de backend — este o suprascriere pur front-end (JS/OWL) a interfeței Punctului de Vânzare.

**Modele**

- Niciunul definit sau extins.

**Vizualizări**

- Niciuna definită la nivel de vizualizări backend; interfața POS este ajustată prin asset-uri JS/XML încărcate în `point_of_sale._assets_pos`.

**Componente Frontend (POS/OWL)**

- `static/src/pos/online_payment_guard.esm.js`: suprascrie logica liniei de plată POS pentru a ascunde/bloca acțiunea "Force done" pe liniile cu metodă de plată online.
- `static/src/pos/online_payment_guard.xml`: șablonul OWL asociat, folosit pentru afișarea mesajului explicativ către casier.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `pos_online_payment`: modulul standard Odoo peste care se aplică siguranța — furnizează metoda de plată online și starea `waiting` a liniei de plată vizate de acest modul.
