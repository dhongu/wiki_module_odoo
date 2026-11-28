# Vehicle Catalog: Agricultural Machines

- **Nume Tehnic:** `deltatech_vehicle_catalog_agri`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_vehicle_catalog_agri
- **Cale Locală:** `odoo-addons/bitshop/deltatech_vehicle_catalog_agri`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Catalog comun de utilaje agricole pentru modulul de compatibilități cu vehicule ([deltatech_vehicle_fitment](../deltatech_vehicle_fitment/index.md)), încărcat o singură dată, în loc să fie introdus din nou pentru fiecare magazin. Conține tipuri de utilaje, mărci cu ortografiile lor alternative și seriile principale.

#### 2. Funcționalități Cheie

- **26 de tipuri de utilaje**: tractor, combină, mașină de recoltat furaje, balotieră, cositoare, greblă și răsturnător, headere pentru cereale și porumb, plug, grapă cu discuri și rotativă, cultivator, semănători, împrăștietoare de îngrășăminte și de gunoi, mașină de stropit, tocător, remorcă agricolă, manitou, utilaj de construcții, motor.
- **200 de mărci** de tractoare, combine, utilaje purtate, mașini de manipulare și construcții și motoare, fiecare cu tipurile sale și cu **celelalte denumiri** folosite în magazine și în liste de piese (CASE-IH, INTERNATIONAL CASE IH, MF, KUHN HUARD…), pe care detecția categoriei și importurile le folosesc pentru a recunoaște marca.
- **Peste 370 de serii**, familiile pe care le numesc clienții (Claas Lexion, Tucano, Dominator, Jaguar; Case IH Puma, Maxxum, Axial-Flow; New Holland T6, CX, CR; John Deere 6R, S; Lemken Juwel; Amazone Cirrus ș.a.), fiecare cu tipul său.
- Catalogul provine din listele de mărci ale dealerilor și magazinelor de piese din România și din mărcile și seriile găsite în magazinele clienților; camioanele și autoturismele sunt excluse.
- **Înregistrările existente sunt reutilizate**: un tip, o marcă sau o serie deja existentă (creată manual sau prin import, cu același nume sau cu o denumire alternativă) este completată, nu duplicată. Denumirile alternative și tipurile doar se adaugă, niciodată nu se șterg, deci o nouă încărcare păstrează modificările utilizatorilor.
- **Fără configurare**: catalogul se încarcă la instalare. După o actualizare care aduce mărci sau serii noi se rulează *Vânzări > Configurare > Vehicule > Update Agricultural Machine Catalog*; o notificare arată ce s-a adăugat. Modelele (de ex. Lexion 570) vin din importurile fiecărui magazin.
- Pașii, cu capturi, sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_vehicle_fitment](../deltatech_vehicle_fitment/index.md)

#### 4. Componente Cheie

**Modele**

- `vehicle.catalog.agri` (model abstract): încarcă tipurile, mărcile și seriile din `tools/catalog_data.py` (metodele `load`, `action_load`), reutilizând înregistrările existente.

**Vizualizări**

- Meniul și acțiunea de server `action_load_agri_catalog` (**Update Agricultural Machine Catalog**), sub *Vânzări > Configurare > Vehicule*.

**Acțiuni Automate / Acțiuni Server**

- `action_load_agri_catalog`: reîncarcă catalogul la cerere. La instalare, catalogul este încărcat de `post_init_hook`.

#### 5. Conexiuni

- [deltatech_vehicle_catalog_auto](../deltatech_vehicle_catalog_auto/index.md): catalogul pereche, pentru autoturisme, SUV-uri, utilitare și camioane.
