# Access Field Control (localizat la `deltatech_access/index.md`)

- **Nume Tehnic:** `deltatech_access`
- **Versiune:** `20.0.0.0.10`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_access`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_access`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul **Access Field Control** permite administratorilor să restricționeze, fără cod, ce pot vedea sau modifica anumite grupuri de utilizatori pe fișele de produs. Pentru fiecare regulă se alege câmpul, grupul și restricția (doar citire, obligatoriu sau invizibil), iar regulile se aplică pe formularele și listele produselor (șabloane de produs și variante). Astfel, câmpuri sensibile precum prețul de vânzare sau costul pot fi protejate fără vederi personalizate.

#### 2. Funcționalități Cheie

- Reguli pe câmp și pe grup de utilizatori: **Readonly** (câmpul se vede, dar nu se poate modifica), **Required** (grupul trebuie să îl completeze) sau **Invisible** (câmpul este ascuns).
- Regulile se salvează pe o vedere anume, în fila **Access Field** a formularului vederii (**Setări > Tehnic > Interfață utilizator > Vederi**, cu modul dezvoltator activ).
- O regulă fără grup se aplică tuturor utilizatorilor, inclusiv administratorului.
- În **Field Name** se poate introduce și numele sau id-ul unui grup, bloc sau pagină din formular (cu **Field** gol și **Invisible** bifat, elementul se ascunde) ori o expresie XPath (orice text care conține `//`).
- Se aplică doar pe vederile `product.template` și `product.product`; regulile salvate pe alte modele nu au efect.
- Sunt restricții de interfață, nu drepturi de acces: câmpurile pot fi modificate în continuare prin import sau API.
- Dacă un meniu deschide produsul fără vedere anume, se aplică regulile tuturor vederilor de produs; dacă numește o vedere, se aplică doar regulile acesteia. Pentru a ascunde **Cost** și în listele de produse, regula se adaugă pe ambele vederi listă.
- După modificarea unei reguli, utilizatorul restricționat trebuie să reîncarce pagina (F5).
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`
- `product`

#### 4. Componente Cheie

**Modele**

- `access.field` (nou): o regulă de acces, cu vederea (`view_id`), grupul (`group_id`), câmpul (`field_id` / `name`) și indicatorii `readonly`, `required`, `invisible`.
- `access.mixin` (abstract): logica de aplicare a regulilor, moștenită de `product.template` și `product.product`.
- `ir.ui.view` (extins): adaugă legătura către regulile de acces ale vederii.
- `product.template`, `product.product` (extinse): aplică regulile pe vederile produselor.

**Vizualizări**

- `view_view_form`: adaugă fila **Access Field** pe formularul vederii (`ir.ui.view`).
- `view_access_field_form` / `view_access_field_list`: formularul și lista unei reguli de acces.

**Acțiuni Automate / Acțiuni Server**

- `action_access_field`: acțiune de fereastră pentru regulile de acces (fără meniu). Modulul nu definește sarcini `ir.cron` sau reguli `base.automation`.

#### 5. Conexiuni

Nu au fost identificate legături funcționale către alte module cu pagină în wiki.
