# Interfață Keez (localizat la `deltatech_keez/index.md`)

- **Nume Tehnic:** `deltatech_keez`
- **Versiune:** `19.0.1.1.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_keez`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_keez`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul „Interfață Keez" permite companiilor care facturează și achiziționează în Odoo, dar țin contabilitatea în platforma online Keez, să transfere documentele fără reintroducere manuală. Pentru o perioadă aleasă, exportă documentele înregistrate ale unei companii sub formă de fișiere Excel în formatul pe care îl importă Keez, împachetate într-o arhivă ZIP. Este o punte bazată pe export de fișiere, nu pe API în timp real.

#### 2. Funcționalități Cheie

- **Furnizori și clienți:** două fișiere de parteneri (denumire, cod fiscal, persoană juridică sau fizică), cu partenerii documentelor și notelor contabile exportate.
- **Documente de intrare (IN):** facturi și note de credit de la furnizori, plus recepții de achiziție, câte un rând pe linie contabilă, cu cont debit și credit, valoare în RON și în valută, tip și cotă TVA.
- **Documente de ieșire (IE):** facturi și note de credit către clienți, în același format.
- **Note contabile (NC):** notele contabile înregistrate în perioadă, opțional limitate la anumite jurnale.
- **Detalii TVA românesc:** tipul și cota TVA și caseta D300 sunt preluate din taxele fiecărei linii; TVA la încasare se recunoaște după poziția fiscală a facturii.
- **Coduri contabile românești:** conturile Odoo sunt convertite în conturi Keez (cont sintetic fără zerouri finale, urmat de analitic).
- **Doar ce e în registru:** se exportă numai documentele înregistrate ale companiei alese; ciornele, documentele anulate și jurnalele altei companii sunt excluse.
- **Coloanele fișierelor IN, IE și NC:** ID, Serie Document, Număr Document, Data Document, Data Scadență, TipDocument, Categorie, TVA Încasare, ContDebit, ContCredit, ValoareRON, ValoareValuta, Valuta, TipTVA, CotaTVA, cod și denumire partener, cod și denumire angajat, Explicație, Import, Este Firmă, D300, Jurnal, Status.
- **Utilizare:** *Contabilitate > Contabilitate > Keez > Export Keez*. Perioada implicită este luna precedentă; se aleg compania, jurnalele pentru notele contabile (toate, dacă rămâne gol) și poziția fiscală pentru TVA la încasare. Arhiva conține `Furnizori_…`, `Clienti_…`, `IN_…`, `IE_…` și, dacă perioada are note contabile, `NC_…`. Importul în Keez începe cu partenerii.
- **Configurare:** necesită planul de conturi românesc (`l10n_ro`) și codul fiscal completat pe parteneri (se exportă drept cod partener). Poziția fiscală pentru TVA la încasare este căutată după nume („incasare") și propusă în wizard, unde poate fi schimbată. Meniul este vizibil doar managerilor de contabilitate.

#### 3. Dependențe

- `account`
- `stock_account`
- `l10n_ro`

Dependență externă Python: `xlsxwriter`.

#### 4. Componente Cheie

Descrierea din `readme/DESCRIPTION.md` acoperă scopul și funcționalitățile modulului, deci componentele nu au fost detaliate prin analiza completă a codului.

**Modele**

- `export.keez` (`wizard/export_keez.py`): wizard tranzitoriu care colectează parametrii exportului (perioadă, companie, jurnale, poziție TVA la încasare, gestiune, ignorare erori), generează fișierele Excel și le returnează într-un ZIP.

**Vizualizări**

- `view_export_keez_form`: formularul wizardului de export, cu descărcarea fișierului rezultat.
- `menu_keez`: meniul „Keez" din Contabilitate, cu intrarea „Export Keez" (`action_export_keez`), pentru grupul `account.group_account_manager`.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni automate sau server.

#### 5. Conexiuni

- [deltatech_contwin](../deltatech_contwin/index.md): modul înrudit de export contabil din Odoo către ContWin, din aceeași familie de interfețe de export Terrabit.
