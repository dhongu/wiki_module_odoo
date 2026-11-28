# GLS Shipping (localizat la `deltatech_delivery_gls/index.md`)

- **Nume Tehnic:** `deltatech_delivery_gls`
- **Versiune:** `20.0.2.1.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_gls
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_gls`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul GLS Shipping integrează în Odoo serviciile de curierat GLS (General Logistics Systems) pentru România, Ungaria, Croația, Cehia, Slovenia și Slovacia. Expedierea se face direct din livrările Odoo: AWB-ul și eticheta, punctele de livrare GLS (parcel shop și lockere), urmărirea, anularea și lista AWB-urilor, prin API-ul MyGLS sau prin vechiul API GLS Online, fără reintroducerea datelor în portalul curierului. Reduce timpul de lucru și erorile de transcriere și oferă clienților informații de urmărire corecte.

#### 2. Funcționalități Cheie

- **AWB și etichetă:** rezervate din livrare, cu eticheta returnată în același apel, în format PDF sau ZPL și în macheta aleasă pe metoda de livrare (A4 2x2, A4 4x1, termic, A6 ș.a.); eticheta se atașează livrării (**Print AWB**, **Cancel AWB**). GLS nu emite a doua oară eticheta unui AWB rezervat, deci atașamentul trebuie păstrat.
- **Două API-uri GLS:** MyGLS și GLS Online (SOAP, pentru conturile românești mai vechi); țara și versiunea (*mygls* / *online*) se aleg pe metoda de livrare, în tabul **GLS Configuration**, împreună cu ID-ul expeditorului, utilizatorul, parola și, la *online*, cheia API de urmărire.
- **Parcel shop și lockere:** punctele GLS ale țării se importă în catalogul comun de lockere (**Use Locker**, **Get Lockers**), se aleg pe hartă cu [deltatech_delivery_locker](../deltatech_delivery_locker/index.md), iar AWB-ul poartă punctul prin serviciul Parcel Shop Delivery (MyGLS).
- **Servicii și opțiuni:** ramburs cu referință și monedă, colete multiple, notificare destinatar prin SMS și e-mail, schimb de colet (retur) și, pe MyGLS, asigurare GLS opțională pentru expedieri cu un singur colet, la o valoare fixă setată pe metoda de livrare.
- **Preț de transport calculat în Odoo**, nu cerut de la GLS: preț fix sau grilă JSON după greutate și ramburs (cu suprataxă opțională pentru ramburs și preț de preavizare).
- **Urmărire:** istoricul stărilor este citit de la GLS printr-o acțiune programată și scris pe livrare (tabul **History**, buton **Refresh**); linkul de urmărire deschide expedierea pe site-ul GLS.
- **Anulare și listă AWB:** AWB-ul se poate anula din Odoo, iar AWB-urile emise în MyGLS (inclusiv cele rezervate direct în portal) se listează în *Inventar > Operațiuni > Delivery AWB List*.
- **Raport ramburs:** cu [deltatech_payment_on_delivery](../deltatech_payment_on_delivery/index.md), fișierul GLS de ramburs se importă și se potrivește cu livrările.
- **Date trimise către GLS:** nume, adresă, localitate, cod poștal, țară, persoană de contact, telefon și e-mail ale expeditorului și destinatarului, numărul de colete, ramburs, referința comenzii, valoarea asigurată (la cerere) și id-ul parcel shop-ului.
- **Limbi:** engleză, română, maghiară, cehă, croată, slovacă, slovenă (traducerile în afară de engleză și română sunt asistate de AI).

Nesuportate: tarife cerute de la GLS, valoarea declarată pe API-ul GLS Online, livrarea sâmbăta, coletul deschis, dimensiunile coletului, etichetele HTML, listele de localități și județe și reobținerea etichetei unui AWB existent. Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

Dependență externă Python: `zeep` (client SOAP pentru serviciile web GLS).

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins, `models/delivery_gls.py`): metoda de livrare GLS, cu crearea și anularea AWB, generarea etichetelor, urmărirea și grila de prețuri.
- `delivery.carrier.service` (extins): serviciile GLS (PSD, FDS, SM2, preavizare ș.a.) disponibile pe metoda de livrare.
- `GLSProvider` / `GlsUncertainResult` (`models/gls_request.py`): clientul API-urilor MyGLS și GLS Online (SOAP prin `zeep`), cu tratarea distinctă a răspunsurilor pierdute în rețea.
- `res.config.settings` (extins, `models/res_config_settings.py`): setările de configurare GLS.

**Vizualizări**

- `views/delivery_gls_view.xml`: tabul **GLS Configuration** pe metoda de livrare și acțiunile aferente AWB/urmărire.

**Date**

- `data/delivery_gls_data.xml`: serviciile GLS predefinite (T09/T10/T12 Express, Saturday, FlexDelivery, SMS, PreAdvice, Parcel Shop Delivery ș.a.).

**Hook-uri**

- `uninstall_hook`: curățare la dezinstalare.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): cadrul de bază pentru metodele de livrare Deltatech, extins cu integrarea GLS.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): harta și catalogul comun de lockere folosite pentru parcel shop GLS.
- [deltatech_payment_on_delivery](../deltatech_payment_on_delivery/index.md): raportul de ramburs GLS potrivit cu livrările.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): valorifică stările de livrare actualizate pe baza urmăririi GLS.
