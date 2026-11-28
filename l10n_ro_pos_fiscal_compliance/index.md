# Romania - Conformitate fiscală POS (AMEF) (localizat la `l10n_ro_pos_fiscal_compliance/index.md`)

- **Nume Tehnic:** `l10n_ro_pos_fiscal_compliance`
- **Versiune:** `20.0.2.4.2`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_pos_fiscal_compliance](https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_pos_fiscal_compliance)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_pos_fiscal_compliance`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul asigură conformitatea fiscală a vânzării cu amănuntul prin POS, conform OUG 28/1999 privind aparatele de marcat electronice fiscale (AMEF). Completează POS-ul Odoo și driverele de fiscalizare (ex. `deltatech_pos`) cu evidența fiscală cerută în România: bonul fiscal urmărit pe fiecare comandă, blocarea închiderii sesiunii când există comenzi plătite fără bon, raportul Z reconciliat cu vânzările și încasările, returul fiscal legat de bonul inițial și arhiva jurnalului electronic AMEF, importată și reconciliată bon cu bon. Comunicarea cu aparatul fizic se face printr-un driver opțional; modulul nu depinde de un driver anume și nu modifică contabilitatea POS.

#### 2. Funcționalități Cheie

- **Urmărirea bonului fiscal** pe fiecare comandă POS: serie, număr, dată/oră fiscală și stare (de fiscalizat / emis / eroare), în fila „Fiscalizare AMEF" a comenzii; răspunsul aparatului intră prin metoda publică `_l10n_ro_apply_fiscal_response()` sau manual, cu **Înregistrează bon fiscal**. O eroare poate fi marcată ca justificată.
- **Activare pe punct de lucru** în **Punct de vânzare → Configurare → Setări**, secțiunea „Conformitate fiscală RO (AMEF)": Fiscalizare AMEF obligatorie, seria aparatului și NUI-ul aparatului (10 cifre, cel din fișierele ANAF, folosit la potrivirea bonurilor din jurnal).
- **Blocarea închiderii sesiunii** cât timp există comenzi plătite fără bon emis și fără eroare justificată.
- **Raportul Z fiscal** (**Punct de vânzare → Fiscalizare AMEF → Rapoarte Z**), calculat din sesiune pe cote TVA și metode de plată, comparat cu valorile declarate de aparat; starea „Reconciliat" sau „Diferențe".
- **Raport „Vânzări TVA pe casă de marcat"**: pivot/listă pe punct de lucru, cotă TVA și lună, din liniile de TVA ale rapoartelor Z reconciliate sau închise, cu export XLSX. Este calculat din datele Odoo, nu din arhiva oficială; vânzările scutite sau cu taxe fixe apar cumulat pe cota „0", iar retururile nu intră (se raportează prin factura storno).
- **Returul fiscal** care referențiază bonul inițial.
- **Import al arhivei jurnalului electronic AMEF** (`.zip` cu fișiere `.p7b`, citite fără certificat sau cheie privată): bonurile se potrivesc cu comenzile pe aparat, numărul bonului în Z și zi; raportul Z al fiecărei zile se completează și se reconciliază automat (total, plăți pe tip ANAF, valoare și TVA pe cotă). Observațiile semnalează abateri de coerență internă, iar fișierul OPIS indică rapoartele Z lipsă.
- **Discrepanțe pe bonuri:** Reconciliat, Sumă diferită, TVA diferit, Lipsă în Odoo, Lipsă în arhiva fiscală; returul (total negativ) nu se semnalează. După lămurire, jurnalul se arhivează.
- **Preluare automată din e-mail (FiscalWire):** aliasul `fiscalwire@<domeniu>` creează câte o arhivă per aparat (după NUI) și rulează importul; un Z deja importat nu se reimportă. Grupul „AMEF: notificări la importul din e-mail" primește rezultatul în chatter și, la probleme, o activitate; trimiterea e-mailului se reglează prin parametrii `amef_notify_mode` (`never` / `problems` / `always`) și `amef_notify_activity`.

#### 3. Dependențe

- `mail`
- `point_of_sale`
- `account`
- `l10n_ro`

Dependență externă Python (nu modul Odoo): `asn1crypto`, pentru decodarea CMS/PKCS7 a fișierelor `.p7b`.

#### 4. Componente Cheie

**Modele**

- `pos.order` (extindere): câmpurile de bon fiscal (serie, număr, dată/oră, stare) și referința la bonul inițial pentru retur.
- `pos.config` / `res.config.settings` (extindere): fiscalizare obligatorie, seria și NUI-ul aparatului pe punct de lucru.
- `pos.payment.method` (extindere): corespondența metodei de plată cu tipul de plată ANAF, folosită la reconcilierea plăților declarate.
- `pos.session` (extindere): blocarea închiderii cât timp există comenzi nefiscalizate.
- `l10n.ro.pos.z.report` (+ `l10n.ro.pos.z.report.vat.line`, `l10n.ro.pos.z.report.payment.line`): raportul Z cu valori calculate vs. declarate și reconciliere; liniile de TVA alimentează raportul de vânzări pe casă de marcat.
- `l10n.ro.amef.journal`: jurnalul electronic AMEF (arhivă, perioadă, punct de lucru, aparat); importul, parsarea, reconcilierea și arhivarea, cu chatter și activități pentru notificările din e-mail.
- `l10n.ro.amef.journal.bon`: o linie per bon din arhivă, cu starea potrivirii cu `pos.order`.
- `l10n_ro_amef_parser` (modul Python): extragerea XML din `.p7b`, parsarea raportului Z și a fișierului OPIS.

**Vizualizări**

- `pos_config_views.xml`: secțiunea „Conformitate fiscală RO (AMEF)" în setările POS.
- `pos_payment_method_views.xml`: tipul de plată ANAF pe metoda de plată.
- `pos_order_views.xml`: fila „Fiscalizare AMEF" pe comanda POS.
- `l10n_ro_pos_z_report_views.xml`: formularul și lista raportului Z, cu reconcilierea.
- `l10n_ro_pos_z_report_summary_views.xml`: pivot/listă „Vânzări TVA pe casă de marcat".
- `l10n_ro_amef_journal_views.xml`: formularul jurnalului AMEF (Importă arhiva, Arhivează, Resetează, bonuri, Z lipsă, buton de discrepanțe).
- `pos_menus.xml`: meniul „Fiscalizare AMEF" cu Rapoarte Z, Vânzări TVA pe casă de marcat, Jurnale electronice AMEF și Discrepanțe bonuri fiscale.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron` sau acțiuni server. Modulul livrează aliasul de e-mail `fiscalwire` (`data/mail_alias.xml`) care declanșează importul la primirea unui mesaj, grupul de notificare și parametrii de sistem aferenți. Restul procesării rulează la apăsarea butoanelor jurnalului.

#### 5. Conexiuni

- [deltatech_pos](../deltatech_pos/index.md): driver de fiscalizare POS care poate apela metoda publică de înregistrare a răspunsului fiscal (integrare opțională).
- [deltatech_ecr_fiscal](../deltatech_ecr_fiscal/index.md): modelul fiscal al driverului, pe care îl conectează puntea.
- [l10n_ro_pos_fiscal_compliance_ecr](../l10n_ro_pos_fiscal_compliance_ecr/index.md): puntea care duce răspunsul casei de marcat în starea fiscală de aici.
- [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md): agregă bonurile fiscale POS în D394, dacă este instalat.
- [l10n_ro_pos_returns](../l10n_ro_pos_returns/index.md): factura de retur pentru bonurile de retur; preia trimiterea la bonul fiscal inițial.
