# Download File (localizat la `deltatech_download/index.md`)

- **Nume Tehnic:** `deltatech_download`
- **Versiune:** `20.0.0.1.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_download
- **Cale Locală:** `odoo-addons/deltatech/deltatech_download`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Implicit, Odoo descarcă fiecare raport PDF ca fișier, iar utilizatorul trebuie să-l deschidă din folderul de descărcări. Cu acest modul, rapoartele PDF se deschid direct într-o filă nouă a browserului, gata de citit sau tipărit, fără a aglomera folderul de descărcări.

#### 2. Funcționalități Cheie

- **Rapoarte PDF într-o filă nouă**: facturi, oferte, avize de livrare și orice alt raport PDF se deschid în vizualizatorul PDF al browserului în loc să fie descărcate.
- **Descărcare directă per raport**: rapoartele care trebuie totuși salvate ca fișier pot fi marcate pentru descărcare directă, unul câte unul.
- **Mobil și IoT neschimbate**: pe telefoane și tablete, precum și pentru rapoartele tipărite printr-un IoT Box, rămâne comportamentul standard Odoo.
- **Compatibil cu blocarea ferestrelor pop-up**: dacă browserul blochează fila nouă, utilizatorul nu este oprit de o eroare.
- Nu necesită configurare. Pentru a păstra descărcarea standard la un raport: modul dezvoltator, **Setări > Tehnic > Acțiuni > Rapoarte**, deschideți raportul și bifați **Direct Download**.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md` și `readme/CONFIGURE.md`, care nu cer explicit analiza componentelor; analiza detaliată a codului a fost omisă conform schemei.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină wiki existentă.
