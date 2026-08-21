# Validare Telefon pe Website (localizat la `deltatech_website_phone_validation/index.md`)

- **Nume Tehnic:** `deltatech_website_phone_validation`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_phone_validation`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_phone_validation`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul adaugă validarea numerelor de telefon introduse de clienți în formularele de adresă din magazinul online (checkout). Atunci când un client completează datele de livrare sau facturare pe website, numărul de telefon este verificat și normalizat automat în format internațional, în funcție de țara selectată. Astfel se reduc erorile de date și se asigură că numerele colectate sunt corecte și utilizabile pentru comunicarea ulterioară cu clientul.

#### 2. Funcționalități Cheie

- Validarea numărului de telefon direct în frontend, în pasul de completare a adresei din magazinul online.
- Normalizarea automată a numărului de telefon în format internațional, pe baza țării alese de client.
- Afișarea unui mesaj de eroare clar atunci când numărul de telefon nu este valid, blocând continuarea comenzii până la corectare.
- Curățarea automată a spațiilor din numărul introdus înainte de validare.

#### 3. Dependențe

- `website_sale`
- `phone_validation`

> Dependență externă Python: `phonenumbers`.

#### 4. Componente Cheie

**Modele**

Modulul nu definește și nu extinde modele Odoo (nu există directorul `models/`).

**Vizualizări**

Modulul nu adaugă vizualizări proprii; intervine asupra fluxului existent de checkout din `website_sale`.

**Controllere**

- `WebsiteSalePhoneValidation` (extinde `website_sale.controllers.main.WebsiteSale`): suprascrie metoda `_validate_address_values` pentru a curăța și valida numărul de telefon introdus în formularul de adresă. Folosește instrumentul `phone_validation.phone_format` cu `force_format="INTERNATIONAL"` și codul/țara `res.country` aleasă, marcând câmpul `phone` ca invalid și adăugând un mesaj de eroare atunci când numărul nu poate fi formatat.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- `website_sale`: modulul intervine în fluxul de checkout al magazinului online definit de acesta.
- `phone_validation`: oferă instrumentul de formatare și validare a numerelor de telefon folosit de acest modul.
