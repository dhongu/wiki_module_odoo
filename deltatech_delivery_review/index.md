# Verificarea Comenzilor - Curieri (localizat la `deltatech_delivery_review/index.md`)

- **Nume Tehnic:** `deltatech_delivery_review`
- **Versiune:** `19.0.0.1.1`
- **Cale:** [https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_delivery_review](https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_delivery_review)
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_review`
- **Ultima Ingestie:** `2026-09-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face puntea dintre verificarea comenzilor și fluxul de curierat: aliniază suma de ramburs
judecată de regula „Ramburs mare" cu suma reală pe care AWB-ul o va încasa, iar în dialogurile de
expediere (Trimite la curier, Validare Livrări) afișează motivul concret pentru care o livrare este
reținută, în loc de un mesaj generic „amânată". Se instalează automat, fără configurare proprie, de
îndată ce sunt prezente ambele module-suport.

#### 2. Funcționalități Cheie

- Regula **Ramburs mare** judecă suma reală de pe AWB (`get_value_to_collect()`): totalul comenzii,
  cu excepția cazului în care o tranzacție de plată vie pe altă metodă îl acoperă deja — astfel și
  comenzile fără nicio tranzacție de plată (telefonice, import marketplace) sunt verificate corect.
- Dialogul **Acțiuni → Trimite la curier** afișează pentru livrările reținute rândul cu motivul
  complet (ex. „reținută pentru verificare: Ramburs 4.200,00 lei peste limita de 3.500,00 lei"), în
  loc de un simplu eșec; comenzile deja trimise sunt sărite la o reluare pe aceeași selecție.
- Raportul **Acțiuni → Validare Livrări** listează, pentru fiecare comandă neprocesată, motivul
  exact pentru care livrarea e reținută.
- Fără motiv de verificare deschis, o livrare amânată păstrează mesajul simplu standard
  („este amânată. Eliberați-o pe comanda de vânzare...").
- Se instalează automat (`auto_install`) când `deltatech_delivery` și [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)
  sunt ambele prezente; nu are meniu sau setări proprii. Se recomandă și instalarea modulului-frate
  [deltatech_delivery_status_review](../deltatech_delivery_status_review/index.md), care amână efectiv livrarea — fără el motivul apare pe comandă,
  dar livrarea nu e amânată și dialogurile nu au ce refuza.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.order`: adaugă `_review_cod_amount()`, care întoarce suma de încasat pe AWB
  (`get_value_to_collect()`) pentru a fi judecată de regula de ramburs mare.
- `stock.picking`: extinde `_delivery_hold_message()` pentru a include, în mesajul de refuz al
  expedierii, motivele deschise de verificare a comenzii (`sale_id._review_open_reasons("delivery")`).

**Vizualizări**

Modulul nu adaugă vizualizări proprii — extinde mesajele afișate deja de dialogurile din
`deltatech_delivery` (Trimite la curier, Validare Livrări).

**Acțiuni Automate / Acțiuni Server**

Nu definește `ir.cron`, `base.automation` sau `ir.actions.server` proprii.

#### 5. Conexiuni

- [deltatech_delivery_status_review](../deltatech_delivery_status_review/index.md): amânarea efectivă a livrării cât timp motivul de verificare e
  deschis; fără el, acest modul nu are ce livrare amânată să explice.
- `deltatech_delivery_status`: expune bifa „Amânată" pe transfer și refuzul la validare, prin
  intermediul [deltatech_delivery](../deltatech_delivery/index.md).
- `payment`: tranzacțiile de plată confirmate decid dacă suma de pe AWB este totalul comenzii sau
  zero.
