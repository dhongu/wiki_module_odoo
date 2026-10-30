# AI - Livechat Customer Context (localizat la `deltatech_ai_livechat_customer/index.md`)

- **Nume Tehnic:** `deltatech_ai_livechat_customer`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_livechat_customer
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_livechat_customer`
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Agentul AI din livechat-ul site-ului web știe cu cine vorbește atunci când vizitatorul este autentificat: din ce companie face parte și dacă aceasta este deja client. Astfel, instrucțiunile agentului pot trata diferit clienții față de prospecți: fără întrebări de calificare a lead-ului pentru un client existent, ci ajutor pe instalarea lui sau deschiderea unui tichet de suport. Vizitatorii anonimi nu sunt afectați.

#### 2. Funcționalități Cheie

- Odoo standard oferă agentului doar numele, funcția, emailul și telefonul vizitatorului autentificat. Modulul adaugă, doar în conversațiile de livechat, linia *Visitor status*: vizitatorul este autentificat în portal sau este utilizator intern (angajat).
- Pentru utilizatorii de portal, contextul include compania vizitatorului (partenerul comercial) și dacă aceasta este deja client (are facturi de client) sau nu are încă facturi.
- Link-urile agentului către această bază de date (de ex. articole Knowledge) sunt rescrise pe domeniul site-ului web pe care discută vizitatorul. Altfel, deschise dintr-un site cu domeniu propriu, ar porni o sesiune de livechat nouă și goală.
- Configurare: nu există nimic de configurat după instalare. În *AI ▸ Agents*, la agentul folosit de canalul de livechat, se adaugă în promptul de sistem o regulă pentru linia *Visitor status* și pentru clienții existenți (de ex. să nu întrebe dacă folosește Odoo sau ce versiune, ci să ajute sau să ceară deschiderea unui tichet de suport).

#### 3. Dependențe

- `ai_livechat`
- `account`

#### 4. Componente Cheie

**Modele**

- `ai.agent` (extins): `_build_system_context` adaugă contextul vizitatorului pentru canalele de livechat cu utilizator nepublic (`_get_livechat_customer_context`); `_post_ai_response` rescrie link-urile către baza de date pe domeniul cererii curente (`_localize_livechat_links`). Clientul este detectat după `customer_rank` al partenerului comercial.

**Vizualizări**

- Modulul nu adaugă vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- `ai`: modulul de bază al agenților AI, al cărui `ai.agent` este extins prin `ai_livechat`.
- `website_livechat`: canalul de livechat de pe site-ul web în care se aplică contextul.
