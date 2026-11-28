# Romania - e-Factura: reguli XML per client

- **Nume Tehnic:** `l10n_ro_efactura_xml_rules`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_efactura_xml_rules
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_xml_rules`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Odoo generează același XML e-Factura (CIUS-RO) pentru toți cumpărătorii, dar cumpărătorii mari cer date diferite în factură, iar o factură fără ele este respinsă la recepție, deși ANAF o validează. Lanțurile de retail cer numărul comenzii și codul propriu al articolului, instituțiile publice cer contractul și lotul de licitație, grupurile cu centre de cost cer referința lor contabilă. Modulul permite configurarea acestor cerințe din interfață, pe partener, fără dezvoltare.

#### 2. Funcționalități Cheie

- **Catalog de 34 de tag-uri CIUS-RO**, fiecare cu codul EN 16931 (BT-xx), denumirea comercială și o explicație; calea fiecărui tag este verificată pe structura UBL folosită de Odoo. Meniu: **Facturare → Configurare → Facturare → Catalog tag-uri e-Factura**.
- **Reguli pe partener**: ce tag se completează și de unde vine valoarea (sursă predefinită: comanda clientului, avizele livrate, codul articolului la client, GTIN; câmp al facturii sau al liniei; text fix; eliminarea tag-ului).
- **Profiluri** (ex. „Lanț retail”): seturi de reguli comune mai multor clienți, atribuite pe partener (**Profiluri XML e-Factura**).
- **Ordinea de aplicare**: contactul facturat, apoi compania-mamă, apoi profilul.
- **Reguli obligatorii**: dacă regula nu dă valoare, factura nu pleacă în SPV, iar mesajul numește clientul, tag-ul și linia.
- **Suprascriere opțională**: bifat, regula înlocuiește valoarea pusă de Odoo; debifat, completează doar dacă tag-ul a rămas gol.
- **Lungimea maximă CIUS-RO** verificată pe valoare: o valoare prea lungă oprește exportul, nu este trunchiată.
- **Drept dedicat** „Gestiune reguli XML e-Factura”, pe care implicit nu îl are nimeni.
- Sursele din comenzi de vânzare, livrări sau codurile de articol ale clientului întorc gol dacă aplicația respectivă nu este instalată. Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.efactura.tag`: catalogul de tag-uri CIUS-RO configurabile.
- `l10n.ro.efactura.source`: sursele predefinite de valoare.
- `l10n.ro.efactura.rule`: regula (tag, sursă, obligatoriu, suprascriere), pe partener sau profil.
- `l10n.ro.efactura.profile`: profil de reguli reutilizabil.
- `res.partner`, `account.move`, `account.edi.xml.ubl_ro`: extinse pentru reguli pe partener și aplicarea lor la generarea XML-ului.

**Vizualizări**

- `view_l10n_ro_efactura_tag_list` / `_form` / `_search`: catalogul de tag-uri.
- `view_l10n_ro_efactura_profile_list` / `_form` / `_search`: profilurile.
- `view_partner_form_efactura_xml_rules`: fila de reguli pe partener.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `l10n_ro_edi`: generarea și trimiterea e-Facturii în SPV, al cărei XML este adaptat de reguli.
