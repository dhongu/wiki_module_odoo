# Web Editor AI (OLG) (localizat la `terrabit_web_editor_ai/index.md`)

- **Nume Tehnic:** `terrabit_web_editor_ai`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_web_editor_ai
- **Cale Locală:** `odoo-addons/terrabit/terrabit_web_editor_ai`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul readuce în editorul de text (câmpuri HTML și compunerea emailurilor) asistentul AI care exista în Odoo Community până la versiunea 18 și a fost scos din Community în 19. Utilizatorii pot genera text sau reformula textul selectat fără o cheie de API proprie, folosind serviciul OLG găzduit de Odoo (prin IAP), a cărui parte de server este încă prezentă în Community 19. Este util pentru instalările care rămân pe Community și nu folosesc modulul Enterprise `ai`.

#### 2. Funcționalități Cheie

- Buton **AI** în bara de instrumente a editorului, lângă „Translate with AI" nativ.
- Comandă **AI** în powerbox (`/AI`), în categoria „AI Tools".
- Dialog de **prompt** (conversație liberă pentru generarea de text), afișat când cursorul nu are selecție.
- Dialog de **alternative** când există text selectat: Correct, Shorten, Lengthen, Friendly, Professional, Persuasive.
- Funcționează atât în câmpurile HTML din backend, cât și în editorul din compunerea emailurilor (mail composer), ca în Odoo 18.
- Nu necesită cheie proprie; serviciul OLG este tarifat prin IAP de Odoo. Modulul este o soluție de tranziție: dacă endpoint-ul OLG este retras, controllerul `generate_text` poate fi suprascris pentru un alt furnizor (ex. cheie OpenAI proprie).

#### 3. Dependențe

- `html_editor`
- `mail`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește și nu extinde modele Python; este doar front-end.

**Vizualizări**

- `chatgpt_plugin.esm.js`: pluginul `OlgChatGPTPlugin`, înregistrat în `MAIN_PLUGINS` (editorul backend) și în `MAIL_CORE_PLUGINS` (editorul din mail composer); expune butonul din toolbar și comanda din powerbox.
- `chatgpt_prompt_dialog` (JS + XML): dialogul de prompt liber.
- `chatgpt_alternatives_dialog` (JS + XML): dialogul cu alternativele de reformulare.
- `chatgpt_plugin.scss`: stiluri pentru dialoguri.

**Acțiuni Automate / Acțiuni Server**

- Niciuna. Backend-ul folosit este controllerul existent `/html_editor/generate_text` din `html_editor`.

#### 5. Conexiuni

- `html_editor`: oferă controllerul `/html_editor/generate_text` și dialogul de bază reutilizate de plugin.
- `mail`: editorul din compunerea emailurilor primește același plugin.
- Modulul Enterprise `ai`: alternativă oficială, neinstalată în scenariul acestui modul.
