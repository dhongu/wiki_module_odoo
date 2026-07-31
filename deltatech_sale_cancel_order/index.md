# Terrabit Sale Cancel Order (localizat la `deltatech_sale_cancel_order/index.md`)

- **Nume Tehnic:** `deltatech_sale_cancel_order`
- **Versiune:** `19.0.0.1.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_cancel_order`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_cancel_order`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul oferă clienților posibilitatea de a solicita anularea unei comenzi de vânzare direct din portal. În loc să anuleze efectiv comanda, modulul înregistrează în backend o cerere de anulare, însoțită obligatoriu de un motiv, astfel încât un operator să poată decide manual dacă și când anulează comanda. Comenzile cu o cerere de anulare sunt evidențiate vizual și pot fi filtrate ușor, iar echipa de vânzări poate fi notificată prin e-mail în funcție de setări. Astfel, procesul de anulare rămâne controlat de companie, păstrând transparența față de client.

#### 2. Funcționalități Cheie

- Permite clientului să solicite anularea unei comenzi de vânzare din portal.
- Solicită obligatoriu un motiv pentru cererea de anulare.
- Comanda nu este anulată efectiv: se emite o cerere de anulare în backend, pe care un operator o poate confirma manual.
- Comenzile cu o cerere de anulare pot fi filtrate.
- Comenzile cu o cerere de anulare sunt afișate cu roșu în vizualizarea de tip listă.
- O bară roșie este afișată în formular pentru comenzile cu o cerere de anulare.
- Motivul cererii de anulare este afișat în chatter-ul comenzii de vânzare.
- În funcție de setări (Vânzări -> Configurare), se trimite un e-mail către agentul de vânzări al comenzii și către alți parteneri.

#### 3. Dependențe

- `sale`
- `portal`

#### 4. Componente Cheie

Documentația acestei secțiuni a fost omisă deoarece modulul include un fișier `readme/DESCRIPTION.md`, care a fost folosit ca sursă principală conform fluxului de ingestie.

#### 5. Conexiuni

- Nu au fost identificate conexiuni suplimentare relevante către alte module documentate în wiki.
