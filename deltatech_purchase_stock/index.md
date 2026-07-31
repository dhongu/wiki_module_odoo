# Purchase Stock (localizat la `deltatech_purchase_stock/index.md`)

- **Nume Tehnic:** `deltatech_purchase_stock`
- **Versiune:** `19.0.1.0.1`
- **Cale:** [https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_stock](https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_stock)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_stock`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul separă comenzile de achiziție create automat prin reaprovizionare (replenishment) de cele create manual de un agent de achiziții. Fără el, cu opțiunea `group_rfq = Always` de pe partenerul furnizor, Odoo standard ar amesteca liniile de reaprovizionare în orice comandă de achiziție ciornă existentă a aceluiași furnizor — inclusiv cele întocmite manual — ceea ce ar putea denatura o comandă pe care un agent de achiziții o pregătește cu atenție.

#### 2. Funcționalități Cheie

- Separă comenzile de achiziție manuale de comenzile de achiziție generate prin reaprovizionare (replenishment).

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `purchase.order`: adaugă câmpul boolean `from_replenishment`, care marchează dacă o comandă a fost generată automat printr-o regulă de reaprovizionare.
- `stock.rule`: suprascrie `_prepare_purchase_order` pentru a seta `from_replenishment = True` pe comenzile create de regulile de stoc, și `_make_po_get_domain` pentru a restrânge căutarea/gruparea comenzilor ciornă existente doar la cele cu `from_replenishment = True` — astfel o nouă nevoie de reaprovizionare nu se mai grupează niciodată într-o comandă ciornă creată manual.

**Vizualizări**

- Modulul nu adaugă vizualizări proprii (nu are date XML în `data`); câmpul `from_replenishment` nu este expus într-o vizualizare dedicată.

**Acțiuni Automate / Acțiuni Server**

- Nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_auto_reorder_rule](../deltatech_auto_reorder_rule/index.md): regulile de reordonare create automat de acest modul pentru fiecare produs nou sunt reutilizate de fluxul de reaprovizionare pe care `deltatech_purchase_stock` îl izolează de comenzile manuale (relevant și pentru teste, unde o singură regulă e permisă per produs/locație/companie).
