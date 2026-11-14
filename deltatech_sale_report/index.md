# Sale Report Additional Info (localizat la `deltatech_sale_report/index.md`)

- **Nume Tehnic:** `deltatech_sale_report`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_report
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_report`
- **Ultima Ingestie:** `2026-11-14`

#### 1. Sumar

Agenții de vânzări care analizează vânzările pe clienți au uneori nevoie de adresa de email a clientului lângă cifre. Modulul adaugă această adresă în raportul de analiză a vânzărilor (`sale.report`), ca un câmp *Partner Email*, disponibil direct în analizele și pivotările standard, fără căutări suplimentare în fișele de contact.

#### 2. Funcționalități Cheie

- **Câmp nou în raport:** *Partner Email* (`partner_email`, text) este adăugat în modelul din spatele analizei de vânzări și citit în aceeași interogare ca restul coloanelor raportului.
- **Valoare curentă:** câmpul arată email-ul stocat în acel moment pe clientul comenzii; nu se copiază nimic pe comandă, deci un email modificat apare și pe comenzile vechi.
- **Filtrare și grupare:** email-ul face parte și din gruparea interogării, deci raportul poate fi filtrat sau grupat după el. Modulul nu adaugă coloană, filtru sau meniu — câmpul se alege manual, de exemplu într-un filtru sau o grupare personalizată.
- **Fără drepturi proprii:** modulul nu definește grupuri sau reguli de acces; cine poate deschide raportul poate citi și email-urile.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.report`: extins cu câmpul `partner_email`, populat prin suprascrierea `_select_additional_fields()` (`partner.email`) și inclus în agregare prin `_group_by_sale()`.

**Vizualizări**

Modulul nu adaugă vizualizări proprii (`data` este gol în manifest); câmpul poate fi expus manual în vizualizările existente bazate pe `sale.report`.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite.

#### 5. Conexiuni

- `sale`: modulul extinde direct raportul standard de vânzări din acest modul.
