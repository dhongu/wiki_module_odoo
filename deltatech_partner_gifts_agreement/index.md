# Deltatech Partner Gifts Service Agreement (localizat la `deltatech_partner_gifts_agreement/index.md`)

- **Nume Tehnic:** `deltatech_partner_gifts_agreement`
- **Versiune:** `19.0.0.0.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_partner_gifts_agreement
- **Cale Locală:** `odoo-addons/bitshop/deltatech_partner_gifts_agreement`
- **Ultima Ingestie:** `2026-10-01`

#### 1. Sumar

Modulul leagă programul de cadouri pentru parteneri de contractele de service. Partenerii care au contracte de service active sunt identificați și incluși automat în campaniile de atenții, astfel încât recompensarea clienților fideli să se facă unitar și cu efort administrativ redus.

#### 2. Funcționalități Cheie

- Adăugare automată în programul de cadouri a partenerilor cu contracte de service, printr-un asistent din meniul Cadouri partener (opțiunea „Add service partners").
- Asistentul cere o singură dată tipul cadoului (simplu, mediu, VIP), data cadoului și modalitatea de livrare (curier, logistică, vânzări, service); creează apoi câte o linie de cadou pentru fiecare partener cu contracte în ciornă sau deschise.
- Pentru fiecare cadou generat se preia adresa de livrare a partenerului (prima adresă de tip livrare) și responsabilul: utilizatorul din contractul de service sau, în lipsă, cel al partenerului.
- Motiv nou de cadou, „Service Agreement", care permite raportarea separată a cadourilor generate din contracte față de cele manuale sau din vânzări.
- Marcaj „Active agreements" pe linia de cadou (în listă și în formular), calculat la actualizarea datelor partenerului: este bifat dacă partenerul sau societatea-mamă are un contract de service care nu este închis.
- Filtru de căutare „Active service agreement", pentru prioritizarea bugetului de atenții.

Notă: sursa a fost `readme/DESCRIPTION.md`, completată cu `NOUTATI_19.md` și cu codul pentru detaliile operaționale.

#### 3. Dependențe

- [deltatech_partner_gifts](../deltatech_partner_gifts/index.md)
- [deltatech_service](../deltatech_service/index.md)

#### 4. Componente Cheie

**Modele**

- `partner.gift.line` (extins): adaugă motivul `service`, câmpul boolean `has_active_agreement` și suprascrie `get_partner_data()` pentru a-l calcula pe baza `service.agreement` (stare diferită de `closed`).
- `add.service.partners.wizard` (tranzitoriu): asistent care generează în masă liniile de cadou din contractele de service.

**Vizualizări**

- `view_partner_gift_tree`, `view_partner_gift_form`: extind lista și formularul cadourilor cu `has_active_agreement`.
- `view_partner_gift_search`: filtrul „Active service agreement".
- `add_partners_wizard_form`: formularul asistentului (tip cadou, dată, modalitate de livrare).

**Acțiuni Automate / Acțiuni Server**

- `action_add_service_partners_wizard`: acțiune de fereastră care deschide asistentul, din meniul „Add service partners" (sub meniul Cadouri partener). Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- [deltatech_partner_gifts](../deltatech_partner_gifts/index.md): modulul de bază pentru cadouri, extins aici.
- [deltatech_service](../deltatech_service/index.md): sursa contractelor de service (`service.agreement`).
