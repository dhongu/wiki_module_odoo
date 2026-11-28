# Romania - e-Factura for Store Sales (localizat la `l10n_ro_edi_ubl_sale_store/index.md`)

- **Nume Tehnic:** `l10n_ro_edi_ubl_sale_store`
- **Versiune:** `20.0.1.0.10`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_edi_ubl_sale_store
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_edi_ubl_sale_store`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul completează e-Factura din localizarea românească pentru vânzările făcute prin casa de marcat. Când pentru o vânzare s-a tipărit deja bon fiscal, factura electronică este marcată automat cu tipul `751`, astfel încât documentul transmis către ANAF să reflecte faptul că livrarea a fost însoțită de bon fiscal, iar vânzarea și TVA-ul să nu fie numărate de două ori.

#### 2. Funcționalități Cheie

- Setează tipul e-facturii la `751` atunci când pentru vânzare a fost tipărit un bon fiscal.
- În lista Apps Store modulul apare cu titlul „Romania - e-Factura for Store Sales" (anterior „Deltatech Sale from Store UBL"); numele tehnic nu s-a schimbat.

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, analiza detaliată a componentelor a fost omisă. Din manifest și cod rezultă doar extinderi ale modelelor `account.move` și `account.edi.xml.ubl_ro`.

**Modele**

- `account.move` (extins): determină dacă factura provine dintr-o vânzare cu bon fiscal.
- `account.edi.xml.ubl_ro` (extins): setează codul tipului de factură `751` în XML-ul e-Facturii.

**Vizualizări**

Niciuna definită de modul.

**Acțiuni Automate / Acțiuni Server**

Niciuna definită de modul.

#### 5. Conexiuni

- `l10n_ro_edi`: modulul de bază pentru e-Factura România, pe care acest modul îl extinde pentru a stabili tipul documentului electronic.
- `deltatech_sale_store`: modul de vânzare din magazin (referit comentat în manifest) ca sursă a contextului de bon fiscal.
- [l10n_ro_efactura_enhancement](../l10n_ro_efactura_enhancement/index.md): aplică aceeași regulă `751` pentru facturile din POS.
