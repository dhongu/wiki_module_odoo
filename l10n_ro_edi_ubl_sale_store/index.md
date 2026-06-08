# Deltatech Sale from Store UBL (localizat la `l10n_ro_edi_ubl_sale_store/index.md`)

- **Nume Tehnic:** `l10n_ro_edi_ubl_sale_store`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_edi_ubl_sale_store
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_edi_ubl_sale_store`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Acest modul completează localizarea românească pentru e-Factura prin tratarea corectă a vânzărilor efectuate prin casa de marcat. Atunci când pentru o vânzare a fost deja emis un bon fiscal, modulul setează automat tipul de e-factură la codul `751`, astfel încât documentul electronic transmis să reflecte faptul că livrarea a fost însoțită de bon fiscal. Scopul principal este conformitatea fiscală corectă a facturilor emise pe baza vânzărilor din magazin.

#### 2. Funcționalități Cheie

- Setează tipul de e-factură ca fiind `751` atunci când pentru vânzare a fost tipărit un bon fiscal.

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, analiza detaliată a componentelor tehnice (modele, vizualizări, acțiuni automate / acțiuni server) a fost omisă. Descrierea modulului nu solicită explicit această analiză, iar prioritizarea Readme prevede omiterea inspecției codului în acest caz.

#### 5. Conexiuni

- `l10n_ro_edi`: modulul de bază pentru e-Factura România, pe care acest modul îl extinde pentru a stabili tipul documentului electronic.
- `deltatech_sale_store`: modul de vânzare din magazin (referit comentat în manifest) ca sursă a contextului de bon fiscal.
