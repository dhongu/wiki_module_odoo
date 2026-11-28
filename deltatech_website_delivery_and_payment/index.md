# Delivery and Payment (localizat la `deltatech_website_delivery_and_payment/index.md`)

- **Nume Tehnic:** `deltatech_website_delivery_and_payment`
- **Versiune:** `20.0.2.2.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_delivery_and_payment
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_delivery_and_payment`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul limitează metodele de livrare și furnizorii de plată oferiți în checkout-ul magazinului online, în funcție de metoda de livrare aleasă, de valoarea și greutatea comenzii și de etichetele clientului. Astfel clientul vede doar combinațiile valide (de exemplu ramburs doar cu curierul), iar comerciantul controlează fin experiența de cumpărare pentru anumite categorii de clienți.

#### 2. Funcționalități Cheie

- **Furnizori de plată în funcție de livrare:** o metodă de livrare poate lista furnizorii de plată permiși împreună cu ea; în pasul de plată clientul vede doar acești furnizori. Fără listă, sunt permiși toți.
- **Limită de valoare a furnizorului de plată:** peste totalul comenzii (taxe incluse) furnizorul nu mai este oferit; un total egal cu limita rămâne permis.
- **Limite de greutate la livrare:** metoda se oferă doar dacă greutatea estimată a coșului este între minim și maxim; o limită goală sau 0 nu se verifică.
- **Restricții după etichetele clientului:** o metodă de livrare sau un furnizor de plată poate fi ascuns clienților cu o anumită etichetă. La livrare se citesc etichetele firmei clientului (partenerul comercial); la plată, etichetele clientului și ale firmei sale. Pentru furnizori, restricția se aplică la checkout, la plata unei facturi din portal și la linkul de plată.
- **Verificare la plată:** furnizorul este verificat din nou la crearea tranzacției, deci unul nepermis este refuzat, inclusiv în express checkout; acesta ascunde metodele de livrare ai căror furnizori permiși nu au express checkout.
- **Furnizor de plată preferat:** câmpul *Payment Provider* de pe firma clientului preselectează metoda de plată a acestuia în pasul de plată, dacă furnizorul este permis pentru comandă.
- **Logo la metoda de livrare:** imaginea *Logo* apare înaintea numelui metodei în checkout.
- **Unde se configurează:** **Website > Configuration > eCommerce > Delivery Methods** (limite de greutate, fila *Payment Acquirer*, *Logo*), **Payment Providers** (fila *Restrictions*: *Value Limit* și etichete) și, pe contact, fila *Sales & Purchase*.
- **Reguli standard care rămân:** ramburs doar la metodele cu opțiunea standard *Cash on Delivery*; *Maximum Amount* și *Max Weight* standard se aplică în plus. Dacă regulile nu lasă nicio opțiune, magazinul afișează mesajul standard de lipsă livrare/plată, deci se păstrează o metodă fără restricții ca rezervă. Pasul-cu-pas cu capturi este în fișa consultant.

#### 3. Dependențe

- `website_sale_stock`

#### 4. Componente Cheie

**Modele**

- `delivery.carrier`: extins cu furnizorii de plată permiși (`acquirer_allowed_ids`), limitele de greutate (`weight_min`, `weight_max`), `logo` și etichetele de restricție.
- `payment.provider`: extins cu `value_limit` și etichetele de restricție; filtrează furnizorii disponibili după comandă (`_filter_allowed_for_order`, `_find_available_providers`).
- `res.partner`: câmpul `provider_id` (furnizorul de plată preferat).
- `sale.order`: `_get_delivery_methods` filtrează metodele după greutate, etichete și furnizori.

**Vizualizări**

- `view_delivery_carrier_form`: limite de greutate, fila *Payment Acquirer*, logo.
- `payment_provider_form`: limita de valoare și etichetele de restricție.
- `view_partner_form`: furnizorul de plată preferat.
- `payment_form_preferred_method` și `delivery_method_logo`: șabloane website pentru preselecția metodei de plată și logoul livrării.

**Controllere**

- `DeliveryPaymentPortal`: refuză la plată un furnizor nepermis pentru comandă.
- `DeliveryRestrictedPayment`: ascunde în express checkout livrările fără furnizori cu express checkout.
- `WebsiteSaleDeliveryPayment`: transmite metoda de plată preferată în pasul de plată.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite.

#### 5. Conexiuni

Nu au fost identificate conexiuni cu alte pagini wiki existente, verificate în manifest sau cod.
