# Interfață ContWin (localizat la `deltatech_contwin/index.md`)

- **Nume Tehnic:** `deltatech_contwin`
- **Versiune:** `19.0.1.0.6`
- **Cale:** `https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_contwin`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_contwin`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul „Interfață ContWin" este o extensie Odoo specializată, dezvoltată de Terrabit, care facilitează exportul datelor din Odoo către programul de contabilitate ContWin. ContWin este o aplicație de contabilitate dezvoltată de Omnidata (Petrescu), utilizată frecvent în România. Modulul funcționează ca o punte între funcționalitatea ERP modernă a Odoo și sistemul de contabilitate ContWin, permițând companiilor să folosească Odoo pentru operațiunile zilnice, păstrând totodată compatibilitatea cu ContWin pentru evidența contabilă și raportarea fiscală.

#### 2. Funcționalități Cheie

- **Export complet de facturi**: exportă atât facturile de intrare (achiziții), cât și cele de ieșire (vânzări) din Odoo către ContWin.
- **Formate multiple de export**:
  - format ContWin (fișiere `.fis`) cu câmpuri delimitate prin punct și virgulă;
  - format SAF-T (Standard Audit File for Tax) pentru raportare standardizată.
- **Mapare detaliată a datelor**: corelarea atentă a câmpurilor Odoo cu formatul așteptat de ContWin, inclusiv coduri de cont, informații despre parteneri, tipuri de TVA și altele.
- **Opțiuni de export configurabile**: filtrare după interval de date, jurnale, unități operaționale și alte criterii.
- **Suport pentru specificul contabil românesc**: tratarea cazurilor speciale precum taxarea inversă și TVA la încasare.
- **Date tranzacționale complete**: exportul detaliilor complete ale tranzacțiilor, inclusiv termene de plată, numere de document, sume, monede și cursuri de schimb.

#### 3. Dependențe

- `base`
- `account`
- `stock`
- [deltatech_contact](../deltatech_contact/index.md)
- `l10n_ro`

Dependență externă Python: `python-stdnum` (pentru validarea codurilor de TVA).

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune nu a fost detaliată prin analiza codului, întrucât fișierul `readme/DESCRIPTION.md` acoperă scopul și funcționalitățile modulului. Pe scurt, implementarea se realizează printr-o interfață de tip wizard (`export_contwin.py`) care colectează parametrii de export, procesează datele contabile din Odoo, le formatează conform specificațiilor ContWin și generează fișierele de export.

#### 5. Conexiuni

- [deltatech_saga](../deltatech_saga/index.md): modul înrudit de export contabil din Odoo către un alt program de contabilitate românesc (SAGA), parte din aceeași familie de interfețe de export Terrabit.
