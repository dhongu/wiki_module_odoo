# Limită de Credit pe Partener — Website (localizat la `terrabit_partner_credit_limit_website/index.md`)

- **Nume Tehnic:** `terrabit_partner_credit_limit_website`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_partner_credit_limit_website
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_credit_limit_website`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul extinde funcționalitatea de limită de credit pe partener către platforma de website/e-commerce a Odoo. Integrează gestiunea limitei de credit direct în experiența de cumpărare online, astfel încât politica de credit a companiei să fie aplicată consecvent atât pe canalele de vânzare tradiționale, cât și pe cele de comerț electronic.

#### 2. Funcționalități Cheie

- Aplică limitele de credit ale partenerului în timpul procesului de checkout pe website.
- Împiedică plasarea comenzilor pe website atunci când limita de credit a clientului ar fi depășită.
- Afișează mesaje de avertizare clienților atunci când se apropie de limita de credit sau o depășesc.
- Oferă opțiuni configurabile pentru tratarea situațiilor de depășire a limitei de credit în interfața website-ului.
- Se integrează fără probleme cu sistemul central de gestiune a limitei de credit (`terrabit_partner_credit_limit`).
- Menține o politică de credit consecventă pe toate canalele de vânzare.
- Oferă opțiuni de configurare pentru diferite abordări de notificare a clienților.
- Suportă checkout ca invitat (guest checkout), cu controale corespunzătoare ale limitei de credit.

Beneficii de afaceri: gestiune unitară a creditului pe toate canalele de vânzare, aplicare în timp real a limitei de credit pentru achizițiile online, reducerea riscului financiar din operațiunile de e-commerce, experiență de client îmbunătățită prin notificări transparente și prevenirea respingerilor neașteptate de comenzi prin informare proactivă.

#### 3. Dependențe

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md)
- `website_sale`
- `payment_custom`

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe fișierul `readme/DESCRIPTION.md`, care nu detaliază componentele tehnice individuale. Conform fluxului de ingestie, analiza codului pentru Modele, Vizualizări și Acțiuni Automate a fost omisă întrucât Readme-ul este prezent.

*Notă tehnică orientativă (neexhaustivă):* modulul extinde `payment.provider` (`_get_compatible_providers`) pentru a restricționa metodele de plată disponibile la checkout când limita de credit e depășită (parametrul de sistem `payment_provider_credit_limit.restrict_all_provider` controlează dacă se restricționează toți furnizorii sau doar cei incompatibili cu plata pe loc/transfer bancar), extinde `res.config.settings` cu setarea „Restrict All Providers”, și adaugă în șablonul `website_sale.payment` un bloc cu bara de progres a limitei de credit, soldul curent și eventualele facturi restante.

#### 5. Conexiuni

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md): modulul de bază (și dependență) care implementează logica de calcul și verificare a limitei de credit, extinsă aici pentru canalul website.
- `website_sale`: modulul standard de e-commerce ale cărui șabloane de checkout (`website_sale.payment`) și setări (`res.config.settings`) sunt extinse.
- `payment_custom`: furnizează modurile de plată personalizate (ex. transfer bancar) folosite în logica de restricționare a furnizorilor de plată.
