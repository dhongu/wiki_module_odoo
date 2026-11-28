# Partner GLN (localizat la `deltatech_gln/index.md`)

- **Nume Tehnic:** `deltatech_gln`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_gln
- **Cale Locală:** `odoo-addons/deltatech/deltatech_gln`
- **Ultima Ingestie:** `2026-11-28`

> **Notă:** Conform documentației modulului, acesta este considerat **Obsolet** (*deprecated*). Funcționalitatea sa de bază a fost mutată și este acum mai bine acoperită de modulul `account_add_gln`. Pentru proiecte noi se recomandă utilizarea directă a `account_add_gln`. Modulul nu va fi migrat la versiunea 20.0, unde GLN face parte din `account`.

#### 1. Sumar

Acest modul a fost conceput pentru a gestiona Numărul Global de Locație (GLN — Global Location Number) la nivel de parteneri în Odoo, pentru schimbul electronic de date (EDI) și pentru procesele logistice. În prezent este marcat ca **obsolet**: GLN-ul este preluat de câmpul standard din `account_add_gln`, iar `deltatech_gln` rămâne doar ca punte de compatibilitate pentru configurațiile mai vechi care încă citesc sau scriu vechiul câmp `gln`.

#### 2. Funcționalități Cheie

- **Câmp `gln` ca punte către câmpul standard** (din 19.0.1.2.0): `gln` este un câmp relat (editabil) pe `global_location_number` din `account_add_gln`, fără coloană proprie; citirea sau scrierea lui `gln` citește sau scrie GLN-ul standard. Codul și datele care folosesc încă `gln` continuă să funcționeze.
- **GLN vizibil la orice partener**: formularul de partener afișează GLN-ul standard pe toți partenerii, nu doar pe adresele de livrare, inclusiv în formularul contactelor copil și în formularul simplificat de partener. Câmpul duplicat *GLN* (și avertismentul „same label" de la fiecare încărcare) a dispărut.
- **Strat de compatibilitate**: acționează ca punte pentru configurațiile vechi care necesită dependența `deltatech_gln`. Modulele EDI (`deltatech_edi` și conectorii lui) nu mai depind de acest modul.
- **Transfer automat al valorilor către câmpul standard** (din 19.0.1.1.0, la actualizare): valorile din `gln` sunt copiate în `global_location_number` doar acolo unde acesta e gol, deci nu se suprascrie nicio corecție făcută în câmpul standard, iar operația poate fi rulată din nou fără risc. Partenerii care au două valori diferite sunt raportați în log, nu modificați; se păstrează valoarea standard. Vechea coloană `gln` rămâne în baza de date, neatinsă, ca rezervă.
- **Pictogramă proprie** (din 19.0.1.1.1), în locul celei generice.
- **Fără fișă de consultant**: modulul este o punte tehnică, fără ecran sau flux propriu; GLN-ul pe care îl configurează un consultant este câmpul standard, descris în fișa modulului [deltatech_edi](../deltatech_edi/index.md).

#### 3. Dependențe

- `account_add_gln`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile „Componente Cheie" sunt omise deoarece „Sumar" și „Funcționalități Cheie" provin din `readme/DESCRIPTION.md`, iar acesta nu solicită explicit analiza codului. La nivel de implementare, modulul extinde `res.partner` cu câmpul relat `gln` (`models/res_partner.py`), face vizibil câmpul standard `global_location_number` prin `views/res_partner_view.xml`, iar scripturile din `migrations/` (`19.0.1.1.0/post-migration.py`, `19.0.1.2.0/pre-migration.py`) mută valorile în câmpul standard.

#### 5. Conexiuni

- `account_add_gln`: modulul de care depinde și care deține câmpul standard `global_location_number`; modulele noi ar trebui să îl folosească direct pe acesta. (Nu are încă pagină wiki.)
- [deltatech_edi](../deltatech_edi/index.md): modulele EDI nu mai depind de `deltatech_gln`; GLN-ul standard se configurează conform fișei acestuia.
