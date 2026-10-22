# Cargus Shipping (localizat la `deltatech_delivery_uc/index.md`)

- **Nume Tehnic:** `deltatech_delivery_uc`
- **Versiune:** `19.0.1.1.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_uc`
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_uc`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul permite expedierea coletelor cu Cargus direct din livrările Odoo: tariful de transport din tabela de prețuri a contractului dumneavoastră, AWB-ul și eticheta lui, urmărirea, anularea și decontul de ramburs, prin API-ul Cargus, fără reintroducerea datelor în portalul curierului. Valoarea de afaceri vine din automatizarea completă a relației cu Cargus pentru companiile care livrează în România și în alte țări deservite de același API.

#### 2. Funcționalități Cheie

- **Tarife din tabela proprie de prețuri:** costul transportului este calculat de Cargus cu tabela contractului dumneavoastră sau se folosește un preț fix, cu un prag opțional peste care se interoghează Cargus.
- **AWB și etichetă:** AWB-ul se emite din livrare, cu eticheta în format PDF, ZPL sau HTML, pe A4 sau pe etichetă 10x14; eticheta unui AWB existent poate fi reobținută, iar AWB-ul poate fi anulat.
- **Opțiuni de expediere:** mai multe colete cu dimensiuni, valoare declarată, ramburs, colet deschis, livrare sâmbăta și plătitorul transportului (expeditor sau destinatar).
- **Puncte de ridicare ale contului:** locațiile de ridicare înregistrate la Cargus se importă, iar fiecare AWB pleacă din cea setată pe metoda de livrare.
- **Lockere și puncte Ship & Go:** punctele Cargus se importă în catalogul de lockere; cu `deltatech_delivery_locker`, punctul ales pentru livrare se transmite în AWB.
- **Localități în România și în străinătate:** județele și localitățile Cargus se importă pentru țările alese pe metoda de livrare (de exemplu Polonia) și se mapează pe agenda de adrese Odoo; AWB-ul transmite țara destinatarului.
- **Urmărire și listă de AWB-uri:** istoricul de stare se citește de la Cargus și se scrie pe livrare; AWB-urile emise în portalul Cargus pot fi listate în Odoo.
- **Decont de ramburs:** cu `deltatech_delivery_cod`, sumele plătite de Cargus devin extras bancar, datat în ziua în care banii au ieșit efectiv de la curier; se includ doar sumele deja virate.

**Configurare (Inventar > Configurare > Livrare > Metode de expediere):**

- Se creează o metodă de livrare cu furnizorul *Cargus* și un produs de tip serviciu.
- În fila de configurare Cargus se completează cheia de abonament (Subscription Key), utilizatorul și parola API.
- Butonul *Initialization* importă tabelele de prețuri din contract; se aleg tabela și serviciul (Standard, Economic Standard etc.).
- Butonul *Get Pickup Locations* importă punctele de ridicare; este necesar cel puțin unul, deoarece orice AWB pleacă dintr-un punct de ridicare Cargus.
- La *Cargus Catalog Countries* se aleg țările de livrare (România, dacă rămâne gol), apoi *Get city* importă județele și localitățile.
- Se aleg tipul și formatul etichetei, plătitorul expedierii și metodele de plată tratate ca ramburs.

**Flux de utilizare:**

- Pe comanda de vânzare se adaugă metoda de livrare Cargus; costul este calculat de Cargus cu tabela de prețuri, dacă metoda nu are preț fix sub prag.
- Pe livrare, *Carrier Details* deschide expedierea: serviciu, număr de colete, greutate, dimensiuni, valoarea coletelor, suma de încasat și opțiuni.
- La validarea transferului, AWB-ul se rezervă la Cargus, referința de urmărire se scrie pe livrare și eticheta se atașează; *Print AWB* o tipărește, *Cancel AWB* anulează expedierea.
- Starea expedierii se citește de la Cargus până la livrare.

**Date trimise către Cargus:** la fiecare cotație sau expediere se transmit numele, adresa, persoana de contact, telefonul și e-mailul destinatarului, coletele (număr, greutate, dimensiuni), valoarea declarată, suma de ramburs, referința comenzii și nota livrării; expeditorul este punctul de ridicare Cargus.

> Notă: pentru selecția lockerului pe hartă este necesar `deltatech_delivery_locker`; pentru decontul de ramburs, `deltatech_delivery_cod`.
>
> Nesuportat: adresarea după numele localității fără id-ul Cargus și nota de retur (restitution note) în AWB.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Sumarul și funcționalitățile au fost preluate din `readme/DESCRIPTION.md`, completate cu `readme/CONFIGURE.md` și `readme/USAGE.md`. Conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune a fost omisă, întrucât Readme-ul nu o acoperă explicit.

#### 5. Conexiuni

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): catalogul de lockere; punctul ales pentru livrare se transmite în AWB.
- [deltatech_delivery_cod](../deltatech_delivery_cod/index.md): decontul de ramburs Cargus transformat în extras bancar.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): gestionarea și urmărirea stărilor de expediere/AWB.
