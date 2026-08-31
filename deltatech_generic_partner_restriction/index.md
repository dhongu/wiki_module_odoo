# Restricție Jurnale pentru Partenerul Generic (localizat la `deltatech_generic_partner_restriction/index.md`)

- **Nume Tehnic:** `deltatech_generic_partner_restriction`
- **Versiune:** `19.0.3.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_generic_partner_restriction
- **Cale Locală:** `odoo-addons/deltatech/deltatech_generic_partner_restriction`
- **Ultima Ingestie:** `2026-08-31`

#### 1. Sumar

**Modul de tranziție, gol.** Funcționalitatea pe care o oferea — restricționarea jurnalelor bancare și de casă la înregistrarea plăților pentru partenerul generic, plus refuzul de a valida o factură de client emisă pe acest partener — a fost comasată în [deltatech_partner_generic](../deltatech_partner_generic/index.md) în versiunea `19.0.3.0.0`. Modulul păstrează doar dependența, astfel încât bazele care îl au instalat preiau restricțiile la actualizare, fără niciun pas manual. Jurnalele bifate ca restricționate sunt păstrate de scriptul de pre-migrare al modulului-gazdă.

Instalările noi folosesc direct `deltatech_partner_generic`.

#### 2. Funcționalități Cheie

Niciuna proprie. Vezi [deltatech_partner_generic](../deltatech_partner_generic/index.md).

#### 3. Dependențe

- [deltatech_partner_generic](../deltatech_partner_generic/index.md)

#### 4. Componente Cheie

Modulul nu declară modele, vizualizări, date sau acțiuni automate. `data` este o listă goală, iar pachetul `models/` a fost eliminat.

#### 5. Conexiuni

- [deltatech_partner_generic](../deltatech_partner_generic/index.md): modulul-gazdă, care conține acum câmpul `restriction` de pe `account.journal`, filtrarea jurnalelor pe `account.payment` și blocarea postării facturilor de client emise pe partenerul generic.
