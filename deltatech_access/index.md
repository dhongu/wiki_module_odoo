# Access Field Control (localizat la `deltatech_access/index.md`)

- **Nume Tehnic:** `deltatech_access`
- **Versiune:** `19.0.0.0.11`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_access
- **Cale Locală:** `odoo-addons/bitshop/deltatech_access`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul **Access Field Control** permite administratorilor să restrângă ce pot vedea sau modifica anumite grupuri de utilizatori pe produse, fără formulare personalizate și fără cod. Pentru fiecare regulă se alege câmpul, grupul și restricția dorită, iar regulile se definesc direct pe vizualizarea produsului. Astfel, de exemplu, un agent de vânzări poate vedea prețul de vânzare doar în citire, fără costul produsului, iar referința poate deveni obligatorie.

#### 2. Funcționalități Cheie

- **Reguli pe grupuri de utilizatori**: un câmp poate fi marcat pentru un grup ca `readonly` (se vede, dar nu se modifică), `required` (trebuie completat) sau `invisible` (ascuns). O regulă fără grup se aplică tuturor utilizatorilor, inclusiv administratorului. Regulile se aplică și utilizatorilor care au grupul prin alt grup (grupuri implicate).
- **Reguli pe vizualizare**: regulile se definesc în fila **Access Field** a vizualizării, din **Settings > Technical > User Interface > Views** (în modul dezvoltator); nu există un meniu separat. La o linie nouă se aleg **Group** și **Field** (**Field Name** se completează automat), apoi **Readonly**, **Required** sau **Invisible**.
- **Container și XPath**: în **Field Name** se poate introduce și numele sau id-ul unui grup, bloc sau pagină din formular (cu **Field** gol și **Invisible** bifat, elementul se ascunde) sau o expresie XPath (orice text care conține `//`).
- **Domeniu de aplicare**: regulile se aplică formularelor și listelor de produs (`product.template` și `product.product`); regulile salvate pe alte modele nu au efect încă.
- **Alegerea vizualizării**: dacă un meniu deschide produsul fără o vizualizare anume, se aplică regulile tuturor vizualizărilor de produs; dacă o numește, se aplică doar regulile salvate pe ea. Listele de produse din **Invoicing > Customers > Products** / **Sales > Products > Products** și din **Invoicing > Vendors > Products** își numesc vizualizarea, deci pentru a ascunde **Cost** și acolo se adaugă aceeași regulă pe ambele liste.
- **Limitări**: sunt restricții de interfață, nu drepturi de acces (câmpurile pot fi modificate prin import sau API); după schimbarea unei reguli, utilizatorul restricționat reîncarcă pagina (F5); orice utilizator intern poate modifica regulile (drepturile pe model sunt acordate grupului Internal User).

#### 3. Dependențe

- `base`
- `product`

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe fișierul `readme/DESCRIPTION.md`, care nu cere explicit detalierea componentelor tehnice. Conform fluxului de ingestie, analiza codului pentru modele, vizualizări și acțiuni automate a fost omisă.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină în wiki.
