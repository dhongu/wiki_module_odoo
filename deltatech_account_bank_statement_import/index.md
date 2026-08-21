# Bank Statements Import Extension (localizat la `deltatech_account_bank_statement_import/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_bank_statement_import
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul extinde funcționalitatea de import al extraselor de cont bancar pentru a accepta fișiere XLSX, pe lângă formatele acceptate în mod standard. În plus, ajută la identificarea automată a partenerului asociat fiecărei tranzacții, reducând munca manuală de reconciliere și potrivire a încasărilor cu partenerii corecți.

#### 2. Funcționalități Cheie

- Import al extraselor de cont bancar din fișiere XLSX.
- Detectare automată a partenerului după numele partenerului (caută un partener cu nume corespunzător).
- Detectare automată a partenerului după referința comenzii de vânzare (caută o comandă de vânzare care corespunde referinței plății și asociază partenerul comercial al acelei comenzi).

#### 3. Dependențe

- `account_bank_statement_import_csv`

#### 4. Componente Cheie

Această secțiune nu este detaliată: documentația se bazează pe `readme/DESCRIPTION.md`, care nu solicită explicit analiza componentelor tehnice (modele, vizualizări, acțiuni automate).

#### 5. Conexiuni

Nu au fost identificate conexiuni suplimentare către alte module documentate în wiki, în afara dependenței directe de mai sus.
