# Advanced Planner AI Assistant (localizat la `deltatech_advanced_planner_ai/index.md`)

- **Nume Tehnic:** `deltatech_advanced_planner_ai`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_advanced_planner_ai
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_advanced_planner_ai`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

**Advanced Planner** calculează când se poate livra efectiv o comandă de vânzare, ce componente lipsesc și ce posturi de lucru sunt supraîncărcate. Acest modul adaugă un asistent AI care **explică** în limbaj simplu rezultatele planificatorului și **propune** ce se poate face: planificatorul calculează, AI-ul explică, oamenii decid. Nimic nu se modifică automat: răspunsurile sunt note sau mesaje, iar cererile de ofertă, comenzile de producție și datele rămân de schimbat de oameni.

#### 2. Funcționalități Cheie

- **Buton Explain planning** pe comenzile de vânzare și pe comenzile planificate: asistentul citește rezultatul planificatorului și postează o notă internă cu **cauza** întârzierii (componenta, furnizorul sau postul de lucru, zilele implicate), maximum trei **opțiuni** disponibile în Odoo (urgentarea unei cereri de ofertă, alt furnizor, livrare împărțită, mutarea datei promise), fiecare cu efectul în zile, și un **mesaj scurt pentru client**, fără detalii interne. Butonul nu apare pe ofertele fără planificare sau când asistentul e dezactivat.
- **Rezumat zilnic** (digest): în fiecare dimineață, într-un canal Discuss (implicit *Planning digest*), cu secțiunile *What changed*, *To do today* și *Risks*; butonul **Send the digest now** din Setări îl verifică imediat.
- **Datele rămân ale dumneavoastră**: la furnizorul AI se trimit doar date de planificare (numere de documente, produse, cantități, date, stări, nume de furnizori și lead time-uri, încărcarea posturilor). Nu se trimit prețuri, sume, nume sau contacte de clienți.
- **Cost sub control**: limită zilnică de cereri AI pe companie (implicit 50; 0 = fără limită) și listă de audit a cererilor (*Manufacturing > Advanced Planning > AI Requests*: dată, tip, document, utilizator, stare, eroare).
- **Framework-ul Odoo AI**: răspunsurile vin de la LLM-ul aplicației Odoo AI (credite AI), cu instrucțiunile agentului *Planning Assistant*; răspunsul e în limba utilizatorului.
- **Activare**: *Settings > Inventory > Planning AI Assistant*, bifa **AI planning assistant**, apoi **Configure the AI agent**, limita zilnică și, opțional, digest-ul.
- **Cerințe**: Odoo 20 **Enterprise** (framework-ul AI) și modulul Advanced Planner.

#### 3. Dependențe

- [deltatech_advanced_planner](../deltatech_advanced_planner/index.md)
- `ai`

#### 4. Componente Cheie

Secțiunea nu este detaliată: documentația se bazează pe `readme/DESCRIPTION.md`, care nu solicită explicit analiza componentelor tehnice (modele, vizualizări, acțiuni automate). Din manifest și structura modulului: modelul `advanced.planner.ai.request` (auditul cererilor), modelul abstract `advanced.planner.ai` (construiește prompturile și apelează agentul), extinderi pe `sale.order`, `advanced.planned.order`, `res.company` și `res.config.settings`; acțiunea programată `ir_cron_planning_ai_digest` (rezumatul zilnic, o dată pe zi), agentul AI *Planning Assistant* și canalul Discuss *Planning digest* (din `data/`).

#### 5. Conexiuni

- [deltatech_advanced_planner](../deltatech_advanced_planner/index.md): planificatorul ale cărui rezultate sunt explicate de asistent.
