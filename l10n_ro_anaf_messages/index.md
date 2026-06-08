# Romania - Mesaje SPV ANAF (generale) (localizat la `l10n_ro_anaf_messages/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_messages`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_messages`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_messages`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul citește mesajele generale din Spațiul Privat Virtual (SPV) al ANAF — notificări și recipisele declarațiilor fiscale — separat de mesajele e-Factura (care rămân în modulul `l10n_ro_message_spv`). Folosește serviciul SPVWS2 (`webserviced.anaf.ro/SPVWS2/rest/listaMesaje`, `descarcare`) prin OAuth2 Bearer, refolosind tokenul de acces gestionat de modulul standard `l10n_ro_edi` (e-Factura). Deoarece ANAF a unificat accesul SPV / e-Factura / e-Transport pe același token `logincert.anaf.ro`, nu este nevoie de un certificat suplimentar pe server: după o singură autentificare din browser (token valabil aproximativ 90 de zile), mesajele se descarcă complet server-side. Recipisele declarațiilor sosesc tot ca mesaje SPV, iar acest modul oferă canalul de preluare a lor, complementar modulului de depunere `l10n_ro_anaf_submission`.

#### 2. Funcționalități Cheie

- Model `l10n.ro.anaf.message` cu mesajele SPV (ID, CIF, tip, dată, detalii, ID solicitare).
- Clasificare automată a tipului mesajului: recipisă / notificare / solicitare / eroare.
- Descărcarea documentului (PDF) asociat fiecărui mesaj.
- Sincronizare manuală (prin buton) și sincronizare programată prin cron (dezactivat implicit).
- Bază URL configurabilă pe companie (mediu de test / producție).

#### 3. Dependențe

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md)

#### 4. Componente Cheie

Analiza codului pentru această secțiune a fost omisă, conform fluxului de ingestie din schema wiki: fișierul `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie, fără a solicita explicit detalierea componentelor tehnice (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server).

#### 5. Conexiuni

- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): modul de depunere a declarațiilor fiscale; recipisele declarațiilor depuse sosesc ca mesaje SPV preluate de acest modul, fiind complementare.
- `l10n_ro_message_spv`: gestionează mesajele SPV de tip e-Factura; acest modul tratează separat mesajele SPV generale (notificări și recipise de declarații).
- `l10n_ro_edi`: modul standard e-Factura care gestionează tokenul OAuth2 / accesul unificat ANAF refolosit pentru descărcarea mesajelor SPV.
