# Chatter Quick Info: Pack

- **Nume Tehnic:** `deltatech_chatter_quick_info_pack`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_chatter_quick_info_pack
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chatter_quick_info_pack`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modul-pachet care instalează dintr-un pas cele trei panouri de informații din chatter: cifrele de care utilizatorul are nevoie când privește o achiziție, o ofertă sau un transfer, chiar lângă document. Nu are cod propriu.

#### 2. Funcționalități Cheie

- Include trei panouri: **Product sales** pe facturi furnizor și comenzi de achiziție (cât din produsele cumpărate s-a vândut, cu produsele nevândute); **Last price to the customer** pe oferte (fiecare linie comparată cu ultimul preț vândut aceluiași client, prețurile mai mici în roșu); **Stock and reservations** pe transferuri (ce nu e acoperit, ce transferuri țin stocul, marfa în intrare, iar la recepții livrările care o așteaptă).
- Toate se bazează pe *Chatter Quick Info*, instalat odată cu ele; în *Settings > Technical > User Interface > Chatter Quick Info* se alege cine vede fiecare panou, pe ce documente și cât de des se reîmprospătează.
- Se instalează și *Sales*, *Purchase*, *Invoicing* și *Inventory*, dacă lipsesc.
- Instalare: din **Apps**; apoi panoul apare în chatter pentru utilizatorii grupului potrivit (achiziții, vânzări, inventar). Dezinstalarea pachetului nu dezinstalează modulele incluse.

#### 3. Dependențe

- [deltatech_chatter_quick_info_purchase](../deltatech_chatter_quick_info_purchase/index.md)
- [deltatech_chatter_quick_info_sale](../deltatech_chatter_quick_info_sale/index.md)
- [deltatech_chatter_quick_info_stock](../deltatech_chatter_quick_info_stock/index.md)

#### 4. Componente Cheie

**Modele**

- Fără cod propriu.

**Vizualizări**

- Nu are vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_chatter_quick_info](../deltatech_chatter_quick_info/index.md): cadrul pe care se bazează cele trei panouri (dependență tranzitivă).
