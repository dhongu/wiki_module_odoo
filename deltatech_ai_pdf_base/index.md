# AI PDF Reading Checks

- **Nume Tehnic:** `deltatech_ai_pdf_base`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_ai_pdf_base
- **Cale Locală:** odoo-addons/bitshop_ent/deltatech_ai_pdf_base
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Verificări comune pentru modulele care citesc documente cu AI (factură furnizor PDF, balanță de verificare PDF). Rulează în cod, fără niciun apel AI, după citirea documentului, și prind erorile de transcriere pe care citirea cu AI le poate lăsa nedetectate.

#### 2. Funcționalități Cheie

- **Valori găsite în textul PDF**: se extrage textul fiecărei pagini și fiecare număr citit de AI (cantitate, preț, valoare linie, totaluri, solduri) este căutat pe propria pagină. O cifră transcrisă greșit care totuși se potrivește la calcul este prinsă aici.
- **Orice format de număr**: `1.234,56`, `1,234.56`, `1234.56`, `1 234,56` și zerourile finale sunt comparate ca aceeași valoare; un `1.234` ambiguu se potrivește și cu 1234, și cu 1.234.
- **Coduri găsite în textul PDF**: coduri de articol și de cont, ignorând spațiile și majusculele.
- **PDF scanat**: o pagină fără strat de text nu este verificată, iar modulul apelant o spune.
- **Cifra de control a codurilor fiscale**: CUI și CNP românești și coduri de TVA UE, cu `python-stdnum`.
- Nu are meniu și nici setări; se instalează ca dependență pentru *Purchase PDF AI Import* și *Trial Balance PDF Import with AI*.

#### 3. Dependențe

- `base`
- `deltatech_partner_match`
- Extern (Python): `python-stdnum`

#### 4. Componente Cheie

**Modele**

- Fără modele; logica este în `tools/pdf_check.py` (funcții de verificare reutilizabile).

**Vizualizări**

- Fără vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_ai_purchase_pdf](../deltatech_ai_purchase_pdf/index.md): folosește verificările pentru facturile furnizor PDF.
