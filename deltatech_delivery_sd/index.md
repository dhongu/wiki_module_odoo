# Sameday Shipping (localizat la `deltatech_delivery_sd/index.md`)

- **Nume Tehnic:** `deltatech_delivery_sd`
- **Versiune:** `20.0.1.13.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_sd
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_sd`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul integrează Odoo cu Sameday Courier, unul dintre principalii curieri din România, și automatizează expedierile de la calculul tarifului până la urmărire și actualizarea statusului livrării. Reduce munca manuală la emiterea AWB-urilor, scade erorile de adresă și oferă clienților informații corecte de urmărire.

#### 2. Funcționalități Cheie

- **Servicii și autentificare**: import automat al tipurilor de servicii Sameday, mai multe servicii simultan, autentificare securizată.
- **AWB**: generare în PDF sau HTML, în formate A4 și A6, anulare pentru comenzi respinse sau modificate; expediere cu mai multe colete, valoare declarată și ramburs.
- **Tarife**: calcul în timp real (**Get Rate** pe comanda de vânzare) pentru tipuri de colet (Package, Small package, Large package), integrat cu prețurile de livrare Odoo.
- **Locații**: import al orașelor și județelor cu id-urile Sameday și al punctelor de ridicare; catalog Out Of Home din `client/ooh-locations` (înlocuiește `client/lockers`, depreciat), cu ambele rețele (lockere easybox și PUDO / Sameday Point) prin `listingType=1`.
- **Livrare în locker / Sameday Point**: locația se alege pe adresa de livrare sau în **Carrier Details** și se trimite în AWB ca `oohLastMile`; serviciul trebuie să fie de tip out-of-home, altfel expedierea e refuzată înainte să ajungă la Sameday. Rețeaua nu se verifică în raport cu serviciul (un Sameday Point poate pleca pe un serviciu de locker). Rambursul se refuză per locație (**Payment at pickup**), nu per rețea. Pentru selecția pe hartă este necesar `deltatech_delivery_locker`.
- **Servicii out-of-home**: easybox (15 Locker NextDay, 30 Crossborder Locker; id-uri sub 500000) și Sameday Point (57 PUDO NextDay, 58 Crossborder PUDO; id-uri de la 500000); **Initialization** le marchează ca **Locker Service** doar la primul import.
- **Urmărire**: link de tracking, istoric de status, actualizarea statusului livrării din Sameday; statusul se interoghează per AWB, nu prin endpoint-urile de sincronizare în bloc.
- **Opțiuni**: ramburs, taxe de serviciu după tipul coletului, deschiderea coletului, retur colet, livrare personală, cont de numerar (informații, încasări ramburs, rapoarte pe perioadă).
- **Configurare**: **Inventory > Configuration > Delivery > Shipping Methods**, **Provider** = *Sameday*, credențialele în fila **Sameday Configuration**, apoi **Initialization** (servicii, județe, orașe, puncte de ridicare).
- Neacoperit: retur către locker/PUDO (servicii 24 și 31), Locker2Locker (51), sincronizare în bloc a statusurilor, AWB în ZPL, nota de restituire, dimensiuni, livrare sâmbăta.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, deoarece există `readme/DESCRIPTION.md`, analiza codului pentru această secțiune este omisă. Pentru orientare, modulul extinde `delivery.carrier`, `delivery.carrier.service`, `res.city`, `res.country`, `res.country.state`, `res.config.settings` și `stock.package.type` (clientul API în `models/`) și conține vizualizarea `views/delivery_sd_view.xml`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru livrare și curieri, extins de acest modul.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): necesar pentru selectarea lockerelor Sameday pe hartă.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): stările de livrare actualizate pe baza statusului Sameday.
- [deltatech_delivery_sd_easybox](../deltatech_delivery_sd_easybox/index.md): modul soră pentru lockerele Sameday (Easybox).
