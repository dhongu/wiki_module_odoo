# Romania - SPV Messages for Odoo Online (localizat la `l10n_ro_message_spv_online/index.md`)

- **Nume Tehnic:** `l10n_ro_message_spv_online`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_message_spv_online
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_message_spv_online`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Registru al mesajelor e-Factura (SPV) pentru instanțele **Odoo Online**, unde nu se pot instala module cu cod Python. Modulul nu are deloc cod Python și se importă ca arhivă zip (Aplicații > Importă modul). Lucrează peste modulul standard românesc de e-Factura (`l10n_ro_edi`), care trimite facturile și descarcă facturile de la furnizori, și doar afișează, într-un singur loc, ceea ce modulul standard păstrează deja.

#### 2. Funcționalități Cheie

- **Meniul „SPV Messages”** în Contabilitate (Facturare): ultimul mesaj SPV al fiecărei facturi trimise și al fiecărei facturi primite, grupat implicit pe stare (*Sent*, *Validated*, *Error*).
- **Filtre**: trimise / primite, în așteptarea ANAF, validate, respinse, cu mesaj de eroare, după dată; grupare după stare, direcție, partener sau lună.
- **Formularul mesajului**: factura, partenerul, totalul, mesajul ANAF, cheia de descărcare, XML-ul mesajului (factura trimisă sau semnătura ANAF) și fișierele facturii (XML și PDF pentru o factură primită), toate descărcabile. Lista afișează partenerul și data facturii; totalul apare pe formular.
- **Factură respinsă**: câmpul *Message* arată motivul ANAF; factura se corectează și se retrimite din factură, ca în modulul standard. Pe o factură aflată în așteptare, *Fetch status* interoghează ANAF doar pentru acea factură.
- **Synchronize now**: rulează sincronizarea standard cu SPV (starea facturilor trimise, facturi noi de la furnizori, create ca ciorne) fără a aștepta acțiunea programată. Pe o companie fără CUI sau fără token SPV, indică ce trebuie configurat întâi; butonul e pentru utilizatorii cu drepturi de facturare.
- **Precondiție**: compania are CUI și este conectată la SPV în *Facturare > Configurare > Setări*, blocul **Romanian E-Factura** (Client ID, Client Secret, **Generate Token**).
- **Limite**: nu potrivește produsele după codul furnizorului și nu creează parteneri din CUI; pe un server cu Python, aceste funcții le oferă modulul OCA `l10n_ro_message_spv`. Tokenul ANAF rămâne în baza de date proprie; în afara sincronizării standard cu SPV, modulul nu trimite date nicăieri.
- Modul **Alpha**, incompatibil (`excludes`) cu `l10n_ro_message_spv`. Fluxul pas cu pas este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

Fără modele proprii și fără Python; extinde modelul standard prin câmpuri create din date (`ir.model.fields`).

- `l10n_ro_edi.document` (din `l10n_ro_edi`): primește câmpurile manuale `x_partner_id`, `x_invoice_date`, `x_currency_id`, `x_amount_total`, `x_received`, `x_attachment_name` și `x_invoice_attachment_ids`.

**Vizualizări**

- `view_l10n_ro_edi_document_list`: lista mesajelor, cu partener, data facturii și starea ca insignă.
- `view_l10n_ro_edi_document_form`: formularul mesajului, cu bară de stare, mesaj ANAF și fișiere descărcabile.
- `view_l10n_ro_edi_document_search`: filtrele și grupările din secțiunea 2.
- `action_spv_messages`: acțiunea ferestrei „SPV Messages”, legată de meniul din Contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `action_spv_synchronize` („Synchronize now”): acțiune server (cod) care lansează sincronizarea standard cu SPV pentru compania curentă; nu există `ir.cron` propriu.

#### 5. Conexiuni

- `l10n_ro_message_spv` (OCA): varianta pentru servere cu Python, cu potrivirea produselor și crearea partenerilor; exclusă reciproc cu acest modul.
- [l10n_ro_message_spv_purchase](../l10n_ro_message_spv_purchase/index.md): extensie a registrului SPV pe partea de achiziții, pentru varianta cu Python.
- [l10n_ro_message_spv_self_billing](../l10n_ro_message_spv_self_billing/index.md): autofacturare pe mesajele SPV, pentru varianta cu Python.
