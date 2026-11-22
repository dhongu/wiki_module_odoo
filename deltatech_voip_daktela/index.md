# Phone - Daktela (localizat la `deltatech_voip_daktela/index.md`)

- **Nume Tehnic:** `deltatech_voip_daktela`
- **Versiune:** `19.0.1.9.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_voip_daktela
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_voip_daktela`
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul conectează aplicația Telefon (VoIP) din Odoo cu Daktela, centrul de contact în cloud. Utilizatorii pot apela orice număr de telefon din Odoo prin telefonul lor Daktela, iar apelurile încheiate în Daktela apar automat în istoricul de apeluri din Odoo, asociate contactului și utilizatorului potrivit.

#### 2. Funcționalități Cheie

- **Domeniu SIP Daktela:** câmpul PBX al furnizorului VoIP este denumit *Domeniu SIP Daktela*, în lista și în formularul furnizorului (*Telefon > Configurare > Furnizori*).
- **Apel prin Daktela:** pentru utilizatorii legați de un agent Daktela, *Sună* de lângă orice număr de telefon sau mobil din Odoo (inclusiv contactele, activitățile și istoricul din Telefon) cere Daktela să apeleze numărul, în format internațional, de pe telefonul Daktela al utilizatorului. Apelul este inițiat de Daktela, iar softphone-ul Odoo nu mai este pornit pentru acești utilizatori (fără *Apel demo* sau erori SIP).
- **Indicații pentru operator:** când Daktela refuză apelul (telefon neconectat, operator care nu e pregătit), Odoo spune ce trebuie făcut (deschide clientul WebRTC, pornește aplicația SIP, intră în coada de ieșire, setează starea *Gata*), urmat de motivul dat de Daktela.
- **Istoric de apeluri:** la fiecare 10 minute, apelurile încheiate în Daktela sunt importate în istoricul Telefon, o singură dată fiecare, la ora reală a apelului, cu direcție, stare, durată, contact (potrivit după număr) și utilizator (potrivit după agentul Daktela). Apelurile interne sunt omise. Cele primite și nepreluate apar ca *Apel ratat*, cele ieșite și nepreluate ca *Apel anulat*.
- **Conexiune API per furnizor:** grupul *API Daktela* din formularul furnizorului conține adresa instanței, tokenul API, fusul orar al orelor apelurilor (implicit Europe/Bucharest), coada de ieșire opțională și utilizatorul implicit; este vizibil doar administratorilor. Butonul *Testează conexiunea* verifică tokenul și arată utilizatorul Daktela al acestuia.
- **Apeluri fără agent:** Telefon arată fiecare utilizator doar apelurile proprii, de aceea apelurile importate fără agent cunoscut (ex. apeluri ratate din coadă) sunt atribuite utilizatorului implicit.
- **Furnizor implicit:** după configurarea furnizorului Daktela, acesta devine furnizorul implicit al utilizatorilor noi și al celor fără furnizor, deci Telefon nu mai rulează în *Mod demo*; un utilizator fără agent Daktela care sună primește mesajul să fie legat de un agent.
- **Setări Daktela per utilizator** (tabul VoIP): *Agent Daktela* (numele unic din Daktela, setat doar de administrator, legat de cel mult un utilizator); *Dispozitiv Daktela* opțional (dispozitiv SIP sau număr extern, cu tipul său), pe care Odoo conectează agentul, în coada de ieșire și în starea *Gata* înainte de fiecare apel; *Coadă de ieșire Daktela* opțională, pentru agenții care sună printr-o altă coadă decât cea a furnizorului; *Utilizator autentificare Daktela*, editabil de utilizator în preferințe, folosit de softphone în locul numelui SIP când Daktela oferă unul separat.
- Fluxul de configurare pas cu pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `voip`

#### 4. Componente Cheie

**Modele**

- `voip.provider` (extins): câmpurile API Daktela, cererile către API, testul conexiunii, autentificarea agentului și importul apelurilor (`_cron_daktela_import_calls`).
- `voip.call` (extins): `daktela_click_to_call`, crearea apelurilor din datele Daktela (câmpul `daktela_id`), potrivirea agentului și a contactului.
- `res.users` / `res.users.settings` (extinse): agentul, dispozitivul, coada și utilizatorul de autentificare Daktela; furnizor implicit.

**Vizualizări**

- `voip_provider_tree_view_inherit_daktela`: coloana *Domeniu SIP Daktela* în lista furnizorilor.
- `voip_provider_view_form_inherit_daktela`: grupul *API Daktela* și butonul de test în formularul furnizorului.
- `daktela_res_user_form`, `daktela_res_users_view_form_preferences`: câmpurile Daktela în tabul VoIP al utilizatorului și în preferințe (doar *Utilizator autentificare* editabil).
- Patch-uri JS (`daktela_click_to_call.esm.js`, `voip_service_patch.esm.js`) peste serviciile `Voip` și `UserAgent` din Telefon, care redirecționează apelul prin Daktela.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_daktela_import_calls`: la fiecare 10 minute importă apelurile încheiate din Daktela în istoricul Telefon.

#### 5. Conexiuni

- `voip`: aplicația Telefon (Enterprise) ale cărei furnizori, apeluri și softphone sunt extinse (dependență directă).
