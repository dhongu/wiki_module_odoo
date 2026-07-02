# Romania - Conformitate fiscală POS (AMEF) (localizat la `l10n_ro_pos_fiscal_compliance/index.md`)

- **Nume Tehnic:** `l10n_ro_pos_fiscal_compliance`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_pos_fiscal_compliance`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_pos_fiscal_compliance`
- **Ultima Ingestie:** `2026-06-08`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul asigură conformitatea fiscală pentru vânzarea cu amănuntul prin POS, conform OUG 28/1999 privind aparatele de marcat electronice fiscale (AMEF). Completează POS-ul Odoo și driverele de fiscalizare (ex. `deltatech_pos`) cu evidența fiscală cerută în România: urmărirea bonului fiscal pe fiecare comandă, blocarea închiderii sesiunii când există comenzi plătite fără bon emis, raportul Z reconciliat cu vânzările și încasările, returul fiscal legat de bonul inițial și arhivarea jurnalului electronic AMEF. Modulul acoperă latura de conformitate (evidență, blocaj, raport Z, arhivă) peste POS-ul Odoo; comunicarea efectivă cu aparatul fiscal se face printr-un driver opțional, modulul nedepinzând de un driver anume.

#### 2. Funcționalități Cheie

- **Urmărirea bonului fiscal** pe fiecare comandă POS: serie, număr, dată/oră fiscală și stare (de fiscalizat / emis / eroare), cu punct de integrare pentru răspunsul aparatului fiscal.
- **Blocarea închiderii sesiunii** POS dacă există comenzi plătite fără bon fiscal emis și fără eroare justificată.
- **Raportul Z fiscal** cu defalcare pe cote TVA și pe metode de plată, reconciliat cu vânzările și încasările din Odoo, evidențiind diferențele.
- **Returul fiscal** care referențiază bonul inițial.
- **Arhiva jurnalului electronic AMEF** (fișiere XML/raport pe perioadă și aparat fiscal).

#### 3. Dependențe

- `point_of_sale`
- `account`
- `l10n_ro`

#### 4. Componente Cheie

Documentația pentru Sumar și Funcționalități Cheie a fost generată din `readme/DESCRIPTION.md`, care nu solicită explicit analiza componentelor tehnice. Conform fluxului de ingestie, analiza codului pentru această secțiune (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server) a fost omisă.

#### 5. Conexiuni

- [deltatech_pos](../deltatech_pos/index.md): driver de fiscalizare POS care poate apela metoda publică de înregistrare a răspunsului fiscal (integrare opțională; modulul nu depinde de el).
