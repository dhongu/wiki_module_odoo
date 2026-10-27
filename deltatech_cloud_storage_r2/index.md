# Cloud Storage Cloudflare R2 (localizat la `deltatech_cloud_storage_r2/index.md`)

- **Nume Tehnic:** `deltatech_cloud_storage_r2`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_cloud_storage_r2
- **Cale Locală:** `odoo-addons/bitshop/deltatech_cloud_storage_r2`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

> Modulul a fost redenumit din `cloud_storage_r2` în `deltatech_cloud_storage_r2` (prefix Terrabit, `[MOV]`, 2026-10-25, versiunea 19.0.1.0.3). Există momentan doar pe branch-ul 19.0 al suitei bitshop; nu este încă migrat pe 20.0.

#### 1. Sumar

Adaugă **Cloudflare R2** (și orice alt serviciu compatibil S3) ca furnizor în cadrul framework-ului Odoo *Cloud Storage*, alături de furnizorii Google și Azure livrați cu Odoo. Atașamentele mari din chatter sunt încărcate direct din browser în bucket, prin URL-uri presemnate, iar descărcarea se face la fel, deci fișierele nu mai trec prin serverul Odoo. R2 nu are taxe de egress, ceea ce reduce costul de stocare și transfer.

#### 2. Funcționalități Cheie

- Încărcare și descărcare directă browser ↔ bucket, cu URL-uri presemnate AWS Signature Version 4, semnate cu biblioteca standard Python (fără dependențe externe).
- Cloudflare R2: sunt necesare doar ID-ul contului, bucket-ul și un token API (access key + secret).
- Alte servicii compatibile S3 (Backblaze B2, AWS S3, Bunny etc.) prin endpoint personalizat și regiune, în locul ID-ului de cont.
- Domeniu public personalizat opțional pentru descărcări; descărcările devin nesemnate, deci se folosește doar pentru un bucket intenționat public.
- Cheia secretă este write-only: nu e trimisă înapoi în browser și nu apare în loguri; lăsând câmpul gol se păstrează secretul salvat.
- Configurare în *Setări > Integrări > Cloud Storage*, alegând furnizorul **Cloudflare R2 / S3-compatible**.
- La salvare se verifică conexiunea (încărcare, descărcare și ștergere a unui obiect `TEST`) și se încearcă setarea automată a regulilor CORS; dacă nu reușește, politica CORS se adaugă manual în bucket. Tokenul R2 are nevoie de drepturi *Object Read & Write* (plus *Admin* pentru CORS automat).
- Avertisment la schimbarea bucket-ului sau a endpoint-ului: atașamentele existente rămân în bucket-ul în care au fost create.
- Script de curățare `utils/cleanup_cloud_storage_r2.py`: Odoo nu șterge obiectele din bucket la ștergerea atașamentelor, iar scriptul (XML-RPC, cu cheie API) listează bucket-ul, verifică în Odoo ce obiecte mai sunt referite și le șterge pe celelalte. Rulează implicit în mod dry run (ștergere doar cu `--delete`), atinge doar chei de forma `<id>/<uuid>/<nume>` și păstrează obiectele mai noi de 24 de ore (`--min-age-hours`).
- Ghidul pas-cu-pas, cu capturi de ecran, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `cloud_storage`

#### 4. Componente Cheie

**Modele**

- `res.config.settings` (extins): câmpurile de configurare R2/S3 (bucket, endpoint, regiune, ID cont, chei, domeniu public), avertisment la schimbarea bucket-ului, verificarea conexiunii și setarea CORS la salvare.
- `ir.attachment` (extins): generează URL-urile și URL-urile presemnate SigV4 pentru obiectele din bucket și extrage informațiile bucket/blob din URL-ul atașamentului.

**Vizualizări**

- `cloud_storage_r2_config_settings_view_form`: extinde formularul de setări Cloud Storage cu opțiunile furnizorului R2 / S3-compatible.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server. Are `uninstall_hook` (blochează dezinstalarea cât timp există atașamente cloud și curăță parametrii de configurare) și `data/neutralize.sql` (șterge parametrii R2 la neutralizarea bazelor de date).

#### 5. Conexiuni

- `cloud_storage`: framework-ul Odoo Cloud Storage pe care modulul îl extinde cu un furnizor nou, alături de Google și Azure.
