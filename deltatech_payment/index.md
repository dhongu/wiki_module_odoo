# Payment – Auto Confirm SO (localizat la `deltatech_payment/index.md`)

- **Nume Tehnic:** `deltatech_payment`
- **Versiune:** `19.0.0.0.12`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde stratul de plăți al Odoo cu două comportamente independente folosite în implementările Terrabit: confirmarea automată a unei comenzi de vânzare la o plată parțială și controlul asupra furnizorilor de plată oferiți pe link-urile de plată. Astfel, comercianții pot accepta avansuri fără să aștepte plata integrală și pot restricționa metodele de plată disponibile atunci când trimit un link de plată unui client, fără să afecteze fluxul normal de checkout din magazinul online.

#### 2. Funcționalități Cheie

- Confirmă comanda de vânzare aflată în starea „ciornă" sau „trimisă" imediat ce se primește o plată (chiar parțială), fără să aștepte suma integrală; clientul primește emailul de confirmare.
- Plățile prin furnizorul `on_delivery` (plată la livrare) nu confirmă comanda: nu s-au încasat bani online, deci cotația rămâne pentru confirmare manuală de către un operator.
- Permite, prin parametrul de sistem `payment.do_not_set_transaction_done` (Setări → Tehnic → Parametri de Sistem, modul developer), ca tranzacția de plată să rămână în afara stării „efectuată" (done) în timp ce comanda de vânzare este totuși confirmată la o plată pozitivă — util când decontarea reală a tranzacției este gestionată separat. Absent sau fals = comportamentul standard Odoo.
- Adaugă pe fiecare furnizor de plată o opțiune „Allowed on Payment Links" („Permis pe Linkuri de Plată"), în secțiunea Disponibilitate (Facturare → Configurare → Plăți online → Furnizori de plată). Este activată implicit la furnizorii online; furnizorii offline (transfer bancar, plată la livrare, `on_delivery`) sunt creați cu opțiunea dezactivată, fiindcă nu se încasează bani online. Valoarea implicită se aplică o singură dată (la instalare, pentru furnizorii existenți, și la crearea furnizorului), iar valoarea modificată manual se păstrează.
- Când se generează un link de plată pentru o comandă de vânzare (Acțiuni → Generate a Payment Link), comanda este marcată ca restricționată; de atunci, plata online a acelei comenzi oferă doar furnizorii cu opțiunea activată, iar cei cu opțiunea dezactivată sunt ascunși.
- Restricția este aplicată din starea de încredere de pe server (comanda de vânzare, validată prin token de acces), nu dintr-un parametru de URL, deci un cumpărător nu o poate elimina editând link-ul. Checkout-ul standard de e-commerce nu este afectat, deoarece comenzile de coș nu sunt niciodată marcate.
- Limitări: restricția este legată de comanda de vânzare, deci se aplică oriunde se plătește online acea comandă (link de plată și „Pay Now" din portal); linkurile de plată pentru facturi nu sunt acoperite; o metodă de plată dispare doar când toți furnizorii compatibili cu ea sunt filtrați.
- Pașii detaliați, cu capturi de ecran, sunt în [Fișa Consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `payment`
- `sale`

#### 4. Componente Cheie

**Modele**

- `payment.transaction` (extins): suprascrie `_check_amount_and_confirm_order` pentru a confirma comenzile de vânzare în starea `draft`/`sent` când suma plătită este pozitivă (exclude explicit furnizorul `on_delivery`, lăsat intenționat pentru confirmare manuală de către un operator, vezi [deltatech_payment_on_delivery](../deltatech_payment_on_delivery/index.md)); suprascrie `_set_done` (nu mai `_set_transaction_done`, apelat de Odoo 19 doar prin `_set_done`) pentru a respecta parametrul de sistem `payment.do_not_set_transaction_done`: când e adevărat, tranzacția își păstrează starea, dar comenzile sunt confirmate.
- `payment.provider` (extins): adaugă câmpul `allow_payment_link` (boolean, implicit `True`; `False` la creare pentru furnizorii offline `on_delivery`, `wire_transfer`, `cash_on_delivery`) și suprascrie `_get_compatible_providers` pentru a filtra furnizorii pe baza acestui câmp, atunci când comanda de vânzare asociată este marcată ca restricționată.
- `sale.order` (extins): adaugă câmpul `payment_link_provider_restricted` (boolean), setat automat la generarea unui link de plată pentru comandă.
- `payment.link.wizard` (extins, model tranzitoriu): suprascrie `default_get` pentru a marca automat comanda de vânzare (`payment_link_provider_restricted = True`) în momentul generării unui link de plată.

**Vizualizări**

- `payment_provider_form`: extinde formularul standard al furnizorului de plată (`payment.payment_provider_form`), adăugând câmpul `allow_payment_link` în secțiunea Disponibilitate.

**Configurare**

- `payment.do_not_set_transaction_done` (parametru de sistem): dacă este adevărat, tranzacțiile de plată nu mai sunt trecute în starea „done", dar comenzile de vânzare asociate sunt confirmate în continuare la o plată pozitivă.
- `post_init_hook`: la instalare dezactivează `allow_payment_link` pe furnizorii offline deja existenți.

#### 5. Conexiuni

- [deltatech_payment_on_delivery](../deltatech_payment_on_delivery/index.md): furnizorul „plată la livrare" (`on_delivery`) este exclus explicit din confirmarea automată la plată parțială, pentru a lăsa confirmarea comenzii pe seama unui operator.
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): gestionează formularele de livrare și plată din magazinul online, context tipic în care se aplică confirmarea comenzii la plată parțială și restricția furnizorilor pe linkuri de plată.
