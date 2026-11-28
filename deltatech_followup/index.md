# Invoice Followup (localizat la `deltatech_followup/index.md`)

- **Nume Tehnic:** `deltatech_followup`
- **Versiune:** `20.0.0.1.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_followup
- **Cale Locală:** `odoo-addons/deltatech/deltatech_followup`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul trimite clienților mementouri automate prin e-mail pentru facturi: cu câteva zile înainte de scadență, la scadență sau după. Pentru fiecare etapă (followup) se aleg data de referință, decalajul în zile și șablonul de e-mail, iar mesajul poate lista facturile vizate împreună cu totalurile clientului. Reduce munca manuală de urmărire a încasărilor.

#### 2. Funcționalități Cheie

- **Etape configurabile**: data folosită (data facturii sau scadența), decalajul în zile (`-2` înseamnă cu două zile înainte, `3` după trei zile) și dacă se procesează doar ziua exactă sau în fiecare zi de atunci încolo.
- **Doar facturi deschise**: notele de credit sunt opționale, iar totalurile apar în moneda companiei sau a clientului.
- **Șablon propriu**: definit pe Contact, cu facturile inserate la `[invoices]`, câte un rând pe factură (număr, date, termen de plată, sume), plus totalul de plată, debitul total și suma restantă.
- **Doar clienții marcați**: primesc mementouri cei cu bifa „Send followup e-mails".
- **Marjă de sumă**: nu se trimite nimic când facturile din e-mail însumează mai puțin decât marja (sau o sumă negativă); pe client rămâne o notă cu motivul.
- **Sume și date în limba clientului**: notele de credit apar negative și se scad din total.
- **Erorile rămân locale**: dacă un client nu poate fi procesat (de exemplu un înlocuitor necunoscut), eroarea se loghează și se notează pe client, iar ceilalți sunt procesați.
- **Rulare din acțiune programată**: pentru toate etapele (`model.run_followup()`) sau doar pentru cele cu anumite coduri (`model.run_followup(["f-1", "AZI"])`); utilizatorul acțiunii are nevoie de grupul „Followup manager".
- **Testare**: parametrul de sistem `followup.override_partner_id` redirecționează e-mailurile către un contact de test.

Pașii detaliați sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

Componentele tehnice nu sunt detaliate în `readme/DESCRIPTION.md`, deci această secțiune nu este dezvoltată (conform fluxului de ingestie). Principalele modele sunt `account.invoice.followup` (etapa de followup), `followup.send.wizard` (rulat din acțiunea programată) și extensia `res.partner` (bifa de followup).

#### 5. Conexiuni

Nu există module conexe cu pagină wiki. Modulul se bazează pe facturile clienților din `account`.
