# Phone - Daktela (localizat la `deltatech_voip_daktela/index.md`)

- **Nume Tehnic:** `deltatech_voip_daktela`
- **Versiune:** `20.0.1.13.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_voip_daktela
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_voip_daktela`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Conectează aplicația Telefon din Odoo cu Daktela, centrala telefonică în cloud. Operatorii sună direct din Odoo, văd apelul în widgetul Telefon, iar istoricul apelurilor din Daktela ajunge automat în Odoo, legat de contact și de utilizator. Modulul este gândit pentru echipe de suport și vânzări care lucrează cu cozi de apeluri în Daktela.

#### 2. Funcționalități Cheie

- **Apel prin Daktela**: pentru utilizatorii legați de un agent Daktela, *Apel* de lângă orice număr cere Daktela să sune numărul de pe telefonul agentului.
- **Telefon web Daktela sau softphone Odoo**: furnizorul alege cine poartă sunetul. Cu softphone-ul Odoo, acesta se înregistrează în Daktela ca dispozitiv WebRTC al agentului, cu credențiale SIP sincronizate (*Sync Daktela phones*), și are suprimare de zgomot.
- **Widget Telefon**: afișează apelul cu cardul contactului (apel inițiat, apoi în convorbire cu cronometru, citit din Daktela la 2 secunde); închiderea se face din butonul roșu sau din Daktela. Transfer, hold, înregistrare și mute sunt dezactivate la apelurile Daktela.
- **Apeluri primite**: se anunță în widget cu *Acceptă* și *Respinge*; apelul fără răspuns devine *Pierdut*. Se configurează cu o adresă de webhook generată pe furnizor, setată în Daktela (*Manage > Settings > Events*).
- **Nu deranja**: pune agentul în pauza Daktela setată pe furnizor (sau *Not ready*); *Disponibil* sau expirarea duratei îl readuce.
- **Dezactivare sonerie** și fila **În așteptare**, cu apelurile din cozile Daktela și butonul *Acceptă* (necesită dreptul *Call pickup* în coadă).
- **Istoric apeluri**: la 10 minute se importă apelurile încheiate, o singură dată fiecare, cu direcție, stare, durată, contact (după număr) și utilizator (după agent). Apelurile interne sunt omise; cele fără agent merg la utilizatorul de rezervă.
- **Apeluri pe țări**: panou lateral *Țară* în istoric, citit din prefixul internațional; numerele se stochează în format internațional.
- **Configurare**: pe furnizor, grupul *Daktela API* (URL instanță, token, fus orar, coadă de ieșire, utilizator de rezervă, buton *Test connection*); pe utilizator, *Daktela Agent* (doar administrator, unic), *Daktela Device* și *Daktela Outbound Queue* opționale.

Fluxul pas cu pas este în fișa de consultant.

#### 3. Dependențe

- `voip`

#### 4. Componente Cheie

**Modele**

- `voip.provider` (extins): câmpurile API Daktela, sincronizarea telefoanelor, webhook.
- `voip.call` (extins): import, țară, legătura cu apelul din Daktela.
- `res.users` și `res.users.settings` (extinse): agent, dispozitiv, coadă și utilizator de autentificare Daktela.
- `mail.activity` (extins): legătura cu apelurile.

**Vizualizări**

- `voip_provider_view_form_inherit_daktela`, `voip_provider_tree_view_inherit_daktela`: formularul și lista furnizorilor.
- `daktela_res_user_form`, `daktela_res_users_view_form_preferences`: fila Telefon a utilizatorului.
- `voip_call_tree_view_inherit_daktela`, `voip_call_view_search_inherit_daktela`: istoricul apelurilor, cu țara.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_daktela_import_calls`: importă apelurile încheiate în istoric, la 10 minute.
- `ir_cron_daktela_end_dnd`: încheie pauza Daktela a unui Nu deranja expirat, la fiecare minut.

#### 5. Conexiuni

- [deltatech_voip_missed_call](../deltatech_voip_missed_call/index.md): lista de apeluri de returnat folosește istoricul importat din Daktela.
- [deltatech_voip_sale](../deltatech_voip_sale/index.md): butonul Comenzi funcționează și la apelurile Daktela.
