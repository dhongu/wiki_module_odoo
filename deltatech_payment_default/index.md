# Metoda de plată implicită pe partener (localizat la `deltatech_payment_default/index.md`)

- **Nume Tehnic:** `deltatech_payment_default`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_payment_default
- **Cale Locală:** `odoo-addons/deltatech/deltatech_payment_default`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă în fereastra **Plătește** de pe facturi bifa **Setează ca implicit**. Când este bifată, metoda de plată aleasă (și implicit jurnalul ei) se reține pe partener și este propusă din nou la plățile următoare. Operatorul nu mai schimbă jurnalul la fiecare încasare sau plată, iar plata ajunge din prima în jurnalul corect (bancă sau casă).

#### 2. Funcționalități Cheie

- Reținerea alegerii în câmpurile standard **Metoda de plată** de pe partener (tab **Vânzări & Achiziții**): una pentru încasări (facturi client) și una pentru plăți (facturi furnizor), separat pe companie. Nu se adaugă câmpuri noi pe partener.
- Valoarea se scrie pe partenerul comercial (firma), deci o preiau toate persoanele de contact; facturile noi emise pe un contact primesc metoda firmei dacă contactul nu are una.
- Facturile deja deschise în momentul setării primesc propunerea în fereastră, dacă nu au o metodă de plată proprie; metoda aleasă explicit pe factură are prioritate.
- Fiecare modificare este consemnată în istoricul (chatter) partenerului: cine, ce metodă, pentru ce companie.
- Bifa apare doar pentru un singur partener și doar utilizatorilor cu drept de facturare și **Contact: Creare**.
- Fără efect contabil propriu: nota contabilă a plății rămâne cea standard.
- Valoarea reținută se poate verifica sau schimba manual pe fișa partenerului.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.payment.register` (extins, wizard): bifa **Setează ca implicit**, propunerea jurnalului și metodei din setarea partenerului, scrierea setării la crearea plății.
- `account.move` (extins): calculul metodei de plată preferate a facturii, cu preluarea implicită de la partenerul comercial.

**Vizualizări**

- `view_account_payment_register_form`: moștenește formularul standard al ferestrei de înregistrare plată și adaugă bifa.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `sale`: comanda de vânzare preia metoda de încasare a partenerului (modul standard, opțional).
