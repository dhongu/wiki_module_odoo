# Romania - Taxe de mediu / AFM (localizat la `l10n_ro_environmental_tax/index.md`)

- **Nume Tehnic:** `l10n_ro_environmental_tax`
- **Versiune:** `20.0.1.5.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_environmental_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_environmental_tax`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Taxe de mediu / AFM, cu focus inițial pe ambalaje. Modulul adaugă profil AFM pe produs, linii de ambalaj cu material, tip și greutate per unitate, cote AFM pe material și o declarație AFM persistentă pe perioadă, calculată din facturile de vânzare postate (cantități introduse pe piață și cantități scutite/exportate), cu trasabilitate până la documentul sursă și raport suport în PDF și XLSX. Prima versiune acoperă raportul suport pentru ambalaje și pregătește extinderea spre baterii, DEEE și alte categorii AFM.

#### 2. Funcționalități Cheie

- Profil AFM pe produs, în fila **AFM / Mediu**: bifa **Supus obligațiilor AFM** și linii de material (material AFM, tip ambalaj Primar/Secundar/Transport, factor cantitate, greutate/cantitate în kg per unitate, marcaj informativ SGR).
- Nomenclator de materiale (ambalaje, baterii, EEE/DEEE, anvelope, uleiuri) și cote AFM pe kg, preîncărcate la instalare (cotele implicite pentru 2025, de verificat anual), cu perioadă de valabilitate.
- Blocarea postării facturilor care conțin produse cu obligații AFM dar fără nicio linie de material activă.
- Declarație AFM persistentă pe perioadă (**Contabilitate → Raportare → AFM / Mediu → Declarații AFM**), cu stări Ciornă → Calculată → Validată; o singură declarație per companie și perioadă.
- Calcul la cerere, prin **Recalculează**, din facturile de vânzare și stornările postate: cantitatea este grupată pe material în **Introdus pe piață** (partener din țara companiei) și **Scutit / export** (partener din altă țară). Importurile, stocurile, POS și e-commerce nu sunt incluse.
- Contracte OIREP (**Contracte OIREP**, activate cu **Activează**): operator, categorie, materiale acoperite, valabilitate și cantitate acoperită per perioadă, distribuită automat la recalculare; acoperirea se poate ajusta manual înainte de validare.
- Linii declarație pe material (introdus, scutit, acoperit OIREP, neacoperit, cotă, contribuție) și linii sursă pentru trasabilitate document → partener → produs → material → flux → cantitate.
- Validarea cere linii calculate și cote pentru toate materialele; declarația validată nu se mai modifică, iar doar un manager poate folosi **Resetează la ciornă**.
- Raport suport în **PDF** (QWeb) și **Export XLSX** (sumar pe material + foaie surse), pentru verificare și arhivare; exportul direct în eTAX/SIATD rămâne manual. Fluxul pas cu pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `account`
- `product`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.afm.material`: nomenclatorul materialelor AFM.
- `l10n.ro.afm.rate`: cotele AFM pe material, cu interval de valabilitate.
- `product.template` (extindere): marcajul de obligație AFM și liniile de ambalaj.
- `l10n.ro.afm.product.line`: linia de profil AFM pe produs (material, tip ambalaj, factor, greutate).
- `l10n.ro.afm.declaration`: declarația pe perioadă, cu recalculare din facturi și rapoarte PDF/XLSX.
- `l10n.ro.afm.declaration.line`: linia declarației pe material.
- `l10n.ro.afm.source.line`: linia sursă de trasabilitate.
- `l10n.ro.afm.operator.contract`: contractul OIREP.
- `account.move` (extindere): validare la postare pentru produse AFM cu profil incomplet.

**Vizualizări**

- `views/product_template_views.xml`: fila **AFM / Mediu** pe produs.
- `views/l10n_ro_environmental_tax_views.xml`: declarații, materiale, cote și contracte OIREP.
- `reports/afm_declaration_report.xml`: raportul suport PDF.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron` sau `base.automation`; calculul rulează la cerere, prin butonul **Recalculează**. Datele inițiale (`data/afm_material_data.xml`, `data/afm_rate_data.xml`) încarcă materialele și cotele.

#### 5. Conexiuni

- [l10n_ro_cbam](../l10n_ro_cbam/index.md): altă raportare de mediu/carbon din aceeași suită `l10n_ro_ent`.
- [l10n_ro_excise_duty](../l10n_ro_excise_duty/index.md): fiscalitate specială (accize) din aceeași suită.
- [l10n_ro_sgr](../l10n_ro_sgr/index.md): sistemul garanție-returnare; câmpul de ambalaj SGR de pe liniile AFM este doar informativ și nu înlocuiește obligația AFM.
