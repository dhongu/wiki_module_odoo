# Deltatech UoM UNECE Codes (localizat la `deltatech_uom_unece/index.md`)

- **Nume Tehnic:** `deltatech_uom_unece`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_uom_unece
- **Cale Locală:** `odoo-addons/deltatech/deltatech_uom_unece`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul permite stabilirea, pe fiecare unitate de măsură, a codului UN/ECE transmis în documentele electronice (e-Factura / UBL, eTransport), în locul corespondenței fixe din Odoo. Standardul Odoo recunoaște doar 28 de unități după ID-ul XML și raportează orice altceva ca `C62` (bucată), fără nicio eroare. Astfel, o unitate creată de utilizator (de exemplu „Cutie de 13 kg”) pleacă tacit ca bucată, iar metrii pătrați, picioarele pătrate și mililitrii livrați de Odoo sunt raportați greșit. Dacă un câmp rămâne gol, comportamentul actual se păstrează, deci modulul se poate instala în siguranță pe o bază în producție.

#### 2. Funcționalități Cheie

- Câmp **Cod UNECE** pe unitatea de măsură (**Setări → Tehnic → Unități de măsură**), disponibil și ca coloană opțională în listă, pentru completare rapidă în masă.
- Nomenclator complet de peste 2.000 de coduri UN/ECE Rec 20 (unități) și Rec 21 (ambalaje, coduri prefixate cu `X`), încărcat la instalare din schema SAF-T publicată de ANAF, cu denumiri în engleză și în română. Se consultă în **Setări → Tehnic → Coduri UNECE**, cu filtrare după sursă.
- Nomenclatorul este un model propriu, nu un câmp de selecție: un consultant poate adăuga sau corecta o intrare din interfață, fără modificări de cod, când ANAF republică lista.
- Codul setat pe unitate are prioritate față de corespondența implicită din Odoo, ceea ce permite corectarea celor greșite.
- La instalare se corectează cele trei unități livrate de Odoo care se raportau tacit ca `C62`: metru pătrat, picior pătrat, mililitru.
- Acoperă ambele căi de generare a documentelor electronice: eTransport și facturile UBL/CII.
- Codurile sunt acceptate de UBL/Peppol BIS 3, CIUS-RO și eTransport. Atenție: `XLTR` are 4 caractere, iar `CodUMType` din eTransport acceptă doar 2 sau 3, deci un astfel de cod este raportabil în SAF-T, dar respins într-o declarație de transport.
- Validări pe cod: unic, 2–4 caractere, doar cifre sau litere mari.
- Utilizare zilnică: nu e nimic de făcut după ce unitatea are cod; pentru verificare se deschide unitatea și se citește câmpul Cod UNECE (gol = se aplică maparea Odoo, deci `C62` pentru unități nerecunoscute).

#### 3. Dependențe

- `account`
- `account_edi_ubl_cii`

#### 4. Componente Cheie

**Modele**

- `uom.unece.code`: nomenclatorul de coduri (cod, denumire traductibilă, sursă rec20/rec21/other, activ); constrângeri de unicitate și de format.
- `uom.uom` (extins): adaugă `unece_code_id` și suprascrie `_get_unece_code()` (folosită de eTransport), cu revenire la maparea standard dacă nu e setat.
- `account.edi.common` (extins): suprascrie `_get_uom_unece_code(uom)` (folosită de facturile UBL/CII, care nu trec prin metoda de pe `uom.uom`).

**Vizualizări**

- `uom_unece_code_view_list` / `uom_unece_code_view_search`: listă și căutare (inclusiv filtrare după sursă) pentru nomenclator, deschise din `uom_unece_code_action` și meniul `uom_unece_code_menu`.
- `uom_uom_view_form_inherit` / `uom_uom_view_list_inherit`: câmpul Cod UNECE pe formularul și lista unităților de măsură.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server. Datele `data/uom.unece.code.csv` și `data/uom_uom_data.xml` încarcă nomenclatorul și corectează cele trei unități Odoo.

#### 5. Conexiuni

- `l10n_ro_etransport`: citește codul prin `uom.uom._get_unece_code()` (nu am verificat modulul în această ingestie).
- `account_edi_ubl_cii`: e-Factura / CIUS-RO folosește codul prin `account.edi.common`.
