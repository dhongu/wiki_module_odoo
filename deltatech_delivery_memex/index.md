# PTT Express (Memex) Shipping (localizat la `deltatech_delivery_memex/index.md`)

- **Nume Tehnic:** `deltatech_delivery_memex`
- **Versiune:** `19.0.1.0.18`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_memex
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_memex`
- **Ultima Ingestie:** `2026-11-15`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul integrează curierul PTT Express (fost Memex) în Odoo: coletele se expediază direct din livrările Odoo, prin serviciul web al curierului, fără a mai introduce datele manual în WebTrucker. Odoo calculează tariful pe comanda de vânzare, rezervă AWB-ul și atașează etichetele PDF la livrare. Acoperă colete multiple, valoare declarată (asigurare), ramburs și opțiuni suplimentare de livrare, fiind util companiilor care livrează cu acest curier.

#### 2. Funcționalități Cheie

- **Tarif pe comanda de vânzare**: costul transportului este calculat de PTT Express pentru serviciul ales, după verificarea că serviciul e disponibil pentru expediția respectivă, sau se folosește un preț fix.
- **AWB și etichete**: AWB-ul se rezervă din livrare; etichetele tuturor coletelor revin odată cu AWB-ul și sunt unite într-un singur PDF atașat livrării.
- **Opțiuni de expediere**: mai multe colete cu greutate și dimensiuni, valoare declarată, ramburs, livrare sâmbăta și notificare SMS a destinatarului.
- **Sume în moneda curierului**: rambursul și suma asigurată sunt convertite din moneda documentului în moneda contractului PTT Express.
- **Asigurare coerentă cu rambursul**: la o expediție asigurată, valoarea asigurată este ridicată cel puțin la suma de încasat, cum cere PTT Express; refuzurile curierului sunt reformulate ca mesaj despre ce trebuie schimbat.
- **Anulare și reîncercări sigure**: un AWB poate fi anulat din Odoo; un răspuns pierdut la rezervare sau anulare este raportat ca rezultat incert, deci apăsarea repetată a butonului nu rezervă un al doilea AWB.
- **Configurare** (*Inventar > Configurare > Livrare > Metode de expediere*, **Provider** = *PTT Express*, produs de livrare de tip serviciu): în tabul **Memex Configuration** se completează **User** și **Password** ale contului PTT Express, **Service** (National Standard, Loco Standard, Express 6 ore Bucuresti, Colete Grele), **Fixed Price** (gol = tarif calculat de curier) și **Additional Price for COD** (adaos pentru comenzile cu ramburs).
- **Utilizare**: pe livrare, **Carrier Details** deschide expediția (serviciu, număr de colete, greutate, dimensiuni, valoare colet, valoare de încasat, opțiuni sâmbătă / SMS); la validarea transferului se rezervă AWB-ul, se scrie referința de urmărire și se atașează etichetele; **Cancel AWB** anulează expediția, iar linkul de urmărire deschide expediția pe site-ul PTT Express.
- **Date trimise către PTT Express**: la fiecare ofertă și expediție se transmit numele, persoana de contact, adresa, localitatea, codul poștal, țara, telefonul și e-mailul expeditorului și destinatarului, coletele (greutate, dimensiuni), rambursul, valoarea asigurată și referința comenzii.
- **Neacceptate**: urmărirea în Odoo (linkul deschide site-ul curierului), listele de localități și județe, etichetele ZPL sau HTML, reluarea etichetei unui AWB existent, lockerele și punctele de ridicare, coletul deschis și nota de restituire.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

Dependență externă Python: `zeep` (client SOAP pentru serviciul web al curierului).

#### 4. Componente Cheie

Secțiunile 1 și 2 provin din `readme/DESCRIPTION.md`, completat cu `CONFIGURE.md` și `USAGE.md`; componentele de mai jos au fost verificate în cod.

**Modele**

- `delivery.carrier` (extins): adaugă tipul de livrare `memex` (PTT Express) cu metodele `memex_rate_shipment`, `memex_send_shipping`, `memex_cancel_shipment` și `memex_get_tracking_link`; opțiunile implicite sunt livrarea sâmbăta și notificarea SMS. Capabilitățile declarate sunt doar `ship` și `cancel`.
- `delivery.carrier.service` (extins): adaugă tipul `memex` pentru serviciile curierului.
- `MemexProvider` (`models/memex_request.py`, clasă Python, nu model Odoo): client SOAP `zeep` către `https://api.pttexpress.ro/?wsdl`, cu timeout de 30 s; verifică serviciile disponibile, evaluează expediția, creează și anulează AWB-ul, ridică asigurarea la valoarea rambursului și tratează răspunsurile pierdute ca rezultat incert (`PttExpressUncertainResult`).

**Vizualizări**

- `view_delivery_carrier_form`: tabul **Memex Configuration** în formularul metodei de livrare, vizibil doar pentru tipul `memex`.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server. Datele conțin cele patru servicii PTT Express (`service_38`, `service_121`, `service_112`, `service_113`) și un `uninstall_hook`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale, dincolo de dependențe, către alte module cu pagină wiki existentă. Urmărirea stării și lockerele nu sunt acceptate de acest modul.
