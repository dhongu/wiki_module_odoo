# Chatter Quick Info

- **Nume Tehnic:** `deltatech_chatter_quick_info`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_chatter_quick_info
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chatter_quick_info`
- **Ultima Ingestie:** `2026-10-17`

#### 1. Sumar

Afișează în partea de sus a chatterului, pe orice document, panouri cu informații actualizate la zi: cifrele de care utilizatorul are nevoie cât timp se uită la document, calculate la deschiderea acestuia, fără câmpuri noi pe formular și fără a părăsi înregistrarea. Modulul este cadrul comun (framework): panourile propriu-zise vin din alte module, iar aici se stabilește cine le vede, în ce ordine apar și cât de des se reîmprospătează.

#### 2. Funcționalități Cheie

- Fiecare panou are un antet cu o insignă (cifra-cheie), un rând de etichete scurte cu fapte și, opțional, un tabel cu link-uri către înregistrările asociate.
- Panourile se pliază și se desfac cu un click, iar starea este reținută separat pentru fiecare utilizator.
- Un panou se poate reîmprospăta singur cât timp documentul rămâne deschis (interval configurabil), sau manual cu butonul de reîmprospătare.
- Configurare din *Setări > Tehnic > Interfață utilizator > Chatter Quick Info* (mod dezvoltator), pentru fiecare panou:
  - **Grupuri**: doar membrii lor văd panoul; gol = toți utilizatorii care pot citi documentul;
  - **Secvență**: ordinea panourilor în chatter;
  - **Interval de reîmprospătare (s)**: `0` = doar la modificarea documentului sau la cerere;
  - **Pliat implicit**: panoul se deschide pliat până îl desface utilizatorul;
  - **Condiție**: domeniu care limitează afișarea la documentele potrivite (ex. doar documente deschise).
- Arhivarea unui panou îl ascunde pentru toți utilizatorii.
- Un panou defect nu blochează celelalte panouri și nici chatterul (eroarea este logată, iar panoul afișează o stare de eroare).
- Siguranță: doar metodele cu prefixul `_chatter_quick_info_` pot fi asociate unui panou, iar panoul rulează cu drepturile utilizatorului curent.

#### 3. Dependențe

- `mail`

#### 4. Componente Cheie

**Modele**

- `chatter.quick.info`: definiția unui panou (nume, model de document, metoda furnizoare, grupuri, secvență, interval de reîmprospătare, pliat implicit, condiție). Validează prefixul și existența metodei, precum și condiția. `get_user_models` returnează modelele cu panouri pentru utilizatorul curent, iar `get_panels` returnează datele panourilor unui document.

**Vizualizări**

- `view_chatter_quick_info_list` / `view_chatter_quick_info_form` / `view_chatter_quick_info_search`: administrarea panourilor (listă cu reordonare, formular, căutare cu grupare după model).
- `action_chatter_quick_info` și meniul `menu_chatter_quick_info`: acces din Setări > Tehnic > Interfață utilizator.
- Componenta front-end OWL `static/src/quick_info/` care randează panourile în chatter.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

Module-pachet care furnizează panourile (fără pagină wiki încă):

- [deltatech_chatter_quick_info_purchase](../deltatech_chatter_quick_info_purchase/index.md): panouri pentru achiziții (ex. vânzări de produs pe comenzi de achiziție).
- [deltatech_chatter_quick_info_sale](../deltatech_chatter_quick_info_sale/index.md): panouri pentru vânzări.
- [deltatech_chatter_quick_info_stock](../deltatech_chatter_quick_info_stock/index.md): panouri pentru stoc.
- [deltatech_chatter_quick_info_pack](../deltatech_chatter_quick_info_pack/index.md): pachet de panouri.
