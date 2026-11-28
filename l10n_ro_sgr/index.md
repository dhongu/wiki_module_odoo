# Romania - Sistem Garanție-Returnare (SGR) (localizat la `l10n_ro_sgr/index.md`)

- **Nume Tehnic:** `l10n_ro_sgr`
- **Versiune:** `20.0.1.7.3`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_sgr](https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_sgr)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_sgr`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează suportul contabil complet pentru **Sistemul Garanție-Returnare (SGR)**, stabilit prin H.G. 1074/2021, republicată, și administrat de RetuRO. Se adresează companiilor care comercializează produse cu ambalaje din sticlă, PET sau aluminiu și care încasează garanția de 0,50 RON/ambalaj de la clienți, o plătesc furnizorilor și o restituie consumatorilor, recuperând-o apoi de la RetuRO. Garanția încasată este tratată ca datorie (462102), cea plătită furnizorului ca creanță (461002), iar cea restituită consumatorului ca creanță față de RetuRO (461003).

#### 2. Funcționalități Cheie

- **Configurare automată la instalare:** produsul SGR, conturile 462102, 461002 și 461003 și taxa de 0% în afara sferei TVA (fără grile în decontul de TVA, categoria e-Factura `E`). Setările se verifică în **Contabilitate → Configurare → Setări**, secțiunea SGR; partenerul RetuRO nu se creează automat.
- **Vânzări:** linia SGR (0,50 RON/ambalaj, în afara sferei TVA, art. 315^5 alin. 2 Cod fiscal), Dr 4111 = Cr 462102; pe comenzile de vânzare apare automat, pe facturile create direct se adaugă manual.
- **Achiziții:** linie SGR inserată automat pe comenzile de cumpărare pentru produsele cu articol SGR; pe factura furnizorului Dr 461002 = Cr 401.
- **Raport sold SGR:** la o dată aleasă, per partener (încasate, plătite, de recuperat de la RetuRO), cu numărul de ambalaje; **Contabilitate → Rapoarte → Sold SGR**.
- **Situația ambalajelor SGR:** raport `account.report` pe interval și tip de ambalaj (sticlă, plastic, metal), cu ambalaje pline și goale nedecontate, detaliat pe documente sau pe zile, cu export PDF/XLSX; **Contabilitate → Rapoarte → Situație ambalaje SGR**.
- **Wizard returnare ambalaje:** restituire în numerar (Dr 461003 = Cr 5311) sau prin notă de credit (Dr 461003 = Cr 4111), în ciornă.
- **Wizard autofactură RetuRO:** înregistrează autofactura lunară (garanții, tarif de gestionare 708, TVA 4427) și regularizarea 462102 = 461002, în ciornă.
- **Wizard reclasificare:** pentru bazele cu versiuni vechi (conturile 461001/462101), mută soldurile pe conturile noi, per partener, în ciornă.
- **e-Factura CIUS-RO:** la plătitorii de TVA linia SGR pleacă cu `TaxCategory = E` și cota 0, cu motivul în BT-120; la neplătitori rămâne `O` / `VATEX-EU-O`. Mențiunea legală apare pe factură și în XML. Fluxul pas-cu-pas este în fișa consultant.

#### 3. Dependențe

- [deltatech_sale_add_extra_line](../deltatech_sale_add_extra_line/index.md)
- [deltatech_purchase_add_extra_line](../deltatech_purchase_add_extra_line/index.md)
- `account`
- `account_reports`
- `account_edi_ubl_cii`
- `l10n_ro`
- `purchase`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md` și `readme/CONFIGURE.md`.

**Modele**

- `res.company` / `res.config.settings`: produsul, conturile și taxa SGR, administratorul RetuRO.
- `product.template`: marcarea produselor cu ambalaj SGR și tipul ambalajului.
- `purchase.order` / `purchase.order.line`: linia SGR automată pe achiziții.
- `account.edi.common` / `account.edi.ubl_cen_en16931`: categoria și motivul scutirii în XML-ul CIUS-RO.
- `l10n.ro.sgr.report` / `l10n.ro.sgr.report.line`: raportul de sold SGR (wizard).
- `l10n.ro.sgr.packaging.report.handler`: handlerul raportului „Situația ambalajelor SGR".
- `l10n.ro.sgr.return.wizard`, `l10n.ro.sgr.settlement.wizard`, `l10n.ro.sgr.reclass.wizard`: returnare, autofactură RetuRO, reclasificare.

**Vizualizări**

- `views/account_move_views.xml`, `views/purchase_order_views.xml`, `views/product_template_views.xml`: liniile SGR pe facturi/comenzi și produs.
- `views/sgr_report_views.xml`: raportul de sold.
- `views/sgr_wizard_views.xml`: wizardurile de returnare, autofactură și reclasificare.
- `views/res_config_settings_views.xml`: setările SGR.
- `data/sgr_packaging_report.xml`: definiția rapoartelor (pe documente și pe zile) și acțiunea client.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): la instalare creează, pentru companiile din România, produsul SGR, conturile și taxa SGR.

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): câmpurile UBL ale taxei SGR sunt folosite la exportul CIUS-RO al e-Facturii.
