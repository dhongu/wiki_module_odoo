# Interfață Keez (localizat la `deltatech_keez/index.md`)

- **Nume Tehnic:** `deltatech_keez`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_keez`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_keez`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul „Interfață Keez" este o extensie Odoo dezvoltată de Terrabit care generează fișiere Excel (XLS) pregătite pentru importul în platforma de contabilitate online Keez. Modulul funcționează ca o punte bazată pe export de fișiere (nu pe API în timp real) între operațiunile zilnice din Odoo și evidența contabilă ținută în Keez, eliminând introducerea manuală a datelor și reducând riscul de erori pentru companiile care își gestionează ERP-ul în Odoo, dar contabilitatea în Keez.

#### 2. Funcționalități Cheie

- Generare de fișiere XLS pentru import în platforma Keez, printr-un wizard de export cu interval de dată configurabil.
- Export separat, arhivat într-un fișier ZIP, pentru: furnizori, clienți, facturi de intrare (achiziții și bonuri fiscale de intrare), facturi de ieșire (vânzări) și note contabile.
- Coloane exportate conform formatului Keez: ID, Serie/Număr Document, Date, Tip Document, Categorie, TVA Încasare, Cont Debit/Credit, Valoare RON/Valută, Tip și Cotă TVA, cod și denumire partener/angajat, explicație, jurnal, status etc.
- Filtrare a exportului pe jurnale contabile specifice sau pe toate jurnalele.
- Tratarea specificului fiscal românesc: identificarea TVA la încasare și a taxării inverse prin poziții fiscale configurabile, precum și corectarea automată a sensului debit/credit pentru conturile de venituri/cheltuieli.

#### 3. Dependențe

- `account`
- `stock_account`
- `l10n_ro`

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune nu a fost detaliată prin analiza codului, întrucât fișierul `readme/DESCRIPTION.md` acoperă scopul și funcționalitățile modulului. Pe scurt, implementarea se realizează printr-un wizard tranzitoriu (`export.keez`, în `wizard/export_keez.py`) care colectează parametrii de export (interval de dată, jurnale, poziții fiscale pentru taxare inversă/TVA la încasare, gestiune), interoghează facturile și notele contabile din Odoo, le formatează conform specificațiilor Keez și generează o arhivă ZIP cu fișierele XLS rezultate. Meniul „Keez" și acțiunea de export sunt disponibile în Contabilitate, pentru utilizatorii din grupul de manager contabil.

#### 5. Conexiuni

- [deltatech_saga](../deltatech_saga/index.md): modul înrudit de export contabil din Odoo către un alt program de contabilitate românesc (SAGA), parte din aceeași familie de interfețe de export Terrabit.
- [deltatech_contwin](../deltatech_contwin/index.md): modul înrudit de export contabil din Odoo către ContWin, parte din aceeași familie de interfețe de export Terrabit.
