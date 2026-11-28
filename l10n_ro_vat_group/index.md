# Romania - Grup fiscal TVA consolidat (localizat la `l10n_ro_vat_group/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_group`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_vat_group
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_vat_group`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul gestionează grupurile fiscale TVA conform art. 269² Cod Fiscal și OPANAF 2731/2016. Permite definirea unui grup de companii cu relații de control (deținere >50%) ca un singur subiect fiscal TVA, cu CUI unic, marcarea automată a tranzacțiilor intra-grup (afișate separat în raport) și generarea unui raport TVA consolidat per membru, pentru decontul depus de membrul raportor.

#### 2. Funcționalități Cheie

- **Grup fiscal TVA** (`l10n.ro.vat.group`, meniul Contabilitate → Configurare → Contabilitate → Grupuri Fiscale TVA, vizibil administratorilor de contabilitate): denumire, CUI grup (`RO_GRP_XXXXXX`), data înregistrării ANAF, companii membre și membru raportor; stări `În constituire → Activ → Dizolvat`.
- **Activare**: verifică minimum 2 companii membre, membru raportor și CUI de grup; completează câmpul „Grup fiscal TVA" pe fiecare companie membră și blochează identificarea și lista membrilor.
- **Marcare automată intra-grup**: la postarea unei facturi de client sau de furnizor către altă companie membră a unui grup activ, documentul primește bifa „Tranzacție intra-grup TVA" și un banner de avertizare; bifa nu mai poate fi modificată după postare. Marcajul nu schimbă nota contabilă.
- **Marcare retroactivă** a documentelor postate înainte de activare, idempotentă (butonul „Marchează retroactiv intra-grup").
- **Buton statistic „Intra-grup"** pe grup, cu lista documentelor marcate, pentru audit.
- **Raport TVA consolidat** (wizard, pe perioadă): per companie membră TVA colectată, TVA deductibilă, intra-grup colectat/deductibil și TVA net, plus totaluri consolidate fără intra-grup; se citește pe ecran, fără export și fără XML D300.
- **Blocare perioadă sincronizată**: „Blochează perioada (toate companiile)" setează data de blocare TVA pe toate companiile membre, doar pentru administratori și doar dacă utilizatorul are acces la toate.
- **Dizolvare grup** („Dizolvă grup", data dizolvării) și revenire la ciornă pentru schimbarea membrilor.
- **Nu include (Beta):** generarea XML D300 consolidat cu CUI de grup (necesită `l10n_ro_anaf_d300`) și formularul 045 de constituire a grupului.
- Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.vat.group`: grupul fiscal TVA (`mail.thread`), cu companii membre, membru raportor, CUI unic și flux de stări.
- `account.move` (extins): marcarea tranzacțiilor intra-grup TVA.
- `res.company` (extins): câmpul `l10n_ro_vat_group_id` (grupul fiscal al companiei).
- Wizard `l10n_ro_vat_group_report_wizard`: calculul raportului TVA consolidat și blocarea perioadei.

**Vizualizări**

- `views/l10n_ro_vat_group_views.xml`: formularul și lista grupului fiscal TVA.
- `views/account_move_views.xml`: bannerul și câmpul de marcare intra-grup pe factură.
- `wizard/l10n_ro_vat_group_report_wizard_views.xml`: raportul TVA consolidat.
- `security/ir.access.csv`: drepturile de acces ale modulului (format Odoo 20).

**Acțiuni Automate / Acțiuni Server**

*Nu sunt definite acțiuni automate; marcarea intra-grup se aplică la postarea facturilor.*

#### 5. Conexiuni

- [l10n_ro_vat_regularization](../l10n_ro_vat_regularization/index.md): regularizarea TVA la nivel de decont.
- [l10n_ro_vat_deductibility](../l10n_ro_vat_deductibility/index.md): deductibilitatea TVA (integral, pro-rata, nedeductibil).
- [l10n_ro_vat_refund](../l10n_ro_vat_refund/index.md): rambursarea TVA.
- `l10n_ro_anaf_d300`: viitorul D300 consolidat cu CUI de grup ar depinde de acest modul.
