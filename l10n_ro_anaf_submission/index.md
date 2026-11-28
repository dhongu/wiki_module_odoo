# Romania - Depunere electronică a declarațiilor ANAF (localizat la `l10n_ro_anaf_submission/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_submission`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_submission
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_submission`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă infrastructura comună pentru depunerea electronică a declarațiilor fiscale ANAF generate în Odoo (D112, D300, D394, D406 etc.). El nu generează declarațiile — acestea sunt produse de modulele dedicate (`l10n_ro_anaf_d112`, `l10n_ro_anaf_d300`, ...) — ci adaugă stratul de urmărire a depunerii și a recipisei. O înregistrare de depunere păstrează fișierul depus, amprenta SHA-256, ID-ul solicitării ANAF, starea, eventualele erori, recipisa și pista de audit (cine și când a depus), iar declarațiile rectificative păstrează legătura cu depunerea inițială.

#### 2. Funcționalități Cheie

- **Depunere manuală (SPV / e-guvernare)** — funcțional complet: contabilul depune fișierul în SPV cu certificatul calificat, introduce ID-ul solicitării în Odoo (fără el, depunerea manuală este refuzată), iar sistemul verifică starea și păstrează recipisa.
- **Depunere prin Terrabit Agent (Terrabit Connect)** — conector complet implementat: Odoo pune fișierul într-o coadă de job-uri; agentul local Terrabit, cu certificatul calificat pe stația contabilului, îl semnează și îl urcă direct la ANAF (SPVWS2), iar ID-ul solicitării, starea și recipisa se sincronizează înapoi în Odoo.
- **Depunere certSIGN Cloud (API)** — conector de semnare PAdES + upload automat direct; interfața și configurarea există, însă conectorul propriu-zis este un *stub* care necesită API-ul comercial certSIGN și se activează când acesta devine disponibil.
- **Registrul depunerilor** în **Contabilitate → Raportare → Declarații ANAF → Depuneri electronice**, cu ciclul de viață Ciornă → Depusă → În prelucrare → Acceptată / Respinsă / Eroare.
- **Verificarea stării** prin butonul **Verifică stare** — interoghează endpoint-ul public ANAF de stare prin ID solicitare (nu necesită certificat) și poate rula automat printr-un cron dezactivat implicit (la 6 ore).
- **Recipisă și pistă de audit** — recipisa se atașează depunerii (butonul **Marchează acceptată** apare după atașare), iar utilizatorul și momentul depunerii sunt reținute și apar în chatter.
- **Declarații rectificative** — butonul **Creează rectificativă** generează o depunere legată de cea inițială, cu buton inteligent care numără corecțiile.
- Configurare în **Setări → Contabilitate**: metoda de depunere implicită și URL-ul public de stare ANAF.
- Cu modulul complementar `l10n_ro_anaf_duk`, fiecare depunere are în plus butonul **Validare DUK** și un status unificat.

#### 3. Dependențe

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md)

#### 4. Componente Cheie

Fișierul `readme/DESCRIPTION.md` este sursa pentru Sumar și Funcționalități Cheie și nu solicită explicit analiza codului pentru componente. Conform fluxului de ingestie din schemă, analiza suplimentară a codului pentru Modele, Vizualizări și Acțiuni Automate / Acțiuni Server a fost omisă.

#### 5. Conexiuni

- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): modul dedicat care generează declarația D112 depusă prin acest strat de infrastructură.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): modul dedicat care generează declarația D300 depusă prin acest strat de infrastructură.
- [l10n_ro_anaf_messages](../l10n_ro_anaf_messages/index.md): preia din SPV recipisele declarațiilor depuse, ca mesaje generale.
- [l10n_ro_anaf_duk](../l10n_ro_anaf_duk/index.md): modul complementar care adaugă validarea DUK și status unificat pe depuneri.
