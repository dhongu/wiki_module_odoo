# Raport încasări (Payment Report)

- **Nume Tehnic:** `deltatech_payment_report`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_payment_report
- **Cale Locală:** odoo-addons/deltatech/deltatech_payment_report
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Contabilul vede, pe o perioadă aleasă, cum se împart banii încasați de la clienți între jurnalele de numerar și bancă și jurnalele facturilor pe care le-au stins. Raportul se generează la cerere, dintr-un wizard simplu de filtrare.

#### 2. Funcționalități Cheie

- **Încasări de la clienți pe jurnale:** sunt luate plățile primite de la clienți în starea Plătit sau Reconciliat, datate în perioadă și înregistrate în jurnalele de numerar și bancă alese. Plățile ciornă, anulate sau respinse și plățile către furnizori sunt excluse.
- **Wizard de filtrare:** Data de început și Data de sfârșit (implicit ziua curentă) și „Incasari”, jurnalele de numerar și bancă incluse (implicit toate).
- **Vizualizări pivot, listă și formular:** butonul **Show** deschide raportul în pivot, cu Jurnal de plată pe rânduri, Jurnal factură pe coloane și suma ca măsură. Lista și formularul arată pentru fiecare plată data, clientul, suma, jurnalul de plată, jurnalul facturii și metoda de plată. Jurnalul facturii este cel al facturii cu care e reconciliată plata.
- **Meniu:** Facturare > Contabilitate > Payment Report (doar grupul Administrator contabilitate).
- **Metoda de plată „card”:** dacă există o metodă de plată cu codul `card`, poate fi folosită doar pe jurnale bancare, o singură dată per jurnal.
- **Limitări:** sunt raportate doar încasările de la clienți; sumele sunt în moneda fiecărei plăți și pivotul le adună fără conversie; o plată reconciliată cu facturi din mai multe jurnale apare sub unul singur; compania wizardului nu filtrează plățile, domeniul îl dau jurnalele selectate.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

Elementele principale, identificate în cod:

**Modele**

- `account.payment.report`: wizard de filtrare (perioadă, jurnale).
- `account.payment.report.line`: liniile raportului, câte una per plată.
- `account.payment.method` (extins): restricția metodei `card` la jurnale bancare, o dată per jurnal.

**Vizualizări**

- `view_account_payment_report_form`: formularul wizardului.
- `view_account_payment_report_line_pivot` / `_list` / `_form` / `_search`: vizualizările raportului.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `account`: plățile și jurnalele din care se construiește raportul.
