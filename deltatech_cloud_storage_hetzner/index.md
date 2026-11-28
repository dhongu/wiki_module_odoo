# Cloud Storage Hetzner Object Storage

- **Nume Tehnic:** `deltatech_cloud_storage_hetzner`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_cloud_storage_hetzner
- **Cale Locală:** `odoo-addons/bitshop/deltatech_cloud_storage_hetzner`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă **Hetzner Object Storage** ca furnizor al cadrului *Cloud Storage* din Odoo. Atașamentele mari din chatter se încarcă din browser direct într-un bucket Hetzner printr-un URL presemnat și se descarcă la fel, deci nu umplu filestore-ul Odoo.

#### 2. Funcționalități Cheie

- Se alege furnizorul **Hetzner Object Storage** și locația (Falkenstein `fsn1`, Nuremberg `nbg1`, Helsinki `hel1`); endpoint-ul și regiunea de semnare sunt completate de Odoo. Câmpurile specifice R2 (account ID, endpoint personalizat, regiune, domeniu public) nu apar.
- Sunt necesare doar numele bucket-ului și credențialele S3 ale proiectului Hetzner.
- La salvare: verificare conexiune (încărcare, descărcare și ștergere a unui obiect `TEST`) și setarea regulii CORS (înlocuiește regulile CORS existente ale bucket-ului). Dacă Hetzner refuză cheile, eroarea se afișează și nu se salvează nimic.
- Schimbarea locației sau a bucket-ului unei configurații salvate afișează avertismentul *Bucket changed*: fișierele existente nu se mută și rămân lizibile cât timp bucket-ul vechi e accesibil cu cheile curente.
- Cu *Upload Record Attachments* bifat, atașamentele din chatter mai mari decât *Minimum File Size* merg în bucket; utilizatorii reîncarcă pagina (F5) după salvarea setărilor.
- Atașamentele locale existente se mută cu modulul standard `cloud_storage_migration`. O bază care a folosit furnizorul „Cloudflare R2 / S3-compatible” cu endpoint Hetzner poate trece la acest furnizor (aceeași locație) fără migrarea atașamentelor; alte treceri sunt refuzate cât există atașamente în cloud.
- Atenție: credențialele S3 ale unui proiect Hetzner citesc și scriu toate bucket-urile proiectului; se recomandă un proiect per client sau restricție prin bucket policy. Detalii pas-cu-pas în fișa consultantului.

#### 3. Dependențe

- `deltatech_cloud_storage_s3`

#### 4. Componente Cheie

**Modele**

- `ir.attachment` (extins): logica furnizorului Hetzner pentru atașamente în cloud.
- `res.config.settings` (extins): câmpurile (locație, bucket, chei) și verificările de la salvare.

**Vizualizări**

- `views/settings.xml`: câmpurile Hetzner în *Setări generale > Cloud Storage*.

**Acțiuni Automate / Acțiuni Server**

- Nu are. Modulul definește un `uninstall_hook`.

#### 5. Conexiuni

- `deltatech_cloud_storage_r2`: furnizorul Cloudflare R2 / S3-compatibil, pe același motor S3.
- `deltatech_cloud_storage_b2`: furnizorul Backblaze B2, pe același motor S3.
