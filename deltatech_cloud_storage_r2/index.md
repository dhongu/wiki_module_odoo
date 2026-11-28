# Cloud Storage Cloudflare R2 (localizat la `deltatech_cloud_storage_r2/index.md`)

- **Nume Tehnic:** `deltatech_cloud_storage_r2`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_cloud_storage_r2
- **Cale Locală:** `odoo-addons/bitshop/deltatech_cloud_storage_r2`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

> Modulul a fost redenumit din `cloud_storage_r2` în `deltatech_cloud_storage_r2` (prefix Terrabit, `[MOV]`, 2026-10-25, versiunea 19.0.1.0.3). Există momentan doar pe branch-ul 19.0 al suitei bitshop; nu este încă migrat pe 20.0.
>
> Din 19.0.1.1.0, motorul S3 (semnare, verificarea conexiunii, CORS, locațiile cunoscute, scriptul de curățare, rândurile din setări) este în modulul `deltatech_cloud_storage_s3`, instalat automat la actualizare; acest modul păstrează doar furnizorul Cloudflare R2 / S3-compatible. Parametrii de sistem își păstrează numele, deci nu se migrează date. Preț: 10 EUR, plus 10 EUR pentru motor.

#### 1. Sumar

Adaugă **Cloudflare R2** (și orice alt serviciu compatibil S3) ca furnizor în cadrul framework-ului Odoo *Cloud Storage*, alături de furnizorii Google și Azure livrați cu Odoo. Atașamentele mari din chatter sunt încărcate direct din browser în bucket, prin URL-uri presemnate, iar descărcarea se face la fel, deci fișierele nu mai trec prin serverul Odoo (cu excepția descărcării mai multor atașamente împreună, ca arhivă zip). R2 nu are taxe de egress, ceea ce reduce costul de stocare și transfer.

#### 2. Funcționalități Cheie

- Încărcare și descărcare directă browser ↔ bucket, cu URL-uri presemnate AWS Signature Version 4, semnate cu biblioteca standard Python (fără dependențe externe).
- Cloudflare R2: sunt necesare doar ID-ul contului, bucket-ul și un token API (access key + secret).
- Alte servicii compatibile S3 (Hetzner Object Storage, AWS S3, Bunny etc.) prin endpoint personalizat și regiune, în locul ID-ului de cont. Pentru Hetzner, regiunea se ia din endpoint (`https://<locație>.your-objectstorage.com`), deci câmpul *Region* poate rămâne gol; adresa bucket-ului afișată de consola Hetzner este refuzată, iar mesajul indică endpoint-ul corect. Backblaze B2 are furnizor propriu în `deltatech_cloud_storage_b2`.
- Domeniu public personalizat opțional pentru descărcări; descărcările devin nesemnate, deci se folosește doar pentru un bucket intenționat public, iar opțiunea se aplică doar fișierelor din bucket-ul curent.
- Cheia secretă este write-only: nu e trimisă înapoi în browser și nu apare în loguri; lăsând câmpul gol se păstrează secretul salvat.
- Se semnează doar bucket-urile folosite de baza de date (parametrul de sistem `cloud_storage_r2_known_locations`, câte un `<host>/<bucket>` pe linie, completat la salvarea setărilor); un atașament care indică altă gazdă sau alt bucket este refuzat. După actualizarea la 19.0.1.0.5, o locație de pe altă gazdă (un endpoint sau un cont R2 anterior) se verifică în log și se adaugă manual.
- Configurare în *Setări > Setări generale > Cloud Storage*, alegând furnizorul **Cloudflare R2 / S3-compatible**; trebuie bifat și **Upload Record Attachments**, altfel Odoo 19 ține atașamentele din chatter în baza de date.
- La salvare se verifică conexiunea (încărcare, descărcare și ștergere a unui obiect `TEST`) și se încearcă setarea automată a regulilor CORS; când le setează singur, Odoo înlocuiește întreaga configurație CORS a bucket-ului. Dacă nu reușește, sau bucket-ul are reguli proprii, politica CORS se adaugă manual. Tokenul R2 are nevoie de drepturi *Object Read & Write* (plus *Admin* pentru CORS automat).
- Avertisment la schimbarea bucket-ului sau a endpoint-ului: atașamentele existente rămân în bucket-ul în care au fost create și rămân accesibile doar dacă vechiul bucket e încă disponibil cu credențialele curente. Atașamentele locale existente pot fi mutate cu modulul standard `cloud_storage_migration` (nu e dependență).
- Trecerea între doi furnizori ai acestui motor e permisă cât timp există atașamente doar dacă endpoint-ul rămâne același; alt endpoint este refuzat.
- Script de curățare `utils/cleanup_cloud_storage_r2.py` (acum în `deltatech_cloud_storage_s3`): Odoo nu șterge obiectele din bucket la ștergerea atașamentelor, iar scriptul (XML-RPC, cu cheie API, utilizator administrator de setări) listează bucket-ul, verifică în Odoo ce obiecte mai sunt referite și le șterge pe celelalte. Rulează implicit în mod dry run (ștergere doar cu `--delete`, ireversibilă), atinge doar chei de forma `<id>/<uuid>/<nume>` și păstrează obiectele mai noi de 24 de ore (`--min-age-hours`). Un bucket trebuie să aparțină unei singure baze Odoo, altfel obiectele celeilalte baze sunt șterse ca nefolosite.
- Ghidul pas-cu-pas, cu capturi de ecran, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `deltatech_cloud_storage_s3`

#### 4. Componente Cheie

**Modele**

- `res.config.settings` (extins): adaugă furnizorul **Cloudflare R2 / S3-compatible** în selecția `cloud_storage_provider` și verifică endpoint-ul personalizat la salvare (doar acest furnizor îl primește de la utilizator). Câmpurile de configurare, verificarea conexiunii și setarea CORS sunt în motorul S3.
- `ir.attachment` (extins): înregistrează furnizorul `r2` în lista furnizorilor semnați prin API-ul S3 (`_get_cloud_storage_r2_providers`); generarea URL-urilor presemnate SigV4 este în motorul S3.

**Vizualizări**

- Modulul nu mai definește vizualizări proprii; rândurile din setările Cloud Storage sunt în `deltatech_cloud_storage_s3`.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server. Are `uninstall_hook` (blochează dezinstalarea cât timp există atașamente cloud și resetează furnizorul când acesta este R2) și o migrare `19.0.1.0.5/post-migrate.py` (înregistrează bucket-urile atașamentelor existente).

#### 5. Conexiuni

- `cloud_storage`: framework-ul Odoo Cloud Storage pe care motorul S3 îl extinde cu un furnizor nou, alături de Google și Azure.
- `deltatech_cloud_storage_s3`: motorul S3 comun (semnare, verificări, CORS, script de curățare), partajat cu furnizorii Backblaze B2 și Hetzner. (Nu are încă pagină wiki.)
- `deltatech_cloud_storage_b2`: furnizor Backblaze B2 pe același motor. (Nu are încă pagină wiki.)
- `deltatech_cloud_storage_hetzner`: furnizor Hetzner Object Storage pe același motor. (Nu are încă pagină wiki.)
- `cloud_storage_migration`: modul standard Odoo pentru mutarea atașamentelor locale existente în bucket (nu e dependență).
