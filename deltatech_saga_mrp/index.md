# SAGA Interface MRP Extension (localizat la `deltatech_saga_mrp/index.md`)

- **Nume Tehnic:** `deltatech_saga_mrp`
- **Versiune:** `19.0.0.0.14`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_saga_mrp
- **Cale Locală:** `odoo-addons/bitshop/deltatech_saga_mrp`
- **Ultima Ingestie:** `2026-11-10`

#### 1. Sumar

Modulul adaugă kiturile (liste de materiale de tip *Kit*) în exportul către SAGA din modulul *SAGA Interface*. În Odoo, un kit se vinde ca un singur produs, dar se livrează prin componentele sale, în timp ce SAGA are nevoie de kitul însuși în stoc ca să îl poată factura. Pentru fiecare kit livrat în perioadă, modulul exportă consumul componentelor și producția kitului, astfel încât SAGA să primească aceleași mișcări de stoc ca Odoo.

#### 2. Funcționalități Cheie

- **Consum de componente:** mișcările de stoc finalizate ale componentelor unui kit, din perioada și compania exportului, ajung într-un fișier de consum (*BC_KIT_*).
- **Producție de kituri:** pentru fiecare transfer, cantitatea fiecărui kit se calculează din componente și ajunge într-un fișier de producție (*PRODUCTIE_KIT_*), cu cod, unitate de măsură, cost și gestiunea SAGA a locației.
- **Varianta corectă:** un kit definit pe un șablon de produs și partajat de mai multe variante se exportă pentru varianta vândută sau cumpărată efectiv, numărând doar componentele aplicabile ei.
- **Unități de măsură convertite:** cantitățile componentelor și ale kitului se convertesc între unitățile mișcărilor, ale listei de materiale și ale produsului (ex. un kit care cere 2 duzini, livrat ca 24 de bucăți, contează ca un kit).
- **Retururi incluse:** componentele care revin în stoc se contorizează ca producție negativă de kit.
- **Flux de utilizare:** exportul se rulează ca de obicei din *Contabilitate > Contabilitate > Saga > Export Saga*; arhiva conține în plus fișierele *BC_KIT_* și *PRODUCTIE_KIT_*, iar sumarul exportului arată câte kituri și câte consumuri de componente au fost exportate. Cele două fișiere se importă în SAGA împreună cu restul exportului, ca kiturile să fie în stoc la importul facturilor de vânzare.
- **Configurare necesară:** modulul *SAGA Interface* configurat (coduri SAGA pe categorii și gestiuni pe locații); fiecare kit și componentă are **Referință internă** (codul SAGA) și categorie de produs cu **Cod SAGA** (altfel linia apare ca eroare sau blochează exportul când **Ignoră erorile** e dezactivat); costul kiturilor trebuie ținut la zi, producția fiind evaluată la costul curent.
- **Doar format DBF:** fișierele de kit se scriu numai în DBF, deci în exportul SAGA trebuie bifat **Format DBF**.
- **Fără date trimise în exterior:** modulul doar adaugă fișiere în arhiva exportului, pe care utilizatorul o importă singur în SAGA.

Cerințe: modulul *SAGA Interface* (`deltatech_saga`) configurat și aplicația Fabricație (`mrp`) pentru listele de materiale.

#### 3. Dependențe

- [deltatech_saga](../deltatech_saga/index.md)
- `mrp`

#### 4. Componente Cheie

**Modele**

- `export.saga` (extindere, `wizard/export_saga.py`): adaugă la colectarea datelor de export identificarea mișcărilor de stoc (`stock.move`) legate de linii de BoM (`bom_line_id`) de tip `phantom` (kituri), le grupează pe transfer (`picking_id`) și produs, calculând cantitățile consumate/produse proporțional cu rețeta; adaugă statistici de export (nr. kituri, nr. consumuri) și exportă fișierele în arhiva ZIP (`do_export_productions_kit`).
- `export.saga.models` (extindere, `wizard/export_saga_models.py`): construiește înregistrările de „producție” pentru fiecare kit (`_export_production_kit`), validând codul SAGA al categoriei de produs (`code_saga`), determinând gestiunea (locația de stoc) și calculând valoarea (cantitate x cost) pentru fișierul DBF.

**Vizualizări**

- Nu sunt definite vizualizări proprii (`"data": []` în manifest); se reutilizează wizard-ul de export din `deltatech_saga`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`; exportul se declanșează manual din wizard-ul de export SAGA.

#### 5. Conexiuni

- [deltatech_saga](../deltatech_saga/index.md): modulul de bază peste care se grefează, oferind wizard-ul și infrastructura de export (scriitor DBF, parametri de export).
- `mrp`: sursa listelor de materiale de tip kit (`phantom`).
- `stock`: furnizează `stock.move`, folosit pentru identificarea și calculul consumurilor/producțiilor de kituri.
