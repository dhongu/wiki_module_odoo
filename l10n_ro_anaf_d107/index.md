# Romania - Declarația 107 ANAF (sponsorizări) (localizat la `l10n_ro_anaf_d107/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d107`
- **Versiune:** `19.0.2.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d107
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d107`
- **Ultima Ingestie:** 2026-09-12
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul gestionează și exportă Declarația 107 privind sponsorizările și bursele private acordate în cursul exercițiului fiscal, conform art. 25 alin. (4) lit. i din Codul Fiscal. Este destinat contribuabililor plătitori de impozit pe profit sau impozit micro-întreprindere care au acordat sponsorizări eligibile. Modulul preia automat sponsorizările din contabilitate, calculează scăzământul de impozit conform formulei legale și generează fișierul XML pentru depunere prin SPV, pe structura oficială ANAF.

#### 2. Funcționalități Cheie

- **Import automat din contabilitate:** preia sponsorizările înregistrate pe conturile 658x, grupate pe parteneri, cu sumele debitoare nete > 0 din perioada anului fiscal (`action_import_from_accounting`); dacă sponsorizările sunt înregistrate pe alt cont, liniile se adaugă manual.
- **Calcul scăzământ** conform formulei legale: `scăzământ = min(total sponsorizări, min(0,75% × CA, 20% × impozit datorat))`.
- **Export XML pe structura oficială ANAF** (rădăcina `<d107>`, namespace `mfp:anaf:dgti:d107:declaratie:v1`, beneficiari `<entit>`), gata de depus prin SPV — fișierul trece validatorul oficial `D107Validator.jar` ("Validare fără erori"). Versiunea anterioară (19.0.1.0.1) genera o structură nedepunabilă (`<declaratie107>`, fără namespace, un singur atribut din peste 20 obligatorii).
- **Câmpuri complete cerute de ANAF:** tipul de impozit (`cod_oblig`: impozit pe profit 102/103/104/105 sau micro 121), exercițiul financiar, declarație rectificativă, alte situații, an fiscal modificat, date de dizolvare cu/fără lichidare, depunere de către succesor, numele semnatarului, beneficiari neindividualizați (anexa `<entit1>`) cu suma reportată/dedusă.
- **Termenul de plată (`scadenta`) se calculează automat:** ZZ=25, decalat cu 6 luni pentru exerciții încheiate până în 2025; de la 2026, cu o lună la dizolvare, două luni pentru `cod_oblig` 104, trei luni pentru 102/103/105 (fără decalaj pentru 121 — micro-întreprinderi).
- **Corelații ANAF verificate înainte de export**, cu mesaje explicite despre ce lipsește: beneficiar fără adresă/cod fiscal, succesor fără CIF, sume pentru beneficiari neindividualizați fără liniile aferente, date de dizolvare contradictorii, câmpuri de an modificat pe tipuri de impozit care nu le admit, semnatar necompletat.
- **Flux de confirmare:** ciornă → confirmată (blochează modificările după depunere).
- **Cine depune:** contribuabilii plătitori de impozit pe profit sau de impozit pe micro-întreprindere care au acordat sponsorizări eligibile.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d107`: declarația D107 propriu-zisă (an fiscal, tip declarant/`cod_oblig`, exercițiu financiar, situații speciale ANAF — rectificativă, an modificat, dizolvare, succesor, semnatar —, cifra de afaceri, impozit datorat, calcul scăzământ, beneficiari neindividualizați, stare ciornă/confirmată); moștenește `mail.thread`, `mail.activity.mixin` și `l10n_ro_anaf.report.handler.mixin` (din `l10n_ro_anaf_base`) pentru chatter, activități și infrastructura comună de atașare/descărcare a declarațiilor ANAF.
- `l10n.ro.anaf.d107.line`: liniile de sponsorizare individualizate ale declarației (partener/denumire/CUI/adresă beneficiar, sumă acordată `Val1`, sumă reportată `Val2`, sumă dedusă `Val3`, sumă eligibilă internă pentru calculul deducerii).
- `l10n.ro.anaf.d107.unnamed.line`: beneficiarii neindividualizați din anexa `<entit1>`, obligatorii când `unnamed_reported` (`Val2_NI`) e mai mare ca zero.

**Vizualizări / Securitate**

- `views/l10n_ro_anaf_d107_view.xml`: lista (`l10n_ro_anaf_d107_list`), formularul (`l10n_ro_anaf_d107_form` — identificare, exercițiu financiar, linii sponsorizări, situații speciale ANAF, beneficiari neindividualizați, calcul deducere), căutarea (`l10n_ro_anaf_d107_search`), acțiunea de fereastră (`action_l10n_ro_anaf_d107`) și meniul (`menu_l10n_ro_anaf_d107`, sub `l10n_ro_anaf_base.menu_account_anaf_declarations`) pentru gestionarea declarației D107.
- `security/ir.model.access.csv`: drepturile de acces pentru `l10n.ro.anaf.d107`, `l10n.ro.anaf.d107.line` și `l10n.ro.anaf.d107.unnamed.line` — grupul `account.group_account_manager` are acces complet, `account.group_account_user` doar citire.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`).* Operațiunile cheie sunt declanșate manual din formular: `action_import_from_accounting` (import sponsorizări din conturile 658x), `action_export_xml` (validare corelații + generare/descărcare fișier XML ANAF), `action_confirm` și `action_reset_draft` (gestiune stare declarație).

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună pentru declarațiile ANAF (mixin-ul de raportare, datele declarantului, atașarea/descărcarea fișierelor XML).
- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): sursa valorii impozitului datorat folosit la calculul limitei de scăzământ.
- [l10n_ro_anaf_d205](../l10n_ro_anaf_d205/index.md): raportări anuale înrudite pentru venituri cu reținere la sursă.
- [l10n_ro_anaf_d207](../l10n_ro_anaf_d207/index.md): raportări anuale înrudite pentru venituri cu reținere la sursă.
- [l10n_ro_anaf_d101](../l10n_ro_anaf_d101/index.md): declarația de impozit pe profit care fixează termenul de depunere și valoarea impozitului.
