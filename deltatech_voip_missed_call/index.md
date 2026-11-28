# Phone - Apeluri pierdute de sunat înapoi (localizat la `deltatech_voip_missed_call/index.md`)

- **Nume Tehnic:** `deltatech_voip_missed_call`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_voip_missed_call
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_voip_missed_call`
- **Ultima Ingestie:** `2026-11-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă într-un singur loc, în aplicația Telefon din Odoo, lista clienților care trebuie sunați înapoi. Când un apel primit de la un client rămâne fără răspuns, numărul lui apare în listă o singură dată, iar linia dispare automat de îndată ce cineva vorbește efectiv cu clientul. Astfel, niciun apel pierdut nu mai rămâne uitat, iar operatorii văd aceeași listă comună.

#### 2. Funcționalități Cheie

- **O linie per client:** un apel primit și pierdut (sau respins) creează o linie pentru numărul respectiv, cu contactul, numărul de încercări și ora ultimei încercări. Apelurile pierdute ulterioare de la același număr se adaugă pe aceeași linie, indiferent de formatul numărului (`0721 000 111`, `+40721000111`); numerele sunt comparate în format internațional, cu țara companiei.
- **Închidere automată:** linia se închide când un utilizator vorbește cu clientul: apel răspuns cu acel număr, fie efectuat (apel înapoi), fie primit (clientul a sunat din nou și a fost preluat). Un apel înapoi la care clientul nu răspunde lasă linia deschisă.
- **Listă comună:** fiecare utilizator intern vede liniile companiilor sale, nu doar apelurile care au sunat la el, deci apelurile pierdute din cozi, fără agent, nu se pierd.
- **Marcare ca rezolvat:** un client contactat pe altă cale (mobil, e-mail) se închide manual, cu înregistrarea cine și când a făcut-o.
- **Note pe linie:** operatorii pot scrie o notă direct în listă sau în formular (ex. „vrea ofertă, sunați după 14:00"); nota rămâne pe linie și după închidere. Celelalte câmpuri nu se modifică manual.
- **Apel înapoi dintr-un clic:** numărul de pe linie este link Telefon, deci apelul înapoi pornește din listă.
- **Meniu și filtre:** *Telefon > Apeluri pierdute*; lista se deschide implicit cu filtrul *De sunat înapoi*, iar filtrul *Rezolvate* arată cine a vorbit cu fiecare client.
- **Funcționează cu orice furnizor VoIP:** liniile urmăresc istoricul de apeluri din aplicația Telefon, fie că apelurile vin din softphone-ul Odoo, fie dintr-o integrare precum Daktela.
- **Reluare la instalare:** la instalare se reiau apelurile pierdute și cele răspunse din ultimele 7 zile, astfel încât lista începe cu clienții care încă așteaptă un apel înapoi.
- **Fără configurare:** singura cerință este ca țara companiei să fie setată (necesară normalizării numerelor). Fluxul pas-cu-pas este în fișa consultant.

#### 3. Dependențe

- `voip`

#### 4. Componente Cheie

**Modele**

- `voip.missed.call`: linia de apel de sunat înapoi, unică per companie și număr cât timp este deschisă (stări: *De sunat înapoi* / *Rezolvat*). Reține contactul, apelurile pierdute asociate, numărul de încercări, prima și ultima încercare, utilizatorul care a rămas fără răspuns, cine/când/prin ce apel a fost închisă și nota. Utilizatorii interni pot scrie doar nota; acțiunea *Marchează ca rezolvat* închide liniile manual.
- `voip.call` (extins): adaugă numărul normalizat în format E.164 (`missed_number`, stocat și indexat) și legătura către linia de apel înapoi. La crearea sau schimbarea stării unui apel (pierdut, respins, încheiat) deschide, extinde sau închide linia numărului. Ignoră numerele interne (interioare, sub 3 cifre) și apelurile din cadrul aceleiași companii.

**Vizualizări**

- `voip_missed_call_view_list`: lista editabilă a liniilor, cu nota modificabilă direct în rând.
- `voip_missed_call_view_form`: formularul unei linii, cu apelurile pierdute ale clientului și butonul de marcare ca rezolvat.
- `voip_missed_call_view_search`: căutare și filtre (inclusiv *De sunat înapoi* și *Rezolvate*).
- `voip_missed_call_action` și meniul `voip_missed_call_menu`: *Telefon > Apeluri pierdute*.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: la instalare reia, în ordine cronologică, apelurile pierdute, respinse și încheiate din ultimele 7 zile pentru a popula lista.
- Regulă de acces `voip_missed_call_company_rule`: fiecare utilizator vede doar liniile companiilor permise. Nu există cron-uri.

#### 5. Conexiuni

- [deltatech_voip_daktela](../deltatech_voip_daktela/index.md): apelurile importate din Daktela intră în istoricul Telefon, deci un apel înapoi închide linia imediat din widget sau la importul de 10 minute; lista *Pierdute* din Daktela nu este modificată de acest modul.
