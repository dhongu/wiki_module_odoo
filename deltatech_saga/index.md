# Interfață SAGA

- **Nume Tehnic:** `deltatech_saga`
- **Versiune:** `19.0.6.6.10`
- **Cale:** `https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_saga`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_saga`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Interfața Deltatech SAGA este un modul cuprinzător conceput pentru a facilita schimbul de date între Odoo și SAGA, un program de contabilitate larg răspândit în România. Această punte de integrare asigură transferul fără probleme al datelor contabile și de stoc între cele două sisteme, eliminând necesitatea introducerii manuale a datelor și reducând riscul de erori. Modulul se adresează companiilor care își gestionează operațiunile în Odoo, dar își păstrează evidența contabilă în SAGA, și este adaptat specific cerințelor fiscale și contabile din România. Integrarea este bazată pe fișiere (export/import), nu pe sincronizare în timp real prin API.

#### 2. Funcționalități Cheie

- Export de date contabile din Odoo către SAGA (clienți și furnizori, facturi de achiziție, facturi de vânzare inclusiv în valută, note contabile).
- Import de date din SAGA în Odoo (clienți și furnizori, facturi de achiziție, facturi de vânzare, note contabile).
- Export/import de parteneri și contacte, cu două câmpuri de referință pentru codurile de Client și de Furnizor din SAGA pe partener.
- Export/import de produse și stocuri; categoriile de produse au un câmp nou pentru tipul de articol SAGA.
- Suport pentru cerințele fiscale și contabile românești, inclusiv tratamente speciale (TVA la încasare, deductibilitate limitată 50%).
- Maparea configurabilă a pozițiilor fiscale și corelarea codurilor de taxe; taxele au un câmp pentru tipul de deducere SAGA (indexul „N50" pentru deductibilitate limitată 50%, „I" pentru nedeductibilitate totală).
- Suport pentru ambele formate de schimb de date: XML (recomandat) și DBF.
- Generarea automată a codurilor SAGA pentru parteneri folosind secvențe sau codul de TVA.
- Câmp pe factură pentru a indica gestiunea/locația folosită la exportul facturilor către SAGA.
- Pentru Odoo Community, utilizatorii trebuie incluși în grupul „Show Full Accounting Features" pentru a accesa meniul de export SAGA.

#### 3. Dependențe

- `base`
- `account`
- `stock`
- `purchase_stock`
- `sale_stock`
- [deltatech_contact](../deltatech_contact/index.md)
- `l10n_ro`

#### 4. Componente Cheie

*Conform fluxului de ingestie, secțiunea „Componente Cheie" este omisă deoarece modulul dispune de fișierul `readme/DESCRIPTION.md` (completat de `readme/USAGE.md`), care a fost folosit pentru Sumar și Funcționalități Cheie.*

#### 5. Conexiuni

- `deltatech_contwin`: modul înrudit de export contabil (interfață către WinMentor / Contwin), documentat în paralel ca alternativă pentru schimbul de date contabile pe piața RO.
