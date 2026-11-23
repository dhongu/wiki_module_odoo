# Terrabit Payable and Receivable in Partner Form (localizat la `terrabit_partner_payable_receivable/index.md`)

- **Nume Tehnic:** `terrabit_partner_payable_receivable`
- **Versiune:** `19.0.1.2.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_partner_payable_receivable
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_payable_receivable`
- **Ultima Ingestie:** `2026-11-23`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul îmbunătățește fișa partenerului adăugând o vizualizare clară și imediată a sumelor de plată și de încasat, oferind contextul financiar esențial direct în înregistrarea partenerului. Din perspectivă de business, această transparență permite echipelor de vânzări și contabilitate să evalueze instantaneu situația financiară și statutul de credit al unui partener înainte de a lua decizii comerciale importante.

#### 2. Funcționalități Cheie

- Vizibilitate financiară în timp real: vezi instantaneu, direct pe fișa partenerului, sumele exacte de plată și de încasat pentru orice partener.
- Evaluare îmbunătățită a creditului: identifici rapid partenerii cu solduri restante pentru a gestiona mai eficient riscul financiar; pe comanda de vânzare apare un banner cu soldul clientului și data celei mai vechi facturi.
- Operațiuni contabile simplificate: soldurile partenerilor sunt calculate din liniile de notă contabilă, iar butoanele **View** de pe fișa partenerului deschid liniile de avans (client sau furnizor).
- Decizii comerciale mai bine informate: permiți echipelor de vânzări să poarte discuții mai documentate cu partenerii, pe baza poziției lor financiare curente; clientul vede soldul deschis și pe pagina de start a portalului.
- Raportare financiară precisă: soldurile de avans se calculează pe grupuri de conturi dedicate, configurabile pe companie (client și furnizor); dacă un grup nu e setat, se folosesc conturile 419% (client), respectiv 409% (furnizor) ale companiei curente.
- Soldul și data se raportează la partenerul comercial: liniile de încasat sunt postate pe compania-mamă, deci o comandă făcută pe un contact (ex. adresă de livrare) arată soldul companiei.

#### 3. Dependențe

- `account`
- `sale_management`

#### 4. Componente Cheie

Documentația acestui modul a fost generată pe baza fișierului `readme/DESCRIPTION.md`, conform fluxului de ingestie. Componentele tehnice de mai jos sunt deduse din `__manifest__.py` și cod, oferite cu titlu orientativ; pentru detalii complete consultă codul sursă.

**Modele**

- `res.partner`: extins cu câmpurile calculate `partner_aml_receivable` („To receive”) și `partner_aml_payable` („To pay”) — sold din liniile de notă contabilă postate, pe conturile `asset_receivable`/`liability_payable`, nereconciliate, până la data curentă —, `receivable_date` (cea mai veche linie nereconciliată de încasat) și sumele de avans client/furnizor (`partner_aml_deposit_customer`, `partner_aml_deposit_vendor`). Calculele se refac la schimbarea companiei. Metodele `view_advance_lines_customer_action` / `view_advance_lines_vendor_action` deschid liniile de avans.
- `res.company` / `res.config.settings`: extinse cu `account_group_deposit_customer_id` și `account_group_deposit_vendor_id`, grupurile de conturi folosite la calculul avansurilor.
- `sale.order`: câmpurile `partner_aml_receivable` și `receivable_date`, preluate prin relație de la partenerul comercial al clientului, pentru bannerul de sold.
- `sale.advance.payment.inv` (vizualizare în `wizard/sale_make_invoice_advance.xml`): afișează opțiunea `deduct_down_payments` în asistentul de facturare când e selectată o singură comandă; fișierul Python al wizardului nu conține cod.

**Vizualizări**

- `view_partner_form_pay_receive` (`views/res_partner.xml`): adaugă pe formularul partenerului, în grupurile de vânzare și achiziție, sumele de încasat/plată, avansurile și butoanele **View**.
- `view_order_form` (`views/sale_view.xml`): banner de avertizare pe comanda de vânzare cu soldul clientului și data celei mai vechi facturi.
- `open_balance_my_home` (`views/templates.xml`): șablon QWeb care afișează soldul deschis (de plată / de încasat) al partenerului comercial al utilizatorului pe paginile portalului.
- `res_config_settings_view_form` (`views/res_config_settings_views.xml`): câmpurile pentru grupurile de conturi de avans client și furnizor, în blocul de conturi implicite din setările de contabilitate.
- `view_sale_advance_payment_inv` (`wizard/sale_make_invoice_advance.xml`): ajustare pe asistentul de facturare în avans.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, reguli `base.automation` sau acțiuni server dedicate în datele modulului.

#### 5. Conexiuni

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md): modul Terrabit înrudit, axat pe gestionarea limitei de credit a partenerului; completează vizibilitatea financiară oferită de acest modul pe fișa partenerului.
