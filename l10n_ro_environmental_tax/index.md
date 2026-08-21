# Romania - Environmental Tax / AFM (FR-48) (localizat la `l10n_ro_environmental_tax/index.md`)

- **Nume Tehnic:** `l10n_ro_environmental_tax`
- **Versiune:** `19.0.1.5.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_environmental_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_environmental_tax`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

MVP pentru FR-48 — Taxe de mediu / AFM, cu focus inițial pe ambalaje. Modulul adaugă profil AFM pe produs, linii de ambalaj cu material, tip și greutate per unitate, cote AFM pe material și o declarație AFM persistentă pe perioadă, calculată din facturile de vânzare postate pentru cantitățile introduse pe piață și cele scutite/exportate, cu trasabilitate completă până la documentul sursă și rapoarte suport în PDF și XLSX. Prima versiune acoperă raportul suport pentru ambalaje și pregătește extinderea spre baterii, DEEE și alte categorii AFM.

#### 2. Funcționalități Cheie

- Profil AFM pe produs (tab dedicat) cu marcarea bunurilor supuse obligațiilor AFM.
- Linii de ambalaj pe produs: material AFM, tip ambalaj (Primar / Secundar / Transport), factor cantitate și greutate/cantitate (kg) per unitate.
- Cote AFM configurabile pe material.
- Declarație AFM persistentă pe perioadă, cu stări Ciornă → Calculată → Validată.
- Calcul automat din facturile de vânzare postate în perioada selectată, cu grupare pe material în cantitate introdusă pe piață (parteneri din aceeași țară) și cantitate scutită/export (parteneri din altă țară).
- Ajustare manuală a cantității acoperite OIREP pe linie, cu distribuire automată din contractele OIREP active la recalculare.
- Trasabilitate completă document → partener → produs → material → flux → cantitate, prin liniile sursă.
- Raport suport al declarației în PDF (QWeb) și export XLSX (sumar pe material + foaie surse).
- Blocarea validării facturilor pentru produse cu obligații AFM dar fără nicio linie de material activă.
- Gestionare contracte OIREP: operator, categorie, materiale acoperite, interval de valabilitate și cantitate acoperită per perioadă.

#### 3. Dependențe

- `account`
- `product`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.afm.material`: nomenclatorul materialelor de ambalaj/AFM (ex. plastic, hârtie/carton, sticlă, metal, baterie portabilă).
- `l10n.ro.afm.rate`: cotele AFM aplicabile per material.
- `product.template` (extindere): câmpul de marcare a obligațiilor AFM și liniile de ambalaj asociate produsului.
- `l10n.ro.afm.product.line`: linia de ambalaj pe produs — material, tip ambalaj, factor cantitate și greutate/cantitate per unitate.
- `l10n.ro.afm.declaration`: declarația AFM persistentă pe perioadă (companie, interval, stare), cu logica de recalculare din facturi și generarea rapoartelor PDF/XLSX.
- `l10n.ro.afm.declaration.line`: linia de declarație per material, cu cantitate introdusă, scutită, acoperită OIREP, neacoperită, cotă și contribuție calculată.
- `l10n.ro.afm.source.line`: linia sursă de trasabilitate (document, partener, produs, material, flux, cantitate) din care se compune declarația.
- `l10n.ro.afm.operator.contract`: contractul OIREP (operator, categorie, materiale acoperite, interval de valabilitate, cantitate acoperită per perioadă).
- `account.move` (extindere): validare la postare — blochează facturile cu produse AFM incomplete (fără linii de material configurate).

**Vizualizări**

- `views/product_template_views.xml`: tabul „AFM / Mediu" pe produs, cu bifa de obligație AFM și liniile de material/ambalaj.
- `views/l10n_ro_environmental_tax_views.xml`: formularele și listele pentru declarația AFM (cu liniile de declarație și liniile sursă), materiale, cote și contracte OIREP.

**Rapoarte**

- `reports/afm_declaration_report.xml`: raportul suport al declarației AFM în format PDF (QWeb), cu antet companie, perioadă, tabel linii și rânduri de semnătură; exportul XLSX (sumar pe material + foaie surse) este generat din același wizard/acțiune a declarației.

**Date**

- `data/afm_material_data.xml`: nomenclatorul inițial de materiale AFM.
- `data/afm_rate_data.xml`: cotele AFM inițiale per material.

**Acțiuni Automate / Acțiuni Server**

*Nu există `ir.cron` sau `base.automation`. Calculul declarației se realizează la cerere, prin butonul „Recalculează", care parcurge facturile de vânzare postate din perioada selectată.*

#### 5. Conexiuni

- [l10n_ro_cbam](../l10n_ro_cbam/index.md): altă localizare de raportare de mediu/carbon pentru piața românească, din aceeași suită `l10n_ro_ent`.
- [l10n_ro_excise](../l10n_ro_excise/index.md): modul înrudit de fiscalitate specială (accize) din aceeași suită `l10n_ro_ent`.
