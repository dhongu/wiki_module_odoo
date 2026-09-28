# Delivery Tracking Dashboard (localizat la `deltatech_delivery_dashboard/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dashboard`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_dashboard
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_dashboard`
- **Ultima Ingestie:** `2026-09-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă o bandă de carduri KPI deasupra listei de AWB-uri de livrare, astfel încât cine urmărește expedierile să vadă dintr-o privire ce colete cer atenție azi — fără să filtreze manual lista. Fiecare card numără AWB-urile aflate într-o anumită situație (în tranzit, livrate azi, întârziate, cu risc de retur, returnate luna asta, cu ramburs pe drum sau fără urmărire), iar un click pe card filtrează lista exact pe ce a numărat cardul respectiv. Modulul folosește doar datele deja colectate de `deltatech_delivery` (starea livrării raportată de curier) și nu adaugă câmpuri noi pe livrări sau comenzi.

#### 2. Funcționalități Cheie

- Șapte carduri KPI: **În tranzit**, **Livrate azi**, **Întârziate ≥ N zile**, **Risc retur ≥ R zile**, **Retururi luna asta**, **Ramburs pe drum** (o sumă per monedă de încasare) și **Fără urmărire**.
- Click pe un card filtrează lista de AWB-uri pe exact ce a numărat cardul; un al doilea click pe alt card înlocuiește filtrul, un al doilea click pe același card îl șterge.
- Cardurile se suprapun intenționat (un colet la locker de o săptămână e și „Întârziat", și „Risc retur") — fiecare răspunde la propria întrebare, nu sunt gândite să se adune.
- Doar AWB-ul curent al livrării este listat; un AWB retrimis după o anulare își păstrează vechiul AWB, care nu mai este numărat.
- Data „În stare din" e data evenimentului raportat de curier (nu ora la care Odoo a interogat starea): un colet livrat seara și interogat după miezul nopții contează ca livrat în seara respectivă.
- Pragurile de „Întârziat" și „Risc retur" sunt configurabile din parametrii de sistem (`delivery_dashboard.overdue_days`, implicit 5 zile; `delivery_dashboard.return_risk_days`, implicit 3 zile).
- Într-o bază multi-companie, fiecare companie vede doar propriile AWB-uri (necesită `deltatech_delivery` 19.0.6.8.1 sau mai nou, care asociază fiecare AWB companiei livrării sale).
- Accesibil din *Inventar → Operațiuni → Delivery AWB → Delivery Tracking*, disponibil utilizatorilor cu grupul Inventar / Utilizator; același grup e verificat și de cererea care calculează cardurile, nu doar de meniu.
- Fluxul complet pas-cu-pas de configurare și testare este detaliat în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.awb` (extindere): adaugă `delivery_state` (stocat, pentru performanță — cardurile numără direct pe `delivery.awb`, fără subquery pe `stock.picking`), `delivery_state_date` (data intrării în starea curentă), `is_current` (AWB-ul curent al livrării, calculat/stocat), `cod_currency_id` (moneda de încasare a rambursului) și câmpul tehnic `dashboard_bucket`, căutabil, pe care se bazează filtrele cardurilor.
- `stock.picking` (extindere): la schimbarea reală a `delivery_state`, actualizează `delivery_state_date` pe AWB-urile livrării cu data evenimentului curierului (nu data pollului), ca să nu se mute înainte la fiecare interogare de stare care doar repetă aceeași stare.

**Vizualizări**

- `view_delivery_awb_dashboard_list`: listă de AWB-uri cu coloane relevante urmăririi (transportator, client, telefon, stare, dată, ramburs) și butoane pentru deschiderea livrării, vizualizarea comenzii și reluarea interogării de stare.
- `view_delivery_awb_dashboard_search`: filtrele de căutare, câte unul pentru fiecare card, toate căutând pe `dashboard_bucket` — astfel un card și lista pe care o deschide nu pot fi în dezacord.
- `action_delivery_awb_dashboard` / meniul „Delivery Tracking”: acțiunea și meniul din *Inventar → Operațiuni*, restricționate la grupul `stock.group_stock_user`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): sursa stărilor de livrare și a cronului de interogare a curierilor pe care se bazează toate cardurile.
