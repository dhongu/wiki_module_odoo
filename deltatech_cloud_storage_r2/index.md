# Cloud Storage Cloudflare R2

- **Nume Tehnic:** `deltatech_cloud_storage_r2`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_cloud_storage_r2
- **Cale Locală:** `odoo-addons/bitshop/deltatech_cloud_storage_r2`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă **Cloudflare R2** (și orice alt serviciu compatibil S3) ca furnizor al cadrului *Cloud Storage* din Odoo. Atașamentele mari din chatter se încarcă din browser direct în bucket printr-un URL presemnat (AWS Signature V4, semnat cu biblioteca standard Python, fără dependențe) și se descarcă la fel, deci nu trec prin serverul Odoo (cu excepția descărcării mai multor atașamente împreună ca zip).

#### 2. Funcționalități Cheie

- Cloudflare R2: sunt necesare doar account ID, bucket și un token API (access key + secret); R2 nu are taxe de egress.
- Alte servicii S3-compatibile (Hetzner Object Storage, AWS S3, Bunny...) prin endpoint și regiune personalizate; pentru Hetzner regiunea se ia din endpoint (se folosește endpoint-ul locației, nu adresa bucket-ului din consola Hetzner). Backblaze B2 are furnizor propriu în `deltatech_cloud_storage_b2`.
- Domeniu public personalizat opțional pentru descărcări (descărcările devin nesemnate; doar pentru bucket-uri publice și doar pentru fișierele bucket-ului curent).
- Secretul (secret access key) e doar la scriere: nu e trimis înapoi în browser și nu apare în loguri. Se lasă gol pentru a păstra secretul salvat.
- Se semnează doar bucket-urile folosite de baza de date (parametrul de sistem `cloud_storage_r2_known_locations`, câte un `<host>/<bucket>` pe linie, completat la salvarea setărilor); un atașament către alt host sau bucket e refuzat. După upgrade la 20.0.1.0.5 se verifică logul: un bucket de pe alt host trebuie adăugat manual.
- Verificare conexiune la salvare (încărcare, descărcare, ștergere obiect `TEST`) și setare CORS pe cât posibil; dacă Odoo setează CORS, înlocuiește toată configurația CORS a bucket-ului, deci cu reguli proprii se setează manual.
- Se bifează și *Upload Record Attachments*, altfel Odoo 20 păstrează atașamentele din chatter în baza de date.
- Curățare obiecte nefolosite: Odoo nu șterge niciodată obiectele din bucket, iar scriptul `utils/cleanup_cloud_storage_r2.py` din `deltatech_cloud_storage_s3` (rulare „dry run” implicit, `--delete` pentru ștergere, păstrează obiectele mai noi de 24 h) șterge orfanii; ștergerea e ireversibilă, un bucket trebuie să aparțină unei singure baze Odoo, iar `ODOO_LOGIN` trebuie să fie administrator de setări.
- Motorul S3 (semnare, verificări, bucket-uri cunoscute, script de curățare) se află în `deltatech_cloud_storage_s3`, instalat odată cu acest modul și comun cu furnizorii Backblaze B2 și Hetzner. Detalii pas-cu-pas în fișa consultantului.

#### 3. Dependențe

- `deltatech_cloud_storage_s3`

#### 4. Componente Cheie

**Modele**

- `ir.attachment` (extins): logica furnizorului R2 / S3-compatibil pentru atașamente în cloud.
- `res.config.settings` (extins): câmpurile și verificările de la salvare.

**Vizualizări**

- Câmpurile furnizorului în *Setări generale > Cloud Storage* (modulul nu are fișiere de vizualizare proprii).

**Acțiuni Automate / Acțiuni Server**

- Nu are cron sau acțiuni server. Modulul definește un `uninstall_hook` și un script de migrare `post-migrate.py` pentru versiunea 20.0.1.0.5 (completarea bucket-urilor cunoscute).

#### 5. Conexiuni

- `deltatech_cloud_storage_b2`: furnizorul Backblaze B2, pe același motor S3.
- `deltatech_cloud_storage_hetzner`: furnizorul Hetzner Object Storage, pe același motor S3.
