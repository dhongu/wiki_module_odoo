# Innoship Shipping (localizat la `deltatech_delivery_innoship/index.md`)

- **Nume Tehnic:** `deltatech_delivery_innoship`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_innoship
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_innoship`
- **Ultima Ingestie:** `2026-09-03`

#### 1. Sumar

Modulul conectează Odoo la Innoship, o platformă de curierat care agregă peste o sută de curieri europeni sub o singură integrare. În loc să se conecteze separat la fiecare curier, comanda de livrare este predată către Innoship — cu un curier ales explicit sau lăsat pe seama regulilor proprii de rutare ale Innoship — iar Innoship rezervă transportul, întoarce AWB-ul și eticheta și raportează starea coletului. Tarifarea, generarea AWB-ului, etichetele, anularea și urmărirea coletului se desfășoară în întregime în fluxul standard de livrare din Odoo, fără un portal separat de sincronizat.

#### 2. Funcționalități Cheie

- O singură cheie API acoperă toți curierii din contul Innoship; curierul se alege per metodă de livrare, din lista de curieri deținuți efectiv de cont, citită de la Innoship (nu introdusă manual)
- Curierul poate fi lăsat și pe seama Innoship ("Innoship (best price)"), care rutează după regulile proprii ale contului
- Generare AWB și etichetă direct din comanda de livrare, în format PDF, ZPL sau HTML, la dimensiune A6, A4 sau formatul propriu al curierului; A6 PDF este formatul cel mai des folosit de curierii români
- Reobținerea etichetei unei AWB existente ("Print Label"), dacă atașamentul a fost șters — fără o nouă rezervare
- Anularea unui transport ("Cancel Shipment") direct la Innoship și la curier
- Tarifare în timp real pentru o comandă de vânzare, câte un tarif per curier deținut de cont; tariful cel mai mic devine prețul de livrare; alternativ, preț fix cu un prag opțional peste care se interoghează Innoship
- Import și gestionare de lockere și puncte de ridicare din catalogul Innoship, restrâns la curierul și țara configurate pe metoda de livrare, integrat prin catalogul comun `delivery.locker` (necesită `deltatech_delivery_locker`, respectiv `deltatech_delivery_locker_website` pentru magazin)
- Import automat al catalogului de județe și localități Innoship; județele sunt potrivite cu nomenclatorul Odoo ignorând diacriticele; localitățile nepotrivite rămân vizibile ca „de mapat" în *Inventar > Configurare > Carrier Localities*, în loc să fie ghicite
- Urmărire: istoricul stărilor transportului este preluat de la Innoship printr-un cron periodic și scris pe livrare; o stare Innoship nerecunoscută lasă starea existentă neschimbată, în loc să fie ghicită
- Opțiuni avansate de expediere: ramburs (COD), valoare declarată, colet multiplu (cu greutatea distribuită pe colete), livrare sâmbăta, colet deschis la livrare, retur colet, plată de expeditor sau de destinatar, ridicare de la o locație de client înregistrată la Innoship
- Reîncercări sigure: un răspuns pierdut la crearea sau anularea unui AWB este raportat ca rezultat incert, nu ca eroare simplă, astfel încât apăsarea repetată a butonului nu rezervă un al doilea AWB pentru același colet; un refuz este raportat cu id-ul de corelare Innoship, primul lucru cerut de suportul lor
- Fluxul de configurare (din CONFIGURE.md): se creează metoda de livrare cu furnizorul Innoship, se completează cheia API și formatul etichetei, apoi se apasă **Init Carrier** pentru a citi curierii deținuți de cont (id-ul numeric, nu numele, este cel folosit la etichetă și anulare); se alege apoi **Service**-ul dorit; **Update address dictionaries** importă județele și localitățile; pentru lockere se activează **Use Locker**, se setează **Locker Country** și se apasă **Import Lockers**
- Innoship nu publică un mediu de test (sandbox) separat — un cont de test folosește aceeași adresă ca unul live, deosebirea fiind doar cheia API; debifarea „Production Environment" pe metoda de livrare NU ține un apel departe de contul live

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins, `CarrierInnoship`): implementează metodele de rezervare AWB, tarifare, anulare, urmărire și import al catalogului de curieri/lockere pentru furnizorul Innoship
- `delivery.carrier.service` (extins, `DeliveryService`): reține curierul numeric Innoship (`innoship_courier_id`) asociat serviciului, folosit la adresarea cererilor de etichetă și anulare
- `res.country.state` / `res.city` (extinse): suportă maparea catalogului de județe și localități Innoship pe nomenclatorul Odoo
- `stock.picking` (extins): expune acțiunile de generare/reobținere etichetă și anulare AWB pe livrare
- `stock.package.type` (extins): suport pentru coletele multiple în payload-ul de expediere
- `res.config.settings` (extins): setări la nivel de configurare generală pentru integrarea Innoship
- `InnoshipProvider` / `InnoshipUncertainResult`: clientul intern pentru API-ul REST Innoship (Order, Price, Label, Track, Location, Courier), cu tratarea distinctă a răspunsurilor pierdute în rețea

**Vizualizări**

- `views/delivery_view.xml`: tabul „Innoship Configuration" pe metoda de livrare (cheie API, tip/format etichetă, buton Init Carrier, opțiuni de locker)
- `views/res_config_settings_views.xml`: integrare în setările generale de inventar/livrare

**Date**

- `data/data.xml`: set inițial de curieri Innoship uzuali pentru România (Cargus, DPD, Fan Courier, GLS, Sameday, TeamCourier ș.a.), înlocuit efectiv la rularea **Init Carrier**

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază peste care se construiește integrarea de curierat
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): catalogul comun de lockere/puncte de ridicare, folosit de acest modul pentru selecția la finalizarea comenzii și în backend
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md): extensia de selecție locker pentru magazinul online (checkout)
