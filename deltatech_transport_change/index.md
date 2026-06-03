# DeltaTech Transport Change (localizat la `deltatech_transport_change/index.md`)

- **Nume Tehnic:** `deltatech_transport_change`
- **Versiune:** `19.0.0.1.4`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_transport_change`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_transport_change`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

DeltaTech Transport Change este un modul tehnic Odoo conceput pentru a gestiona exportul modificărilor de configurație și transportul acestora între medii (Dezvoltare → Staging → Producție) într-o manieră structurată și controlată prin versiuni. Modulul oferă o funcționalitate similară cu cererile de transport din SAP, permițând administratorilor de sistem și consultanților să urmărească, să exporte și să migreze datele de configurație în siguranță. Este ideal pentru clienții cu mai multe instanțe Odoo, unde modificările de configurație trebuie aplicate consecvent și trasabil între medii, ajutând la menținerea reproductibilității, a auditabilității și a controlului versiunilor pentru datele tehnice de configurație.

#### 2. Funcționalități Cheie

- **Export configurație în CSV/XML:** exportă cu ușurință modele, câmpuri și înregistrări selectate, cu filtre de domeniu opționale, declanșat dintr-un buton de formular sau dintr-o acțiune server de listă. Prima coloană din CSV-ul generat este întotdeauna External ID-ul (`id`) fiecărei înregistrări, asigurând reimport fiabil și consecvență între medii.
- **Maparea relațiilor:** convertește automat câmpurile relaționale many2one și many2many în referințe XMLID pentru un transport fiabil.
- **Integrare cu repository (Repo):** stochează informații despre modulele clientului, URL-urile repository-urilor Git, ramurile și credențialele, pentru a facilita implementarea controlată prin versiuni.
- **Automatizare Git:** suportă commit automat și push opțional al fișierelor de configurație exportate către repository.
- **Transport între medii:** permite migrarea în siguranță a modificărilor de configurație din Dezvoltare către Staging și Producție.
- **Extensibil și configurabil:** adăugarea de noi modele, câmpuri și configurații de export fără modificarea nucleului modulului.

#### 3. Dependențe

- `base`
- `mail`

Dependență externă Python: `GitPython`.

#### 4. Componente Cheie

Sumarul și funcționalitățile au fost preluate din `readme/DESCRIPTION.md`, care nu detaliază componente tehnice specifice. Conform fluxului de ingestie, analiza codului pentru această secțiune este omisă.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale cu alte module documentate în wiki.
