# Phone - Daktela (localizat la `deltatech_voip_daktela/index.md`)

- **Nume Tehnic:** `deltatech_voip_daktela`
- **Versiune:** `19.0.1.10.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_voip_daktela
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_voip_daktela`
- **Ultima Ingestie:** `2026-11-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul conectează aplicația Telefon (VoIP) din Odoo cu Daktela, centrul de contact în cloud. Utilizatorii pot apela orice număr de telefon din Odoo prin telefonul lor Daktela, văd apelul în widgetul Telefon (inclusiv apelurile primite și cele aflate în așteptare în coadă), iar apelurile încheiate în Daktela apar automat în istoricul de apeluri din Odoo, asociate contactului și utilizatorului potrivit. Funcția „Nu deranjați” din Odoo oprește și sunatul în Daktela.

#### 2. Funcționalități Cheie

- **Domeniu SIP Daktela:** câmpul PBX al furnizorului VoIP este denumit *Domeniu SIP Daktela*, în lista și în formularul furnizorului (*Telefon > Configurare > Furnizori*).
- **Apel prin Daktela:** pentru utilizatorii legați de un agent Daktela, *Sună* de lângă orice număr de telefon sau mobil din Odoo (inclusiv tastatura Telefon, contactele, activitățile și istoricul) cere Daktela să apeleze numărul, în format internațional, de pe telefonul Daktela al utilizatorului. Apelul este inițiat de Daktela, iar partea SIP a softphone-ului Odoo nu este pornită pentru acești utilizatori.
- **Telefon web Daktela sau softphone Odoo:** furnizorul alege cine transportă sunetul. Cu *Telefonul web Daktela* (implicit), apelurile merg prin API-ul Daktela. Cu *Softphone Odoo*, softphone-ul Telefon se înregistrează în Daktela ca dispozitiv WebRTC al agentului, cu datele SIP sincronizate din Daktela (butonul *Sincronizează telefoanele Daktela*), și funcționează ca la orice furnizor SIP. Această variantă nu este documentată oficial de Daktela.
- **Apeluri primite în widget:** cu webhook-ul Daktela configurat (adresă cu token secret, generată pe furnizor și setată în Daktela), un apel primit sună în widgetul Telefon cu contactul găsit după număr, cu *Acceptă* și *Respinge*, fără sonerie Odoo. Un apel preluat în telefonul Daktela apare ca „în convorbire”, iar unul nepreluat apare imediat ca *Apel ratat* în istoric.
- **Apeluri Daktela în widget:** widgetul arată apelul cu cartea de vizită a contactului: *Apel ieșit* până răspunde cealaltă parte, apoi *În convorbire* cu cronometru, citit din Daktela la 2 secunde cât durează apelul. Butonul roșu închide apelul în Daktela, iar un apel închis în Daktela se închide singur și în widget. Transferul, reținerea, înregistrarea, mut și tastatura sunt dezactivate pe durata unui apel Daktela. Butonul *Deschide telefonul Daktela* (căști) din antet deschide telefonul web Daktela.
- **„Nu deranjați” oprește și Daktela (nou în 19.0.1.10.0):** pentru agenții Daktela, *Nu deranjați* din widgetul Telefon (pe o durată sau până la reactivare) pune agentul pe pauza Daktela configurată pe furnizor (*Pauză Daktela pentru Nu deranjați*, câmpul `daktela_dnd_pause`) sau pe *Nepregătit*; Daktela nu mai sună agentul, iar apelanții așteaptă în coadă. *Disponibil* sau expirarea duratei readuce agentul. Expirarea este verificată de un cron la un minut.
- **Fila „În așteptare” (nou în 19.0.1.10.0):** listează apelurile care așteaptă în cozile Daktela, cu contactul găsit după număr, coada și timpul de așteptare; *Acceptă* dă apelul agentului.
- **Indicații pentru operator:** când Daktela refuză apelul (telefon neconectat, operator care nu e pregătit), Odoo spune ce trebuie făcut (deschide clientul WebRTC, pornește aplicația SIP, intră în coada de ieșire, setează starea *Gata*), urmat de motivul dat de Daktela.
- **Istoric de apeluri:** la fiecare 10 minute, apelurile încheiate în Daktela sunt importate în istoricul Telefon, o singură dată fiecare, cu direcție, stare (răspuns, ratat, nepreluat), durată, contact (potrivit după număr) și utilizator (potrivit după agentul Daktela). Apelurile interne sunt omise. Apelul inițiat din Odoo apare imediat în istoric, iar importul îl completează cu orele Daktela.
- **Conexiune API per furnizor:** grupul *API Daktela* din formularul furnizorului conține adresa instanței, tokenul API, fusul orar al orelor apelurilor (implicit Europe/Bucharest), coada de ieșire opțională, pauza pentru *Nu deranjați* și utilizatorul implicit; este vizibil doar administratorilor. Butonul *Testează conexiunea* verifică tokenul.
- **Apeluri fără agent:** Telefon arată fiecare utilizator doar apelurile proprii, de aceea apelurile importate fără agent cunoscut (ex. apeluri ratate din coadă) sunt atribuite utilizatorului implicit.
- **Furnizor implicit:** după configurarea furnizorului Daktela, acesta devine furnizorul implicit al utilizatorilor noi și al celor fără furnizor, deci Telefon nu mai rulează în *Mod demo*.
- **Setări Daktela per utilizator** (tabul VoIP): *Agent Daktela* (numele unic din Daktela, setat doar de administrator, legat de cel mult un utilizator); *Dispozitiv Daktela* opțional (dispozitiv SIP sau număr extern, cu tipul său), pe care Odoo conectează agentul, în coada de ieșire și în starea *Gata* înainte de fiecare apel; *Coadă de ieșire Daktela* opțională; *Utilizator autentificare Daktela*, editabil de utilizator în preferințe, folosit de softphone în locul numelui SIP când Daktela oferă unul separat.
- Fluxul de configurare pas cu pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `voip`

#### 4. Componente Cheie

**Modele**

- `voip.provider` (extins): câmpurile API Daktela (`daktela_url`, `daktela_api_token`, `daktela_phone`, `daktela_dnd_pause`, token și adresă webhook), cererile către API, testul conexiunii, sincronizarea telefoanelor, apelurile în așteptare și importul apelurilor (`_cron_daktela_import_calls`).
- `voip.call` (extins): `daktela_click_to_call`, crearea apelurilor din datele Daktela (câmpul `daktela_id`), potrivirea agentului și a contactului.
- `res.users` / `res.users.settings` (extinse): agentul, dispozitivul, coada și utilizatorul de autentificare Daktela; furnizor implicit; `daktela_dnd_paused` și logica pauzei la schimbarea *Nu deranjați* (`_cron_daktela_end_dnd`).

**Vizualizări**

- `voip_provider_tree_view_inherit_daktela`: coloana *Domeniu SIP Daktela* în lista furnizorilor.
- `voip_provider_view_form_inherit_daktela`: grupul *API Daktela*, webhook-ul și butoanele de test/sincronizare în formularul furnizorului.
- `daktela_res_user_form`, `daktela_res_users_view_form_preferences`: câmpurile Daktela în tabul VoIP al utilizatorului și în preferințe (doar *Utilizator autentificare* editabil).
- Patch-uri JS (`daktela_click_to_call.esm.js`, `daktela_go_ready.esm.js`, `daktela_waiting.esm.js`, `voip_service_patch.esm.js`) și șabloane (`softphone.xml`, `daktela_waiting.xml`) peste widgetul Telefon: apel prin Daktela, starea apelului, fila *În așteptare*.
- Controller `DaktelaWebhook` (`controllers/main.py`): primește evenimentele de apel de la Daktela.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_daktela_import_calls`: la fiecare 10 minute importă apelurile încheiate din Daktela în istoricul Telefon.
- `ir_cron_daktela_end_dnd`: la fiecare minut încheie pauza Daktela a agenților al căror *Nu deranjați* a expirat.

#### 5. Conexiuni

- `voip`: aplicația Telefon (Enterprise) ale cărei furnizori, apeluri și softphone sunt extinse (dependență directă).
- [deltatech_voip_missed_call](../deltatech_voip_missed_call/index.md): complementar, fără dependență în cod; apelurile primite și nepreluate importate din Daktela apar ca *Apel ratat* în istoricul Telefon, de unde lista de apeluri de sunat înapoi le poate prelua.
