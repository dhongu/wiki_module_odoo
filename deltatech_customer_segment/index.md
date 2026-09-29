# Deltatech Customer Segment (localizat la `deltatech_customer_segment/index.md`)

- **Nume Tehnic:** `deltatech_customer_segment`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_customer_segment
- **Cale Locală:** `odoo-addons/bitshop/deltatech_customer_segment`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

În fiecare noapte, modulul calculează pentru fiecare client (și pentru fiecare companie) poziția lui în portofoliul de vânzări: cât de des cumpără, cât a cumpărat, cât are de plată și în ce categorie de portofoliu se încadrează. Clientul este judecat în raport cu propriul ritm de cumpărare, nu cu o medie a firmei, astfel încât un cumpărător săptămânal tăcut trei săptămâni este „în risc”, iar unul trimestrial tăcut două luni este încă activ. Rezultatele stau într-un tabel propriu, fără câmpuri adăugate pe partener, și oferă agenților și directorului de vânzări lista zilnică de clienți de sunat.

#### 2. Funcționalități Cheie

- **Ritm de cumpărare:** media zilelor dintre achiziții, calculată pe istoricul clientului, și numărul de zile de când nu a mai cumpărat.
- **Segment de ritm:** nou, activ, în risc, adormit sau pierdut, raportat la ritmul propriu al clientului.
- **Vânzări:** total de la început, ultimele 12 luni, perioada curentă față de cea anterioară, achiziție medie, creștere.
- **Creanțe:** sold deschis, sumă restantă, număr de facturi restante și vechimea celei mai vechi, citite doar din facturile de client.
- **Clasificare de portofoliu:** client de top, în creștere, cu potențial ridicat, comenzi mici (upsell), stabil, în scădere, inactiv (trei niveluri) sau risc de plată, plus scor de risc și scor de potențial.
- **Sursa datelor:** facturi de client postate (note de credit scăzute) sau comenzi de vânzare confirmate, fără TVA și în moneda companiei; vânzările contactelor se cumulează la firma-mamă.
- **Setări (Vânzări > Portofoliu clienți > Setări):** sursa, excluderea persoanelor fizice (doar B2B), prefixele conturilor de venit numărate ca vânzări (implicit `70`), perioada de comparație în luni, pragurile în moneda companiei; buton „Recalculează acum”.
- **Utilizare:** Vânzări > Portofoliu clienți > Segmente clienți, cu filtre (în scădere, inactiv, risc de plată, în risc pe ritm propriu, a cumpărat o singură dată, clienții mei), vedere pivot și grafic; din fișa partenerului, Acțiune > Segment client.
- **Roluri:** „Clienți proprii” (agentul vede doar clienții pe care este vânzător) și „Toți clienții” (director, editează pragurile); regulă multi-companie.
- Detaliile pas cu pas sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale_management`
- `account`

#### 4. Componente Cheie

**Modele**

- `deltatech.customer.segment`: un rând per client și companie, cu ritmul, vânzările, creanțele, clasificarea și scorurile; conține motorul de recalculare.
- `deltatech.customer.segment.config`: setările per companie (sursă, conturi de vânzări, perioadă, praguri).

**Vizualizări**

- `view_customer_segment_list`, `view_customer_segment_form`, `view_customer_segment_pivot`, `view_customer_segment_graph`, `view_customer_segment_search`: interfața portofoliului.
- `view_customer_segment_config_form`: formularul de setări.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_customer_segment_recompute`: „Customer Segment: nightly recompute”, recalculare nocturnă.
- `action_server_partner_customer_segment`: deschide segmentul din fișa partenerului.
- `action_server_customer_segment_config`: deschide setările companiei.

#### 5. Conexiuni

- [deltatech_customer_analysis](../deltatech_customer_analysis/index.md) (F2): tabloul de analiză a clienților, depinde de acest modul și folosește motorul de segmentare.
- [deltatech_sale_missions](../deltatech_sale_missions/index.md) (F3): misiunile săptămânale de vânzare, depind de acest modul și pornesc de la segmentele calculate aici.
- Ambele fac parte din familia „portofoliu clienți”; nu au încă pagină wiki, deci rămân text.
