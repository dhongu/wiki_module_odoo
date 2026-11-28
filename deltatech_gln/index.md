# Partner GLN (localizat la `deltatech_gln/index.md`)

- **Nume Tehnic:** `deltatech_gln`
- **Versiune:** `20.0.1.1.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_gln
- **Cale Locală:** `odoo-addons/deltatech/deltatech_gln`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul afișează codul **GLN (Global Location Number)** pe formularul partenerului, pe sub-formularul de contact / adresă și pe formularul simplificat de partener, prin câmpul `gln`. Începând cu Odoo 20.0, GLN-ul este un identificator standard al partenerului (`EAN/GLN`), păstrat de `base`; modulul nu mai are o copie proprie a valorii, ci citește, scrie și caută direct în identificatorul standard. Astfel, modulele construite peste `deltatech_gln` (EDI, EDINET etc.) continuă să funcționeze și văd aceeași valoare ca facturarea electronică standard (UBL/Peppol).

#### 2. Funcționalități Cheie

- Câmpul **GLN** (`gln`) pe formularul de partener, pe sub-formularul de contact / adresă și pe formularul simplificat.
- Câmpul este doar un proxy peste identificatorul standard `EAN/GLN` al partenerului: citire, scriere și căutare (inclusiv operatori de tip `like` / `ilike` și `in`) se fac pe stocarea standard.
- Se aplică validarea standard: un GLN malformat (cifră de control EAN greșită) este refuzat.
- Păstrează compatibilitatea cu modulele care depind de `gln`.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): câmpul `gln`, calculat din `additional_identifiers["EAN_GLN"]`, cu `inverse` (scriere în identificatorul standard) și `search` (căutare SQL pe identificator).

**Vizualizări**

- `view_partner_form`: moștenește `base.view_partner_form` și adaugă câmpul GLN.
- `view_partner_simple_form`: moștenește `base.view_partner_simple_form` și adaugă câmpul GLN.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [deltatech_edi](../deltatech_edi/index.md): modul care depinde de `deltatech_gln` și folosește GLN-ul partenerului.
