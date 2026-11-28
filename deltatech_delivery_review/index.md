# Sale Order Review - Couriers

- **Nume Tehnic:** `deltatech_delivery_review`
- **Versiune:** `20.0.0.1.11`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_delivery_review
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_review`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul leagă verificarea comenzilor de vânzare de fluxul de curierat din `deltatech_delivery`: regula „Ramburs mare" judecă suma reală pe care curierul o va încasa, iar dialogurile de expediere afișează motivul concret pentru care o livrare este reținută, în loc de un simplu „amânată". Se instalează explicit, doar acolo unde se dorește verificarea comenzilor; nu se instalează automat și nu are meniu sau setări proprii.

#### 2. Funcționalități Cheie

- **Regula „Ramburs mare"** judecă suma de încasat: ce mai are de plătit clientul (totalul comenzii sau restul din facturile postate), minus plățile online încheiate sau autorizate. O plată eșuată sau în așteptare nu se numără, o plată parțială acoperă doar suma ei, iar o comandă fără curier nu este ramburs. Fără acest modul, regula vede doar tranzacțiile unui furnizor explicit de ramburs.
- **Acțiuni > Trimite la curier:** pentru livrările reținute, rândul devine roșu și arată motivul complet (ex. „reținută pentru verificare: Ramburs 4.200 lei peste limita de 3.500 lei"), fără a afecta restul lotului; după aprobare, reluarea pe aceeași selecție sare comenzile deja trimise, deci niciun AWB nu se dublează.
- **Acțiuni > Validare Livrări:** notificarea numește motivele pentru fiecare comandă neprocesată, în locul unui „transferul este amânat" generic.
- **Urmă de audit:** motivele rămân pe comandă (butonul **Reviews**), iar aprobarea lasă o notă în chatter.
- Reținerea efectivă (amânarea livrării) vine din [deltatech_delivery_status_review](../deltatech_delivery_status_review/index.md); `deltatech_delivery` refuză expedierea unei livrări amânate indiferent de buton. Se instalează și acest modul, altfel motivul apare doar pe comandă.
- Regula se verifică în *Vânzări > Configurare > Order Review Rules* (activă, cu limită și grup de aprobare). Pașii cu capturi sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.order`: adaugă `_review_cod_amount()`, care întoarce suma de încasat pe AWB (`get_value_to_collect()`) pentru a fi judecată de regula de ramburs mare.
- `stock.picking`: extinde `_delivery_hold_message()` pentru a include, în mesajul de refuz al expedierii, motivele deschise de verificare a comenzii (`sale_id._review_open_reasons("delivery")`).

**Vizualizări**

Modulul nu adaugă vizualizări proprii; extinde mesajele afișate de dialogurile din `deltatech_delivery` (Trimite la curier, Validare Livrări).

**Acțiuni Automate / Acțiuni Server**

Nu definește `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_delivery_status_review](../deltatech_delivery_status_review/index.md): amânarea efectivă a livrării cât timp motivul de verificare e deschis.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): bifa „Amânată" pe transfer și refuzul la validare.
- `payment`: starea ultimei tranzacții de plată a comenzii decide suma de pe AWB.
