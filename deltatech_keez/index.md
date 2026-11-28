# Interfață Keez (localizat la `deltatech_keez/index.md`)

- **Nume Tehnic:** `deltatech_keez`
- **Versiune:** `20.0.1.1.2`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_keez`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_keez`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite ținerea contabilității în Keez, platforma românească de contabilitate online, în timp ce facturarea și achizițiile se fac în Odoo. Pentru o perioadă aleasă, exportă documentele postate ale unei companii ca fișiere Excel în formatul pe care îl importă Keez, împachetate într-un singur fișier ZIP. Este un export de fișiere, nu o integrare API în timp real.

#### 2. Funcționalități Cheie

- **Furnizori și clienți:** două fișiere de parteneri (denumire, cod fiscal, firmă sau persoană fizică), cu partenerii documentelor și notelor contabile exportate.
- **Documente de intrare (IN):** facturi de furnizor, note de credit și recepții de achiziție, un rând per linie contabilă, cu cont debit și credit, valoare în RON și în valută, tip și cotă TVA.
- **Documente de ieșire (IE):** facturi de client și note de credit, în același format.
- **Note contabile (NC):** notele contabile postate din perioadă, opțional limitate la anumite jurnale.
- **Detalii TVA românesc:** tipul TVA, cota și rubrica D300 se iau din taxele fiecărei linii, iar TVA la încasare se recunoaște după poziția fiscală a facturii.
- **Conturi contabile românești:** conturile Odoo sunt convertite în conturi Keez (cont sintetic fără zerouri finale, urmat de analitic).
- **Doar ce e în registru:** se exportă numai documentele postate ale companiei alese; ciornele, documentele anulate și jurnalele altei companii sunt excluse.
- **Coloanele fișierelor IN, IE și NC:** ID, Serie Document, Numar Document, Data Document, Data Scadenta, TipDocument, Categorie, Tva Incasare, ContDebit, ContCredit, ValoareRON, ValoareValuta, Valuta, TipTVA, CotaTVA, Cod partener, Denumire partener, Cod angajat, Denumire angajat, Explicatie, Import, Este Firma, D300, Jurnal, Status.
- **Flux de utilizare:** *Contabilitate > Contabilitate > Keez > Export Keez*; perioada implicită este luna precedentă, se aleg **Compania**, jurnalele pentru notele contabile (toate, dacă e gol) și poziția fiscală pentru TVA la încasare; după **Aplică** se descarcă ZIP-ul cu `Furnizori_…`, `Clienti_…`, `IN_…`, `IE_…` și, dacă perioada are note contabile, `NC_…`. În Keez se importă fișierele, începând cu partenerii.
- **Configurare:** planul de conturi românesc (`l10n_ro`) instalat, parteneri cu cod fiscal (exportat drept cod partener); poziția fiscală pentru TVA la încasare este găsită după nume („incasare") și propusă în wizard, unde poate fi schimbată. Meniul este vizibil doar managerilor de contabilitate.

#### 3. Dependențe

- `account`
- `stock_account`
- `l10n_ro`

Dependență externă Python: `xlsxwriter`.

#### 4. Componente Cheie

*Readme-ul acoperă funcționalitățile, dar nu detaliază componentele tehnice; elementele de mai jos au fost confirmate în cod.*

**Modele**

- `export.keez` (wizard tranzitoriu, `wizard/export_keez.py`): colectează parametrii (perioadă, companie, jurnale, poziții fiscale), interoghează facturile și notele contabile, le formatează conform Keez și generează arhiva ZIP cu fișierele XLSX.

**Vizualizări**

- `view_export_keez_form` și `action_export_keez` (`wizard/export_keez_view.xml`): formularul și acțiunea asistentului de export.
- `menu_keez` (`views/menu.xml`): meniul *Keez* din Contabilitate, restricționat grupului de manager contabil.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește acțiuni programate.

#### 5. Conexiuni

- [deltatech_saga](../deltatech_saga/index.md): modul înrudit de export contabil din Odoo către un alt program de contabilitate românesc (SAGA), parte din aceeași familie de interfețe de export Terrabit.
- [deltatech_contwin](../deltatech_contwin/index.md): modul înrudit de export contabil din Odoo către ContWin, parte din aceeași familie de interfețe de export Terrabit.
