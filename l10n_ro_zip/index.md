# Romania - Postal Codes (localizat la `l10n_ro_zip/index.md`)

- **Nume Tehnic:** `l10n_ro_zip`
- **Versiune:** `19.0.0.0.11`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_zip
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_zip`
- **Ultima Ingestie:** `2026-11-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă o bază de date cu codurile poștale din România, gata de folosit imediat după instalare. Sunt importate automat aproximativ 52.000 de coduri poștale, fiecare legat de județul și localitatea corespunzătoare, în marile orașe la nivel de stradă. La completarea adresei unui partener, utilizatorul caută strada în câmpul de cod poștal, iar codul, localitatea, județul și țara se completează automat. Astfel se elimină erorile de introducere manuală și se asigură date de adresă corecte, utile pentru livrări, facturare și e-Factura.

#### 2. Funcționalități Cheie

- Adaugă modelul `res.zip` cu ~52.000 de înregistrări de coduri poștale românești, fiecare conținând: cod poștal, localitate, județ, țară, tip stradă, nume stradă, sector (București), oficiu poștal și adresa oficiului.
- Datele sunt importate automat la instalare dintr-un fișier SQL, corelate cu județele și localitățile din `l10n_ro_city`, și se actualizează la upgrade printr-o migrare; partenerii își păstrează codul poștal. Ultima actualizare (19.0.0.0.11) aduce date reîmprospătate de pe posta-romana.ro pentru Sfântu Gheorghe, Bacău și Iași, plus străzi din OpenStreetMap (licență ODbL) pentru orașe mici, precum Huși, Negrești, Murgeni, Tecuci, Târgu Bujor și Berești.
- Consultare: *Contacts → Configuration → Localization → Zip Codes*, cu căutare după primele cifre ale codului.
- Extinde formularul partenerului (`res.partner`) cu câmpul `Cod Poștal (zip_id)`, sub localitate, filtrat după localitatea partenerului. La selecție completează codul poștal standard (`zip`), localitatea, județul și țara; strada și numărul adresei rămân cum au fost introduse. Dacă se schimbă localitatea ulterior, strada se alege din nou.
- Căutarea funcționează după codul numeric, după numele străzii sau după tipul străzii. Ordinea cuvintelor nu contează („Nicolae Balcescu" găsește „Balcescu Nicolae"), iar datele oficiului poștal nu au diacritice, deci căutarea fără diacritice este mai sigură.
- Lista derulantă arată strada și, estompat, codul poștal, localitatea, sectorul și județul.
- Suportă sectoarele municipiului București (1–6): localitatea este sectorul, iar câmpul **Sector** reține numărul lui.
- Pașii detaliați, cu capturi de ecran, sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base_address_extended`
- `l10n_ro_city`

#### 4. Componente Cheie

**Modele**

- `res.zip`: codul poștal, cu localitate, județ, țară, tip și nume de stradă, sector, oficiu și adresă. Căutarea după nume extinde domeniul standard la stradă și tip de stradă, cuvânt cu cuvânt.
- `res.partner`: extins cu `zip_id`; la selecție completează `zip`, localitatea, județul și țara.

**Vizualizări**

- `view_res_zip_form` / `view_res_zip_tree`: formularul și lista codurilor poștale, cu acțiunea `action_res_zip` și meniul *Zip Codes* sub *Contacts → Configuration → Localization*.
- `view_res_partner_form_inherit_zip`: adaugă câmpul de cod poștal pe formularul partenerului, în adresa extinsă.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`; datele se încarcă prin `post_init_hook` la instalare.

#### 5. Conexiuni

- `l10n_ro_city`: furnizează județele și localitățile cu care sunt corelate codurile poștale.
- `base_address_extended`: adresa extinsă a partenerului (localitate, stradă), în care se inserează câmpul de cod poștal.
