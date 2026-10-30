# AI Helpdesk Chat Dispatcher (localizat la `deltatech_ai_helpdesk_chat/index.md`)

- **Nume Tehnic:** `deltatech_ai_helpdesk_chat`
- **Versiune:** `19.0.0.1.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/deltatech_ai_helpdesk_chat
- **Cale Locală:** `odoo-addons/terrabit/deltatech_ai_helpdesk_chat`
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Agentul AI Tibi citește chatul de suport pe care clienții îl scriu din propriul Odoo (canalul „Terrabit Support” al conectorului Helpdesk) și propune ce să se facă cu fiecare bloc de mesaje noi: legarea de un tichet existent, deschiderea unui tichet nou, un răspuns, o întrebare de clarificare sau ignorarea. În această versiune (Alpha) modulul doar **propune**: nimic nu ajunge la client până când un consultant nu aplică decizia. Rulează exclusiv pe baza de date a helpdesk-ului Terrabit.

#### 2. Funcționalități Cheie

- Cinci acțiuni posibile pentru un bloc de mesaje:
  - **Legare de tichet**: mesajele aparțin unui tichet deschis al clientului și sunt copiate în tichet, ca răspuns al clientului.
  - **Tichet nou**: se deschide tichetul pentru client, cu mesajele ca descriere, iar numărul tichetului se trimite în chat.
  - **Răspuns**: o întrebare simplă primește răspuns direct în chat.
  - **Întrebare**: când nu e clar ce vrea clientul, Tibi întreabă.
  - **Ignorare**: mulțumiri, „ok”, discuții între colegii clientului.
- Decizia apare ca **notă internă** în canalul clientului, cu butoanele **Aplică** și **Respinge**, precum și în Helpdesk › Tichete › Propuneri chat. Notele nu sunt trimise niciodată clientului.
- Aplicarea sau respingerea e înregistrată (cine, când); tichetul nou trece prin aceleași metode ca fluxul manual, deci apare la client în „Tichetele mele”.
- Măsuri de siguranță:
  - Blocul e citit la un minut după ultimul mesaj al clientului, deci un mesaj scris în bucăți e decis o singură dată.
  - Răspunsul AI e validat în Python: doar cele cinci acțiuni, doar tichete ale acelui client, încredere minimă 0,75 pentru legare și 0,85 pentru răspuns, altfel Tibi întreabă (motivul coborârii se păstrează pe propunere).
  - Dacă un consultant a scris în canal în ultimele 10 minute, Tibi doar leagă mesajele de tichet și nu răspunde.
  - Un răspuns AI inutilizabil (JSON invalid, tichet străin) nu creează nimic: canalul primește o notă pentru consultant.
- Configurare: în AI › Agenți › **Tibi (chat dispatcher)** se alege modelul LLM și, opțional, articole Knowledge ca surse pentru răspunsuri; consultanții trebuie să fie membri ai echipei de helpdesk a serviciului IAP `terrabit_helpdesk`, fiind membrii canalelor de suport și destinatarii notelor.

#### 3. Dependențe

- [terrabit_iap_server_helpdesk](../terrabit_iap_server_helpdesk/index.md)
- [terrabit_helpdesk_ai_reply](../terrabit_helpdesk_ai_reply/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.ai.chat.proposal`: decizia lui Tibi pentru un bloc de mesaje (acțiune, tichet, încredere, titlu, prioritate, răspuns, stare propus/aplicat/respins, decident); metodele `action_apply` / `action_reject`.
- `discuss.channel` (extins): programează citirea la un minut după mesajul clientului, construiește promptul, validează decizia AI și creează propunerea; câmpuri `ai_dispatch_at`, `ai_last_message_id`.
- `iap.server.account` (extins): exclude notele interne din mesajele trimise clientului.

**Vizualizări**

- `ai_chat_proposal_view_list` și `ai_chat_proposal_view_form`: lista și formularul propunerilor, cu butoanele Aplică / Respinge.
- Controller `/deltatech_ai_helpdesk_chat/proposal/<id>/<apply|reject>`: butoanele din nota Discuss sunt linkuri protejate cu token; cer grupul utilizator Helpdesk.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ai_dispatch_chat`: „AI Helpdesk Chat: dispatch client messages”, la 15 minute, plus declanșare la termenul fiecărui bloc; decide canalele cu termenul atins.
- `ai_agent_chat_dispatcher`: agentul AI „Tibi (chat dispatcher)” cu promptul de dispecer.

#### 5. Conexiuni

- [terrabit_helpdesk_ai_reply](../terrabit_helpdesk_ai_reply/index.md): oferă agentul Tibi, al cărui partener semnează răspunsurile din chat.
- [terrabit_iap_server_helpdesk](../terrabit_iap_server_helpdesk/index.md): aduce chatul clienților prin serverul IAP și crearea tichetelor pentru cont.
- `helpdesk`: tichetele și grupurile de acces.
