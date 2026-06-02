# Invoice Followup (localizat la `deltatech_followup/index.md`)

- **Nume Tehnic:** `deltatech_followup`
- **Versiune:** `19.0.0.1.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_followup`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_followup`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul oferă un sistem simplu de urmărire a facturilor neîncasate (followup), prin trimiterea automată de e-mailuri către clienți. Fiecare element de followup definește când și cum se trimite notificarea, raportându-se la data facturii sau la data scadenței, cu un decalaj configurabil în zile (înainte sau după). Trimiterea se face programat, printr-o sarcină cron, fie pentru toate elementele de followup, fie doar pentru cele selectate prin cod. Valoarea de afaceri constă în reducerea efortului manual de relaționare cu clienții pentru încasarea creanțelor și în îmbunătățirea fluxului de numerar.

#### 2. Funcționalități Cheie

- Configurarea elementelor de followup cu: nume, cod (utilizabil în cron pentru a rula doar anumite followup-uri), stare activă, câmpul de dată de referință (data facturii sau data scadenței) și numărul relativ de zile față de acea dată (ex. `-5` = cu 5 zile înainte, `3` = la 3 zile după).
- Personalizarea mesajului trimis: subiectul e-mailului, adresa expeditorului și corpul mesajului (cu blocuri preconfigurate disponibile prin ajutorul câmpului).
- Marcarea partenerilor care vor primi followup-uri, printr-o opțiune dedicată la nivel de partener.
- Programarea trimiterii prin cron, folosind modelul `followup.send.wizard`: `model.run_followup()` pentru toate elementele sau `model.run_followup(["12D", "20D"])` pentru cele selectate prin cod.
- Configurarea unui partener de test (override), prin parametrul de sistem `followup.override_partner_id`, pentru a redirecționa e-mailurile în scop de testare.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune este omisă deoarece există un fișier `readme/DESCRIPTION.md`, iar acesta acoperă scopul și funcționalitățile modulului fără a solicita explicit detalierea componentelor tehnice.

#### 5. Conexiuni

Nu au fost identificate module conexe cu pagină wiki existentă. Modulul se integrează cu funcționalitatea standard de contabilitate (`account`) pentru gestionarea facturilor clienți.
