# Vehicle Fitment

- **Nume Tehnic:** `deltatech_vehicle_fitment`
- **Versiune:** `20.0.1.2.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_vehicle_fitment
- **Cale Locală:** `odoo-addons/bitshop/deltatech_vehicle_fitment`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Permite clienților și vânzătorilor să găsească piesele de schimb care se potrivesc unui anumit vehicul sau utilaj: un tractor, o combină, un autoturism sau o furgonetă. Este baza selectorului de vehicul din magazin (marcă → model → motor) și a importurilor de compatibilități.

#### 2. Funcționalități Cheie

- **Catalog de vehicule**: mărci, serii (sau generații) și modele, cu tip de vehicul, ani de producție și atribute libere (motor, caroserie, locuri…).
- **Compatibilități**: legarea unui produs de o marcă, o serie sau un model. O piesă legată de o serie se potrivește tuturor modelelor seriei; una legată de marcă, tuturor modelelor ei.
- **Restricții opționale** pe o compatibilitate: anii de producție și valorile atributelor (de ex. doar pentru motorul FPT 10.3), în coloana **Only for**.
- **Piese universale și consumabile** („Fits All Vehicles”), afișate pentru orice vehicul.
- **Căutare de produse** după marca, seria sau modelul căruia i se potrivesc, din lista de produse și din formularele de marcă, serie și model (butonul **Parts**); filtrele *Fits All Vehicles* și *Without Vehicles* găsesc produsele universale, respectiv nelegate.
- Fiecare compatibilitate își păstrează **sursa** (manual, import, feed furnizor, categorie de produs, denumire produs, cod OEM, sugestie AI) și un indicator **Verified**: importurile ulterioare nu suprascriu și nu șterg liniile confirmate de o persoană. În *Vânzări > Produse > Vehicle Fitments* se văd toate liniile, cu **Level**, **Source** și **Verified**, filtrul *To Verify* și gruparea după sursă.
- **Termen românesc configurabil**: *utilaj* (implicit, pentru mașini agricole) sau *vehicul* (magazine de piese auto), din *Vânzări > Configurare > Setări > Catalog de produse > Romanian Term for Vehicles*; alegerea se aplică tuturor modulelor de vehicule instalate care au varianta (`i18n_extra/ro_vehicul.po`) și se reaplică la fiecare instalare sau actualizare de modul.
- **Configurare** (*Vânzări > Configurare > Vehicule*): Vehicle Types, Vehicle Attributes, apoi Vehicle Brands, Vehicle Series (opțional) și Vehicle Models. Catalogul se editează cu grupul *Sales / Administrator*, iar compatibilitățile cu *Sales / User*.
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `vehicle.type`: tipul vehiculului (tractor, autoturism, SUV…).
- `vehicle.brand`: marca, cu tipurile și celelalte denumiri.
- `vehicle.series`: seria sau generația unei mărci.
- `vehicle.model`: modelul, cu ani de producție și atribute.
- `vehicle.attribute` și `vehicle.attribute.value`: caracteristicile care disting variantele aceluiași model (motor, caroserie).
- `vehicle.fitment`: legătura produs - marcă/serie/model, cu nivel, sursă, restricții și indicatorul Verified.
- `product.template` și `product.product` (extinse): tab-ul **Vehicles**, „Fits All Vehicles” și căutarea după vehicul.
- `res.config.settings` și `ir.module.module` (extinse): setarea termenului românesc și reaplicarea ei după instalare/actualizare.

**Vizualizări**

- Formulare și liste pentru tipuri, mărci, serii, atribute, modele și compatibilități (`views/vehicle_*_views.xml`), meniurile sub *Vânzări > Configurare > Vehicule* și tab-ul **Vehicles** din produs.
- Secțiunea **Product Catalog** din setările Vânzărilor, cu termenul românesc.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni automate sau acțiuni server. Drepturile sunt în `security/ir.access.csv`.

#### 5. Conexiuni

- [deltatech_vehicle_catalog_auto](../deltatech_vehicle_catalog_auto/index.md): catalog încărcat de autoturisme, SUV-uri, utilitare și camioane.
- [deltatech_vehicle_catalog_agri](../deltatech_vehicle_catalog_agri/index.md): catalog încărcat de utilaje agricole.
