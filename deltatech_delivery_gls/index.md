# GLS Shipping (localizat la `deltatech_delivery_gls/index.md`)

- **Nume Tehnic:** `deltatech_delivery_gls`
- **Versiune:** `19.0.2.2.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_gls
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_gls`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite expedierea cu GLS direct din livrările Odoo, în România, Ungaria, Croația, Cehia, Slovenia și Slovacia: AWB-ul și eticheta lui, punctele GLS (parcel shop și lockere), urmărirea, anularea și lista de AWB-uri. Se folosește API-ul MyGLS sau, pentru conturile mai vechi, API-ul GLS Online, fără a reintroduce datele în portalul curierului. Se câștigă timp, scad erorile de transcriere, iar statusul coletului ajunge automat în livrare.

#### 2. Funcționalități Cheie

- **AWB și etichetă:** AWB-ul se emite din comanda de livrare, iar eticheta vine în același apel, ca PDF sau ZPL, în formatul ales pe metoda de livrare (A4 2x2, A4 4x1, termic, A6 etc.).
- **Două API-uri GLS:** MyGLS (publicat de GLS în fiecare din cele șase țări) și GLS Online (SOAP, folosit de conturile românești vechi). Țara și API-ul se aleg pe fiecare metodă de livrare; pentru GLS Online e nevoie și de cheia API de urmărire.
- **Configurare:** în *Inventar > Configurare > Livrare > Metode de expediere*, furnizor GLS, fila *GLS Configuration*: țară, versiune API, ID expeditor, utilizator, parolă, serviciu (PSD, FDS, SM1/SM2 etc.), format etichetă, metode de plată tratate ca ramburs și un adaos pentru ramburs.
- **Preț de transport calculat în Odoo:** GLS nu returnează tarife. Prețul vine din *Fixed Price* sau, dacă acesta e zero, dintr-o grilă JSON (pe greutate și pe sumă ramburs, plus prețul de preavizare); fără preț fix și fără grilă nu se oferă cotație.
- **Puncte GLS (parcel shop și lockere):** punctele de livrare ale țării se importă în catalogul comun de lockere și se aleg pe hartă cu `deltatech_delivery_locker`. Punctul ajunge în AWB doar cu serviciul Parcel Shop Delivery, pe MyGLS. Catalogul e identificat după țară, variantă de API și cont (`_gls_locker_catalog_key`), deci un al doilea cont GLS nu arhivează punctele primului; punctele dispărute din feed se arhivează la importul următor.
- **Servicii și opțiuni:** ramburs cu referință și monedă, mai multe colete, notificare SMS/e-mail a destinatarului, schimb de colet (retur) și, pe MyGLS, asigurare GLS opțională pentru un colet unic, cu valoare fixă setată pe metoda de livrare (se taxează de GLS). Serviciile SM1/SM2 se trimit doar pentru expedieri în țara expeditorului (din 19.0.2.2.4); în străinătate AWB-ul pleacă fără ele.
- **Urmărire:** istoricul de status se citește din GLS printr-o acțiune programată și se scrie pe livrare până la livrare; fila *History* îl listează, iar *Refresh* îl citește imediat. Referințele non-numerice sunt ignorate, iar un AWB problematic nu blochează celelalte livrări.
- **Anulare și listă AWB:** *Cancel AWB* anulează AWB-ul la GLS; în *Inventar > Operațiuni > Delivery AWB List* (MyGLS) se listează AWB-urile contului, inclusiv cele emise direct în portalul GLS.
- **MyGLS `WebshopEngine`:** cererea `PrintLabels` trimite `"WebshopEngine": "Odoo"`, obligatoriu în API-ul MyGLS.
- **Date trimise la GLS:** nume, adresă, localitate, cod poștal, țară, persoană de contact, telefon și e-mail ale expeditorului și destinatarului, numărul de colete, suma, referința și moneda de ramburs, referința comenzii, valoarea asigurată (dacă e cerută) și ID-ul punctului GLS.
- **Nesuportat:** tarife de la GLS, valoare declarată pe GLS Online, livrare sâmbătă, colet deschis, dimensiuni colet, etichetă HTML, liste de localități/județe și re-descărcarea etichetei unui AWB existent (GLS nu o emite a doua oară, deci eticheta atașată livrării se păstrează).
- **Limbi:** engleză, română, maghiară, cehă, croată, slovacă, slovenă (traducerile în afară de en/ro sunt asistate de AI).

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

Dependență externă Python: `zeep` (client SOAP pentru serviciile web GLS).

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins, `models/delivery_gls.py`): metoda de livrare GLS, cu AWB, anulare, etichete, urmărire, import lockere și calculul prețului.
- `delivery.carrier.service` (extins, `models/delivery_gls.py`): serviciile GLS (24H, PSD, FDS, SM1, SM2 etc.), încărcate din date.
- `gls.request` (`models/gls_request.py`): clientul pentru API-urile GLS Online și MyGLS (SOAP prin `zeep`).
- `res.config.settings` (extins, `models/res_config_settings.py`): setările GLS.

**Vizualizări**

- `view_delivery_carrier_form_with_provider_fc` (`views/delivery_gls_view.xml`): fila *GLS Configuration* pe formularul metodei de livrare.

**Acțiuni Automate / Acțiuni Server**

- Citirea statusului de la GLS se face printr-o acțiune programată (conform USAGE.md); modulul nu definește un cron propriu în `data/`. `uninstall_hook` curăță datele la dezinstalare.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): cadrul de bază al metodelor de livrare Deltatech, extins aici cu GLS (dependență directă).
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): catalogul comun de lockere în care se importă punctele GLS (`delivery.locker`, verificat în cod; modul opțional).
