# Cloud Storage Backblaze B2

- **Nume Tehnic:** `deltatech_cloud_storage_b2`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_cloud_storage_b2
- **Cale Locală:** `odoo-addons/bitshop/deltatech_cloud_storage_b2`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă **Backblaze B2** ca furnizor al cadrului *Cloud Storage* din Odoo, alături de Google, Azure și Cloudflare R2. Atașamentele mari din chatter se încarcă din browser direct în bucket-ul B2 printr-un URL presemnat, deci nu trec prin serverul Odoo și nu umplu filestore-ul.

#### 2. Funcționalități Cheie

- În setări se alege **Backblaze B2** și se completează doar bucket-ul, endpoint-ul bucket-ului și o cheie de aplicație; regiunea de semnare se citește din endpoint.
- Verificări specifice B2 la salvare: endpoint-ul trebuie să fie unul S3 de B2, iar o conexiune refuzată explică faptul că cheia master nu funcționează cu API-ul S3.
- Un bucket B2 configurat deja prin furnizorul „Cloudflare R2 / S3-compatible” cu endpoint personalizat trece la *Backblaze B2* (același endpoint) împreună cu atașamentele; trecerea la alt endpoint e refuzată cât există atașamente.
- Construit pe motorul S3 `deltatech_cloud_storage_s3` (fără modulul R2): secret doar la scriere, semnare doar pentru bucket-urile folosite de baza de date, verificare conexiune, setare CORS pe cât posibil, script de curățare a obiectelor nefolosite.
- Configurare (detalii în fișa consultantului): bucket **privat**, cheie de aplicație cu Read and Write restrânsă la bucket (nu cheia master); în *Setări > Setări generale > Cloud Storage* se bifează și *Upload Record Attachments*; CORS se setează manual în B2 (cheia restrânsă nu poate); lifecycle „Keep only the last version of the file”, fiindcă B2 păstrează toate versiunile.
- Descărcările nu forțează disposition-ul *attachment* pe B2; numele fișierului rămâne cel al atașamentului.

#### 3. Dependențe

- `deltatech_cloud_storage_s3`

#### 4. Componente Cheie

**Modele**

- `ir.attachment` (extins): logica furnizorului B2 pentru atașamente în cloud.
- `res.config.settings` (extins): câmpurile și verificările de la salvare pentru B2.

**Vizualizări**

- `views/settings.xml`: câmpurile B2 în *Setări generale > Cloud Storage*.

**Acțiuni Automate / Acțiuni Server**

- Nu are. Modulul definește un `uninstall_hook`.

#### 5. Conexiuni

- `deltatech_cloud_storage_r2`: furnizorul Cloudflare R2 / S3-compatibil, pe același motor S3 (modulul R2 nu e necesar pentru B2).
- `deltatech_cloud_storage_hetzner`: furnizorul Hetzner Object Storage, pe același motor S3.
