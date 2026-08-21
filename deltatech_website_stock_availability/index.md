# eCommerce Stock Availability (localizat la `deltatech_website_stock_availability/index.md`)

- **Nume Tehnic:** `deltatech_website_stock_availability`
- **Versiune:** `19.0.1.0.9`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_stock_availability`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_stock_availability`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul permite afișarea stocului pe website sub un anumit prag, oferind clienților posibilitatea de a comanda un produs chiar dacă stocul disponibil nu este suficient. Pe lângă disponibilitate, modulul estimează și numărul de zile în care se va face livrarea, luând în calcul timpul de livrare definit pe produs, numărul de zile de siguranță și numărul de zile de livrare de la furnizor pentru produsele care nu se află pe stoc. Astfel, magazinul online comunică transparent atât cantitatea disponibilă, cât și termenul realist de livrare.

#### 2. Funcționalități Cheie

- Afișarea stocului pe website doar atunci când acesta scade sub un anumit prag configurabil.
- Posibilitatea de a comanda produse chiar dacă stocul curent nu este suficient.
- Calculul automat al numărului de zile estimate până la livrare.
- Estimarea termenului de livrare ține cont de timpul de livrare definit pe produs, de numărul de zile de siguranță și de timpul de livrare de la furnizor pentru produsele care nu sunt pe stoc.

#### 3. Dependențe

- `website`
- `website_sale_stock`
- `purchase`
- [deltatech_vendor_stock](../deltatech_vendor_stock/index.md)

#### 4. Componente Cheie

*Documentația pentru această secțiune este generată din `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului (modele, vizualizări, acțiuni) este omisă deoarece nu este menționată explicit în Readme.*

#### 5. Conexiuni

- [deltatech_vendor_stock](../deltatech_vendor_stock/index.md): furnizează informațiile despre stocul și timpul de livrare de la furnizor, folosite la estimarea termenului de livrare pentru produsele care nu sunt pe stoc.
