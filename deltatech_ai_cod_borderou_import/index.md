# Courier Borderou Import with AI (Import borderou curier cu AI)

- **Nume Tehnic:** `deltatech_ai_cod_borderou_import`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_cod_borderou_import
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_cod_borderou_import`
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Fiecare curier trimite borderoul de ramburs într-un format propriu, iar de obicei fiecare format ar cere un import separat. Acest modul importă borderoul **oricărui curier** în jurnalul de decontare al curierului: un agent AI găsește coloanele, Odoo citește rândurile, identifică clientul și comanda fiecărui colet și creează extrasul de decontare.

#### 2. Funcționalități Cheie

- **Orice curier, orice format**: XLSX, XLS sau CSV, cu bloc de titlu deasupra tabelului, antete repetate pe fiecare pagină, rând de total, sume în format românesc (`1.234,56`) sau internațional (`1,234.56`).
- **AI găsește coloanele, Odoo citește valorile**: agentul indică doar unde se află datele (rândul de antet, AWB, sumă, dată, destinatar, referință, comision, celula cu data plății, eticheta rândului de total). Nu transcrie niciodată o valoare: AWB-urile și sumele sunt citite din fișier de Odoo, deci o cifră nu poate fi citită greșit.
- **Întrebat o singură dată per format**: maparea confirmată la import se salvează; următorul borderou cu aceleași antete se citește fără AI, fără cost și cu același rezultat.
- **Client și comandă pentru fiecare colet**: după AWB, prin transportul aceluiași curier din aceeași companie; dacă AWB-ul nu găsește transport, după referința comenzii din borderou (număr comandă sau referință client). Niciodată după nume.
- **Verificare înainte de import**: rândurile sunt afișate cu clientul și comanda găsite, coletele negăsite și totalul fișierului față de suma rândurilor. O coloană se poate schimba manual (fila **Columns**) și rândurile se recitesc (**Read Again with These Columns**).
- **Aceleași reguli de decontare ca la ceilalți curieri**: rândurile trec prin `deltatech_delivery_cod`: sumă fără AWB sau AWB dublat oprește importul, rândul de total trebuie să corespundă, un AWB deja importat este sărit, iar o linie de transfer echilibrează extrasul cu mișcarea bancară.
- **Cost sub control**: activare opțională per companie (implicit oprită) și limită zilnică de formate citite cu AI (implicit 20 per companie, 0 = nelimitat).
- **Furnizorul dumneavoastră**: folosește cadrul AI nativ Odoo și cheia din **Setări → AI**; modelul agentului **Courier Borderou Reader AI** se poate alege din **AI → Agents**. Timpul de așteptare: parametrul de sistem `deltatech_ai_cod_borderou_import.timeout` (implicit 120 s).
- **Sigur prin construcție**: agentul vede doar antetele și primele/ultimele rânduri și i se cere să nu urmeze instrucțiuni scrise în fișier.
- **Flux de utilizare**: **Contabilitate → Clienți → Import Courier Borderou** sau butonul **Import Borderou** de pe jurnalul de decontare al curierului; la jurnal (tip bancă) se setează **Courier** în *Advanced Settings → Courier COD Settlement*. Mapările salvate se gestionează în **Contabilitate → Configurare → Contabilitate → Courier Borderou Mappings** (corectare sau arhivare).
- **Date trimise în afara Odoo**: pentru un format nemaiimportat, primele 40 și ultimele 8 rânduri ale fișierului (inclusiv numele destinatarilor) ajung la furnizorul AI. Un format salvat nu trimite nimic.

#### 3. Dependențe

- [deltatech_delivery_cod](../deltatech_delivery_cod/index.md)
- `sale_stock`
- `ai`
- Python extern: `openpyxl`

#### 4. Componente Cheie

**Modele**

- `cod.borderou.mapping`: maparea salvată a coloanelor pentru un format de borderou (reutilizată fără AI).
- `cod.borderou.ai.import` (wizard) și `cod.borderou.ai.import.line`: citirea fișierului, apelul agentului AI, verificarea rândurilor și crearea extrasului de decontare.
- `res.company`, `res.config.settings`: activarea importului cu AI și limita zilnică.
- `account.journal`: buton de import pe jurnalul de decontare.

**Vizualizări**

- `view_cod_borderou_ai_import_form`: wizardul de import (rânduri, coloane, total).
- `view_cod_borderou_mapping_list` / `view_cod_borderou_mapping_form`: mapările salvate.
- `view_account_journal_form_cod_borderou_ai`, `res_config_settings_view_form_cod_borderou_ai`: integrarea în jurnal și în setări.

**Acțiuni Automate / Acțiuni Server**

- `ai_agent_cod_borderou_reader`: agentul AI *Courier Borderou Reader AI* (`ai.agent`, date). Nu există cron-uri.

#### 5. Conexiuni

- [deltatech_delivery_cod](../deltatech_delivery_cod/index.md): logica comună de decontare ramburs (validare, dubluri, total de control, linie de transfer).
