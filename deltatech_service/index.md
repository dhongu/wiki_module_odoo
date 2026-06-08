# Services Agreement Obsolete (localizat la `deltatech_service/index.md`)

- **Nume Tehnic:** `deltatech_service`
- **Versiune:** `19.0.2.0.4`
- **Cale:** `https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service`
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

`deltatech_service` este un modul „umbrelă" (de tranziție) din suita de service Terrabit. El nu aduce funcționalitate proprie, ci servește doar ca punct de instalare care atrage automat modulul de gestiune a contractelor de service. Numele său tehnic „Services Agreement Obsolete" și manifestul indică faptul că modulul este considerat **învechit (obsolete)**: rolul de gestiune efectivă a acordurilor de service a fost mutat în modulul dedicat `deltatech_service_agreement`. Practic, este păstrat pentru compatibilitate și pentru a asigura o cale de migrare lină pentru bazele de date existente.

#### 2. Funcționalități Cheie

Fișierul `readme/DESCRIPTION.md` este prezent, dar gol din punct de vedere al conținutului (conține doar antetul „Features:", fără funcționalități listate). Modulul nu declară date, vizualizări sau cod propriu în manifest. Singura funcție efectivă este:

- Instalarea automată a modulului de gestiune a acordurilor de service prin dependența directă către `deltatech_service_agreement`.

#### 3. Dependențe

- `deltatech_service_agreement`

#### 4. Componente Cheie

Conform regulilor de ingestie, fișierul `readme/DESCRIPTION.md` există, deci analiza codului pentru această secțiune este **omisă**. În plus, manifestul nu declară fișiere de date, vizualizări sau modele (`"data": []`), iar modulul nu conține un director `models/` sau `views/` — nu există componente tehnice proprii de documentat.

#### 5. Conexiuni

- `deltatech_service_agreement`: modulul către care a fost mutată gestiunea efectivă a acordurilor de service; este singura dependență și succesorul funcțional al acestui modul învechit.
