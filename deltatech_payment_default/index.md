# Payment Default Method (localizat la `deltatech_payment_default/index.md`)

- **Nume Tehnic:** `deltatech_payment_default`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_payment_default
- **Cale Locală:** `odoo-addons/deltatech/deltatech_payment_default`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă în asistentul de înregistrare a plății (*Înregistrează plata* pe facturi) o bifă *Set as default*. Când este bifată, metoda de plată folosită (și deci jurnalul ei) se memorează pe partener și este propusă la plățile următoare, ceea ce scutește contabilul de alegerea repetată a jurnalului.

#### 2. Funcționalități Cheie

- Alegerea se salvează în câmpul standard *Payment Method* din tabul *Sales & Purchase* al partenerului: una pentru încasări (facturi client) și una pentru plăți (facturi furnizor), pe companie; nu se adaugă câmpuri noi.
- Valoarea se scrie pe partenerul comercial (compania), deci o folosesc toate contactele; facturile noi adresate unui contact preiau valoarea companiei dacă el nu are una.
- Facturile deja deschise primesc implicitul în asistent, atâta timp cât nu au o metodă proprie; o metodă setată explicit pe factură câștigă.
- Fiecare modificare este înregistrată în chatter-ul partenerului (cine, ce metodă, ce companie).
- Bifa apare doar pentru un singur partener și doar utilizatorilor cu dreptul *Contact Creation* și drept de editare pe facturi.
- Flux: *Pay* pe factură, alegi jurnalul și metoda, bifezi *Set as default*, *Create Payment*.

Pașii cu capturi sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.payment.register` (wizard extins): bifa *Set as default* și scrierea metodei pe partenerul comercial.
- `account.move` (extins): `_compute_preferred_payment_method_line_id` folosește implicitul companiei pentru contacte.

**Vizualizări**

- `view_account_payment_register_form`: adaugă bifa în asistentul de plată.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- Nu are legături cu alte module din wiki.
