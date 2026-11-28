# PTT Express (Memex) Shipping (localizat la `deltatech_delivery_memex/index.md`)

- **Nume Tehnic:** `deltatech_delivery_memex`
- **Versiune:** `20.0.1.0.16`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_memex`
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_memex`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite expedierea cu PTT Express (fostul Memex) direct din livrările Odoo: tariful pe comanda de vânzare, AWB-ul cu etichetele PDF și anularea acestuia, prin serviciul web al curierului, fără nimic reintrodus în WebTrucker. Acoperă scenarii uzuale precum colete multiple, valoare declarată, ramburs și opțiuni suplimentare de livrare.

#### 2. Funcționalități Cheie

- Tarif pe comanda de vânzare: costul transportului e evaluat de PTT Express pentru serviciul ales, după verificarea disponibilității serviciului pentru expediere, sau se folosește un preț fix (opțional, cu adaos pentru ramburs).
- AWB emis din livrare; etichetele tuturor coletelor se unesc într-un singur PDF atașat livrării.
- Opțiuni de expediere: mai multe colete cu greutate și dimensiuni, valoare declarată, ramburs, livrare sâmbăta și notificare SMS a destinatarului.
- Sumele de ramburs și asigurare se convertesc în moneda contractului PTT Express.
- Asigurare corelată cu rambursul: valoarea asigurată se ridică cel puțin la suma de încasat, iar refuzurile curierului sunt reformulate într-un mesaj clar.
- Anulare AWB din Odoo; un răspuns pierdut la emitere sau anulare e raportat ca rezultat incert, deci o nouă apăsare nu emite un al doilea AWB.
- Configurare: *Inventar > Configurare > Livrare > Metode de livrare*, provider *PTT Express*, fila **Memex Configuration** (utilizator, parolă, serviciu: National Standard, Loco Standard, Express 6 ore București, Colete Grele; **Fixed Price**, **Additional Price for COD**).
- Date trimise curierului: nume, contact, adresă, localitate, cod poștal, țară, telefon și e-mail ale expeditorului și destinatarului, coletele, rambursul, valoarea asigurată și referința comenzii.
- Nesuportate: urmărirea în Odoo (linkul deschide site-ul PTT Express), listele de localități și județe, etichete ZPL sau HTML, redescărcarea etichetei unui AWB existent, lockere și puncte de ridicare, colet deschis, nota de restituire.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

Dependență externă Python: `zeep` (client SOAP pentru serviciul web al curierului).

#### 4. Componente Cheie

Sumarul și funcționalitățile au fost preluate din `readme/DESCRIPTION.md`, `USAGE.md` și `CONFIGURE.md`, conform fluxului de ingestie. Analiza detaliată a componentelor tehnice nu a fost efectuată, deoarece Readme-ul nu o solicită explicit.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru integrările de curierat, pe care acest modul îl extinde pentru curierul PTT Express.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): urmărirea stării expedierilor pentru integrările de livrare.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): gestionarea lockerelor pentru curierii care oferă livrare în puncte de ridicare automate.
