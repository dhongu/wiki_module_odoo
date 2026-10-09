# Romania - e-Factura: reguli XML per client (localizat la `l10n_ro_efactura_xml_rules/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_xml_rules`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_efactura_xml_rules
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_xml_rules`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Odoo generează același XML e-Factura (CIUS-RO) pentru toți cumpărătorii, dar cumpărătorii mari cer date diferite în factură și o resping la recepție dacă lipsesc, chiar dacă ANAF o validează: lanțurile de retail cer numărul comenzii și codul propriu al articolului, instituțiile publice cer contractul și lotul de licitație, grupurile cu centre de cost cer referința lor contabilă. Modulul permite configurarea acestor cerințe din interfață, pe client sau în profiluri reutilizabile, fără dezvoltare.

#### 2. Funcționalități Cheie

- **Catalog de 34 de tag-uri CIUS-RO**, fiecare cu codul EN 16931 (BT-xx), denumire comercială și explicație; calea fiecărui tag este verificată pe structura UBL folosită de Odoo, astfel încât XML-ul să rămână în ordinea cerută de schemă. Meniu: **Facturare → Configurare → Facturare → Catalog tag-uri e-Factura**. Coloana „Lungime maximă" = 0 înseamnă fără limită CIUS-RO; unele tag-uri există doar pe facturi (ex. BT-11, nu și pe nota de credit).
- **Reguli pe partener** (tab-ul **e-Factura XML** al clientului): ce tag se completează și de unde vine valoarea. „Valoare din" poate fi o sursă predefinită (comanda clientului, avizele livrate, codul articolului la client, GTIN), un câmp al facturii sau al liniei, un text fix sau eliminarea tag-ului.
- **Profiluri** (**Configurare → Facturare → Profiluri XML e-Factura**): seturi de reguli comune mai multor clienți (ex. „Lanț retail"), atribuite pe partener. Fiecare regulă are: tag, „Se aplică pe" (facturi / note de credit / ambele), „Valoare din", „Suprascrie", „Obligatoriu".
- **Ordinea de aplicare**: regula contactului facturat, apoi a firmei-mamă, apoi a profilului. Pentru tag-urile cu o singură valoare câștigă prima regulă găsită; la tag-urile repetabile (ex. BT-22 nota facturii, BT-160/161 atribute de articol) regulile se adună, până la primul nivel care elimină tag-ul.
- **Suprascrie**: bifat înlocuiește valoarea pusă de Odoo; debifat, regula completează doar dacă Odoo a lăsat tag-ul gol.
- **Reguli obligatorii**: dacă regula nu dă valoare, factura nu pleacă în SPV, iar mesajul numește clientul, tag-ul și linia.
- **Lungimea maximă CIUS-RO** se verifică pe valoare: o valoare prea lungă oprește exportul, nu este trunchiată.
- **Sursele opționale** (comenzi de vânzare, livrări, codurile articolului la client) întorc gol dacă aplicația respectivă nu e instalată; pentru BT-156 se folosește `deltatech_sale_product_reference`.
- **Drept dedicat** „Gestiune reguli XML e-Factura" (secțiunea Contabilitate), pe care implicit nu îl are nimeni; emiterea facturilor nu necesită acest drept.
- Atenție: modulul nu modifică totalurile sau TVA-ul; BT-7 și BT-8 se configurează doar cu acordul contabilului și nu se folosesc împreună (BR-CO-03). Dacă regulile se schimbă după o trimitere eșuată, trebuie șters atașamentul `_cius_ro.xml` din istoricul facturii, altfel se retrimite XML-ul vechi.
- Modul comercial (OPL-1, 100 EUR), stadiu Beta.

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.efactura.tag`: catalogul de tag-uri CIUS-RO (cod BT, cale XML, nivel document/linie, lungime maximă, repetabil).
- `l10n.ro.efactura.source`: sursele predefinite de valori (referința facturii, comanda clientului, avize livrate etc.).
- `l10n.ro.efactura.rule`: regula unui tag, atașată unui partener sau unui profil, cu validări asupra sursei, textului și câmpului.
- `l10n.ro.efactura.profile`: profil de reguli reutilizabil între clienți.
- `account.edi.xml.ubl_ro` (extins): aplică regulile la generarea XML-ului CIUS-RO și blochează exportul la reguli obligatorii fără valoare.
- `account.move` (extins): calculează regulile efective (contact, firmă-mamă, profil).
- `res.partner` (extins): profil, reguli proprii și reguli moștenite (doar citire).

**Vizualizări**

- `view_l10n_ro_efactura_tag_list` / `view_l10n_ro_efactura_tag_form` / `view_l10n_ro_efactura_tag_search`: catalogul de tag-uri.
- `view_l10n_ro_efactura_profile_list` / `view_l10n_ro_efactura_profile_form` / `view_l10n_ro_efactura_profile_search`: profilurile și regulile lor.
- `view_l10n_ro_efactura_rule_list` / `view_l10n_ro_efactura_rule_inherited_list`: regulile proprii și cele moștenite.
- `view_partner_form_efactura_xml_rules`: tab-ul **e-Factura XML** pe partener.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server; catalogul de tag-uri și sursele vin ca date (`data/l10n_ro_efactura_tag_data.xml`, `data/l10n_ro_efactura_source_data.xml`).

#### 5. Conexiuni

- `l10n_ro_edi`: generatorul CIUS-RO / trimiterea în SPV a cărui ieșire XML este ajustată.
- [deltatech_sale_product_reference](../deltatech_sale_product_reference/index.md): ține codurile articolelor la client, folosite pentru BT-156.
- `sale` / `stock`: sursele „comanda clientului" și „avize livrate" (opționale).
