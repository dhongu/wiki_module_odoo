# Romania - ANAF Partner Data for Odoo Online (localizat la `l10n_ro_anaf_partner_online/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_partner_online`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_anaf_partner_online
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_anaf_partner_online`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Completează partenerii români pe baza CUI-ului, folosind datele ANAF, inclusiv pe **Odoo Online**: modulul nu conține cod Python și se importă ca arhivă zip (Apps > Import Module). Interogarea propriu-zisă rulează în serviciul Terrabit, care întreabă ANAF și trimite datele înapoi în baza de date a clientului. Utilizatorul economisește munca de introducere manuală a denumirii, adresei sediului și a statutului fiscal al partenerilor.

#### 2. Funcționalități Cheie

- **Buton ANAF pe formularul partenerului:** lângă CUI (câmpul VAT), completează înainte de salvare denumirea, adresa sediului (județ, localitate, cod poștal), CUI-ul cu prefixul `RO` doar pentru plătitorii de TVA și telefonul. Butonul e ascuns pe contactele unei companii. Dacă browserul nu poate ajunge la serviciu, partenerul se salvează, iar interogarea rămâne în coadă.
- **Actualizare în masă:** *Acțiuni > Update from ANAF* pe o selecție de parteneri (și pe formularul partenerului); serviciul răspunde în câteva secunde, iar pe fiecare partener găsit se postează o notă în chatter cu modificările urmărite. Partenerii fără CUI sunt ignorați. Răspunsul se scrie doar dacă utilizatorul care a trimis cererea poate edita partenerul și acesta are încă același CUI.
- **Statut ANAF pe partener (fila ANAF):** plătitor de TVA, inactiv fiscal, radiat, nr. de înregistrare la registrul comerțului (J…) și data ultimei verificări. Fila apare după prima verificare.
- **Activare dintr-un clic:** *Contacte > Configurare > ANAF > ANAF Service*, butonul **Activate**; tokenul serviciului se scrie automat în baza de date, cu interogări de probă gratuite. Pe același ecran: **Buy Credits** și **Refresh Credits**. Se consumă un credit per răspuns ANAF (firmă găsită sau negăsită); CUI invalid sau ANAF indisponibil nu se taxează.
- **Cine ce vede:** utilizatorii care editează parteneri (*Contact Creation*) pot citi contul de serviciu și folosesc butonul și acțiunea de actualizare. Doar administratorii activează serviciul, cumpără credite și văd cererile (*ANAF Requests*) cu răspunsurile lor.
- **Ce pleacă din baza de date:** CUI-ul căutat, tokenurile contului și ale cererii, id-ul cererii, UUID-ul și adresa bazei de date (pentru răspuns); la activare, și denumirea și CUI-ul companiei. Cererile, starea și erorile rămân vizibile în *ANAF Requests*.
- **Urmărirea cererilor:** lista arată tipul, numele (CUI-ul), starea și eroarea; cererile cu eroare sunt colorate în roșu. O cerere fără răspuns după 10 minute se retrimite o singură dată.
- **Incompatibil** cu `l10n_ro_partner_create_by_vat` și `l10n_ro_partner_autocomplete` (declarate în `excludes`; importul zip se oprește cu un mesaj de eroare dacă unul dintre ele e instalat).

Serviciul este oferit de Terrabit; după interogările de probă, creditele se cumpără de la Terrabit. Pașii detaliați, cu capturi, sunt în fișa consultantului.

#### 3. Dependențe

- `deltatech_iap_online`
- `contacts`

#### 4. Componente Cheie

Modulul nu are cod Python; folosește date și un widget JS.

**Modele**

- `res.partner` (extins prin câmpuri manuale `x_`): `x_anaf_vat_payer`, `x_anaf_inactive`, `x_anaf_struck_off`, `x_anaf_trade_register`, `x_anaf_last_check`, completate de serviciu.
- `x_iap_online_service` (din `deltatech_iap_online`): înregistrarea serviciului `anaf_partner_online`, definită în `data/iap_online_service_data.xml`.

**Vizualizări**

- `view_partner_form` (`res.partner.form.anaf.online`): adaugă butonul ANAF lângă CUI și fila **ANAF** pe formularul partenerului.
- `action_anaf_service` / `action_anaf_requests`: ecranele *ANAF Service* și *ANAF Requests* din *Contacte > Configurare > ANAF*.
- Widget JS `anaf_lookup_widget` (`static/src/js/anaf_lookup_widget.esm.js`): interoghează serviciul din browser și completează formularul.

**Acțiuni Automate / Acțiuni Server**

- `action_anaf_lookup_partners` (*Update from ANAF*): trimite cereri pentru partenerii selectați.
- `action_anaf_apply`: scrie răspunsul ANAF pe partener (apelată de serviciu).

#### 5. Conexiuni

- [l10n_ro_partner_autocomplete](../l10n_ro_partner_autocomplete/index.md): alternativă cu cod Python pentru completarea din ANAF; se exclud reciproc.
- `l10n_ro_partner_create_by_vat`: alternativă excluisă prin manifest.
