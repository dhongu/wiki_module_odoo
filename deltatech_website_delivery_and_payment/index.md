# Delivery and Payment (localizat la `deltatech_website_delivery_and_payment/index.md`)

- **Nume Tehnic:** `deltatech_website_delivery_and_payment`
- **Versiune:** `19.0.2.1.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_delivery_and_payment
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_delivery_and_payment`
- **Ultima Ingestie:** `2026-11-04`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul limitează metodele de livrare și furnizorii de plată oferiți în finalizarea comenzii din magazinul online (eCommerce), în funcție de metoda de livrare aleasă, valoarea și greutatea comenzii și etichetele clientului. Clientul vede doar combinațiile valide, iar magazinul controlează fin experiența de cumpărare pentru anumite categorii de clienți.

#### 2. Funcționalități Cheie

- **Furnizori de plată în funcție de metoda de livrare**: o metodă de livrare poate lista furnizorii de plată permiși cu ea (de exemplu ramburs doar cu curierul). La pasul de plată clientul vede doar acești furnizori; o metodă fără listă îi permite pe toți.
- **Limită de valoare pentru furnizorul de plată**: peste acest total al comenzii (taxe incluse) furnizorul nu mai este oferit; un total egal cu limita încă e permis. Limita se compară cu totalul în moneda comenzii, fără conversie.
- **Limite de greutate pentru metoda de livrare**: metoda e oferită doar când greutatea estimată a coșului (greutatea produsului × cantitatea, doar bunuri) e între minim și maxim. O limită goală sau 0 nu se verifică (50 - 0 înseamnă „de la 50 kg în sus").
- **Restricții după etichetele clientului**: o metodă de livrare sau un furnizor de plată pot fi ascunse clienților care au una dintre etichetele lor. Pentru metodele de livrare se citesc etichetele companiei clientului (partenerul comercial); pentru furnizorii de plată, etichetele clientului din comandă. Pentru o persoană de contact, o etichetă setată doar pe companie ascunde metoda de livrare, dar nu și furnizorul de plată: eticheta se setează pe ambele când trebuie ascunse amândouă.
- **Unde se configurează**:
    - **Website → Configurare → eCommerce → Metode de livrare**, pe metoda de livrare: *Weight limits* lângă preț; fila *Payment Acquirer*: *Payments Provider Allowed* și *Restrict for partners with label*.
    - **Website → Configurare → eCommerce → Furnizori de plată**, pe furnizor, grupul *Restrictions*: *Value Limit* și *Restrict Label*.
    - Clienții se etichetează la **Website → eCommerce → Clienți**, câmpul **Tags**.
- **Reguli standard care se aplică în continuare**: ramburs doar la metodele de livrare cu opțiunea standard *Cash on Delivery* și, dacă lista e completată, doar dacă e în *Payments Provider Allowed*; se aplică și *Maximum Amount* al furnizorului și *Max Weight* al metodei de livrare. Regulile doar ascund opțiuni, nu adaugă furnizori sau metode nepublicate.
- Dacă regulile nu lasă nicio metodă de livrare, magazinul afișează „Sorry, we are unable to ship your order."; dacă nu lasă niciun furnizor, pasul de plată arată *No payment method available*. Se păstrează o metodă de livrare și un furnizor fără restricții ca rezervă.
- Modulul mai adaugă un *Logo* pe formularul metodei de livrare și un câmp *Payment Provider* pe fila *Sales & Purchase* a contactului; sunt păstrate pentru alte module și rapoarte și nu sunt folosite în finalizarea comenzii.

#### 3. Dependențe

- `website_sale_stock`

#### 4. Componente Cheie

Funcționalitățile provin din `readme/DESCRIPTION.md`, completat din `readme/USAGE.md`; mai jos sunt reperele confirmate în cod.

**Modele**

- `delivery.carrier` (extins): `acquirer_allowed_ids`, `weight_min`, `weight_max`, `logo`, `restrict_label_ids` și `is_restricted(partner_id)`.
- `payment.provider` (extins): `value_limit`, `restrict_label_ids`, `is_restricted(partner_id)` și filtrarea în `_get_compatible_providers`.
- `sale.order` (extins): `_get_delivery_methods` și `_check_carrier_quotation`, care aplică restricțiile asupra metodelor de livrare.
- `res.partner` (extins): câmpul `provider_id` (*Payment Provider*), nefolosit în finalizarea comenzii.

**Vizualizări**

- `view_delivery_carrier_form`: moștenește formularul metodei de livrare (limite de greutate, logo, fila *Payment Acquirer*).
- `payment_provider_form`: moștenește formularul furnizorului de plată (grupul *Restrictions*).
- `view_partner_form`: adaugă câmpul *Payment Provider* pe contact.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `website_sale_stock`: baza magazinului online peste care se aplică restricțiile (singura legătură funcțională verificată; nu are pagină wiki).
