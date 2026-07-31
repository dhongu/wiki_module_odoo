# Terrabit Payable and Receivable in Partner Form (localizat la `terrabit_partner_payable_receivable/index.md`)

- **Nume Tehnic:** `terrabit_partner_payable_receivable`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_partner_payable_receivable
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_payable_receivable`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul îmbunătățește fișa partenerului adăugând o vizualizare clară și imediată a sumelor de plată și de încasat, oferind contextul financiar esențial direct în înregistrarea partenerului. Din perspectivă de business, această transparență permite echipelor de vânzări și contabilitate să evalueze instantaneu situația financiară și statutul de credit al unui partener înainte de a lua decizii comerciale importante.

#### 2. Funcționalități Cheie

- Vizibilitate financiară în timp real: vezi instantaneu, direct pe fișa partenerului, sumele exacte de plată și de încasat pentru orice partener.
- Evaluare îmbunătățită a creditului: identifici rapid partenerii cu solduri restante pentru a gestiona mai eficient riscul financiar.
- Operațiuni contabile simplificate: utilizezi o filă specializată pentru a vizualiza și reconcilia soldurile partenerilor, calculate din liniile de notă contabilă.
- Decizii comerciale mai bine informate: permiți echipelor de vânzări să poarte discuții mai documentate cu partenerii, pe baza poziției lor financiare curente.
- Raportare financiară precisă: asiguri reflectarea corectă a soldurilor partenerilor folosind grupuri de conturi dedicate pentru plățile în avans.

#### 3. Dependențe

- `account`
- `sale_management`

#### 4. Componente Cheie

Documentația acestui modul a fost generată pe baza fișierului `readme/DESCRIPTION.md`, conform fluxului de ingestie. Componentele tehnice de mai jos sunt deduse din `__manifest__.py` și oferite cu titlu orientativ; pentru detalii complete consultă codul sursă.

**Modele**

- `res.partner`: extins pentru a afișa sumele de plată și de încasat direct pe fișa partenerului.
- `res.config.settings`: extins pentru configurarea grupurilor de conturi folosite la calculul soldurilor (inclusiv plăți în avans).

**Vizualizări**

- `views/res_partner.xml`: adaugă pe formularul partenerului afișarea sumelor de plată/încasat și fila specializată pentru reconcilierea soldurilor.
- `views/sale_view.xml`: ajustări pe vizualizările de vânzări.
- `views/res_config_settings_views.xml`: opțiuni de configurare a grupurilor de conturi.
- `wizard/sale_make_invoice_advance.xml`: ajustări pe asistentul de facturare în avans.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, reguli `base.automation` sau acțiuni server dedicate în datele modulului.

#### 5. Conexiuni

- `terrabit_partner_credit_limit`: modul Terrabit înrudit, axat pe gestionarea limitei de credit a partenerului; completează vizibilitatea financiară oferită de acest modul pe fișa partenerului.
