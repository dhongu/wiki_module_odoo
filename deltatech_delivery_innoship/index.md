# Innoship Shipping (localizat la `deltatech_delivery_innoship/index.md`)

- **Nume Tehnic:** `deltatech_delivery_innoship`
- **Versiune:** `20.0.1.2.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_innoship
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_innoship`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul conectează Odoo la Innoship, o platformă de curierat care agregă peste o sută de curieri europeni sub o singură integrare. În loc de câte o integrare pentru fiecare curier, livrarea este predată către Innoship — cu un curier ales explicit sau lăsat pe seama regulilor proprii de rutare ale Innoship — iar Innoship rezervă transportul, întoarce AWB-ul și eticheta și raportează starea coletului. Tarifarea, generarea AWB-ului, etichetele, anularea și urmărirea se desfășoară în fluxul standard de livrare din Odoo, fără un portal separat de sincronizat. Modulul este în stadiul Beta.

#### 2. Funcționalități Cheie

- O singură cheie API acoperă toți curierii contului; curierul se alege per metodă de livrare din lista curierilor deținuți efectiv, citită de la Innoship, sau se lasă pe seama Innoship („Innoship (best price)").
- Generare AWB și etichetă din livrare, în PDF, ZPL sau HTML, la A6, A4 sau formatul curierului; reobținerea etichetei unui AWB existent (**Print Label**) și anularea transportului (**Cancel Shipment**) la Innoship și la curier.
- Tarifare în timp real pentru comanda de vânzare, câte un tarif per curier deținut; cel mai mic devine prețul de livrare. Alternativ, preț fix, cu prag opțional sub care se interoghează Innoship.
- Lockere și puncte de ridicare din catalogul Innoship, restrânse la curierul și țara configurate, prin catalogul comun `delivery.locker`; AWB-ul se adresează după id-ul locației, iar o locație dispărută din catalog este arhivată, nu ștearsă.
- Import al județelor și localităților Innoship, potrivite cu nomenclatorul Odoo fără a ține cont de diacritice; localitățile nepotrivite rămân „de mapat" în *Inventar > Configurare > Carrier Localities*, nu sunt ghicite.
- Urmărire: istoricul stărilor este preluat periodic de la Innoship și scris pe livrare; o stare nerecunoscută lasă starea existentă neschimbată.
- Opțiuni de expediere: ramburs, valoare declarată, colete multiple (greutatea distribuită pe colete), livrare sâmbăta, colet deschis, retur colet, plată de expeditor sau destinatar, ridicare de la o locație de client înregistrată la Innoship.
- Reîncercări sigure: un răspuns pierdut la crearea sau anularea AWB-ului este raportat ca rezultat incert, deci apăsarea repetată nu rezervă un al doilea AWB; un refuz apare cu id-ul de corelare Innoship, cerut de suportul lor.
- Configurare (tab **Innoship Configuration** pe metoda de livrare): cheia API și formatul etichetei, apoi **Initialization** (citește curierii contului), alegerea **Service**, **Get city** pentru localități; pentru lockere se bifează **Use Locker**, se setează **Locker Country** și **Locker Catalog** și se apasă **Get Lockers**.
- Innoship nu are mediu de test separat: un cont de test folosește aceeași adresă ca unul live, deosebirea fiind doar cheia API.
- Date trimise către Innoship: numele, adresa și telefonul destinatarului, coletele (greutate, valoare declarată), rambursul și adresa de ridicare sau referința ei la Innoship.
- Nesuportate: crearea locațiilor de ridicare la Innoship, manifestul, cererea de ridicare, tipărirea în masă, decontul de ramburs, AWB de retur, webhook de urmărire. Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins, `CarrierInnoship`): rezervare AWB, tarifare, anulare, urmărire și import de curieri/lockere pentru furnizorul Innoship.
- `delivery.carrier.service` (extins): reține curierul numeric Innoship, folosit la adresarea cererilor de etichetă și anulare.
- `res.country.state` / `res.city` (extinse): maparea catalogului de județe și localități Innoship pe nomenclatorul Odoo.
- `stock.picking` (extins): acțiunile de obținere a etichetei și anulare AWB pe livrare.
- `stock.package.type` (extins): suport pentru coletele multiple în cererea de expediere.
- `res.config.settings` (extins): setări generale pentru integrare.
- `InnoshipProvider` / `InnoshipUncertainResult`: clientul API-ului REST Innoship, cu tratarea distinctă a răspunsurilor pierdute în rețea.

**Vizualizări**

- `views/delivery_view.xml`: tabul **Innoship Configuration** pe metoda de livrare.
- `views/res_config_settings_views.xml`: integrare în setările generale.

**Date**

- `data/data.xml`: curieri Innoship uzuali pentru România (Cargus, DPD, Fan Courier, GLS, Sameday ș.a.), înlocuiți efectiv la rularea **Initialization**.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază al integrărilor de curierat.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): catalogul comun de lockere folosit pentru selecție în backend și checkout.
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md): selecția lockerului în magazinul online.
