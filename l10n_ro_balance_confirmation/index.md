# Confirmare de Sold pentru România (localizat la `l10n_ro_balance_confirmation/index.md`)

- **Nume Tehnic:** `l10n_ro_balance_confirmation`
- **Versiune:** `19.0.0.0.8`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_balance_confirmation
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_balance_confirmation`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul „Confirmare de Sold pentru România" este o extensie Odoo specializată care generează documente de confirmare a soldului pentru partenerii de afaceri, conform cerințelor contabile românești. Permite companiilor să creeze extrase de cont pentru partenerii lor (clienți și furnizori) la o dată specificată, facilitând procesul de reconciliere a soldurilor și asigurând conformitatea cu reglementările financiare locale. Documentele rezultate includ și un formular de răspuns integrat, ușurând procedura de confirmare și procesul de audit.

#### 2. Funcționalități Cheie

- **Generarea extrasului de cont**: creează extrase de cont pentru parteneri la o dată specificată, în format standard conform cerințelor din România, cu generare PDF pentru documentare și distribuire și posibilitatea selectării mai multor parteneri pentru generare în lot.
- **Calculul soldului la o dată specifică**: calcul precis al soldurilor partenerilor la o dată dată, cu suport pentru debite și credite, extinzând funcționalitatea nativă Odoo pentru raportare la dată istorică și afișarea corectă a soldurilor în moneda companiei.
- **Șablon de document personalizat**: format standard de extras de cont conform normelor românești, cu secțiune pentru informațiile emitentului (companie), secțiune pentru informațiile destinatarului (partener), afișarea soldului la data specificată și textul standard al procedurii de confirmare.
- **Formular de răspuns**: secțiune integrată pentru răspunsul partenerului, cu opțiuni de confirmare a sumei, spațiu pentru menționarea modalității de plată, secțiune pentru obiecții și explicații în caz de discrepanțe și spații pentru semnăturile persoanelor responsabile.
- **Interfață de utilizare simplă**: wizard pentru selectarea datei de raportare, posibilitatea de a selecta mai mulți parteneri simultan, generare directă din interfața partenerilor și validări pentru evitarea erorilor de utilizare.

#### 3. Dependențe

- `account`
- `l10n_ro_config`

#### 4. Componente Cheie

Conform secțiunii „Technical Implementation" din `readme/DESCRIPTION.md`, modulul extinde funcționalitatea standard Odoo pentru parteneri astfel:

**Modele**

- `res.partner`: extins pentru calculul corect al soldurilor la o dată specificată (debite și credite, în moneda companiei).

**Vizualizări**

- Wizard pentru introducerea datei de referință și selectarea partenerilor, cu generare directă din interfața partenerilor.

**Rapoarte**

- Șablon QWeb personalizat pentru extrasul de cont (confirmarea de sold), cu format standard românesc și formular de răspuns integrat.

> Notă: detalierea completă a modelelor, vizualizărilor și acțiunilor automate nu a fost extrasă din cod, deoarece `readme/DESCRIPTION.md` este prezent și acoperă secțiunile de mai sus la nivel descriptiv (conform fluxului de ingestie din `schema.md`). Fișierele `readme/USAGE.md` și `readme/FISA_CONSULTANT.md` nu există în modul.

#### 5. Conexiuni

- `account`: modulul de contabilitate de bază care furnizează datele de sold ale partenerilor folosite în confirmare.
- `l10n_ro_config`: configurarea localizării românești pe care se sprijină acest modul.
