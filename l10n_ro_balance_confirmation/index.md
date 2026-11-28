# Romania - Confirmare de sold (localizat la `l10n_ro_balance_confirmation/index.md`)

- **Nume Tehnic:** `l10n_ro_balance_confirmation`
- **Versiune:** `20.0.2.3.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_balance_confirmation
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_balance_confirmation`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul generează documente de **confirmare de sold** (extras de cont) pentru partenerii de afaceri, conform cerințelor contabile din România: le tipărește la cerere sau le trimite în masă pe email, cu urmărire pe fiecare partener. Combină două fluxuri complementare: tipărirea la cerere a extrasului pentru unul sau mai mulți parteneri la o dată aleasă și o campanie pe email, cu un document dedicat care păstrează câte o linie per partener și urmărește rezultatul fiecărei confirmări. Ajută firmele să deruleze campanii periodice de reconciliere (de exemplu la inventarierea anuală a creanțelor și datoriilor) și să păstreze un istoric auditabil al comunicării cu partenerii.

#### 2. Funcționalități Cheie

- **Tipărire la cerere:** din **Facturare → Clienți → Clienți**, bifați partenerii și alegeți **Tipăriți → Confirmare sold**; dialogul cere data confirmării, data emiterii, tipul partenerului (client / furnizor / ambele), termenul de răspuns și, opțional, afișarea avansurilor; rezultatul este un PDF cu câte un extras per partener.
- **Campanie pe email cu urmărire:** document numerotat `CONF/AAAA/00001`, cu flux ciornă → generat → trimis → finalizat; în **Facturare → Clienți → Confirmări de sold**, scopul se stabilește pe parteneri sau pe tip de cont (creanțe / datorii / ambele), cu omiterea soldurilor zero. Butoanele **Generează liniile → Generează PDF-urile → Trimite email-urile** (sau **Generează și trimite**); fiecare linie are starea pregătit / fără email / trimis / eroare, soldul la dată, PDF-ul atașat și data trimiterii; contoare live și istoric în chatter. Liniile cu eroare se retrimit după corectare.
- **Urmărirea răspunsurilor:** emailul se postează în chatterul partenerului, iar răspunsul lui ajunge în același fir și marchează linia ca *Răspuns primit*; contabilul o marchează apoi *Confirmat* sau *Neconfirmat* (cu soldul partenerului, diferența calculată automat și observații). Meniul **Răspunsuri la confirmările de sold** oferă filtre pentru soldurile neconfirmate de la inventariere.
- **Documente deschise la data de referință:** sub sold, PDF-ul listează documentele încă deschise (tip și număr, dată, scadență, valoare inițială, rest), cu restul calculat la data confirmării din reconcilierile parțiale de până la acea dată; plățile nealocate și avansurile pot fi într-un tabel separat, iar totalul tabelului egalează soldul afișat; export XLSX din dialog și din campanie.
- **Confirmare în valută:** documentele sunt grupate pe monedă, cu suma în moneda documentului și contravaloarea în lei la cursul documentelor; filtru de monedă (toate, doar moneda companiei sau una anume).
- **Soldul la o dată anume:** calculat din liniile postate până la acea dată, independent de reconcilierile ulterioare; se confirmă doar conturile comerciale (clienți 411x / 413x, furnizori 401x / 403x / 404x), iar avansurile 409 / 419 pot fi afișate separat.
- **Șablon de document personalizat:** secțiuni emitent și destinatar, text standard de confirmare, formular de răspuns integrat (sumă confirmată, mod de plată, obiecții, semnături), titlu editabil (implicit „EXTRAS DE CONT"), semnatari cu nume și funcție (impliciți pe companie, în fila **Confirmare sold**, modificabili la fiecare tipărire sau campanie); partenerii români primesc documentul în română, ceilalți în limba lor; emailul este bilingv RO/EN.
- **Drepturi:** grupurile „Poate tipări confirmare sold" și „Trimitere confirmări de sold"; pentru răspunsuri automate sunt necesare serverul de email de ieșire și aliasul / catchall-ul pe intrare.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `mail`

#### 4. Componente Cheie

Analiza codului pentru această secțiune a fost limitată la elementele pe care le menționează explicit `readme/DESCRIPTION.md` (secțiunea „Technical Implementation").

**Modele**

- `res.partner` (extins): calculează soldurile de încasat / de plătit la o dată dată (`_credit_debit_get` cu contextul `date_to`), ca sumă `debit - credit` a liniilor postate până la acea dată.
- `l10n.ro.balance.confirmation`: documentul campaniei, cu linii per partener și flux generare → randare PDF → trimitere.
- `l10n_ro.balance_confirm_dialog` (wizard): dialogul de tipărire la cerere din fișa partenerului.
- Model abstract partajat pentru opțiunile documentului (documente deschise, filtru de monedă, titlu, semnatari), folosit de wizard și de campanie.

**Vizualizări**

- Raportul QWeb al extrasului de cont românesc.
- `views/res_partner_balance.xml`, `wizard/confirm_balance.xml`, `views/l10n_ro_balance_confirmation_views.xml`: opțiunea de tipărire, dialogul și campaniile cu liniile și răspunsurile lor.

**Acțiuni Automate / Acțiuni Server**

- `data/mail_template_data.xml`: șablonul de email bilingv (`mail.template`) cu PDF-ul confirmării atașat.
- `data/sequence_data.xml`: secvența de numerotare a campaniilor (`CONF/AAAA/00001`).

#### 5. Conexiuni

- `l10n_ro_report_common`: nu mai este dependență directă; modulul folosește doar `account`, `l10n_ro` și `mail`.
