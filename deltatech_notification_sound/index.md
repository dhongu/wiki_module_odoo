# Notification Sound (localizat la `deltatech_notification_sound/index.md`)

- **Nume Tehnic:** `deltatech_notification_sound`
- **Versiune:** `19.0.2.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_notification_sound
- **Cale Locală:** `odoo-addons/deltatech/deltatech_notification_sound`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul adaugă feedback sonor pentru notificările din backend-ul Odoo, astfel încât operatorii sunt avertizați instantaneu fără a urmări permanent ecranul. Când apare o notificare (succes, avertisment, eroare sau informare), se redă automat un sunet scurt și distinct în funcție de tipul mesajului. Fiecare utilizator poate activa sau dezactiva sunetele din preferințele proprii, integrarea fiind complet transparentă, fără elemente suplimentare de interfață.

#### 2. Funcționalități Cheie

- Redă sunete diferite în funcție de tipul notificării:
  - Succes → `notify.wav`
  - Avertisment → `exclamation.wav`
  - Eroare (danger) → `error.wav`
  - Informare → `bell.wav`
- Integrare transparentă cu backend-ul (fără interfață suplimentară); aplică un patch peste serviciul `notification` (`add()`), decuplând funcționalitatea de ciclul de viață al componentei OWL `Notification`.
- Activele sunt încărcate prin `web.assets_backend` (JS + sunete).
- Comutator per utilizator în Preferințe: fiecare utilizator poate activa/dezactiva sunetele notificărilor din profilul propriu.
- Preferința este citită direct din informațiile de sesiune (`@web/session`, `session.user_context.notification_sound_enabled`), fără niciun apel RPC suplimentar.
- Fișierele de sunet pot fi înlocuite, fiind stocate în `static/src/sounds/`.

#### 3. Dependențe

- `base`
- `web`

#### 4. Componente Cheie

> Notă: secțiunile de mai jos sunt incluse deoarece fișierul `readme/DESCRIPTION.md` descrie explicit componentele tehnice ale modulului.

**Modele**

- `res.users`: extins cu un câmp nou `notification_sound_enabled` (boolean, implicit `True`) care stochează preferința utilizatorului de a primi feedback sonor la notificări.
- `ir.http`: metoda `session_info()` este îmbogățită pentru a include flag-ul `notification_sound_enabled` în `user_context`, expunând astfel preferința către frontend.

**Vizualizări**

- `views/res_users_views.xml` (`view_users_form_inherit_notification_sound`): adaugă comutatorul „Enable notification sounds" în secțiunea de Preferințe a formularului de utilizator (`base.view_users_form`).

**Componente Frontend (JS / OWL)**

- `static/src/js/notification_sound.esm.js`: aplică un patch (`patch()`) peste `notificationService`, suprascriind metoda `add()` pentru a reda sunetul corespunzător tipului de notificare (`success`, `warning`, `danger`, `info`; implicit `warning`) înainte de afișarea efectivă a mesajului. Redarea eșuează silențios dacă browserul blochează autoplay-ul.
- `static/src/sounds/`: fișierele audio (`notify.wav`, `exclamation.wav`, `error.wav`, `bell.wav`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- Nu există conexiuni funcționale documentate către alte module din wiki.
