# Interfață ContWin (localizat la `deltatech_contwin/index.md`)

- **Nume Tehnic:** `deltatech_contwin`
- **Versiune:** `19.0.1.0.15`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_contwin
- **Cale Locală:** `odoo-addons/bitshop/deltatech_contwin`
- **Ultima Ingestie:** `2026-10-31`

#### 1. Sumar

Modulul „ContWin Interface" permite ca evidența contabilă să rămână în ContWin, programul de contabilitate românesc, în timp ce facturarea, achizițiile și stocurile se gestionează în Odoo. Pentru o perioadă aleasă, modulul exportă documentele postate ale unei singure companii în formatul text pe care îl importă ContWin și, la nevoie, în tabele pregătite pentru SAF-T, toate împachetate într-un singur fișier ZIP. Astfel, firmele pot folosi Odoo pentru operațiunile zilnice, păstrând compatibilitatea cu ContWin pentru contabilitate și raportare fiscală.

#### 2. Funcționalități Cheie

- **Achiziții și vânzări:** facturi de furnizor și de client, note de credit și recepții, cu conturi, sume în RON și în valută, curs de schimb, scadență, tip și cotă de TVA.
- **Plăți și încasări:** înregistrările de bancă și de casă din perioadă, câte un fișier pe jurnal, cu contul jurnalului sau al plății.
- **Transferuri între depozite:** pentru un depozit ales, intrările de stoc ale mărfurilor care au intrat în el și au ieșit din el către alte locații.
- **Tabele SAF-T:** unități de măsură, produse, linii de facturi de intrare și de ieșire cu tipul și codul de taxă SAF-T și numerele de înregistrare ale partenerilor, pregătite pentru fișierul D406.
- **Specific TVA românesc:** TVA la încasare se recunoaște din poziția fiscală a facturii; CNP-ul persoanelor fizice este validat înainte de export.
- **Filtre:** jurnale, unitate operațională (jurnalele unei filiale) și depozit.
- **O singură companie o dată:** se includ doar documentele companiei alese în export, iar jurnalele altei companii sunt refuzate.
- **Utilizare:** *Contabilitate > Contabilitate > ContWin > Export ContWin* (manageri de contabilitate). Se aleg perioada, **Compania**, **Modul** (*Contwin*, *SAFT* sau *All*) și, la nevoie, jurnalele, unitatea operațională și depozitul; apoi **Apply** și se descarcă ZIP-ul:
  - *Contwin*: `IN_…` și `IE_…` (facturi), `INT_…` și `IET_…` (transferuri între depozite), `TOT_…` (totul într-un fișier) și un fișier pe jurnal de bancă sau de casă;
  - *SAFT*: `UM_SAFT_…`, `PRODUCTS_SAFT_…`, `IN_SAFT_…`, `IE_SAFT_…` și `TOT_SAFT_…`;
  - *All*: ambele seturi.
  Fișierele text se importă apoi în ContWin.
- **Configurare prealabilă:** planul de conturi românesc (`l10n_ro`) instalat, parteneri cu cod fiscal (sau CNP pentru persoane fizice, din `deltatech_contact`); pentru filiale se setează **Operating Unit** pe jurnalele fiecărei filiale, iar alegerea ei în export selectează acele jurnale; poziția fiscală pentru TVA la încasare este găsită după nume („incasare”) și propusă în wizard, unde poate fi schimbată; pentru tabelele SAF-T se instalează localizarea SAF-T românească, care adaugă tipurile și codurile de taxă.
- **De știut:**
  - fișierul `IN_…` conține doar facturile de furnizor cu cont din clasa 3 (mărfuri și materiale); facturile doar de servicii se înregistrează altfel în ContWin;
  - în fișierele de bancă, orice cont în afară de bancă și partener se exportă ca `5125` (inclusiv comisionul bancar), deci un comision necesită nota 627 = 5125 în ContWin; în cele de casă se exportă drept contul de casă, deci o înregistrare de casă cu alte conturi decât casa și partenerul (comision, diferență) trebuie corectată manual în ContWin;
  - codul de TVA este A pentru cota standard (21%, 19%), B pentru cota redusă (11%, 9%) și C pentru restul; liniile de TVA (4426/4427) preiau codul taxei lor.

#### 3. Dependențe

- `base`
- `account`
- `stock`
- [deltatech_contact](../deltatech_contact/index.md)
- `l10n_ro`

Dependență externă Python: `python-stdnum` (pentru validarea codurilor de TVA).

#### 4. Componente Cheie

*Conform fluxului de ingestie, analiza detaliată a componentelor este omisă, deoarece `readme/DESCRIPTION.md` este prezent. Mai jos sunt doar reperele confirmate în cod.*

**Modele**

- `export.contwin`: wizard tranzitoriu (`wizard/export_contwin.py`) care colectează parametrii (perioadă, companie, mod, jurnale, unitate operațională, depozit, poziții fiscale), generează fișierele text și le împachetează în ZIP.
- `account.journal` (extins): câmpul `operating_unit_id`, folosit la selectarea jurnalelor unei filiale.

**Vizualizări**

- `menu_contwin`: meniul **ContWin** din *Contabilitate > Contabilitate*, vizibil managerilor de contabilitate.
- `wizard/export_contwin.xml`: formularul wizardului de export.

#### 5. Conexiuni

- [deltatech_saga](../deltatech_saga/index.md): modul înrudit de export contabil din Odoo către un alt program de contabilitate românesc (SAGA), din aceeași familie de interfețe de export Terrabit.
