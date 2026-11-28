# Postis Shipping Locker (localizat la `deltatech_delivery_postis_locker/index.md`)

- **Nume Tehnic:** `deltatech_delivery_postis_locker`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_postis_locker
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_postis_locker`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Acest modul permite clientului unui magazin online să aleagă, direct la finalizarea comenzii, un locker sau un punct de ridicare Postis de pe harta pusă la dispoziție de Postis, astfel încât coletul să fie expediat acolo și nu la adresa de domiciliu. Extinde metoda de livrare **Postis Shipping** cu widget-ul de hartă al Postis, înregistrează locația aleasă și adresează AWB-ul către acea locație, nu către client.

#### 2. Funcționalități Cheie

- **Selecția locației pe harta Postis**: harta se deschide la checkout, la pasul de livrare, doar pentru coșurile în care toate produsele sunt marcate ca potrivite pentru locker; cheia hărții se configurează pe metoda de livrare, per cont de client; există mod demo pentru hartă, independent de credențialele API.
- **Selecția este înregistrată, nu doar afișată**: locația aleasă se salvează în catalogul comun de lockere (`delivery.locker`), se creează o adresă de livrare pentru ea și se setează pe comandă; aceeași locație aleasă din nou refolosește înregistrările existente; comanda este recotată la adresa locației.
- **Adresare corectă a AWB-ului**: expedierea poartă id-ul locației și localitatea ei; localitatea este rezolvată pe nomenclatorul Odoo, astfel încât Postis primește un id de localitate, nu doar un nume; o localitate ambiguă rămâne nerezolvată, nu este ghicită.
- **O selecție ilizibilă oprește checkout-ul**: payload-ul este acceptat sub toate grafiile de câmpuri folosite de harta Postis; o selecție fără id de locație identificabil readuce clientul la pasul de livrare cu un mesaj, în loc să confirme o comandă care ar pleca la adresa de domiciliu.
- **Configurare** (pe metoda de livrare Postis): se bifează **Use Locker**, se completează **Postis Map Key** (obligatoriu pentru deschiderea hărții) și, opțional, **Postis Map Demo Mode** (afectează doar harta; AWB-ul se emite mereu cu credențialele metodei). Produsele care încap într-un locker se marchează cu **For Locker**; un coș cu un produs nemarcat nu primește transportatorul de locker.
- **Limite cunoscute**: payload-ul hărții este citit sub mai multe grafii, deoarece Postis nu l-a publicat ca contract stabil (la un nume neacoperit, checkout-ul se oprește cu mesaj și payload-ul se scrie în log); nu există import al catalogului de lockere Postis, deci harta din backend arată doar locațiile folosite cel puțin o dată.

#### 3. Dependențe

- [deltatech_delivery_postis](../deltatech_delivery_postis/index.md)
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, deoarece există `readme/DESCRIPTION.md`, analiza codului pentru această secțiune este omisă. Pentru orientare, modulul extinde `delivery.carrier` și `website` (în `models/`) și conține vizualizările `views/delivery_view.xml` și `views/templates.xml` (butonul hărții la checkout).

#### 5. Conexiuni

- [deltatech_delivery_postis](../deltatech_delivery_postis/index.md): metoda de livrare Postis de bază, extinsă cu selecția de locker pe hartă.
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md): filtrarea metodelor de livrare după compatibilitatea produselor (`for_locker`) și contextul de checkout.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): catalogul comun `delivery.locker` în care se înregistrează locația aleasă (prin `deltatech_delivery_locker_website`).
