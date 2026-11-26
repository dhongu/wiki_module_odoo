# Romania - e-Factura B2C (persoane fizice) (localizat la `l10n_ro_efactura_consumer/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_consumer`
- **Nume anterior:** `l10n_ro_efactura_b2c` (redenumit pe 23.09.2026: numele vechi e ocupat pe Odoo Apps de alt furnizor)
- **Versiune:** `19.0.1.0.8`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_efactura_consumer
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_consumer`
- **Ultima Ingestie:** `2026-11-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde modulul `l10n_ro_edi` pentru a suporta transmiterea facturilor către persoane fizice (B2C) prin SPV (Spațiul Virtual Privat) conform CIUS-RO. Adaugă câmpul CNP pe partener cu validare automată, înlocuiește identificatorul implicit `0000000000000` din XML cu CNP-ul real și blochează trimiterea facturilor cu CNP invalid, asigurând conformitatea declarațiilor B2C. Companiile care facturează exclusiv către persoane juridice cu cod de TVA nu au nevoie de el.

#### 2. Funcționalități Cheie

- **Câmp CNP pe partener** („CNP (Persoană Fizică RO)”): apare sub **TVA** în formularul clientului (Facturare → Clienți → Clienți sau Contacte) cât timp partenerul este de tip **Persoană** (nu Companie) și țara fiscală a firmei este România. Validare la salvare prin algoritmul Luhn RO: exact 13 cifre, prima cifră între 1 și 8, cifra de control corectă (ponderile `2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9` pe primele 12 cifre; restul împărțirii sumei la 11 e cifra de control, un rest de 10 dă 1). Un CNP greșit nu se salvează și apare dialogul **Eroare de validare**. Câmpul calculat „CNP Valid” indică rezultatul.
- **Generare XML CIUS-RO B2C:** când clientul este persoană fizică cu CNP valid, CNP-ul real înlocuiește `0000000000000`, cu `schemeID="CNP"` atât în `PartyIdentification/ID`, cât și în `PartyLegalEntity/CompanyID`. CNP-ul se citește de pe contactul principal al clientului (partenerul comercial), nu de pe adresele de livrare sau de facturare.
- **Client fără CNP:** facturile nu sunt blocate; se trimit cu identificatorul anonim `0000000000000` (comportamentul standard al `l10n_ro_edi`). În lista **Clienți**, coloana opțională **CNP** (meniul coloanelor opționale) ajută la identificarea clienților fără CNP sau cu CNP care nu le aparține (de exemplu din date migrate).
- **Validare pre-trimitere:** blochează trimiterea în SPV dacă CNP-ul este completat dar invalid (de exemplu printr-un import); în chatter apare mesajul „Factura nu este gata să fie trimisă: CNP invalid pentru clientul …”. Se corectează CNP-ul pe client și se retrimite factura.
- **Avertizare pe factură:** banner galben informativ pe facturile și notele de credit de client când clientul (contactul principal) este de tip Persoană, partenerul de pe factură are țara România, iar CNP-ul lipsește sau este invalid; rămâne până la corectarea CNP-ului.
- **Trimitere în SPV:** pe factura confirmată se apasă **Trimite**, se bifează **Trimite E-Factura către SPV** și se confirmă. Dacă SPV respinge identificatorul cumpărătorului (`BT-47`), se verifică că CNP-ul are exact 13 cifre.
- **Corectarea unui CNP după trimitere:** factura trimisă rămâne în SPV cu CNP-ul inițial; dacă acesta nu aparținea clientului, se emite o notă de credit pentru factura inițială, se corectează CNP-ul pe client și se emite o factură nouă — ambele documente se trimit în SPV.
- **Migrare date:** la instalare, dacă `deltatech_contact` este prezent, copiază CNP-urile existente din câmpul `cnp` în `l10n_ro_cnp` (doar unde câmpul nou e gol). Migrarea nu rulează la instalarea ulterioară a lui `deltatech_contact`; atunci CNP-urile se completează manual sau prin import (Contacte → Importare).
- **Protecție GDPR:** câmpul CNP este restricționat la grupul `base.group_user` (utilizatori interni); portalul și utilizatorii publici nu îl văd. Fiind dată cu caracter personal, politica de confidențialitate trebuie să menționeze stocarea CNP-urilor, accesul la formularul partenerului se limitează la personal autorizat, iar cererile de ștergere a datelor se procesează inclusiv pentru CNP.
- **Configurare:** nu adaugă setări de conexiune; certificatul digital, tokenul și URL-ul ANAF rămân cele din `l10n_ro_edi`, iar câmpul CNP apare automat dacă firma are localizarea RO activă.

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extindere): câmpul `l10n_ro_cnp` (restricționat la `base.group_user`) și câmpul calculat și stocat `l10n_ro_cnp_valid` („CNP Valid”), plus constrângerea `_check_l10n_ro_cnp` care aplică validarea Luhn RO la salvare.
- `account.move` (extindere): câmpul calculat `l10n_ro_cnp_missing` (condiția bannerului B2C, calculată pe server) și suprascrierea `_l10n_ro_edi_get_pre_send_errors`, care oprește trimiterea pentru CNP invalid.
- `account.edi.xml.ubl_ro` (extindere abstractă, fișierul `account_edi_xml_ubl_ro.py`): suprascrie `_ubl_add_accounting_customer_party_legal_entity_nodes` pentru a pune CNP-ul cu `schemeID="CNP"` în `PartyLegalEntity` și `PartyIdentification`.

**Vizualizări**

- `views/res_partner_views.xml`: câmpul CNP și indicatorul de validitate pe partener, plus coloana opțională CNP în lista de clienți.
- `views/account_move_views.xml`: bannerul de avertizare pe formularul facturii.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: migrarea CNP-urilor existente din `deltatech_contact` (dacă modulul este prezent). Nu sunt definite `ir.cron` sau `base.automation`.

#### 5. Conexiuni

- [l10n_ro_efactura_dedup](../l10n_ro_efactura_dedup/index.md): modul înrudit pentru fluxurile e-Factura; pagina lui menționează acest modul ca modul conex.
- [deltatech_contact](../deltatech_contact/index.md): sursa opțională a CNP-urilor existente (câmpul `cnp`), copiate la instalare prin `post_init_hook`.
