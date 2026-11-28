# Vehicle Catalog: Cars

- **Nume Tehnic:** `deltatech_vehicle_catalog_auto`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_vehicle_catalog_auto
- **Cale Locală:** `odoo-addons/bitshop/deltatech_vehicle_catalog_auto`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Catalog comun de autovehicule pentru modulul de compatibilități cu vehicule ([deltatech_vehicle_fitment](../deltatech_vehicle_fitment/index.md)), încărcat o singură dată, în loc să fie introdus din nou pentru fiecare magazin de piese și accesorii auto. Conține tipuri de vehicule, mărci cu ortografiile lor alternative și seriile principale.

#### 2. Funcționalități Cheie

- **4 tipuri de vehicule**: autoturism, SUV, vehicul comercial ușor, camion.
- **66 de mărci** de autoturisme, SUV-uri, furgonete și camioane, fiecare cu tipurile sale și cu **celelalte denumiri** folosite în magazine și în liste de piese (VW, MERCEDES, SKODA, CITROEN, SSANG YONG…), pe care detecția categoriei și importurile le folosesc pentru a recunoaște marca.
- **Peste 440 de serii**, modelele pe care le numesc clienții (Dacia Logan, Duster; Volkswagen Golf, Passat, Tiguan; Peugeot 308, 3008, Partner; Mercedes-Benz C-Class, Sprinter, Actros ș.a.), fiecare cu tipul său.
- Mărcile și seriile sunt scrise ca în selectoarele de vehicule ale magazinelor românești de accesorii auto, deci un import care citește un asemenea selector le găsește, în loc să le creeze din nou.
- **Înregistrările existente sunt reutilizate**: un tip, o marcă sau o serie deja existentă (creată manual sau prin import, cu același nume sau cu o denumire alternativă) este completată, nu duplicată. Denumirile alternative și tipurile doar se adaugă, niciodată nu se șterg, deci o nouă încărcare păstrează modificările utilizatorilor.
- **Fără configurare**: catalogul se încarcă la instalare. După o actualizare care aduce mărci sau serii noi se rulează *Vânzări > Configurare > Vehicule > Update Car Catalog*; o notificare arată ce s-a adăugat. Generațiile (de ex. Golf VIII) vin din importurile fiecărui magazin.
- Pașii, cu capturi, sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_vehicle_fitment](../deltatech_vehicle_fitment/index.md)

#### 4. Componente Cheie

**Modele**

- `vehicle.catalog.auto` (model abstract): încarcă tipurile, mărcile și seriile din `tools/catalog_data.py`, reutilizând înregistrările existente.

**Vizualizări**

- Meniul și acțiunea de server **Update Car Catalog**, sub *Vânzări > Configurare > Vehicule*.

**Acțiuni Automate / Acțiuni Server**

- Acțiunea de server **Update Car Catalog**: reîncarcă catalogul la cerere. La instalare, catalogul este încărcat de `post_init_hook`.

#### 5. Conexiuni

- [deltatech_vehicle_catalog_agri](../deltatech_vehicle_catalog_agri/index.md): catalogul pereche, pentru utilaje agricole.
