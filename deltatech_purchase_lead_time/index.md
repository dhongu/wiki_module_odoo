# Termen de livrare măsurat al furnizorului

- **Nume Tehnic:** `deltatech_purchase_lead_time`
- **Versiune:** `20.0.1.0.4`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_purchase_lead_time`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_purchase_lead_time`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul măsoară termenul real de livrare al furnizorilor din istoricul de achiziții, în loc să se bazeze doar pe „Termenul de livrare” scris manual în lista de prețuri a furnizorului. O observație este o linie de comandă de achiziție confirmată și recepționată: zilele calendaristice de la confirmarea comenzii până la prima recepție. Valorile apar pe listele de prețuri ale furnizorilor și pot fi folosite de instrumentele de planificare, unde opțiunea este activată; modulul nu schimbă nimic pe cont propriu.

#### 2. Funcționalități Cheie

- Calcul, pentru fiecare linie din lista de prețuri a furnizorului, al **medianei**, al unui **percentil** configurabil (P80 implicit), al **abaterii** (σ, baza unui stoc de siguranță) și al **numărului de observații**.
- Livrările parțiale ulterioare (backorder) nu măresc termenul; retururile și comenzile altor companii nu se numără.
- Valoarea provine de la cel mai specific nivel cu istoric suficient: furnizor și produs, apoi furnizor pe toate produsele, altfel termenul configurat. Sursa (măsurat pe produs, măsurat pe furnizor, configurat) este afișată mereu.
- Pe linia de furnizor din fișa produsului (fila **Achiziție**) apar termenul măsurat, sursa, numărul de observații, mediana și abaterea; în listele de prețuri furnizor, coloanele opționale **Termen măsurat**, **Sursa termenului** și **Observații termen**.
- Setări în *Achiziții > Configurare > Setări*, secțiunea **Termen de livrare măsurat**: percentila (80 implicit) și numărul minim de observații (5 implicit), înainte ca valoarea măsurată să înlocuiască termenul configurat.
- Fereastra de istoric este cea a ratei de livrare la timp a furnizorului (parametrul `purchase_stock.on_time_delivery_days`, 365 de zile implicit).
- Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `purchase.vendor.lead.time` (model abstract): calculul medianei, percentilei, abaterii și al sursei termenului.
- `product.supplierinfo` (extins): câmpurile calculate ale termenului măsurat pe linia de furnizor.
- `res.config.settings` (extins): percentila și numărul minim de observații.

**Vizualizări**

- `product_supplierinfo_form_view`: grupul **Termen măsurat** sub termenul de livrare.
- `product_supplierinfo_tree_view`: coloane opționale pentru termenul măsurat.
- `res_config_settings_view_form`: setările modulului în Achiziții.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_nap](../deltatech_nap/index.md): raportul de necesar de achiziții poate folosi termenul măsurat, unde opțiunea este activată (conform descrierii modulului).
- [deltatech_advanced_planner](../deltatech_advanced_planner/index.md): planificatorul avansat folosește termenul măsurat, unde opțiunea este activată.
