# Deltatech Invoice to Draft (localizat la `deltatech_invoice_to_draft/index.md`)

- **Nume Tehnic:** `deltatech_invoice_to_draft`
- **Versiune:** `19.0.2.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_to_draft`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_to_draft`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul **Deltatech Invoice to Draft** restricționează accesul la readucerea facturilor și notelor contabile în starea de ciornă, o operațiune sensibilă care poate afecta integritatea datelor contabile. Doar utilizatorii care fac parte dintr-un grup dedicat pot readuce documentele confirmate în starea de ciornă, ceea ce ajută companiile să păstreze un control riguros asupra modificărilor efectuate pe facturile deja emise sau contabilizate.

#### 2. Funcționalități Cheie

- Butonul „Resetare la ciornă" (Reset To Draft) de pe factură este vizibil doar pentru utilizatorii din grupul „Can reset account move to draft"
- Adaugă butonul „Anulează Înregistrarea" (Cancel Entry), care readuce factura în starea de ciornă și apoi o anulează direct

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe fișierul `readme/DESCRIPTION.md`, care nu detaliază componentele tehnice individuale. Conform fluxului de ingestie, analiza codului pentru modele, vizualizări și acțiuni automate a fost omisă, deoarece Readme-ul este prezent și nu solicită explicit această analiză.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale documentate către alte module cu pagină în wiki.
