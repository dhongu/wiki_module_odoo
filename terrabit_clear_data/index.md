# Terrabit Clear Data (localizat la `terrabit_clear_data/index.md`)

- **Nume Tehnic:** `terrabit_clear_data`
- **Versiune:** `19.0.1.0.11`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_clear_data
- **Cale Locală:** `odoo-addons/terrabit/terrabit_clear_data`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Instrument pentru administratori, destinat curățării datelor tranzacționale dintr-o bază de date Odoo (documente de stoc, vânzări, achiziții, facturi, producție, proiecte, mailuri), cu opțiunea de a șterge și datele de bază (produse, parteneri, liste de materiale). Este util la pregătirea unei baze de date pentru producție după testare sau la golirea unei baze de demonstrație, putând lucra pentru o singură companie sau pentru toate. Operațiunea este ireversibilă și se face direct în baza de date, de aceea se folosește doar pe medii de test sau după o copie de siguranță. Modulul este în stadiul Beta.

#### 2. Funcționalități Cheie

- Wizard accesibil din meniul **Clear Data** (în meniul de setări tehnice, sub `base.next_id_6`), vizibil doar grupului Administrare sistem (`base.group_system`).
- Confirmare explicită: ștergerea pornește doar dacă este bifat „Sunt sigur că vreau să șterg datele!”.
- Filtrare pe companie: câmpul Company (implicit compania curentă) limitează ștergerea la compania aleasă; fără companie se șterge global.
- Documente (bifate implicit): stoc, vânzări, achiziții, facturi, documente contabile (extrase, note contabile, rapoarte), proiecte, comenzi de producție.
- Date de bază (nebifate implicit): ștergere LDM, toate produsele, produse finite, semifabricate, parteneri.
- Ștergere mailuri (mesaje, urmăritori, atașamente orfane), cu ștergere în loturi pentru tabele mari.
- Curățare condiționată de modulele instalate: costuri de achiziție (landed costs), joburi de coadă, consumuri și comenzi de service, inventare, pontaje, deconturi de cheltuieli, tichete helpdesk, KDS, valorizare stoc și altele.
- Ștergerea produselor respectă compania aleasă: produsele partajate (fără companie) se șterg doar dacă nu e aleasă nicio companie sau dacă aceasta e singura din bază.
- Ștergerea unei companii curăță în prealabil depozitele, regulile de stoc, site-urile web și conturile asociate.
- Avertisment: există bug-uri deschise (`readme/bugs.md`), printre care SQL invalid la ștergerea partenerilor / produselor finite fără companie selectată, commit-uri intermediare care lasă ștergeri parțiale la eroare și incompatibilități în `res.company.unlink` pe Odoo 19.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `ir.data.clear`: model tranzitoriu (wizard) cu opțiunile de ștergere; `do_clear()` orchestrează pașii (`del_stock_step1`, `del_mrp`, `del_bom`, `del_sale`, `del_invoice`, `del_account_extrase`, `del_purchase`, `del_all_products`, `del_service_consumption`, `del_expenses_deduction`) și rulează SQL direct.
- `res.company` (extins): `unlink()` șterge înainte depozitele, regulile de stoc, site-urile web și conturile companiei, apoi mută utilizatorii pe compania curentă.

**Vizualizări**

- `view_clear_data_form`: formularul wizardului, cu grupurile Confirmare, Date de Bază, Documente, Mails și Date Demo, și butonul „Sterge datele”.
- `action_clear_data` / `menu_clear_data`: acțiunea fereastră modală și intrarea de meniu.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni automate sau cron-uri.

#### 5. Conexiuni

- [deltatech_service_agreement](../deltatech_service_agreement/index.md): consumurile de service (`service_consumption`) sunt șterse la curățarea facturilor, dacă modulul este instalat.
- [deltatech_expenses](../deltatech_expenses/index.md): deconturile de cheltuieli sunt șterse la curățarea facturilor, dacă modulul este instalat.
- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): datele de valorizare a stocului sunt curățate dacă modulul este instalat.
- `stock`, `mrp`, `sale`, `purchase`, `account`, `project`, `helpdesk`, `queue_job`: modulele ale căror date tranzacționale sunt curățate când sunt instalate.
