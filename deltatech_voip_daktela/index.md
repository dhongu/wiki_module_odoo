# Phone - Daktela

- **Nume Tehnic:** `deltatech_voip_daktela`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_voip_daktela
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_voip_daktela`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul conectează aplicația Telefon (VoIP) din Odoo cu Daktela, centrul de contact în cloud. Utilizatorii pot apela un contact direct din fișa acestuia, prin telefonul lor Daktela, iar apelurile încheiate în Daktela apar automat în istoricul de apeluri din Odoo, asociate contactului și utilizatorului potrivit.

#### 2. Funcționalități Cheie

- **Domeniu SIP Daktela:** câmpul PBX al furnizorului VoIP este denumit *Domeniu SIP Daktela*, în lista și în formularul furnizorului (*Telefon > Configurare > Furnizori*).
- **Apel prin Daktela:** butonul *Sună prin Daktela* de pe fișa contactului cere Daktela să apeleze numărul contactului de pe telefonul Daktela al utilizatorului; apelul este inițiat de Daktela, nu de softphone-ul Odoo.
- **Istoric de apeluri:** la fiecare 10 minute, apelurile încheiate în Daktela sunt importate în istoricul Telefon, cu direcție, stare (răspuns, ratat, fără răspuns), durată, contact (potrivit după număr) și utilizator (potrivit după agentul Daktela). Apelurile interne sunt omise, iar fiecare apel este importat o singură dată.
- **Conexiune API per furnizor:** grupul *API Daktela* din formularul furnizorului conține adresa instanței, tokenul API, fusul orar al orelor apelurilor și utilizatorul implicit; este vizibil doar administratorilor.
- **Apeluri fără agent:** Telefon arată fiecare utilizator doar apelurile proprii, de aceea apelurile importate fără agent cunoscut (ex. apeluri ratate din coadă) sunt atribuite utilizatorului implicit.
- **Setări Daktela per utilizator:** în tabul VoIP al utilizatorului, *Agent Daktela* (numele unic din Daktela, setat doar de administrator, legat de cel mult un utilizator) și, opțional, *Utilizator autentificare Daktela*, editabil de utilizator în preferințe, folosit de softphone în locul numelui SIP când Daktela oferă unul separat.
- Apelurile primite și nepreluate apar ca *Apel ratat*, iar cele ieșite și nepreluate ca *Apel anulat*.
- Fluxul de configurare pas cu pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `voip`

#### 4. Componente Cheie

**Modele**

- `voip.provider` (extins): câmpurile API Daktela și logica de import a apelurilor (`_cron_daktela_import_calls`).
- `voip.call` (extins): crearea apelurilor din datele Daktela, potrivirea agentului și a contactului.
- `res.users` / `res.users.settings` (extinse): *Agent Daktela* și *Utilizator autentificare Daktela*.
- `res.partner` (extins): acțiunea *Sună prin Daktela*.

**Vizualizări**

- `voip_provider_tree_view_inherit_daktela`: coloana *Domeniu SIP Daktela* în lista furnizorilor.
- `voip_provider_view_form_inherit_daktela`: grupul *API Daktela* în formularul furnizorului.
- `daktela_res_user_form`, `daktela_res_users_view_form_preferences`: câmpurile Daktela în tabul VoIP al utilizatorului și în preferințe.
- `view_partner_form_inherit_daktela`: butonul *Sună prin Daktela* pe contact.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_daktela_import_calls`: la fiecare 10 minute importă apelurile încheiate din Daktela în istoricul Telefon.

#### 5. Conexiuni

- `voip`: aplicația Telefon în care sunt importate apelurile (dependență directă).
