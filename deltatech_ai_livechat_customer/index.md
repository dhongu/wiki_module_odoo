# AI - Livechat Customer Context

- **Nume Tehnic:** `deltatech_ai_livechat_customer`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_ai_livechat_customer
- **Cale Locală:** odoo-addons/bitshop_ent/deltatech_ai_livechat_customer
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Agentul AI al chatului de pe website știe cu cine vorbește atunci când vizitatorul este autentificat. Odoo standard îi oferă agentului doar numele, funcția, emailul și telefonul vizitatorului; modulul adaugă compania vizitatorului și faptul că este deja client, ca promptul agentului să poată trata diferit clienții față de prospecți.

#### 2. Funcționalități Cheie

- **Context suplimentar în conversațiile livechat**: dacă vizitatorul este autentificat pe portal sau este utilizator intern, compania sa (partenerul comercial) și dacă acea companie este deja client (are facturi de client).
- **Linkuri către domeniul site-ului**: linkurile agentului către această bază de date (ex. articole Knowledge) sunt rescrise pe domeniul website-ului pe care chatuiește vizitatorul; altfel, un link pe URL-ul de bază ar porni o sesiune livechat nouă, goală.
- **Prompt diferențiat**: în *AI ▸ Agents*, agentul chatului primește o regulă pentru linia *Visitor status* (ex. fără întrebări de calificare pentru un client existent, ci ajutor sau tichet de suport).
- **Vizitatorii anonimi** nu sunt afectați.
- Nu are nimic de configurat după instalare.

#### 3. Dependențe

- `ai_livechat`
- `account`

#### 4. Componente Cheie

**Modele**

- `ai.session` (extins): adaugă în context starea vizitatorului, compania și statutul de client.
- `ai.agent` (extins): rescrierea linkurilor către domeniul website-ului.

**Vizualizări**

- Fără vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `im_livechat`: canalul de chat al website-ului în care agentul răspunde.
