# Purchase Stock

- **Nume Tehnic:** `deltatech_purchase_stock`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_stock
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_stock`
- **Ultima Ingestie:** `2026-11-13`

#### 1. Sumar

Reaprovizionarea poate adăuga liniile sale într-o comandă de achiziție ciornă existentă a furnizorului, inclusiv într-una pe care un agent de achiziții o pregătește manual. Modulul marchează comenzile de achiziție create de reaprovizionare și o împiedică să folosească orice altă comandă, astfel încât comenzile întocmite manual să rămână separate de cele generate automat.

#### 2. Funcționalități Cheie

- **Marcaj de reaprovizionare:** comenzile de achiziție create de o regulă de stoc, de exemplu dintr-o regulă de reaprovizionare (reordering rule), primesc automat marcajul `from_replenishment`.
- **Comenzile manuale rămân curate:** căutarea unei comenzi existente în care să se adauge linii primește o condiție în plus — comanda trebuie să poarte marcajul. Comenzile fără marcaj nu sunt niciodată folosite.
- **Reaprovizionările se contopesc în continuare:** nevoile succesive de reaprovizionare ale aceluiași furnizor merg în aceeași comandă marcată, așa cum verifică testele modulului.
- **Comenzi existente:** comenzile create înainte de instalare nu au marcaj, deci reaprovizionarea nu adaugă linii în ele.
- **Fără ecran:** modulul nu adaugă vizualizări, meniuri sau setări, iar marcajul nu apare pe formularul comenzii de achiziție.
- **Limitare:** marcajul nu se șterge niciodată, deci o comandă marcată rămâne deschisă pentru reaprovizionare chiar dacă un agent adaugă ulterior linii manual.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): câmpul boolean `from_replenishment`, care marchează comenzile generate printr-o regulă de stoc.
- `stock.rule` (extins): `_prepare_purchase_order` setează `from_replenishment = True` pe comenzile create de regulile de stoc, iar `_make_po_get_domain` adaugă condiția `from_replenishment = True` la căutarea comenzilor ciornă existente.

**Vizualizări**

- Modulul nu adaugă vizualizări proprii (lista `data` din manifest este goală); câmpul `from_replenishment` nu este afișat.

**Acțiuni Automate / Acțiuni Server**

- Nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- `purchase_stock`: modulul standard ale cărui reguli de stoc (`stock.rule`) creează comenzile de achiziție de reaprovizionare, a căror grupare o restrânge acest modul.
