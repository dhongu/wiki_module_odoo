# Cloud Storage S3 Engine

- **Nume Tehnic:** `deltatech_cloud_storage_s3`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_cloud_storage_s3
- **Cale Locală:** `odoo-addons/bitshop/deltatech_cloud_storage_s3`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Motorul S3 comun al furnizorilor Terrabit pentru cadrul *Cloud Storage* din Odoo. Nu adaugă singur un furnizor: se instalează automat odată cu modulul furnizorului ales (Cloudflare R2, Backblaze B2 sau Hetzner Object Storage). Fișierele ajung direct din browser în bucket, fără să treacă prin serverul Odoo.

#### 2. Funcționalități Cheie

- Adrese presemnate de încărcare și descărcare (AWS Signature Version 4, doar biblioteca standard Python, fără dependențe externe).
- Cheia secretă de acces este doar pentru scriere: nu se trimite înapoi în browser și nu apare în jurnale.
- Se semnează doar bucket-urile folosite de baza de date (`cloud_storage_r2_known_locations`); un atașament către alt host sau alt bucket este refuzat.
- Verificarea conexiunii la salvare (încărcare, descărcare și ștergere a unui obiect `TEST`) și configurarea CORS, în măsura posibilului.
- Trecerea între furnizori pe același endpoint păstrează atașamentele lizibile; un alt endpoint este refuzat cât timp există atașamente.
- Script de curățare `utils/cleanup_cloud_storage_r2.py`: listează bucket-ul și șterge obiectele nefolosite de Odoo (implicit doar simulare).
- Configurarea se face din *Setări > Setări generale > Cloud Storage*, în modulul furnizorului; un furnizor nou își adaugă cheia în `ir.attachment._get_cloud_storage_r2_providers()`.

#### 3. Dependențe

- `cloud_storage`

#### 4. Componente Cheie

**Modele**

- `ir.attachment` (extins): semnarea adreselor S3, lista furnizorilor și a locațiilor cunoscute.
- `res.config.settings` (extins): opțiunea `cloud_storage_provider` și parametrii comuni ai furnizorilor.

**Vizualizări**

- `cloud_storage_r2_config_settings_view_form`: rândurile comune de setări (bucket, chei) în secțiunea Cloud Storage din setările generale.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni automate; are `uninstall_hook`.

#### 5. Conexiuni

- `deltatech_cloud_storage_r2`: furnizor Cloudflare R2 sau alt serviciu compatibil S3.
- `deltatech_cloud_storage_b2`: furnizor Backblaze B2.
- `deltatech_cloud_storage_hetzner`: furnizor Hetzner Object Storage.
