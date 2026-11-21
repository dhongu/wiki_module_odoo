# Validare Telefon pe Website (localizat la `deltatech_website_phone_validation/index.md`)

- **Nume Tehnic:** `deltatech_website_phone_validation`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_phone_validation
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_phone_validation`
- **Ultima Ingestie:** `2026-11-21`

#### 1. Sumar

Numerele de telefon introduse în checkout vin în multe formate, iar cele greșite se descoperă abia când cineva sună. Modulul verifică numărul în momentul în care clientul trimite adresa din magazinul online și îl rescrie în format internațional, în funcție de țara selectată. Astfel se reduc erorile de date, iar numerele colectate sunt corecte și utilizabile pentru comunicarea ulterioară cu clientul.

#### 2. Funcționalități Cheie

- **Spații eliminate:** spațiile de la începutul și sfârșitul numărului sunt șterse înainte de verificările standard.
- **Format internațional:** dacă verificările standard trec, numărul este citit pentru țara aleasă în adresă și rescris în format internațional, deci un număr local primește prefixul de țară.
- **Numere invalide:** un număr care nu poate fi citit pentru țara respectivă este marcat ca invalid, cu mesajul *The phone number is not valid:* urmat de motiv; adresa nu poate fi trimisă până la corectare.
- **Orice tip de adresă:** verificarea se aplică numărului de telefon al oricărei adrese trimise astfel, indiferent de tip.
- Modulul intervine doar asupra validării adresei din checkout-ul website-ului și doar asupra câmpului de telefon.

#### 3. Dependențe

- `website_sale`
- `phone_validation`

> Dependență externă Python: `phonenumbers` (trebuie instalată pe server).

#### 4. Componente Cheie

**Modele**

Modulul nu definește și nu extinde modele Odoo (nu există directorul `models/`).

**Vizualizări**

Modulul nu adaugă vizualizări proprii; intervine asupra fluxului existent de checkout din `website_sale`.

**Controllere**

- `WebsiteSalePhoneValidation` (extinde `website_sale.controllers.main.WebsiteSale`): suprascrie metoda `_validate_address_values` (fără parametrul `is_main_address`, pe care Odoo 19 nu îl mai transmite) pentru a curăța și valida numărul de telefon. Folosește `phone_validation.phone_format` cu `force_format="INTERNATIONAL"` și țara `res.country` aleasă, marcând câmpul `phone` ca invalid și adăugând un mesaj de eroare atunci când numărul nu poate fi formatat.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- `website_sale`: modulul intervine în fluxul de checkout al magazinului online definit de acesta.
- `phone_validation`: oferă instrumentul de formatare și validare a numerelor de telefon folosit de acest modul.
