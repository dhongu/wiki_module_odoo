# Deltatech Partner Gifts (localizat la `deltatech_partner_gifts/index.md`)

- **Nume Tehnic:** `deltatech_partner_gifts`
- **Versiune:** `19.0.0.1.11`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_partner_gifts
- **Cale Locală:** `odoo-addons/bitshop/deltatech_partner_gifts`
- **Ultima Ingestie:** `2026-11-12`

#### 1. Sumar

Trimiterea de cadouri către clienți și parteneri cere evidența cine primește ce, unde și cum. Modulul ține cadourile ca linii, le creează în masă și tipărește etichetele de livrare, simplificând organizarea campaniilor de cadouri către parteneri.

#### 2. Funcționalități Cheie

- **Linii de cadou:** meniul *Gift lines* listează câte o linie pe cadou, cu *Partner*, *Partner address* (opțional), *Gift date*, *Type* (Calendar / Simple / Medium / VIP), *Reason*, *Salesperson*, etichetele partenerului (*Tags*) și o stare de la *Draft* la *Done* (Draft, Approved, Ready, Sent, Done).
- **Adăugare în masă:** acțiunea *Add gifts*, rulată pe contactele selectate, creează pentru fiecare contact o linie *Draft* cu tipul, data, motivul și transportatorul introduse, plus agentul de vânzări al contactului și prima adresă de livrare, dacă există.
- **Copiere sau modificare:** *Copy/Modify* duplică liniile selectate sau le modifică pe toate deodată, folosind doar valorile completate; o copie cere o *Gift date*.
- **Etichetă de livrare:** *Print partner gifts* tipărește câte o pagină pe cadou, cu expeditorul (compania utilizatorului) și numele, adresa și telefonul destinatarului, plus *Attention of*. Destinatarul este *Partner address*, altfel prima adresă de livrare a partenerului, altfel partenerul însuși.
- **Valoare facturată:** acțiunea *Get partner data* setează *Invoiced this year* la facturile de client postate minus notele de credit din anul curent; rămâne zero fără aplicația de facturare.
- Pe contact, butonul *Gifts* deschide liniile de cadou ale acestuia. Grupul *User* poate citi liniile; *Admin* le poate edita și poate rula acțiunile în masă, inclusiv *Set done* și *Set draft*.

#### 3. Dependențe

- `contacts`

#### 4. Componente Cheie

Conform regulilor de ingestie, Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`; mai jos sunt doar reperele confirmate în cod.

**Modele**

- `partner.gift.line`: linia de cadou (cu `mail.thread`, câmpurile principale urmărite) — partener, adresă, dată, stare, tip, motiv, agent de vânzări, tip și detalii transportator, „Attention of”, `invoiced_this_year` și etichetele partenerului (calculate și stocate).
- `res.partner` (extins): metoda `view_gifts`, pentru butonul *Gifts* de pe contact.
- `add.partners.wizard` (tranzitoriu): creează în masă linii de cadou pentru contactele selectate.
- `copy.gift.wizard` (tranzitoriu): copiază sau modifică în masă liniile selectate.

**Vizualizări**

- `views/gift_views.xml`: lista și formularul liniilor de cadou.
- `views/res_partner.xml`: butonul *Gifts* pe contact.
- `views/gift_report.xml`: raportul etichetei de livrare (*Print partner gifts*).
- `wizard/add_partners.xml`, `wizard/gift_copy.xml`: formularele wizardurilor.

**Acțiuni Automate / Acțiuni Server**

- `action_set_done` (*Set done*): trece liniile selectate în starea *Done*; doar grupul *Admin*.
- `action_set_draft` (*Set draft*): trece liniile selectate în starea *Draft*; doar grupul *Admin*.
- `action_get_partner_data` (*Get partner data*): calculează *Invoiced this year* și reîmprospătează etichetele; doar grupul *Admin*.
- Nu sunt definite sarcini `ir.cron` sau reguli `base.automation`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale verificate către alte module documentate în wiki.
