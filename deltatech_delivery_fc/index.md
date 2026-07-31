# Fan Curier Shipping (localizat la `deltatech_delivery_fc/index.md`)

- **Nume Tehnic:** `deltatech_delivery_fc`
- **Versiune:** `19.0.1.3.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_delivery_fc
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_fc`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul Fan Curier Shipping este o extensie Odoo dezvoltată de Terrabit care asigură integrarea directă între sistemul de gestiune a livrărilor din Odoo și Fan Courier, unul dintre principalii curieri din România. Modulul permite companiilor să își automatizeze operațiunile de expediere cu Fan Courier direct din Odoo, simplificând întregul proces de livrare — de la calculul tarifelor și generarea AWB-ului, până la urmărirea coletelor. Este deosebit de util pentru companiile din România care expediază produse pe plan intern prin Fan Courier și care doresc să automatizeze generarea documentelor de transport și urmărirea în timp real a expedierilor.

#### 2. Funcționalități Cheie

- Generarea AWB în mai multe formate: PDF (pentru tipărire standard), ZPL (pentru imprimante termice de etichete) și HTML (pentru afișare web).
- Opțiuni complete de expediere: colete multiple într-o singură expediere, dimensiuni și greutate, valoare declarată (asigurare), ramburs (cash on delivery), livrare sâmbăta, deschidere colet la livrare și notă de retur în AWB.
- Crearea AWB-ului direct din comenzile de vânzare sau din comenzile de livrare din Odoo, precum și ștergerea AWB-ului pentru expedierile anulate.
- Urmărirea în timp real a statusului expedierii și accesul la istoricul stărilor coletului.
- Calcularea automată a costului de transport, integrată cu sistemul de calcul al prețului de livrare din Odoo.
- Gestionarea locațiilor: sincronizarea cu lista de orașe și județe Fan Courier și posibilitatea de a expedia folosind numele orașului, fără a fi nevoie de ID-ul orașului.
- Integrare cu lockerele FanBox (puncte de ridicare): import și sincronizare automată a lockerelor în Odoo, specificarea numelui lockerului în AWB, selectarea lockerului pe hartă în checkout și curățarea automată a lockerelor cu coordonate GPS invalide.
- Opțiuni de configurare dedicate integrării Fan Courier, personalizarea ambalării produselor conform cerințelor curierului și configurarea punctului de ridicare (din adresa contractuală).

Notă: Expedierea cu ID de oraș și ID de județ nu este suportată (se folosește identificarea după nume). Pentru selectarea lockerului pe hartă este necesară și instalarea modulului [deltatech_delivery_locker](../deltatech_delivery_locker/index.md).

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

*Conform fluxului de ingestie, descrierea provine din `readme/DESCRIPTION.md`; analiza detaliată a codului (modele, vizualizări, acțiuni) a fost omisă întrucât Readme-ul acoperă funcționalitatea modulului.*

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): cadrul de bază pentru integrarea curierilor, extins de acest modul cu funcționalitatea specifică Fan Courier.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): necesar pentru selectarea pe hartă a lockerelor FanBox (puncte de ridicare) în checkout.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): legat de urmărirea statusului și a istoricului expedierilor.
