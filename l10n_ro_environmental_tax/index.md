# Romania - Taxe de mediu / AFM (FR-48) (localizat la `l10n_ro_environmental_tax/index.md`)

- **Nume Tehnic:** `l10n_ro_environmental_tax`
- **Versiune:** `19.0.1.5.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_environmental_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_environmental_tax`
- **Ultima Ingestie:** `2026-11-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru taxele de mediu / AFM (Fondul pentru Mediu), cu focus inițial pe ambalaje. Adaugă profil AFM pe produs, linii de material cu tip și greutate per unitate, cote AFM pe material și o declarație AFM persistentă pe perioadă, calculată din facturile de vânzare și stornările postate pentru cantitățile introduse pe piață și cele scutite/exportate, cu trasabilitate completă până la documentul sursă și rapoarte suport în PDF și XLSX. Nomenclatorul acoperă, pe lângă ambalaje, baterii, EEE/DEEE, anvelope și uleiuri; în versiunea curentă calculul folosește doar facturile de vânzare și retururile (importurile, stocurile, POS și e-commerce nu sunt incluse).

#### 2. Funcționalități Cheie

- **Profil AFM pe produs** (fila **AFM / Mediu**): bifa **Supus obligațiilor AFM** și liniile de material — material AFM, tip ambalaj (Primar / Secundar / Transport, doar pentru categoria Ambalaje), factor cantitate (1,0 pentru baterii, EEE, anvelope, uleiuri), greutate/cantitate (kg) per unitate și marcajul informativ **Ambalaj SGR**. Produsele nemarcate sunt ignorate la calcul.
- **Nomenclator de materiale și cote preîncărcate** (**Contabilitate > Raportare > AFM / Mediu > Materiale AFM** și **Cote AFM**): plastic, hârtie/carton, metal, sticlă, lemn, aluminiu, compozit pentru ambalaje; 4 tipuri de baterii; 10 categorii EEE/DEEE; 5 tipuri de anvelope; 4 tipuri de uleiuri. Cotele (RON/kg) au interval de valabilitate, iar cea mai recentă cotă activă la data declarației se aplică; cotele implicite pentru 2025 trebuie verificate anual.
- **Declarație AFM persistentă pe perioadă** (**Declarații AFM**), cu stări Ciornă → Calculată → Validată; nu pot exista două declarații pentru aceeași companie și perioadă.
- **Calcul din facturi:** butonul **Recalculează** parcurge facturile (`out_invoice`) și stornările (`out_refund`) postate din interval, transformă cantitățile în kg și le grupează pe material în **Introdus pe piață** (parteneri din aceeași țară cu compania) și **Scutit / export** (parteneri din altă țară); retururile scad cantitatea.
- **Contracte OIREP** (**Contracte OIREP**): operator, categorie, materiale acoperite, interval de valabilitate și cantitate acoperită per perioadă; se activează cu **Activează**, iar cantitatea acoperită se distribuie automat la recalcularea declarației și poate fi ajustată manual pe linie. Neacoperit = introdus − acoperit (minim 0), iar contribuția = neacoperit × cotă.
- **Trasabilitate completă** document → partener → produs → material → flux → cantitate (kg), în fila **Linii sursă**.
- **Validare:** reușește doar dacă declarația are linii calculate și toate materialele au cote pentru perioadă; după validare declarația nu mai poate fi recalculată, modificată sau ștearsă, iar **Resetează la ciornă** e rezervat rolului managerial.
- **Raport suport** în PDF (QWeb, cu antet companie, perioadă, totaluri și rubrici de semnătură) și export XLSX (sumar pe material + foaia Surse), disponibile după ieșirea din starea Ciornă; exportul direct în formatele eTAX/SIATD rămâne manual până la publicarea schemelor oficiale.
- **Blocarea validării facturilor** pentru produse cu obligații AFM dar fără nicio linie de material activă.
- **Dependență Python:** exportul XLSX folosește biblioteca `xlsxwriter` (de instalat separat).

#### 3. Dependențe

- `account`
- `product`
- `l10n_ro`
- Dependență Python (nedeclarată în manifest): `xlsxwriter`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.afm.material`: nomenclatorul materialelor AFM (ambalaje, baterii, EEE, anvelope, uleiuri).
- `l10n.ro.afm.rate`: cotele AFM per material (categorie, material, interval de valabilitate, cotă/kg).
- `product.template` (extins): bifa de obligație AFM și liniile de material asociate produsului, cu verificarea profilului.
- `l10n.ro.afm.product.line`: linia de material pe produs — material, tip ambalaj, factor cantitate și greutate/cantitate per unitate.
- `l10n.ro.afm.declaration`: declarația AFM pe perioadă (companie, interval, stare), cu `action_compute`, `action_validate`, `action_reset_to_draft`, `action_print_pdf` și `action_export_xlsx`.
- `l10n.ro.afm.declaration.line`: linia de declarație per material, cu cantitate introdusă, scutită, acoperită OIREP, neacoperită, cotă și contribuție.
- `l10n.ro.afm.source.line`: linia sursă de trasabilitate din care se compune declarația.
- `l10n.ro.afm.operator.contract`: contractul OIREP (stări Ciornă → Activ → Expirat, cu `action_activate`, `action_expire`).
- `account.move` (extins): `action_post` blochează facturile cu produse AFM incomplete.

**Vizualizări**

- `product_template_form_view_l10n_ro_afm`: fila „AFM / Mediu” pe produs.
- `view_l10n_ro_afm_declaration_form` / `_list` / `_search`: declarația AFM, cu liniile de declarație și liniile sursă.
- `view_l10n_ro_afm_material_list`, `view_l10n_ro_afm_rate_list`: materialele și cotele AFM.
- `view_l10n_ro_afm_operator_contract_form` / `_list`: contractele OIREP.
- `menu_l10n_ro_afm_root` și submeniurile Declarații, Contracte OIREP, Materiale, Cote, sub Contabilitate > Raportare > AFM / Mediu.
- `action_report_afm_declaration` (`report_afm_declaration`): raportul PDF al declarației.
- `data/afm_material_data.xml`, `data/afm_rate_data.xml`: nomenclatorul și cotele inițiale.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron` sau `base.automation`. Calculul declarației se face la cerere, prin butonul **Recalculează**.

#### 5. Conexiuni

- [l10n_ro_cbam](../l10n_ro_cbam/index.md): altă localizare de raportare de mediu/carbon pentru piața românească, din aceeași suită `l10n_ro_ent`.
- [l10n_ro_excise_duty](../l10n_ro_excise_duty/index.md): modul înrudit de fiscalitate specială (accize) din aceeași suită `l10n_ro_ent`.
