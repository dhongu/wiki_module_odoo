# POS Online Payment Safeguards (localizat la `deltatech_pos_online_payment/index.md`)

- **Nume Tehnic:** `deltatech_pos_online_payment`
- **Versiune:** `19.0.0.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_pos_online_payment
- **Cale Locală:** `odoo-addons/bitshop/deltatech_pos_online_payment`
- **Ultima Ingestie:** `2026-11-18`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul nou în 19.0. Elimină posibilitatea ca un casier să marcheze manual, prin butonul **Force done**, o plată online din Punctul de Vânzare ca fiind încasată înainte ca furnizorul de plăți să o confirme. Fără această siguranță, butonul închide comanda și echilibrează sesiunea POS pe bani care nu au ajuns niciodată în cont, iar discrepanța apare abia la reconcilierea bancară.

#### 2. Funcționalități Cheie

- Ascunde butonul **Force done** pe liniile de plată care folosesc o metodă de plată online, păstrându-l disponibil pentru terminalele de plată fizice (starea `waiting` este comună plăților online și terminalelor).
- Blochează și acțiunea din spatele butonului, nu doar afișarea lui, astfel încât linia nu poate fi forțată nici dintr-un ecran rămas deschis de dinainte de instalare.
- Afișează casierului mesajul **Online payment cannot be forced**, care îl invită să reîncerce plata sau să schimbe metoda de plată.
- Funcționează independent de furnizor: se aplică oricărui provider folosit ca metodă de plată online în POS (inclusiv cele Terrabit: ING WebPay, EuPlatesc, Monri, Libra Pay, BT iPay, Revolut, mobilPay) și oricărui alt provider suportat de Odoo.
- Nu are setări proprii; se aplică imediat ce un punct de vânzare are o metodă de plată online. Pregătirea acesteia se face în **Point of Sale > Configuration > Payment Methods** (metodă cu **Online Payment** bifat; **Allowed Providers** gol = toți furnizorii publicați, toți în moneda punctului de vânzare) și în **Point of Sale > Configuration > Settings**, secțiunea **Payment** (Odoo permite o singură metodă online pe punct de vânzare).
- La casă, clientul plătește prin fereastra **Scan to pay** (cod QR, sumă, referința comenzii), iar comanda se finalizează doar după confirmarea furnizorului; linia afișează **Request sent**, fără buton **Force done**.
- Se instalează deliberat, nu automat, pentru ca butonul să nu dispară fără avertisment la clienții ai căror casieri îl folosesc pentru terminale fizice; recomandat înainte de prima plată online la casă.

#### 3. Dependențe

- `pos_online_payment`

#### 4. Componente Cheie

Modulul nu adaugă modele sau vizualizări de backend — este o suprascriere pur front-end (JS/OWL) a interfeței Punctului de Vânzare.

**Modele**

- Niciunul definit sau extins.

**Vizualizări**

- Niciuna la nivel de backend; interfața POS este ajustată prin asset-uri JS/XML încărcate în `point_of_sale._assets_pos`.

**Componente Frontend (POS/OWL)**

- `static/src/pos/online_payment_guard.esm.js`: ascunde/blochează acțiunea „Force done" pe liniile cu metodă de plată online.
- `static/src/pos/online_payment_guard.xml`: șablonul OWL asociat, folosit pentru mesajul explicativ către casier.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `pos_online_payment`: modulul standard Odoo peste care se aplică siguranța — furnizează metoda de plată online și starea `waiting` a liniei de plată vizate de acest modul.
- [deltatech_payment_revolut](../deltatech_payment_revolut/index.md): furnizor Terrabit utilizabil ca plată online în POS.
- [deltatech_payment_ing_webpay](../deltatech_payment_ing_webpay/index.md): furnizor Terrabit utilizabil ca plată online în POS.
- [deltatech_payment_eu_platesc](../deltatech_payment_eu_platesc/index.md): furnizor Terrabit utilizabil ca plată online în POS.
- [deltatech_payment_monri](../deltatech_payment_monri/index.md): furnizor Terrabit utilizabil ca plată online în POS.
- [deltatech_payment_libra_pay](../deltatech_payment_libra_pay/index.md): furnizor Terrabit utilizabil ca plată online în POS.
- [deltatech_payment_bt_ipay](../deltatech_payment_bt_ipay/index.md): furnizor Terrabit utilizabil ca plată online în POS.
- [deltatech_payment_mobilpay](../deltatech_payment_mobilpay/index.md): furnizor Terrabit utilizabil ca plată online în POS.
