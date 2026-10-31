# Invoice Followup (localizat la `deltatech_followup/index.md`)

- **Nume Tehnic:** `deltatech_followup`
- **Versiune:** `19.0.0.1.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_followup
- **Cale Locală:** `odoo-addons/deltatech/deltatech_followup`
- **Ultima Ingestie:** `2026-10-31`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul trimite clienților mesaje e-mail automate de reamintire pentru facturile neîncasate: cu câteva zile înainte de scadență, chiar în ziua scadenței sau după aceasta. Pentru fiecare pas de reamintire (un *followup*) se aleg data de referință, decalajul în zile și șablonul de e-mail, iar mesajul poate lista facturile vizate împreună cu totalurile clientului. Valoarea de afaceri constă în reducerea efortului manual de relaționare cu clienții pentru încasarea creanțelor și în îmbunătățirea fluxului de numerar.

#### 2. Funcționalități Cheie

- **Pași de reamintire configurabili:** data folosită (data facturii sau data scadenței), decalajul în zile (`-2` = cu două zile înainte, `3` = la trei zile după) și comparatorul: **Equal** procesează doar ziua exactă (o zi în care acțiunea programată nu rulează se pierde), iar **Greater or equal** procesează toate facturile de la acea zi încolo, deci reamintirea se repetă zilnic.
- **Doar facturi deschise:** opțiunea **Only open invoices** (implicit activă); notele de credit sunt opționale (**Parse refund invoices**), iar totalurile se pot afișa în moneda companiei sau în moneda clientului (**Use customer currency**).
- **Șablon de e-mail propriu:** se creează pe modelul Contact și se alege în followup (câmp obligatoriu). Facturile se inserează în locul marcajului `[invoices]`, câte un rând per factură (număr, date, termen de plată, sume), definit în câmpul **Invoices placeholder** cu `$number`, `$payment_term_id`, `$date_invoice`, `$date_due`, `$amount_untaxed`, `$amount_tax`, `$amount_total`, `$amount_due`, `$currency`. În corpul șablonului se pot folosi `${object.name}`, `$total_debit`, `$total_all_debit`, `$total_due_debit` și `$currency`.
- **Doar clienții marcați:** primesc reamintiri partenerii cu opțiunea **Send followup e-mails** bifată (sub câmpul **Tags**); bifa trebuie pusă pe contactul care apare pe factură, nu pe compania-părinte.
- **Marjă de sumă:** nu se trimite nimic dacă facturile din e-mail însumează marja configurată sau mai puțin (ori o sumă negativă, când notele de credit depășesc facturile), iar pe client se postează o notă cu motivul.
- **Sume și date în limba clientului:** notele de credit apar cu semn negativ și se scad din total.
- **Erorile rămân locale:** dacă un client nu poate fi procesat (de exemplu un marcaj necunoscut), eroarea se loghează și se notează pe acel client, iar ceilalți clienți sunt procesați în continuare.
- **Rulare dintr-o acțiune programată:** pe modelul `followup.send.wizard`, cu `model.run_followup()` pentru toate followup-urile sau `model.run_followup(["f-1", "AZI"])` pentru cele cu codurile date, astfel încât pași diferiți să ruleze la momente diferite. Utilizatorul acțiunii programate are nevoie de grupul **Followup manager**.
- **Configurare:** followup-urile se definesc în **Facturare > Configurare > Followups** (drepturi de manager contabilitate și grupul **Followup manager**).
- **E-mailurile trimise** apar în **Setări > Tehnic > Email > Emails** până la expediere; cu **Auto Delete** activ pe șablon se șterg după trimitere.
- **Testare:** parametrul de sistem `followup.override_partner_id` (id de contact) redirecționează e-mailurile către acel contact; se șterge înainte de intrarea în producție.
- O reamintire nu înlocuiește o notificare formală de neplată. Fluxul pas cu pas este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

*Conform fluxului de ingestie, analiza detaliată a componentelor este omisă, deoarece `readme/DESCRIPTION.md` este prezent și nu o cere explicit. Mai jos sunt doar reperele confirmate în cod.*

**Modele**

- `account.invoice.followup`: definiția unui pas de reamintire (dată de referință, decalaj, comparator, șablon, marjă, cod).
- `followup.send.wizard`: model tranzitoriu cu metoda `run_followup(codes)`, apelată din acțiunea programată.
- `res.partner` (extins): câmpul `send_followup`.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu livrează un cron preconfigurat; acțiunea programată se creează manual (vezi mai sus).

#### 5. Conexiuni

Nu au fost identificate module conexe cu pagină wiki existentă. Modulul se integrează cu contabilitatea standard (`account`) pentru facturile clienților.
