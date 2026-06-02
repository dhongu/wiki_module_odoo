# Deltatech Cash Statement Extension (localizat la `deltatech_cash_statement/index.md`)

- **Nume Tehnic:** `deltatech_cash_statement`
- **Versiune:** `19.0.3.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_cash_statement
- **Cale Locală:** `odoo-addons/deltatech/deltatech_cash_statement`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Acest modul oferă o unealtă pentru actualizarea rapidă a soldurilor de casă din extrasele bancare (registrele de casă) din Odoo. Este util în special pentru responsabilii de contabilitate care trebuie să ajusteze soldurile inițiale ale extraselor de casă, pentru ca evidențele financiare să fie corecte. Modulul ajută la rezolvarea diferențelor apărute în registrele de casă, integrându-se direct în fluxul de lucru contabil standard.

#### 2. Funcționalități Cheie

- **Actualizare rapidă a soldului**: adaugă un asistent (wizard) dedicat pentru actualizarea soldului inițial al extraselor de casă selectate, printr-o interfață simplă.
- **Integrare în fluxul contabil**: se integrează fără fricțiuni cu modelul standard de extras bancar din Odoo și este accesibil direct din vizualizarea de tip listă a extraselor, prin meniul **Acțiune**.
- **Integritatea datelor**: conceput pentru profesioniștii din contabilitate, pentru a ajuta la rezolvarea diferențelor din registrele de casă.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, modulul pune la dispoziție un asistent (wizard) accesibil din meniul **Acțiune** al listei de extrase de casă. Pașii de utilizare:

1. Se navighează la **Contabilitate > Tablouri de bord** sau **Facturare > Tablouri de bord**.
2. Se deschide un jurnal de tip **Numerar (Cash)** și lista extraselor sale.
3. Se selectează unul sau mai multe extrase care trebuie actualizate.
4. Din meniul **Acțiune** se alege **Cash Update Balances**.
5. În asistentul afișat se introduce soldul inițial corect (**Balance Start**) și se apasă butonul **Aplică** pentru a actualiza extrasele selectate.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module documentate în wiki. Singura dependență este modulul standard `account`.
