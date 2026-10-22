# Sale Contact (localizat la `deltatech_sale_contact/index.md`)

- **Nume Tehnic:** `deltatech_sale_contact`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_contact
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_contact`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul limitează și ghidează modul în care sunt selectate contactele pe comenzile de vânzare și pe facturi. Pe comanda de vânzare clientul principal poate fi doar o companie/persoană de nivel superior (fără părinte), iar adresele de facturare și de livrare sunt restrânse la contactele copil ale acelui client, de tipul corespunzător. În plus, modulul permite marcarea unui contact ca adresă implicită (de facturare sau livrare) și semnalarea partenerilor care preferă facturi „verzi" (fără PDF descărcat implicit la trimitere). Scopul este reducerea erorilor de selecție a contactelor și automatizarea alegerii adreselor corecte.

#### 2. Funcționalități Cheie

- Limitarea clientului de pe comanda de vânzare la parteneri de nivel superior (fără părinte).
- Restrângerea adresei de facturare la contactele copil de tip „facturare" ale clientului selectat.
- Restrângerea adresei de livrare la contactele copil de tip „livrare" ale clientului selectat.
- Limitarea partenerului de pe factură (`account.move`) la parteneri de nivel superior.
- Marcarea unui contact drept adresă implicită de facturare sau livrare (`contact_default`), cu selecție automată la rezolvarea adreselor și unicitate per tip de adresă.
- Marcaj „Factură verde" (`print_green_invoice`) pe partener: la trimiterea facturii, metoda implicită „Descărcare" (`manual`) este înlocuită cu e-mail, deci PDF-ul nu se mai descarcă implicit; poate fi totuși bifat manual în wizard.

#### 3. Dependențe

- `sale`
- `contacts`
- [deltatech_contact](../deltatech_contact/index.md)
- `account`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): adaugă câmpurile `contact_default` (contact implicit pentru facturare/livrare) și `print_green_invoice` (factură verde). Suprascrie `address_get` pentru a returna contactul implicit și `write` pentru a păstra un singur contact implicit per tip.
- `sale.order` (extins): aplică domenii pe `partner_id`, `partner_invoice_id` și `partner_shipping_id` pentru a limita selecția la parteneri de nivel superior și la contactele copil potrivite.
- `account.move` (extins): aplică domeniu pe `partner_id` pentru a limita selecția la parteneri de nivel superior.
- `account.move.send` (extins, abstract): suprascrie `_get_default_sending_methods`: pentru un partener comercial cu `print_green_invoice`, metoda `manual` (descărcare) este înlocuită implicit cu `email`.

**Vizualizări**

- `view_partner_form`: extinde formularul de partener pentru a afișa `print_green_invoice` și, pe contactele copil, `contact_default` (vizibil doar pentru tip livrare/facturare).
- `view_partner_simple_form`: adaugă `contact_default` în formularul simplificat de partener.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- [deltatech_contact](../deltatech_contact/index.md): modul de bază pentru gestionarea contactelor, pe care se sprijină logica de limitare a selecției.
