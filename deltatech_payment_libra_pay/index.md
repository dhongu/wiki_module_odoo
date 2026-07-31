# LibraPay Acquirer (localizat la `deltatech_payment_libra_pay/index.md`)

- **Nume Tehnic:** `deltatech_payment_libra_pay`
- **Versiune:** `19.0.1.0.7`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_libra_pay`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_libra_pay`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul integrează Odoo cu LibraPay, gateway-ul de plată securizat oferit de Libra Internet Bank în România. Permite companiilor să accepte plăți online cu cardul (Visa, Mastercard) atât pentru comenzile din magazinul online (eCommerce), cât și pentru facturile din portalul clienților, oferind o experiență de plată fiabilă și adaptată pieței românești. Fluxul folosește redirecționarea către pagina de plată găzduită de bancă, astfel încât datele cardului nu ajung niciodată pe serverul Odoo, iar statusul comenzilor și facturilor este actualizat automat pe baza confirmării primite de la bancă.

#### 2. Funcționalități Cheie

- Acceptarea plăților cu cardul prin metoda „Pay with card (LibraPay)” în procesul de checkout din eCommerce.
- Plata facturilor deschise direct din portalul clientului, cu card de credit sau debit.
- Actualizarea automată a statusului comenzilor de vânzare și al facturilor pe baza feedback-ului în timp real de la Libra Internet Bank.
- Notificări asincrone (IPN — Instant Payment Notifications) pentru a garanta înregistrarea plății chiar dacă clientul închide browserul înainte de redirecționare.
- Flux de redirecționare securizat: datele cardului sunt introduse pe infrastructura sigură a băncii, asigurând conformitatea PCI.
- Moduri de Test (sandbox) și Live (producție), cu endpoint-uri separate.
- Integrare directă cu modulele standard Odoo `payment` și `website_sale`.
- Mesaje configurabile pentru diferitele rezultate ale plății (Done, Cancel, Pending).

#### 3. Dependențe

- `payment`
- `website_sale`

Dependențe Python externe: `phpserialize`.

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune nu este detaliată deoarece documentația se bazează pe `readme/DESCRIPTION.md`, care nu solicită explicit analiza componentelor tehnice (modele, vizualizări, acțiuni automate).

Pe scurt, din `__manifest__.py` reiese că modulul definește un nou furnizor de plată (`payment.provider`) și o metodă de plată dedicate LibraPay, plus controllere pentru gestionarea redirecționării de retur și a notificărilor IPN (`/payment/libra_pay/ipn`).

#### 5. Conexiuni

- `payment`: framework-ul standard Odoo de furnizori și tranzacții de plată, pe care se construiește acest acquirer.
- `website_sale`: magazinul online Odoo, unde LibraPay apare ca metodă de plată la checkout.
