# Fan Curier Shipping (localizat la `deltatech_delivery_fc/index.md`)

- **Nume Tehnic:** `deltatech_delivery_fc`
- **Versiune:** `20.0.1.7.13`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_fc
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_fc`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul Fan Curier Shipping integrează direct în Odoo curierul Fan Courier, unul dintre principalii curieri din România. Companiile își automatizează expedierile fără a părăsi Odoo: de la calculul tarifului și generarea AWB-ului, până la urmărirea coletului și livrarea în lockere FANbox. Este util pentru firmele din România care expediază intern prin Fan Courier și vor să elimine introducerea manuală a datelor în portalul curierului.

#### 2. Funcționalități Cheie

- Generarea AWB în mai multe formate: PDF (tipărire standard), ZPL (imprimante termice) și HTML (afișare web); AWB-ul se poate reobține (**Print AWB**) sau anula (**Cancel AWB**) din livrare.
- Opțiuni de expediere: colete multiple, dimensiuni și greutate, valoare declarată (asigurare), ramburs, livrare sâmbăta, deschidere colet la livrare.
- Crearea AWB-ului din comanda de vânzare sau din livrare (**Carrier Details**, apoi validarea transferului sau trimiterea la transportator); numărul AWB ajunge în referința de urmărire, iar eticheta se atașează livrării.
- Tarif calculat de Fan Courier la adăugarea metodei de livrare pe comandă (sau preț fix, sub un prag configurat), integrat cu calculul de preț de livrare din Odoo.
- Urmărirea stării expedierii: evenimentele apar în tabul **History** al livrării, iar starea în lista AWB-urilor, până la livrare.
- Gestionarea locațiilor: sincronizare cu orașele și județele Fan Courier; expedierea se face după nume, nu după ID de oraș.
- Lockere FANbox: butonul **Get Lockers** importă catalogul, clientul alege lockerul pe hartă în checkout, numele lockerului se trimite în AWB, iar punctele cu coordonate GPS invalide sunt arhivate.
- Configurare (tab **Fan Curier Configuration**): **Client ID**, utilizator și parolă ale contractului; punctul de ridicare (**Pickup Location Source**) poate veni de pe transportator, din depozit (cu Client ID propriu pe fiecare depozit) sau din compania curentă.

Notă: expedierea cu ID de oraș și ID de județ nu este suportată. Pentru selecția lockerului pe hartă este necesar și [deltatech_delivery_locker](../deltatech_delivery_locker/index.md). Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

*Conform fluxului de ingestie, descrierea provine din `readme/DESCRIPTION.md`; analiza detaliată a codului (modele, vizualizări, acțiuni) a fost omisă întrucât Readme-ul acoperă funcționalitatea modulului.*

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): cadrul de bază pentru integrarea curierilor, extins de acest modul cu funcționalitatea specifică Fan Courier.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): necesar pentru selectarea pe hartă a lockerelor FANbox în checkout.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): legat de urmărirea statusului și a istoricului expedierilor.
