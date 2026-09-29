# Romania - Sistem Garanție-Returnare (SGR) (localizat la `l10n_ro_sgr/index.md`)

- **Nume Tehnic:** `l10n_ro_sgr`
- **Versiune:** `19.0.1.6.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_sgr
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_sgr`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează suportul contabil complet pentru **Sistemul Garanție-Returnare (SGR)**, stabilit prin H.G. 1074/2021, republicată, și administrat de RetuRO Sistem Garanție-Returnare SA. Este destinat companiilor care comercializează produse cu ambalaje primare din sticlă, PET sau aluminiu și care au obligația legală de a încasa garanția de 0,50 RON/ambalaj de la clienți, de a o plăti furnizorilor și de a o restitui consumatorilor, recuperând-o apoi de la RetuRO. Monografia contabilă urmează precizarea Ministerului Finanțelor din 26.02.2024 (garanția încasată este o datorie) și CECCAR Business Review nr. 2/2024 (garanția plătită și cea restituită sunt creanțe).

#### 2. Funcționalități Cheie

- **Configurare automată la instalare** — produs SGR (serviciu, nestocabil, 0,50 RON), conturile `462102` (garanții încasate, datorie), `461002` (garanții plătite, creanță) și `461003` (de recuperat de la RetuRO), plus taxa 0% în afara sferei TVA, fără grile în decontul de TVA, cu categoria e-Factura `E` (cota 0).
- **Vânzări** — linia SGR se adaugă manual pe factura de vânzare (nu se inserează automat): 0,50 RON/ambalaj, în afara sferei TVA (art. 315^5 alin. 2 Cod fiscal); nota contabilă Dr 4111 = Cr 462102. Garanția nu este venit, ci datorie.
- **Achiziții (PO)** — linie SGR inserată automat pe comenzile de cumpărare pentru produsele cu `extra_product_id` = articol SGR (cantitate din `extra_qty`); ștergere în cascadă la eliminarea liniei-părinte; pe factura furnizorului, Dr 461002 = Cr 401 (garanția nu intră în costul mărfii).
- **Raport sold SGR** — soldul la o dată aleasă, per partener: garanții încasate, garanții plătite și de recuperat de la RetuRO, cu echivalentul în număr de ambalaje; **Contabilitate → Rapoarte → Sold SGR**.
- **Wizard returnare ambalaje** — restituirea garanției în numerar (Dr 461003 = Cr 5311) sau prin notă de credit către client (Dr 461003 = Cr 4111), în ciornă; **Contabilitate → Înregistrări → Returnare ambalaje SGR**.
- **Wizard autofactură RetuRO** — înregistrează în ciornă autofactura lunară: Dr 4111 RetuRO = Cr 461003 (garanții) + Cr 708 (tarif de gestionare) + Cr 4427 (TVA din taxa aleasă), plus regularizarea opțională Dr 462102 = Cr 461002; **Contabilitate → Înregistrări → Autofactură RetuRO**. Încasarea se face din extrasul de cont.
- **Wizard reclasificare conturi SGR** — pentru bazele care au lucrat cu versiunile anterioare (conturile 461001 / 462101, cu funcțiunea inversată): propune, per partener și în ciornă, nota de mutare a soldurilor pe conturile noi; **Contabilitate → Înregistrări → Reclasificare conturi SGR** (grupul Consilier contabil). Refuză o a doua reclasificare cât timp există o ciornă pe conturile vechi.
- **Integrare e-Factura CIUS-RO** — la companiile plătitoare de TVA, linia SGR pleacă cu `TaxCategory = E`, cota 0, cu motivul explicit „Garanție SGR — în afara sferei TVA (art. 315^5 alin. (2) Cod fiscal)" în BT-120; subtotalurile `E` se separă după motivul scutirii. La companiile neplătitoare de TVA taxa rămâne pe `O` / `VATEX-EU-O`. Aceeași mențiune apare și pe factura PDF.
- **Setări** — în Contabilitate → Configurare → Setări, secțiunea „Sistem Garanție-Returnare (SGR)": articolul SGR, cele trei conturi, administratorul SGR (partenerul RetuRO, care nu se creează automat) și taxa SGR; conturile pot fi schimbate (de exemplu pe 167 / 267).
- **Actualizare de la versiuni anterioare** — migrările creează conturile noi și trec pe ele setările și produsul SGR; produsul SGR este scos din evidența stocului (`is_storable = False`), ca linia SGR de pe factura furnizorului să nu ajungă pe contul de stoc. Notele deja postate nu se modifică.

#### 3. Dependențe

- [deltatech_sale_add_extra_line](../deltatech_sale_add_extra_line/index.md)
- [deltatech_purchase_add_extra_line](../deltatech_purchase_add_extra_line/index.md)
- `account`
- `account_edi_ubl_cii`
- `l10n_ro`
- `purchase`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, `readme/USAGE.md` și `readme/CONFIGURE.md`:

**Modele**

- `res.company` / `res.config.settings`: setările SGR la nivel de companie (produs, conturile 462102 / 461002 / 461003, partenerul RetuRO, taxa SGR).
- `account.move`: gestionează linia SGR pe facturile de vânzare/achiziție.
- `purchase.order` / `purchase.order.line`: inserare/eliminare automată a liniei SGR pe baza `extra_product_id`/`extra_qty` de pe produs.
- `product.template`: marcarea produselor cu ambalaj SGR.
- `account.edi.common`, `account.edi.ubl_cen_en16931`: categoria de taxă și motivul scutirii SGR în XML-ul CIUS-RO.
- `l10n.ro.sgr.report` / `l10n.ro.sgr.report.line`: raportul de sold SGR per partener.

**Wizard-uri**

- `l10n.ro.sgr.return.wizard`: returnare ambalaje (numerar sau notă de credit).
- `l10n.ro.sgr.settlement.wizard`: autofactura RetuRO.
- `l10n.ro.sgr.reclass.wizard`: reclasificarea soldurilor de pe conturile vechi.

**Vizualizări / Date**

- `data/account_sgr_data.xml`: date de referință statice (produsul, conturile și taxa se creează prin `post_init_hook`).
- `views/account_move_views.xml`, `views/purchase_order_views.xml`: liniile SGR pe facturi și comenzi.
- `views/sgr_report_views.xml`: raportul de sold SGR.
- `views/sgr_wizard_views.xml`: wizardurile de returnare, autofactură și reclasificare.
- `views/res_config_settings_views.xml`: setările SGR.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): la instalare, pentru fiecare companie din România (sau, în lipsă, pentru toate), creează produsul SGR, conturile 462102 / 461002 / 461003 și taxa SGR 0%.
- Migrări (`migrations/`): mută setările pe conturile noi și corectează produsul SGR (nestocabil).

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): câmpurile UBL ale taxei SGR (`ubl_cii_tax_category_code`, `ubl_cii_tax_exemption_reason_code`) folosite la exportul e-Facturii CIUS-RO.
