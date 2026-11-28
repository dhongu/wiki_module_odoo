# TBI Bank Payment Provider

- **Nume Tehnic:** `deltatech_payment_tbi_bank`
- **Versiune:** `20.0.1.0.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_payment_tbi_bank
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_tbi_bank`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă în Odoo un furnizor de plată pentru finanțarea în rate oferită de TBI Bank în magazinul online. La checkout, clientul este redirecționat către TBI Bank pentru cererea de finanțare, iar decizia băncii actualizează automat tranzacția: aprobată, respinsă sau în așteptare. Funcționează atât pentru comenzi de vânzare, cât și pentru facturi plătite din portal. Decizia aparține băncii: o cerere nu poate fi aprobată, capturată sau anulată din Odoo.

#### 2. Funcționalități Cheie

- **Furnizor nou** `tbi Bank` (`code = tbi_bank`), disponibil la checkout și la plata facturilor din portal.
- **Cerere construită din comandă sau factură**: datele clientului și liniile (denumire, cantitate, preț, SKU, imagine) se iau din factură, altfel din comanda de vânzare, altfel dintr-o linie unică.
- **Comunicare criptată**: cererea este criptată RSA cu cheia publică TBI și trimisă din browser către endpoint-ul Finalize; răspunsul băncii este decriptat pe server cu cheia ta privată.
- **Mediu de test și producție**: adresa Finalize se alege automat; cu **Live** debifat se folosește mediul de test (UAT) al băncii.
- **Stări tranzacție**: aprobat → **Confirmed**, respins → **Canceled** (cu motivul băncii în **Message**), în așteptare sau status necunoscut → **Pending** (modulul nu reinterogează banca).
- **Plată contabilă**: la aprobare se creează plata în jurnalul furnizorului (**In Process** până la reconcilierea cu extrasul); comisionul băncii nu este calculat de modul, ci se înregistrează la reconciliere.
- **Configurare** în **Accounting > Configuration > Online Payments > Payment Providers > TBI Bank**, tab **Configuration**: User, Password, Store ID, Provider Code, cheile PEM (publică TBI și privată proprie, vizibile doar grupului Settings), jurnalul de plată; câmpul **Tbi Bank Mode** se lasă gol (flux într-o singură fază).
- Limitări: `order_total` se trimite rotunjit la număr întreg, iar codul de categorie implicit al liniilor este `8`.

Fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `payment`
- `website_sale`
- `phone_validation`
- Pachet Python: `cryptography`

#### 4. Componente Cheie

**Modele**

- `payment.provider`: extins cu codul `tbi_bank`, credențialele, cheile PEM și URL-ul Finalize.
- `payment.transaction`: construiește și criptează cererea, procesează răspunsul decriptat și mapează statusul băncii pe starea tranzacției.
- `account.payment.method`: metoda de plată a furnizorului.

**Vizualizări**

- `views/payment_views.xml`: formularul furnizorului (tab Configuration).
- `views/payment_templates.xml`: formularul de redirecționare către TBI Bank.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni programate; `data/payment_provider_data.xml` și `data/payment_method_data.xml` creează furnizorul și metoda de plată, iar `post_init_hook` / `uninstall_hook` le pregătesc la instalare/dezinstalare.

#### 5. Conexiuni

- `account`: plata contabilă și reconcilierea cu extrasul.
- `sale`: comenzile de vânzare din care se construiește cererea de finanțare.
