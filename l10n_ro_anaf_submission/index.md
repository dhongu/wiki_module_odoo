# Romania - Depunere electronică declarații ANAF (FR-53) (localizat la `l10n_ro_anaf_submission/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_submission`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_submission
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_submission`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul oferă infrastructura comună pentru depunerea electronică a declarațiilor fiscale ANAF generate în Odoo (D112, D300, D394, D406 etc.), conform cerinței FR-53. El nu generează declarațiile — acestea sunt produse de modulele dedicate (`l10n_ro_anaf_d112`, `l10n_ro_anaf_d300`, ...) — ci adaugă stratul de urmărire a depunerii și a recipisei. O înregistrare de depunere păstrează fișierul depus, amprenta SHA-256, ID-ul solicitării ANAF, starea, eventualele erori, recipisa și pista de audit (cine și când a depus), iar declarațiile rectificative păstrează legătura cu depunerea inițială.

#### 2. Funcționalități Cheie

- **Depunere manuală (SPV / e-guvernare)** — fluxul disponibil azi, funcțional complet: contabilul depune fișierul în SPV cu certificatul calificat, introduce ID-ul solicitării în Odoo, iar sistemul verifică starea și păstrează recipisa.
- **Depunere TDec (agent local ANAF)** — conector complet implementat: Odoo trimite fișierul prin API-ul REST TDec (`POST /api/`), preia UID-ul, verifică starea (Index ANAF + „Recipisa OK") și descarcă automat recipisa PDF; aplicația TDec rulează local, ține certificatul calificat și semnează + transmite declarațiile la ANAF.
- **Depunere certSIGN Cloud (API)** — conector de semnare PAdES + upload automat direct; interfața și configurarea există, însă conectorul propriu-zis este un *stub* care necesită API-ul comercial certSIGN și se activează când acesta devine disponibil.
- **Verificarea stării** — interoghează endpoint-ul public ANAF de stare prin ID solicitare (nu necesită certificat) și poate rula automat printr-un cron dezactivat implicit.
- **Urmărirea depunerii și a recipisei** — păstrarea fișierului depus, a amprentei SHA-256, a ID-ului solicitării ANAF, a stării, a erorilor și a recipisei.
- **Pistă de audit** — înregistrarea utilizatorului și a momentului depunerii.
- **Declarații rectificative** — păstrarea legăturii cu depunerea inițială.

#### 3. Dependențe

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

Fișierul `readme/DESCRIPTION.md` este sursa pentru Sumar și Funcționalități Cheie și nu solicită explicit analiza codului pentru componente. Conform fluxului de ingestie din schemă, analiza suplimentară a codului pentru Modele, Vizualizări și Acțiuni Automate / Acțiuni Server a fost omisă.

#### 5. Conexiuni

- `l10n_ro_anaf_d112`: modul dedicat care generează declarația D112 depusă prin acest strat de infrastructură.
- `l10n_ro_anaf_d300`: modul dedicat care generează declarația D300 depusă prin acest strat de infrastructură.
