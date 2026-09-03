# Romania - Invoice Report Terrabit (localizat la `l10n_ro_invoice_report/index.md`)

- **Nume Tehnic:** `l10n_ro_invoice_report`
- **Versiune:** `19.0.3.4.20`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_invoice_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_invoice_report`
- **Ultima Ingestie:** `2026-08-31`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul extinde raportul de factură standard din Odoo pentru a se conforma cerințelor specifice din România și pentru a oferi opțiuni suplimentare de personalizare. Adaugă pe documentele tipărite detalii la nivel de linie (preț fără TVA, valoare TVA, numerotare), informații legale și logistice (delegat, mijloc de transport, mențiunea privind scutirea de semnătură și ștampilă) și gestionează documentele de plată corelate (chitanțe, dispoziții de plată/încasare), oferind în același timp numeroase opțiuni de configurare din setările de facturare.

#### 2. Funcționalități Cheie

- **Detalii linii factură**:
    - Afișarea prețului unitar fără TVA.
    - Afișarea valorii TVA pe fiecare linie.
    - Afișarea totalului cu taxe pe fiecare linie (configurabil).
    - Numerotarea automată a liniilor de factură (Ord).
    - Opțiune de a elimina numele produsului de pe linie dacă există o descriere specifică.
    - Afișarea prețului fără discount.
- **Informații suplimentare pe document**:
    - Câmpuri dedicate pentru **Delegat** și **Mijloc de transport**.
    - Afișarea textului legal privind scutirea de semnătură și ștampilă (conform Codului Fiscal).
    - Posibilitatea de a adăuga un text adițional de la partener pe factură (`info_for_invoice`).
    - Vizibilitatea configurabilă pentru email, telefon și marcaje în adresa facturii.
    - Afișarea informațiilor despre livrări (Pickings) și AWB-uri direct pe factură.
    - Inserarea logoului **Coface** la finalul facturii (activabil din setări).
- **Gestiune documente corelate**:
    - **Chitanță, dispoziție de plată și dispoziție de încasare** tipărite din plată (raportul „Voucher / Payment" pe `account.payment`), cu titlul potrivit tipului de plată și cu suma în cifre și în litere.
    - Pentru plățile pe **jurnal de casă**, documentul iese ca formular de casierie complet: **codul formularului** (14-4-4 la plată, 14-4-1 la încasare), **casieria**, rândul pentru **actul de identitate** al beneficiarului la plăți, și **cele trei semnături** — conducătorul unității, casierul și beneficiarul. La plățile bancare aceste elemente nu se tipăresc, nefiind vorba de un document de casă.
    - Părțile sunt etichetate după rolul lor real în operațiune: pe documentele de casă, **Plătitor / Beneficiar** la plată și **Beneficiar / Depunător** la încasare. Etichetele „Client / Furnizor" rămân doar pe celelalte cazuri — la o restituire de marfă către o persoană fizică, beneficiarul nu e furnizor.
    - Gestionarea corectă a semnelor pentru stornări (Credit Notes).
- **Rapoarte dedicate**:
    - Raport de factură în limba companiei, indiferent de limba partenerului.
    - Șabloanele sunt scrise în engleză și traduse prin `i18n/ro.po`, deci documentele ies în română la clienții RO. Odoo potrivește traducerile de șablon prin `msgid` **exact**, cu newline-urile și indentarea din interiorul textului: dacă șablonul e reindentat fără a resincroniza `ro.po`, traducerea rămâne în fișier dar nu se mai aplică, iar documentul iese în engleză deși fișierul pare complet. Verificat și corectat: pe forma curentă a șablonului sunt 127 de stringuri, dintre care cele care ajung pe documente sunt traduse.
    - **Limba facturii tipărite vine de la partenerul companiei**, nu de la utilizator: pe o companie configurată pe engleză, documentul iese în engleză deși interfața e în română. E felul în care funcționează raportul „în limba companiei", nu un defect — dar trebuie știut la configurare.
- **Configurare flexibilă**:
    - Numeroase opțiuni în setările de facturare pentru a activa sau dezactiva elementele menționate mai sus (Sarcini delegat, comentarii plată, index linii, etc.).

> **Cerințe tehnice:** Necesită instalarea bibliotecii `num2words` (recomandat: `pip3 install num2words==0.5.12`).

#### 3. Dependențe

- `base`
- `account`
- `l10n_ro_config`
- `purchase`
- `sale`
- `stock_delivery`

#### 4. Componente Cheie

> Secțiune omisă: fișierul `readme/DESCRIPTION.md` acoperă deja Sumarul și Funcționalitățile Cheie, iar conform schemei de ingestie analiza codului pentru Componente Cheie (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server) nu se efectuează decât dacă este cerută explicit în Readme.

#### 5. Conexiuni

- `l10n_ro_config`: modulul de configurare al localizării românești care găzduiește setările de facturare valorificate de acest raport.
- `stock_delivery`: sursa informațiilor despre livrări (Pickings) și AWB-uri afișate pe factură.
- [l10n_ro_cash_bank_enhanced](../l10n_ro_cash_bank_enhanced/index.md): registrul numerotat al dispozițiilor de casă, pentru mișcările de numerar care nu trec printr-o plată contabilă; documentul de aici acoperă cazul `account.payment`, iar cele două nu se dublează.
- [l10n_ro_pos_returns](../l10n_ro_pos_returns/index.md): restituirile de la casa de marcat, care nu produc `account.payment` și își iau dispoziția de plată din registrul modulului de casierie.
