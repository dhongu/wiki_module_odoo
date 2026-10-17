# Chatter Quick Info: Pack (localizat la `deltatech_chatter_quick_info_pack/index.md`)

- **Nume Tehnic:** `deltatech_chatter_quick_info_pack`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_chatter_quick_info_pack
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chatter_quick_info_pack`
- **Ultima Ingestie:** `2026-10-17`

#### 1. Sumar

Modul-pachet care instalează dintr-un singur pas trei panouri informative afișate în chatter, lângă document: cifrele de care utilizatorul are nevoie când se uită la o achiziție, o ofertă sau un transfer. Modulul nu are cod propriu; instalarea lui aduce, dacă lipsesc, și aplicațiile Vânzări, Achiziții, Facturare și Inventar.

#### 2. Funcționalități Cheie

- **Vânzări produs** (din `deltatech_chatter_quick_info_purchase`), pe facturi furnizor și comenzi de achiziție: cât din produsele cumpărate s-a vândut de la data documentului și în total, plus produsele care nu s-au vândut.
- **Ultimul preț către client** (din `deltatech_chatter_quick_info_sale`), pe oferte: fiecare linie este comparată cu ultimul preț vândut aceluiași client; prețurile mai mici apar cu roșu.
- **Stoc și rezervări** (din `deltatech_chatter_quick_info_stock`), pe transferuri: ce nu este acoperit, ce transferuri ține stocul rezervat, marfa în intrare și, la recepții, livrările care o așteaptă.
- Toate trei se bazează pe *Chatter Quick Info*, instalat odată cu ele; din *Setări > Tehnic > Interfață utilizator > Chatter Quick Info* se alege cine vede fiecare panou, pe ce documente (condiție) și cât de des se reîmprospătează.
- Panoul apare în partea de sus a chatterului pentru utilizatorii grupului potrivit (achiziții, vânzări, inventar).
- Dezinstalarea pachetului nu dezinstalează modulele incluse.

#### 3. Dependențe

- [deltatech_chatter_quick_info_purchase](../deltatech_chatter_quick_info_purchase/index.md)
- [deltatech_chatter_quick_info_sale](../deltatech_chatter_quick_info_sale/index.md)
- [deltatech_chatter_quick_info_stock](../deltatech_chatter_quick_info_stock/index.md)

#### 4. Componente Cheie

**Modele**

Modulul nu definește modele proprii (pachet fără cod).

**Vizualizări**

Nu definește vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

Nu definește.

#### 5. Conexiuni

- [deltatech_chatter_quick_info](../deltatech_chatter_quick_info/index.md): modulul de bază al panourilor, adus tranzitiv de cele trei module incluse.
- `purchase`, `sale`, `account`, `stock`: aplicațiile standard pe care se afișează panourile, aduse tranzitiv.
