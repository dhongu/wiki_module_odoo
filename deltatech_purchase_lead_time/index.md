# Measured Vendor Lead Time (Termen de livrare măsurat al furnizorului)

- **Nume Tehnic:** `deltatech_purchase_lead_time`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_purchase_lead_time
- **Cale Locală:** `odoo-addons/bitshop/deltatech_purchase_lead_time`
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Modulul măsoară termenul real de livrare al furnizorilor pe baza istoricului de achiziții, în loc să se bazeze doar pe „Termen de livrare” introdus manual pe lista de prețuri a furnizorului. Pentru fiecare linie de furnizor se calculează valori statistice (mediană, percentilă, abatere), iar sursa valorii este mereu afișată, astfel încât o valoare estimată să nu fie prezentată drept măsurată. Modulul nu modifică nimic de la sine: valorile sunt informative, iar instrumentele de planificare le folosesc doar acolo unde opțiunea este activată.

#### 2. Funcționalități Cheie

- **Observație** = o linie de comandă de achiziție confirmată și recepționată de la furnizor: zilele calendaristice de la confirmarea comenzii până la prima recepție. Recepțiile parțiale ulterioare (backorder) nu o prelungesc; retururile și comenzile altor companii nu se numără.
- Pentru fiecare linie din lista de prețuri a furnizorului se calculează:
  - **mediana** și o **percentilă** configurabilă (implicit P80) a termenelor observate;
  - **abaterea** (σ) a termenului, intrare pentru un stoc de siguranță care acoperă livrările întârziate;
  - **numărul de observații** din spatele valorilor.
- Valorile vin de la cel mai specific nivel cu istoric suficient: furnizor + produs, apoi furnizor pe toate produsele lui, altfel termenul configurat. Sursa (măsurat pe produs / măsurat pe furnizor / configurat) este afișată.
- Pe produs, fila **Achiziție**, la linia furnizorului, sub **Termen de livrare** apare **Termen de livrare măsurat**, cu sursa, numărul de observații, mediana și abaterea.
- În listele de prețuri ale furnizorilor, coloanele opționale **Termen de livrare măsurat**, **Sursa termenului** și **Observații termen** pot fi adăugate.
- Configurare în **Achiziții > Configurare > Setări**, secțiunea **Measured Vendor Lead Time**:
  - **Percentila termenului** (implicit 80): ponderea recepțiilor trecute sosite în termenul măsurat; P50 este mediana, o percentilă mai mare dă un termen mai prudent;
  - **Observații minime** (implicit 5): liniile recepționate necesare înainte ca valoarea măsurată să o înlocuiască pe cea configurată.
- Fereastra de istoric este cea a ratei de livrare la timp a furnizorului: parametrul de sistem `purchase_stock.on_time_delivery_days` (365 de zile implicit).
- Utilizare recomandată: comparați valoarea măsurată cu cea configurată și corectați termenul configurat când nu mai corespunde realității, sau activați termenul măsurat în instrumentele de planificare.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `purchase.vendor.lead.time` (model abstract): calculează observațiile (interogare SQL pe liniile de comandă confirmate și mișcările de stoc „done” din locația furnizor), setările și sintetizarea (mediană, percentilă, abatere).
- `product.supplierinfo` (extins): câmpurile calculate `measured_lead_time`, `measured_lead_time_median`, `measured_lead_time_sigma`, `measured_lead_time_count`, `measured_lead_time_source`.
- `res.config.settings` (extins): percentila și numărul minim de observații.

**Vizualizări**

- `product_supplierinfo_form_view`: moștenește formularul liniei de furnizor și adaugă termenul măsurat.
- `product_supplierinfo_tree_view`: coloane opționale în lista liniilor de furnizor.
- `res_config_settings_view_form`: secțiunea de setări din Achiziții.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_nap](../deltatech_nap/index.md): raportul de necesar de achiziție (NAP) depinde de acest modul și folosește termenul măsurat acolo unde opțiunea este activată.
- [deltatech_advanced_planner](../deltatech_advanced_planner/index.md): planificatorul avansat depinde de acest modul și folosește termenul măsurat acolo unde opțiunea este activată.
