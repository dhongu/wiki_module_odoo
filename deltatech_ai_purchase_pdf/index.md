# Purchase PDF AI Import

- **Nume Tehnic:** `deltatech_ai_purchase_pdf`
- **Versiune:** `20.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_ai_purchase_pdf
- **Cale Locală:** odoo-addons/bitshop_ent/deltatech_ai_purchase_pdf
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Nu toți furnizorii trimit e-Factura XML. Modulul importă pe comanda de achiziție factura furnizorului în format **PDF**, la fel ca XML-ul: un agent AI citește antetul, liniile și totalurile documentului, iar asistentul de import *Purchase UBL* face restul.

#### 2. Funcționalități Cheie

- **Același asistent, XML sau PDF**: butonul *Import Invoice* al comenzii acceptă un PDF; dacă nu există XML UBL atașat, asistentul ia ultimul PDF al comenzii.
- **AI citește, Odoo decide**: agentul doar transcrie documentul într-un JSON strict; potrivirea produselor (cod de bare, cod furnizor, denumire), acțiunea pe linie, actualizarea prețului furnizorului, recepția și factura sunt pașii deterministi din *Purchase UBL*.
- **Mereu revizuit**: un PDF nu se importă direct; previzualizarea afișează un banner și lista neconcordanțelor (cantitate × preț ≠ valoare, linii ≠ total, TVA + bază ≠ total de plată, CUI furnizor necitit).
- **Verificat față de textul PDF**: cantitatea, prețul, valoarea și codul fiecărei linii, plus totalurile, sunt căutate în textul paginii; CUI-ul furnizorului este verificat cu cifra de control. Un PDF scanat nu este verificat, iar previzualizarea o spune.
- **Progres și relecturi**: pentru PDF-uri cu mai multe pagini, un dialog arată paginile citite, liniile găsite și timpul rămas; paginile cu avertismente se pot citi din nou (*Read Again Pages with Warnings* sau *Pages to read again*), păstrând produsele alese pe celelalte pagini.
- **Un apel AI per document**: extracția este păstrată pe asistent, deci previzualizarea și importul citesc PDF-ul o singură dată.
- **Cu potrivire AI a produselor**: dacă este instalat *Purchase UBL AI Product Matching*, liniile neplasate primesc sugestie de produs, ca la XML.
- **Cost controlat**: activare opțională per companie (implicit oprit) și limită zilnică de documente (implicit 50, 0 = nelimitat), în *Settings → Purchase → Invoicing → PDF Invoice Import with AI*.
- **Odoo AI**: PDF-ul este citit de LLM-ul serviciului Odoo AI (Enterprise, credite IAP), cu răspunsul constrâns de o schemă JSON; nu se alege model sau cheie pe agent.
- **Sigur**: documentul este tratat ca date, iar agentul nu urmează instrucțiuni scrise în el.
- **Parametri de sistem opționali**: `deltatech_ai_purchase_pdf.timeout` (implicit 300 s), `.pages_per_call` (implicit 1), `.parallel_calls` (implicit 3).

#### 3. Dependențe

- [deltatech_purchase_ubl](../deltatech_purchase_ubl/index.md)
- `ai`
- [deltatech_ai_pdf_base](../deltatech_ai_pdf_base/index.md)
- `deltatech_task_progress`

#### 4. Componente Cheie

**Modele**

- `purchase.ubl.import.wizard` (extins, cu `task.progress.mixin`): citirea PDF-ului cu AI, progres, relectură de pagini, avertismente.
- `purchase.ubl.import.wizard.line` (extins): pagina de origine a liniei.
- `purchase.pdf.ai.page`: rezultatul citirii per pagină.
- `purchase.order`, `res.company`, `res.config.settings` (extinse): alegerea PDF-ului, activarea per companie și limita zilnică.
- `ai.agent` (extins): agentul *Purchase Invoice PDF Reader AI*.

**Vizualizări**

- `views/ubl_import_wizard_views.xml`: asistentul de import cu banner, avertismente și relectură.
- `views/res_config_settings_views.xml`: activarea importului PDF cu AI și limita zilnică.

**Acțiuni Automate / Acțiuni Server**

- `data/ai_agent_data.xml`: agentul AI *Purchase Invoice PDF Reader AI*; nu are cron.

#### 5. Conexiuni

- [deltatech_purchase_ubl](../deltatech_purchase_ubl/index.md): pașii deterministi ai importului (produse, recepție, factură).
- [deltatech_ai_pdf_base](../deltatech_ai_pdf_base/index.md): verificările în textul PDF și cifra de control.
