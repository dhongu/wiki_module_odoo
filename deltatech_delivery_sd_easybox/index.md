# Sameday Shipping EasyBox - Obsolete (localizat la `deltatech_delivery_sd_easybox/index.md`)

- **Nume Tehnic:** `deltatech_delivery_sd_easybox`
- **Versiune:** `19.0.0.0.23`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_sd_easybox
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_sd_easybox`
- **Ultima Ingestie:** `2026-11-15`

#### 1. Sumar

**Modul obsolet pe 19.0** (ascuns în Apps, dar încă instalabil). Alegerea lockerului în checkout este acum asigurată de [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md), cu harta Odoo de locații de ridicare alimentată din catalogul de lockere Sameday al [deltatech_delivery_sd](../deltatech_delivery_sd/index.md); pentru instalări noi se folosește acel modul. Acest modul rămâne doar pentru bazele de date care îl au deja instalat și poate fi dezinstalat după ce metoda de livrare în locker trece pe `deltatech_delivery_locker_website`. Modulul adaugă în checkout-ul magazinului online harta proprie Sameday cu lockerele Easybox: clientul apasă **Select Easybox**, alege un locker, iar lockerul devine adresa de livrare a comenzii, cu curierul Sameday setat pe coș. AWB-ul este emis apoi de `deltatech_delivery_sd` către acel Easybox.

#### 2. Funcționalități Cheie

- **Harta Sameday în checkout**: pluginul oficial Sameday pentru lockere se deschide într-o fereastră la pasul de livrare, deci clientul vede lockerele așa cum le arată Sameday.
- **Lockerul ca adresă de livrare**: Easybox-ul ales este salvat ca adresă de livrare sub un contact „Sameday EasyBoxs”, cu județul și localitatea potrivite cu agenda de adrese Odoo.
- **Curier setat automat**: pe comandă se setează curierul Sameday cu ID de client al hărții; dacă există mai mulți, cel deja de pe coș, altfel un curier de tip locker al companiei site-ului.
- **Doar pentru produse de locker**: butonul apare doar când toate produsele din coș pot fi livrate în locker (**Can be delivered in locker** pe produs).
- **Erori clare**: o selecție care nu poate fi citită readuce clientul în checkout cu un mesaj, nu pe o pagină de eroare.
- **Configurare**: se instalează și se configurează `deltatech_delivery_sd` (credențiale, **Initialization**, **Get city**); de la Sameday se cere ID-ul de client al pluginului hărții și se completează ca **Sd Client Id** în tabul **Sameday Configuration** al metodei de livrare (nu este credențială API); se bifează **Use Locker** și se alege un serviciu de locker (Locker NextDay); pe produsele care încap într-un Easybox se bifează **Can be delivered in locker**.
- **Date trimise către Sameday**: browserul clientului încarcă pluginul de pe serverele Sameday și primește ID-ul de client al hărții și utilizatorul API Sameday al curierului; datele comenzii și ale clientului nu se trimit la acest pas, ci odată cu AWB-ul, prin `deltatech_delivery_sd`.
- **Limitări**: harta se deschide pentru România, în limba română. Modulul este în stadiul `Beta` și nu a fost încă validat pe o bază de date de producție. Clasele CSS din modulele anterioare pentru butoanele de selecție nu mai sunt documentate în readme.

#### 3. Dependențe

- [deltatech_delivery_sd](../deltatech_delivery_sd/index.md)
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md)

#### 4. Componente Cheie

Secțiunile 1 și 2 provin din `readme/DESCRIPTION.md`, completat cu `CONFIGURE.md` și `USAGE.md`; componentele de mai jos au fost verificate în cod.

**Modele**

- `delivery.carrier` (extins): câmpul `sd_client_id` (ID-ul de client al hărții, trimis browserului, nu credențială API); `_get_credentials` îl expune sub cheia informativă `client_id`.
- `website` (extins): `_easy_box_carrier` alege curierul Sameday pentru hartă, `easy_box_client` întoarce parametrii hărții (țara `RO`, limba `ro`), iar `get_easy_box_partner` găsește sau creează lockerul ca partener de tip livrare (inactiv, sub „Sameday EasyBoxs”), cu județ și localitate căutate normalizat în nomenclator.
- `res.partner` „Sameday EasyBoxs” (`sameday_partner`): contactul-părinte al lockerelor, creat din date.

**Controlere**

- `WebsiteSaleEasyBoxAddresses` (extinde `WebsiteSale`): `/shop/easy_box_client` întoarce configurația hărții; `/shop/easy_box_set` setează lockerul ca adresă de livrare și aplică metoda de livrare pe coș, apoi redirecționează la checkout sau la `callback`; la erori redirecționează cu parametrul `easybox_error`.

**Vizualizări**

- `delivery_form` (moștenește `website_sale.delivery_form`): butonul **Select Easybox** și mesajul de eroare, vizibile doar când `for_locker` este adevărat.
- `view_delivery_carrier_form_with_provider_sd`: câmpul **Sd Client Id** în tabul de configurare Sameday al metodei de livrare.
- Active frontend: `easybox.esm.js` și `override.scss`.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server. Include o migrare `post-migration` pentru versiunea `19.0.0.0.17`, care a eliminat importul vechi de lockere.

#### 5. Conexiuni

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): catalogul de lockere (`delivery.locker`) folosit de înlocuitorul acestui modul.
- [deltatech_delivery](../deltatech_delivery/index.md): cadrul general de livrare peste care funcționează integrarea Sameday.
