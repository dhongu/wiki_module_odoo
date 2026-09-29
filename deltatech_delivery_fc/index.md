# Fan Curier Shipping (localizat la `deltatech_delivery_fc/index.md`)

- **Nume Tehnic:** `deltatech_delivery_fc`
- **Versiune:** `19.0.1.7.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_fc
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_fc`
- **Ultima Ingestie:** `2026-09-29`

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
- Import de lockere care nu șterge nimic: locațiile scoase din catalogul Fan Courier (sau fără coordonate) sunt arhivate, nu șterse, deci nu mai sunt oferite pe hartă, dar istoricul comenzilor și adresele partenerilor rămân intacte. Arhivarea se face doar după o preluare completă și este limitată la rețeaua importată de transportator (câmpul „Pickup Point Type”: FANbox, PayPoint sau birou); transportatorii existenți continuă să importe FANbox-uri. Locațiile poartă în `locker_type` rețeaua de origine. Un AWB poate fi emis și pentru o locație retrasă între timp, dacă comanda a fost plasată cât timp era listată.
- Reîncercare automată a expedierii când un FANbox este prea nou pentru catalogul Fan Courier: AWB-ul este reluat după câteva minute (până la 4 încercări, ~12 minute), prin mecanismul comun din [deltatech_delivery_locker](../deltatech_delivery_locker/index.md), în loc să eșueze cu „locker not found”.
- Reobținerea etichetei unui AWB existent (`fc_get_label`): dacă eticheta a fost ștearsă din picking, se reia de la Fan Courier. Formatul paginii setat pe transportator (A4/A5/A6) ajunge acum efectiv la Fan Courier (A6 este respectat doar pentru ePOD); eticheta ePOD are extensia `.pdf`.
- Import de localități care nu mai creează dubluri în `res.city`: localitățile ambigue sau necunoscute apar ca „to map” în `delivery.carrier.city`, iar checkout-ul oferă doar localitățile deservite de Fan Courier.
- Opțiuni de configurare dedicate integrării Fan Courier (Client ID, utilizator, parolă, în fila „Fan Courier Configuration” a metodei de livrare), personalizarea ambalării produselor conform cerințelor curierului și configurarea punctului de ridicare (din adresa contractuală).
- Client ID pe mai multe contracte: se folosește, în ordine, Client ID de pe metoda de livrare, apoi Referința adresei de ridicare a depozitului, apoi Referința primei locații de ridicare. Pentru depozite cu contracte diferite, câmpul de pe metodă rămâne gol, iar în fila „Pickup Location” (sursa „Warehouse”) se adaugă câte o linie per depozit, cu Referința = Client ID-ul contractului. Câmpul Client ID este vizibil doar grupului Setări.
- Erori frecvente: „The client id do not exists” (Client ID lipsă, greșit sau din alt contract decât utilizatorul/parola) și timeout după 30 de secunde către `api.fancourier.ro`.

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
