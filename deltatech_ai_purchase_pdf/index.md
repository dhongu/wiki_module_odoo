# Purchase PDF AI Import

- **Nume Tehnic:** `deltatech_ai_purchase_pdf`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_purchase_pdf
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_purchase_pdf`
- **Ultima Ingestie:** `2026-10-21`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Nu toți furnizorii trimit factura în format e-Factura XML. Acest modul permite importul facturii de furnizor în format **PDF** direct din comanda de achiziție, în același mod ca la XML: un agent AI citește antetul, liniile și totalurile documentului, iar asistentul de import din *Purchase UBL* face restul (potrivirea produselor, prețurile furnizorului, recepția și factura de achiziție). Utilizatorul verifică întotdeauna rezultatul într-o previzualizare înainte de import.

#### 2. Funcționalități Cheie

- **Același asistent, XML sau PDF**: butonul **Import Invoice** (în română „Import factură”, din `deltatech_purchase_ubl` 19.0.1.4.19) de pe comanda de achiziție acceptă și un PDF. Dacă la comandă nu există un XML UBL atașat, asistentul preia ultimul PDF atașat; fișierul poate fi ales și direct în asistent.
- **AI citește, Odoo decide**: agentul doar transcrie documentul într-un JSON strict (antet, linii, totaluri). Potrivirea produselor (cod de bare, cod furnizor, denumire), acțiunea pe fiecare linie, actualizarea prețurilor furnizorului, recepția și factura sunt pașii deterministi din *Purchase UBL*.
- **Mereu verificat**: un PDF nu se importă niciodată direct. Previzualizarea se deschide cu un banner de avertizare și listează ce nu se potrivește: linie la care cantitate × preț diferă de valoare, linii care nu însumează totalul indicat, TVA plus bază diferite de totalul de plată, CUI-ul furnizorului necitit.
- **Progres la citire**: pentru PDF-uri cu mai multe pagini, un dialog arată paginile citite, liniile găsite și timpul rămas; o pagină eșuată poate fi recitită.
- **Un apel AI per document**: extracția se păstrează pe asistent, deci previzualizarea și importul citesc PDF-ul o singură dată.
- **Compatibil cu potrivirea AI a produselor**: cu [deltatech_purchase_ubl_ai](../deltatech_purchase_ubl_ai/index.md) instalat, liniile rămase neplasate primesc o sugestie de produs, ca la XML.
- **Costuri sub control**: activare opțională per companie (implicit dezactivat) și limită zilnică de documente citite cu AI (implicit 50 per companie, 0 = nelimitat), din **Setări → Achiziții → Facturare → PDF Invoice Import with AI**.
- **Furnizorul tău de AI**: folosește cadrul AI nativ Odoo și cheia din **Setări → AI**; modelul trebuie să accepte fișiere PDF (OpenAI GPT-4o sau mai nou, Google Gemini sau Claude cu [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md)). Modelul agentului se poate schimba din **AI → Agents → Purchase Invoice PDF Reader AI**; instrucțiunile sunt traductibile.
- **Sigur prin construcție**: documentul este tratat ca date; agentului i se spune să nu urmeze niciodată instrucțiuni scrise în el.
- **Parametri de sistem opționali**: `deltatech_ai_purchase_pdf.timeout` (secunde de așteptare pentru un răspuns, implicit 300), `deltatech_ai_purchase_pdf.pages_per_call` (pagini citite la o cerere, implicit 1; mai multe pagini pierd linii la facturi lungi), `deltatech_ai_purchase_pdf.parallel_calls` (pagini citite simultan de dialogul de progres, implicit 3).

#### 3. Dependențe

- [deltatech_purchase_ubl](../deltatech_purchase_ubl/index.md)
- `ai`

#### 4. Componente Cheie

**Modele**

- `purchase.ubl.import.wizard` (extins): acceptă PDF, apelează agentul AI, extrage și combină paginile, verifică totalurile și contorizează limita zilnică.
- `purchase.pdf.ai.page` (tranzitoriu): o pagină din PDF citită de AI, folosită de dialogul de progres.
- `purchase.order` (extins): încărcarea PDF-ului din comandă/listă (`create_document_from_attachment`).
- `ai.agent` (extins): prompt de sistem traductibil.
- `res.company` / `res.config.settings` (extinse): activarea importului PDF cu AI, limita zilnică și contoarele de apeluri.

**Vizualizări**

- `view_purchase_ubl_import_wizard_inherit_pdf_ai`: moștenește asistentul de import; adaugă bannerul de avertizare și lista diferențelor pentru PDF.
- `res_config_settings_view_form_purchase_pdf_ai`: opțiunile din Setări → Achiziții.
- Componentă JS `read_progress` (`static/src/read_progress/`): dialogul de progres la citirea paginilor.

**Acțiuni Automate / Acțiuni Server**

- `ai_agent_purchase_pdf_extraction`: agentul AI „Purchase Invoice PDF Reader AI” (date, nu acțiune planificată). Modulul nu definește cron-uri.

#### 5. Conexiuni

- [deltatech_purchase_ubl_ai](../deltatech_purchase_ubl_ai/index.md): sugestii AI de produs pentru liniile nepotrivite.
- [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md): permite folosirea modelelor Claude, care acceptă PDF.
