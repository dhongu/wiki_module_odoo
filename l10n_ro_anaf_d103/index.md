# Romania - ANAF D103 Declaration (localizat la `l10n_ro_anaf_d103/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d103`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d103](https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d103)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d103`
- **Ultima Ingestie:** `2026-07-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul generează exportul XML al Decontului lunar privind accizele (D103) direct din Odoo Enterprise, pentru antrepozitarii fiscali autorizați obligați să raporteze lunar la ANAF accizele datorate (Codul Fiscal Titlul VIII). Se așază peste infrastructura de accize din `l10n_ro_excise` (categorii de produse accizabile, marcarea produselor, cotele și modelul de declarație) și produce fișierul XML D103, gata de depus pe portalul ANAF.

#### 2. Funcționalități Cheie

- **Export XML D103**: generare fișier XML pentru decontul lunar, din liniile declarației de accize (categorie, cantitate, U.M., cotă, acciză), cu antet de identificare a companiei (CUI, denumire, lună, an).
- **Calcul automat al liniilor**: prin acțiunea „Calculează" a declarației, liniile sunt agregate per categorie de acciză din facturile postate ale perioadei (vânzări, cu storno pe note de credit).
- **Izolare față de D120**: exportul D103 folosește propriul template XML; decontul anual D120 este tratat de modulul-soră [l10n_ro_anaf_d120](../l10n_ro_anaf_d120/index.md), peste aceeași infrastructură [l10n_ro_excise](../l10n_ro_excise/index.md).

#### 3. Dependențe

- [l10n_ro_excise](../l10n_ro_excise/index.md)
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.excise.declaration` (extins): adaugă metoda `_export_d103_xml()`, hook apelat de dispatcher-ul `export_to_xml` din `l10n_ro_excise` pentru declarațiile de tip `d103`. Construiește antetul (CUI, denumire companie, lună, an) și liniile (categorie, cantitate, U.M., acciză) din `line_ids`, randează template-ul QWeb XML, generează numele fișierului `D103_<CUI>_<AAAALL>.xml` și trece declarația din starea `confirmed` în `exported`.

**Vizualizări**

Nu adaugă vizualizări proprii; folosește formularul declarației de accize definit în `l10n_ro_excise`, unde butonul „Export XML" declanșează generarea specifică D103.

**Acțiuni Automate / Acțiuni Server**

Nu definește `ir.cron`, `base.automation` sau `ir.actions.server`. Singura piesă de date este template-ul QWeb `report/d103_xml_template.xml`, folosit doar pentru randarea conținutului XML al exportului.

#### 5. Conexiuni

- [l10n_ro_anaf_d120](../l10n_ro_anaf_d120/index.md): modul-soră care tratează decontul anual D120 peste aceeași infrastructură de accize.
- [l10n_ro_excise](../l10n_ro_excise/index.md): furnizează modelul `l10n.ro.excise.declaration`, categoriile de produse accizabile și dispatcher-ul `export_to_xml` extins de acest modul.
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună pentru declarațiile ANAF ale companiilor românești.
