# POS Price Lock (localizat la `deltatech_pos_price_lock/index.md`)

- **Nume Tehnic:** `deltatech_pos_price_lock`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_price_lock
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_price_lock`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Odoo permite restricționarea modificării prețului în Point of Sale doar pentru manageri. Dacă toți angajații de la casă sunt manageri, sau dacă firma vrea un preț fix la raft indiferent cine vinde, restricția standard nu ajunge. Modulul adaugă un pas suplimentar: blocarea modificării manuale a prețului pentru toți utilizatorii casei, inclusiv pentru manageri.

#### 2. Funcționalități Cheie

- **Manageri incluși:** opțiune nouă per casă (POS), sub *Price Control*; când e bifată, nimeni nu mai poate schimba prețul produsului pe comandă, nici casierii, nici managerii.
- **Toate căile manuale sunt închise:** tasta *Price* din tastatura numerică este dezactivată, iar verificarea de preț din *Employees* (`pos_hr`) refuză modificarea cu mesajul obișnuit.
- **Prețurile se adaptează în continuare automat:** prețurile recalculate de Odoo (liste de prețuri, poziții fiscale, taxe incluse în preț) funcționează normal; doar modificarea manuală este blocată.
- **Corecțiile se fac pe produs:** un preț greșit se corectează în fișa produsului și ajunge la casă de acolo; cu *POS Price Sync* instalat, noul preț ajunge la casele deschise fără reîncărcare.
- **Configurare:** *Point of Sale > Configuration > Settings*, se alege casa, la *Pricing* se bifează *Price Control*, apoi *Managers included*; la o sesiune deja deschisă se reîncarcă pagina casei.
- **Limitare:** blocarea este verificată în interfața casei; prețul comenzilor nu este verificat pe server.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `pos.config` (extins): câmpul boolean `lock_price_for_managers` (*Managers included*).
- `res.config.settings` (extins): câmpul `pos_lock_price_for_managers`, legat de configurarea casei.

**Vizualizări**

- `views/res_config_settings_views.xml`: bifa *Managers included* sub *Price Control* în setările POS.

**Acțiuni Automate / Acțiuni Server**

- Nu există. În front-end, `static/src/js/pos_store.esm.js` extinde `PosStore` pentru a refuza modificarea manuală a prețului când blocarea este activă.

#### 5. Conexiuni

- [deltatech_pos_price_sync](../deltatech_pos_price_sync/index.md): propagă prețul corectat pe produs către casele deschise, fără reîncărcare.
- `pos_hr`: verificarea de preț din *Employees* respectă blocarea.
