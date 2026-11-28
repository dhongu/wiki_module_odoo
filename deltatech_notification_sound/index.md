# Notification Sound (localizat la `deltatech_notification_sound/index.md`)

- **Nume Tehnic:** `deltatech_notification_sound`
- **Versiune:** `20.0.2.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_notification_sound
- **Cale Locală:** `odoo-addons/deltatech/deltatech_notification_sound`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Operatorii care lucrează în alte ferestre sau departe de ecran pierd notificările afișate în colțul backend-ului Odoo. Modulul redă un sunet scurt la fiecare notificare din backend, diferit pentru fiecare tip de notificare, astfel încât operatorul aude ce s-a întâmplat fără să urmărească ecranul.

#### 2. Funcționalități Cheie

- Un sunet pentru fiecare tip de notificare:
  - succes: `notify.wav`;
  - avertisment (folosit și pentru notificările fără tip): `exclamation.wav`;
  - eroare: `error.wav`;
  - informare: `bell.wav`.
- Fișierele de sunet se găsesc în `static/src/sounds/` și pot fi înlocuite.
- Opțiunea **Enable notification sounds**, bifată implicit, activează sau dezactivează sunetele pentru un utilizator; modificarea se aplică după reîncărcarea paginii.
- Nu necesită configurare: sunetele se aud imediat după instalare. Opțiunea se schimbă din *Settings > Users & Companies > Users*, fila *Preferences* a utilizatorului.
- Limitări: opțiunea e pe formularul de utilizator folosit de administratori (utilizatorii nu o pot schimba din *My Preferences*); browserele pot bloca sunetul până la primul click sau tastare în pagină, deci prima notificare după încărcare poate fi mută; browserele de mobil pot dezactiva sunetele.

#### 3. Dependențe

- `base`
- `web`

#### 4. Componente Cheie

Secțiunea e omisă: `readme/DESCRIPTION.md` nu cere explicit analiza componentelor tehnice.

#### 5. Conexiuni

- Nu există conexiuni funcționale către alte module din wiki.
