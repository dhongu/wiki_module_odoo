# Deltatech Payment (localizat la `deltatech_payment/index.md`)

- **Nume Tehnic:** `deltatech_payment`
- **Versiune:** `19.0.0.0.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul extinde stratul de plăți al Odoo cu două comportamente independente folosite în implementările Terrabit: confirmarea automată a unei comenzi de vânzare la o plată parțială și controlul asupra furnizorilor de plată oferiți pe link-urile de plată. Astfel, comercianții pot accepta avansuri fără să aștepte plata integrală și pot restricționa metodele de plată disponibile atunci când trimit un link de plată unui client, fără să afecteze fluxul normal de checkout din magazinul online.

#### 2. Funcționalități Cheie

- Confirmă comanda de vânzare aflată în starea „ciornă" sau „trimisă" imediat ce se primește o plată (chiar parțială), fără să aștepte suma integrală.
- Permite, prin parametrul de sistem `payment.do_not_set_transaction_done`, ca tranzacția de plată să rămână în afara stării „efectuată" (done) în timp ce comanda de vânzare este totuși confirmată la o plată pozitivă — util când decontarea reală a tranzacției este gestionată separat.
- Adaugă pe fiecare furnizor de plată o opțiune „Permis pe Linkuri de Plată" (în secțiunea Disponibilitate), activată implicit, astfel încât furnizorii existenți continuă să funcționeze neschimbat.
- Când se generează un link de plată pentru o comandă de vânzare, comanda este marcată ca restricționată; de atunci, plata online a acelei comenzi oferă doar furnizorii cu opțiunea activată, iar cei cu opțiunea dezactivată sunt ascunși.
- Restricția este aplicată din starea de încredere de pe server (comanda de vânzare, validată prin token de acces), nu dintr-un parametru de URL, deci un cumpărător nu o poate elimina editând link-ul. Checkout-ul standard de e-commerce nu este afectat, deoarece comenzile de coș nu sunt niciodată marcate.

#### 3. Dependențe

- `payment`
- `sale`

#### 4. Componente Cheie

**Modele**

- `payment.transaction` (extins): suprascrie `_check_amount_and_confirm_order` pentru a confirma comenzile de vânzare în starea `draft`/`sent` când suma plătită este pozitivă (exclude explicit furnizorul `on_delivery`, lăsat intenționat pentru confirmare manuală de către un operator, vezi [deltatech_payment_on_delivery](../deltatech_payment_on_delivery/index.md)); suprascrie `_set_transaction_done` pentru a respecta parametrul de sistem `payment.do_not_set_transaction_done`.
- `payment.provider` (extins): adaugă câmpul `allow_payment_link` (boolean, implicit `True`) și suprascrie `_get_compatible_providers` pentru a filtra furnizorii pe baza acestui câmp, atunci când comanda de vânzare asociată este marcată ca restricționată.
- `sale.order` (extins): adaugă câmpul `payment_link_provider_restricted` (boolean), setat automat la generarea unui link de plată pentru comandă.
- `payment.link.wizard` (extins, model tranzitoriu): suprascrie `default_get` pentru a marca automat comanda de vânzare (`payment_link_provider_restricted = True`) în momentul generării unui link de plată.

**Vizualizări**

- `payment_provider_form`: extinde formularul standard al furnizorului de plată (`payment.payment_provider_form`), adăugând câmpul `allow_payment_link` în secțiunea Disponibilitate.

**Configurare**

- `payment.do_not_set_transaction_done` (parametru de sistem): dacă este adevărat, tranzacțiile de plată nu mai sunt trecute în starea „done", dar comenzile de vânzare asociate sunt confirmate în continuare la o plată pozitivă. Se configurează din Setări > Tehnic > Parametri de Sistem.

#### 5. Conexiuni

- [deltatech_payment_on_delivery](../deltatech_payment_on_delivery/index.md): furnizorul „plată la livrare" (`on_delivery`) este exclus explicit din confirmarea automată la plată parțială, pentru a lăsa confirmarea comenzii pe seama unui operator.
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): gestionează formularele de livrare și plată din magazinul online, context tipic în care se aplică confirmarea comenzii la plată parțială și restricția furnizorilor pe linkuri de plată.
