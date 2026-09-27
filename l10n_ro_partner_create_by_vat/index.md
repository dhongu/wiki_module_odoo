# Romania - Partner Create by VAT (localizat la `l10n_ro_partner_create_by_vat/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_create_by_vat`
- **Versiune:** `20.0.0.9.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_partner_create_by_vat
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_partner_create_by_vat`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Modulul completează automat fișa unui partener pe baza codului de TVA (CUI/CIF): operatorul introduce doar CUI-ul unei firme românești, iar Odoo interoghează în timp real serviciul web al ANAF pentru a prelua denumirea, adresa, codul CAEN, telefonul și starea de plătitor de TVA a firmei. Astfel se elimină introducerea manuală a datelor de identificare ale unui partener nou și se reduc riscurile de greșeală (nume incorect, adresă incompletă, CUI invalid), în special la înregistrarea rapidă a unor furnizori sau clienți noi.

#### 2. Funcționalități Cheie

- La completarea câmpului CUI/CIF pe fișa partenerului (când țara e România), datele sunt preluate automat de la ANAF și se scriu în: denumire, adresă (stradă, localitate, județ, cod poștal), telefon, cod CAEN, număr de înregistrare la Registrul Comerțului și indicatorul "plătitor de TVA" (`l10n_ro_vat_subjected`) — CUI-ul primește automat prefixul `RO` dacă firma e plătitoare de TVA.
- Câmpul "Romania - Old Name" (`l10n_ro_old_name`) poate fi completat manual cu denumirea anterioară a firmei; dacă la o interogare ulterioară ANAF întoarce tot vechea denumire, actualizarea automată e ignorată (util când firma și-a schimbat numele, dar baza ANAF nu e încă la zi).
- Istoric "ANAF - Active State History": la fiecare schimbare a stării de inactivitate a firmei raportată de ANAF (dată inactivare/reactivare/publicare/radiere, act de autorizare, stare înregistrare), se adaugă automat o linie nouă în tab-ul de informații ANAF de pe fișa partenerului — istoricul nu duplică o intrare deja existentă cu aceleași date.
- Istoric "ANAF - VAT Subjected History": la fel, se păstrează istoricul perioadelor de înregistrare/radiere ca plătitor de TVA (dată început, dată sfârșit, an fiscal, mesaj ANAF), cu o linie per perioadă raportată de ANAF.
- Interogarea ANAF (`res.partner._get_Anaf`) e configurabilă din Setări → Tehnic → Parametri → Parametri de Sistem, prin trei chei opționale (cu valori implicite funcționale fără nicio configurare): `l10n_ro_partner_create_by_vat.anaf_url` (endpoint-ul ANAF), `l10n_ro_partner_create_by_vat.anaf_api_key` (cheie API, dacă ANAF impune autentificare — aceeași cheie e reutilizată și de sincronizarea în masă din `l10n_ro_fiscal_validation`) și `l10n_ro_partner_create_by_vat.anaf_api_key_header_tag` (numele header-ului HTTP care transportă cheia, implicit `x-api-key`).
- Dacă ANAF nu găsește firma sau serviciul web nu răspunde, utilizatorul primește un avertisment pe formular (mesajul de eroare returnat de ANAF), fără a bloca introducerea manuală a datelor.

#### 3. Dependențe

- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): adaugă câmpurile `l10n_ro_old_name`, `l10n_ro_active_anaf_line_ids`, `l10n_ro_vat_subjected_anaf_line_ids` și logica de interogare/mapare ANAF (`_get_Anaf`, `_Anaf_to_Odoo`, `get_result_address`, `ro_vat_change`).
- `l10n.ro.res.partner.anaf.status`: istoricul stărilor de activ/inactiv raportate de ANAF pentru un partener (dată început/sfârșit, dată publicare/radiere, act de autorizare).
- `l10n.ro.res.partner.anaf.scptva`: istoricul perioadelor de înregistrare ca plătitor de TVA raportate de ANAF pentru un partener.

**Vizualizări**

- `view_partner_create_by_vat_einvoice`: extinde formularul de creare rapidă a partenerului după CUI (din `l10n_ro_config`) cu câmpul "Old Name".
- `view_partner_anaf_status_form`: adaugă în tab-ul de informații ANAF de pe fișa partenerului (din `l10n_ro_config`) cele două liste de istoric — stare activ/inactiv și înregistrare TVA.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul — actualizarea se declanșează la modificarea câmpului CUI (`@api.onchange("vat", "country_id")` pe `res.partner`), nu pe bază de programare.

#### 5. Conexiuni

- `l10n_ro_fiscal_validation`: reutilizează cheia API de ANAF configurată de acest modul pentru sincronizarea în masă a datelor fiscale ale partenerilor.
