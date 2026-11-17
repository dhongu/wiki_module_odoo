# Notification Sound (localizat la `deltatech_notification_sound/index.md`)

- **Nume Tehnic:** `deltatech_notification_sound`
- **Versiune:** `19.0.2.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_notification_sound
- **Cale Locală:** `odoo-addons/deltatech/deltatech_notification_sound`
- **Ultima Ingestie:** `2026-11-17`

#### 1. Sumar

Modulul adaugă feedback sonor pentru notificările din backend-ul Odoo, astfel încât operatorii care lucrează în alte ferestre sau departe de ecran sunt avertizați instantaneu. Când apare o notificare (succes, avertisment, eroare sau informare), se redă automat un sunet scurt și distinct în funcție de tipul mesajului. Sunetele pot fi activate sau dezactivate pentru fiecare utilizator, de către un administrator, iar integrarea este complet transparentă, fără elemente suplimentare de interfață.

#### 2. Funcționalități Cheie

- Redă sunete diferite în funcție de tipul notificării:
  - Succes → `notify.wav`
  - Avertisment (folosit și pentru notificările fără tip) → `exclamation.wav`
  - Eroare (danger) → `error.wav`
  - Informare → `bell.wav`
- Integrare transparentă cu backend-ul (fără interfață suplimentară); aplică un patch peste serviciul `notification` (`add()`), decuplând funcționalitatea de ciclul de viață al componentei OWL `Notification`.
- Activele sunt încărcate prin `web.assets_backend` (JS + sunete).
- Comutator per utilizator, **Enable notification sounds** (bifat implicit): se setează de un administrator în Setări → Utilizatori și companii → Utilizatori, în fila Preferințe a formularului utilizatorului. Utilizatorii nu îl pot schimba singuri din „Preferințele mele"; modificarea are efect după reîncărcarea paginii.
- Preferința este citită din contextul utilizatorului (`user.context.notification_sound_enabled`), fără niciun apel RPC suplimentar; sunetele rămân active dacă preferința lipsește și se opresc doar când a fost dezactivată explicit.
- Fișierele de sunet pot fi înlocuite, fiind stocate în `static/src/sounds/`.
- Limitări: browserele pot bloca sunetul până când utilizatorul face un clic sau tastează în pagină, deci prima notificare după încărcare poate fi silențioasă; browserele mobile pot suprima aceste sunete.

#### 3. Dependențe

- `base`
- `web`

#### 4. Componente Cheie

> Notă: secțiunile de mai jos sunt incluse deoarece fișierul `readme/DESCRIPTION.md` descrie explicit componentele tehnice ale modulului.

**Modele**

- `res.users`: extins cu un câmp nou `notification_sound_enabled` (boolean, implicit `True`) care stochează preferința utilizatorului de a primi feedback sonor la notificări.
- `ir.http`: metoda `session_info()` este îmbogățită pentru a include flag-ul `notification_sound_enabled` în `user_context`, expunând astfel preferința către frontend.

**Vizualizări**

- `views/res_users_views.xml` (`view_users_form_inherit_notification_sound`): adaugă comutatorul „Enable notification sounds" în grupul de preferințe (`other_preferences`) al formularului de utilizator (`base.view_users_form`).

**Componente Frontend (JS / OWL)**

- `static/src/js/notification_sound.esm.js`: aplică un patch (`patch()`) peste `notificationService`, suprascriind metoda `add()` pentru a reda sunetul corespunzător tipului de notificare (`success`, `warning`, `danger`, `info`; implicit `warning`) înainte de afișarea efectivă a mesajului. Redarea eșuează silențios dacă browserul blochează autoplay-ul.
- `static/src/sounds/`: fișierele audio (`notify.wav`, `exclamation.wav`, `error.wav`, `bell.wav`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- Nu există conexiuni funcționale documentate către alte module din wiki.
