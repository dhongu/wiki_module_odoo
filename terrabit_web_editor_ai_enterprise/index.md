# Web Editor AI (OLG) - Enterprise bridge (localizat la `terrabit_web_editor_ai_enterprise/index.md`)

- **Nume Tehnic:** `terrabit_web_editor_ai_enterprise`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_web_editor_ai_enterprise
- **Cale Locală:** `odoo-addons/terrabit/terrabit_web_editor_ai_enterprise`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Punte între asistentul AI din editorul de text (`terrabit_web_editor_ai`, pe serviciul OLG găzduit de Odoo) și modulul Enterprise `ai`, care adaugă propriul asistent în editor, pe cheie proprie de LLM. Fără această punte, pe Enterprise ar apărea două intrări AI în editor. Modulul le face mutual exclusive în funcție de configurare, astfel încât utilizatorul vede un singur asistent.

#### 2. Funcționalități Cheie

- Fără cheie proprie de LLM configurată: rămâne doar butonul OLG (serviciul găzduit de Odoo, prin IAP, fără cheie), iar pluginul nativ `ai` din editor este eliminat. Reproduce experiența din Odoo 18.
- Cu cheie OpenAI / Google configurată: rămâne asistentul nativ `ai` (cheie proprie), iar butonul OLG este eliminat.
- Cheia este considerată configurată dacă există parametrul de sistem `ai.openai_key` sau `ai.google_key`, ori variabila de mediu `ODOO_AI_CHATGPT_TOKEN` sau `ODOO_AI_GEMINI_TOKEN`.
- Alegerea se calculează pe server și ajunge în clientul web prin `session_info` (`web_editor_ai_use_olg`); o schimbare de cheie se aplică la următoarea reîncărcare a paginii.
- Restul funcțiilor modulului `ai` (câmpuri AI, agenți, asistentul din chatter) rămân neatinse; este afectat doar pluginul editorului rich-text.
- Se instalează automat (`auto_install`) când sunt prezente `ai` și `terrabit_web_editor_ai`.

#### 3. Dependențe

- `ai`
- `terrabit_web_editor_ai`

#### 4. Componente Cheie

**Modele**

- `ir.http` (extins): `session_info` expune `web_editor_ai_use_olg`, calculat de `_web_editor_ai_use_olg` (True când nu există nicio cheie proprie de LLM).

**Vizualizări**

- Modulul nu definește vizualizări XML. Logica din client este în `static/src/web_editor_ai_olg_fallback.esm.js` (încărcat în `web.assets_backend`).

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `terrabit_web_editor_ai`: asistentul OLG din editor, a cărui prezență se coordonează cu pluginul nativ `ai`.
