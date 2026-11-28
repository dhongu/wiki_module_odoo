# Chatter Quick Info

- **Nume Tehnic:** `deltatech_chatter_quick_info`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_chatter_quick_info
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chatter_quick_info`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Afișează panouri de informații live în partea de sus a chatterului oricărui document: cifrele de care utilizatorul are nevoie cât timp privește documentul, calculate la deschidere, fără câmpuri noi în formular și fără a părăsi înregistrarea. Modulul este cadrul (framework-ul); panourile propriu-zise vin din alte module.

#### 2. Funcționalități Cheie

- Fiecare panou are un antet cu insignă (cifra-cheie), un rând de chip-uri (fapte scurte) și, opțional, un tabel cu link-uri către înregistrările legate.
- Panourile se pliază/desfac dintr-un clic și își rețin starea per utilizator; un panou se poate reîmprospăta singur cât timp documentul rămâne deschis.
- Configurare în *Settings > Technical > User Interface > Chatter Quick Info* (mod dezvoltator), per panou:
  - **Groups**: doar membrii lor văd panoul (gol: orice utilizator care poate citi documentul);
  - **Sequence**: ordinea panourilor;
  - **Refresh Interval (s)**: reîncărcare periodică (`0`: doar la modificarea documentului sau cu butonul de reîmprospătare);
  - **Folded by Default**: panoul se deschide pliat;
  - **Condition**: domeniu care limitează panoul la anumite documente (ex. doar cele deschise).
- Arhivarea unui panou îl ascunde pentru toți.

#### 3. Dependențe

- `mail`

#### 4. Componente Cheie

**Modele**

- `chatter.quick.info`: definiția unui panou (model, metodă, grupuri, secvență, interval de reîmprospătare, condiție).

**Vizualizări**

- `view_chatter_quick_info_list`, `view_chatter_quick_info_form`, `view_chatter_quick_info_search`: administrarea panourilor.
- Componenta de chatter din `static/src` care randează panourile.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_chatter_quick_info_purchase](../deltatech_chatter_quick_info_purchase/index.md): panoul *Product sales* pe facturi furnizor și comenzi de achiziție.
- [deltatech_chatter_quick_info_sale](../deltatech_chatter_quick_info_sale/index.md): panoul cu ultimul preț către client pe oferte.
- [deltatech_chatter_quick_info_stock](../deltatech_chatter_quick_info_stock/index.md): panoul de stoc și rezervări pe transferuri.
- [deltatech_chatter_quick_info_pack](../deltatech_chatter_quick_info_pack/index.md): instalează cele trei panouri odată.
