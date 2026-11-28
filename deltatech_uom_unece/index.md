# UoM UNECE Codes (localizat la `deltatech_uom_unece/index.md`)

- **Nume Tehnic:** `deltatech_uom_unece`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_uom_unece
- **Cale Locală:** `odoo-addons/deltatech/deltatech_uom_unece`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Permite alegerea, pe fiecare unitate de măsură, a codului UN/ECE trimis în documentele electronice (e-Factura, e-Transport), din nomenclatorul publicat de ANAF, și permite ca mai multe unități să folosească același cod. Extinde câmpul standard UN/ECE Code din `account_edi_ubl_cii`, acolo unde acesta nu ajunge: nomenclator în loc de text liber și coduri partajate (de exemplu „Cutie 13 kg” și „Cutie 5 kg” pot avea ambele `XBX`).

#### 2. Funcționalități Cheie

- Nomenclatorul ANAF (SAF-T, foaia `Unitati_masura`) încărcat la instalare: peste două mii de coduri UN/ECE Rec 20 (unități) și Rec 21 (ambalaje, prefixate cu `X`), cu denumirea în engleză și traducerea ANAF în română. Se poate completa sau corecta din interfață, fără modificări de cod.
- Câmpul **UNECE Code** pe unitate (listă, coloană opțională, și formular), cu același cod permis pe oricâte unități.
- Precedența: codul ales aici, apoi câmpul standard UN/ECE Code al unității, apoi maparea internă Odoo (`C62` pentru unitățile nerecunoscute). Dacă rămâne gol, comportamentul actual nu se schimbă, deci instalarea e sigură pe o bază în producție.
- Codul se aplică în toate documentele electronice (facturi UBL/CII, CIUS-RO, e-Transport), citit prin `uom.uom._get_unece_code()`; în XML, `cbc:InvoicedQuantity` primește de exemplu `unitCode="XBX"`.
- Meniul **Setări > Coduri UNECE** (doar grupul Setări), filtrabil după sursă (Rec 20 / Rec 21). Lista unităților se deschide din Facturare > Configurare > Setări, blocul **Unități și ambalaje**, după bifarea opțiunii.
- Atenție: nomenclatorul conține `XLTR` (4 caractere), dar `CodUMType` din e-Transport acceptă doar 2-3, deci un astfel de cod e raportabil în SAF-T, dar respins la declarația de transport. Reîncărcarea nomenclatorului după o republicare ANAF: `scripts/import_unece_from_saft.py`.
- Verificarea unităților la go-live și pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- `account`
- `account_edi_ubl_cii`

#### 4. Componente Cheie

**Modele**

- `uom.unece.code`: nomenclatorul de coduri (cod, denumire traductibilă, sursă Rec 20/21, activ).
- `uom.uom`: extins cu `unece_code_id`, care are prioritate în `_get_unece_code()`.

**Vizualizări**

- `uom_unece_code_view_list`, `uom_unece_code_view_search`, `uom_unece_code_action`: lista, căutarea și acțiunea meniului Coduri UNECE.
- `uom_uom_view_form_inherit`, `uom_uom_view_list_inherit`: câmpul UNECE Code pe formularul și lista unităților.

**Acțiuni Automate / Acțiuni Server**

- Nu are; datele din `data/uom.unece.code.csv` se încarcă la instalare. Acces (`security/ir.access.csv`): citire pentru utilizatori, drepturi complete pentru grupul Setări.

#### 5. Conexiuni

- [deltatech_uom_domain](../deltatech_uom_domain/index.md): extinde listele de unități pe achiziții; pentru vânzări cere mai întâi coduri UNECE reale.
