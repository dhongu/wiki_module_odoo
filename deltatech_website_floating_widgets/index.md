# Website Floating Widgets (Butoane flotante pe site)

- **Nume Tehnic:** `deltatech_website_floating_widgets`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_floating_widgets
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_floating_widgets`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul adaugă pe site butoane de contact fixe, în marginea din dreapta, care rămân pe ecran indiferent cât derulează vizitatorul: telefon, e-mail, WhatsApp, rețele sociale sau orice altă adresă. Butoanele se configurează din backend, fără cod, iar fiecare are pictograma, culorile și forma proprii, ceea ce face contactarea firmei mai rapidă și păstrează aspectul site-ului în linie cu identitatea vizuală.

#### 2. Funcționalități Cheie

- Butoane personalizabile, afișate în dreapta site-ului; pictograma se alege dintr-o listă predefinită (Phone, Email, WhatsApp, Facebook, Instagram, TikTok, LinkedIn, Map Marker etc.), cu previzualizare live în formular.
- Tipuri de legătură: URL, telefon (`tel:`) sau e-mail (`mailto:`) — prefixul pentru telefon și e-mail este adăugat automat de modul.
- Pentru legăturile externe se introduce protocolul complet (ex. `https://`); altfel adresa este tratată ca legătură relativă în site.
- Opțiune de deschidere în filă nouă, per buton.
- Vizibilitate separată pe desktop și pe mobil.
- Formă a butonului: cerc, pătrat sau colțuri rotunjite; culoare de fundal și de text configurabile (implicit `#875A7B` / `#FFFFFF`).
- Ordinea se stabilește prin secvență (drag and drop în listă); butoanele pot fi dezactivate (arhivate) fără ștergere.
- Configurare din meniul Site → Floating Widgets (`website.menu_site`).

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

**Modele**

- `website.floating.widget`: un buton flotant (nume, pictogramă, legătură, tip, filă nouă, secvență, afișare mobil/desktop, culori, formă). Metoda `get_link()` construiește adresa finală (`tel:`, `mailto:` sau URL).

**Vizualizări**

- `website_floating_widget_view_list` / `website_floating_widget_view_form`: listă și formular de configurare, cu previzualizarea pictogramei.
- `website_floating_widget_action` și meniul `menu_website_floating_widget`: acces din Site.
- `floating_widgets` (template, moștenește `website.layout`): randează butoanele active după `#wrapwrap`; ascunderea pe desktop/mobil se face cu clase Bootstrap. Stilurile sunt în `static/src/scss/floating_widgets.scss` (`web.assets_frontend`).

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `website`: modulul extinde layout-ul site-ului. Butoanele nu sunt legate de un site anume, ci apar pe toate site-urile (căutarea nu filtrează după website).
