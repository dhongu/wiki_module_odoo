# Romania - Asistent import e-Factura (verificare față de comandă) (localizat la `l10n_ro_efactura_import_assist/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_import_assist`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_efactura_import_assist
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_import_assist`
- **Ultima Ingestie:** `2026-09-12`

#### 1. Sumar

Modulul închide ultimul gol din fluxul FR-03 (e-Factura B2B bidirecțional prin SPV):
atunci când o factură de la furnizor este importată automat din SPV și e legată de o
comandă de achiziție, factura este confruntată linie cu linie cu comanda pe cantitate și
preț. Dacă apar diferențe peste toleranțele acceptate, postarea facturii este blocată
până când operatorul ia o decizie explicită — acceptă cu ajustare sau refuză total, caz
în care furnizorul este notificat automat prin e-mail cu tabelul diferențelor.

#### 2. Funcționalități Cheie

- Verificare automată la import a facturilor SPV legate de o comandă de achiziție:
  compară **cantitatea** (față de rămasul de facturat — recepționat sau comandat, în
  funcție de politica de facturare a produsului) și **prețul unitar** (față de linia din
  PO), cu **toleranțe procentuale configurabile pe companie**.
- Toleranțele se setează în **Setări → Contabilitate → SPV Import Assistant** (cantitate %
  și preț %; implicit 0, deci orice diferență e semnalată).
- La diferențe peste toleranțe, factura intră în starea **„Pending Decision"**: postarea
  (manuală sau automată) este blocată, apare un banner de avertizare pe factură și o
  activitate pentru operator; liniile cu probleme sunt listate în fila **„SPV
  Discrepancies"**.
- Wizard de decizie explicită, accesibil din butonul **Review Discrepancies**:
  - **Accept with adjustment** — deblochează postarea (pentru refuz parțial, se
    ajustează întâi liniile facturii, apoi se acceptă);
  - **Refuse** — factura se anulează, iar furnizorul poate primi opțional un e-mail cu
    tabelul diferențelor.
- Liniile facturate suplimentar, fără corespondent în comandă, sunt semnalate ca
  „Line not in PO".
- Verificare manuală re-rulabilă pe orice factură ciornă, cu acțiunea **Re-check
  Discrepancies** din fila SPV Discrepancies.

#### 3. Dependențe

- `l10n_ro_edi`
- `purchase`

#### 4. Componente Cheie

Nu au fost analizate separat — conform fluxului de ingestie, secțiunea a fost acoperită
integral de `readme/DESCRIPTION.md` și `readme/USAGE.md`.

#### 5. Conexiuni

- [l10n_ro_efactura_dedup](../l10n_ro_efactura_dedup/index.md): modul frate care acoperă
  deduplicarea facturilor SPV cu cheie extinsă (CUI + Serie/Nr + Dată + Valoare); acest
  modul se ocupă exclusiv de verificarea cantitate/preț și decizia de acceptare/refuz.
- `l10n_ro_edi`: asigură transportul SPV (trimitere, status, recipisă, import inbound) pe
  care se bazează acest modul.
