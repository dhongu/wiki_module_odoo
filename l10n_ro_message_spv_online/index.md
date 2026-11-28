# Romania - Mesaje SPV pentru Odoo Online

- **Nume Tehnic:** `l10n_ro_message_spv_online`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_message_spv_online
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_message_spv_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Registru al mesajelor e-Factura (SPV) care funcționează și pe **Odoo Online**: modulul nu are cod Python și se importă ca arhivă zip. Lucrează peste modulul standard `l10n_ro_edi`, care trimite facturile și descarcă facturile de furnizor, și arată într-un singur loc ce păstrează deja modulul standard: facturi trimise, primite, respinse.

#### 2. Funcționalități Cheie

- Meniul **Mesaje SPV** în Facturare (Contabilitate): ultimul mesaj al fiecărei facturi trimise și al fiecărei facturi primite, grupate după stare (*Trimis*, *Validat*, *Eroare*).
- Filtre: trimise / primite, în așteptare la ANAF, validate, respinse, cu mesaj de eroare, după dată; grupare după stare, direcție, partener sau lună.
- Formular de mesaj: factura, partenerul, totalul, mesajul ANAF, cheia de descărcare, XML-ul mesajului (factura trimisă sau semnătura ANAF) și fișierele facturii (XML și PDF la o factură primită), toate descărcabile.
- Butonul **Sincronizează acum**: rulează sincronizarea standard cu SPV (starea facturilor trimise, facturi de furnizor noi) fără a aștepta acțiunea programată; cere data de la care se sincronizează (până la 60 de zile în urmă). Pe o companie fără CIF sau fără token SPV spune ce trebuie setat întâi. Butonul **Preia starea** întreabă ANAF pentru o singură factură aflată în așteptare.
- Nu potrivește produsele după codul furnizorului și nu creează parteneri din CUI (pe server cu Python o face `l10n_ro_message_spv`). Tokenul ANAF rămâne în baza de date; modulul nu trimite date nicăieri în afara sincronizării standard.
- Se exclude reciproc cu `l10n_ro_message_spv`. Flux detaliat: [Fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `l10n_ro_edi.document` (extins prin vizualizări și câmpuri definite în `data/ir_model_fields_data.xml`): mesajul SPV afișat în registru.

**Vizualizări**

- `view_l10n_ro_edi_document_list`, `view_l10n_ro_edi_document_form`, `view_l10n_ro_edi_document_search`: lista, formularul și filtrele registrului.
- `action_spv_messages`: acțiunea din meniul Mesaje SPV.

**Acțiuni Automate / Acțiuni Server**

- `action_spv_synchronize` (*Sincronizează acum*): acțiune server care rulează sincronizarea standard cu SPV.

#### 5. Conexiuni

- [l10n_ro_message_spv](../l10n_ro_message_spv/index.md): varianta cu Python pentru instalări care o pot rula; exclusă reciproc.
- [l10n_ro_message_spv_side_panel_online](../l10n_ro_message_spv_side_panel_online/index.md): vedere împărțită peste acest registru.
