# AI PDF Reading Checks (localizat la `deltatech_ai_pdf_base/index.md`)

- **Nume Tehnic:** `deltatech_ai_pdf_base`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_pdf_base
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_pdf_base`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Verificări comune pentru modulele care citesc documente cu AI (factura de furnizor în PDF, balanța de verificare în PDF). Ele rulează în cod, fără niciun apel AI, după ce documentul a fost citit, și prind cifrele sau codurile transcrise greșit de AI chiar și atunci când calculele se leagă în continuare. Rezultatul apare ca avertismente în ecranele modulelor care folosesc verificarea; modulul nu are meniuri și nici setări.

#### 2. Funcționalități Cheie

- **Valori găsite în textul PDF-ului:** se extrage textul fiecărei pagini, iar fiecare număr citit de AI (cantitate, preț, valoare de linie, totaluri, solduri din balanță) este căutat pe pagina lui. O cifră transcrisă greșit, dar care se leagă aritmetic (de exemplu o cantitate greșită cu valoarea liniei calculată din ea), este astfel semnalată.
- **Toate formatele de număr:** `1.234,56`, `1,234.56`, `1234.56`, `1 234,56` și zerourile de la final sunt tratate ca aceeași valoare; un `1.234` ambiguu se potrivește și cu 1234, și cu 1,234. Semnul nu contează, iar o valoare tipărită cu mai multe zecimale se potrivește și cu rotunjirea la bani.
- **Coduri găsite în textul PDF-ului:** codurile de articol și de cont, cu spațiile și literele mari/mici ignorate (cratima contează).
- **PDF scanat:** o pagină fără strat de text (sub 10 caractere sau fără nicio cifră) nu se verifică, iar modulul apelant o spune explicit. Valorile zero sau goale nu se verifică.
- **Cifra de control a codului fiscal:** CUI și CNP românesc și coduri de TVA UE, cu `python-stdnum`; un cod gol, din afara UE sau fără prefix la o companie din afara României nu se verifică. Verificarea nu atestă că firma există sau e activă în scopuri de TVA.
- **Limite:** verificarea arată doar dacă valoarea e tipărită pe pagină, nu și pe rândul ei; nu prinde sume schimbate între rânduri, debit/credit inversat, valori mici care apar oricum pe pagină sau coduri trunchiate.
- Avertismentele nu corectează și nu blochează nimic; decizia rămâne la operator. Detalii, exemple și lista de verificări sunt în fișa consultantului. Mesajele din importul facturii sunt deocamdată în engleză.
- Se instalează ca dependență a modulelor *Purchase PDF AI Import* și *Trial Balance PDF Import with AI*.

#### 3. Dependențe

- `base`
- [deltatech_partner_match](../deltatech_partner_match/index.md) (furnizează `check_vat`)
- Bibliotecă Python externă: `python-stdnum`

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări, cron-uri sau acțiuni server; este o bibliotecă de funcții Python.

**Modele**

- Niciunul.

**Vizualizări**

- Niciuna.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

**Bibliotecă (`tools/pdf_check.py`)**

- `PdfTextCheck`: ține textul PDF-ului pagină cu pagină; oferă `number_found`, `code_found`, `has_text` și `pages_without_text`.
- `page_texts`, `text_numbers`, `token_values`: extragerea textului și recunoașterea formatelor de număr.
- `check_vat`: reexportat din `deltatech_partner_match`, o singură implementare a verificării CUI / CNP / TVA UE.

#### 5. Conexiuni

- [deltatech_ai_purchase_pdf](../deltatech_ai_purchase_pdf/index.md): folosește verificările la previzualizarea facturii de furnizor citite din PDF (linii, totaluri, CUI furnizor).
- [deltatech_ai_trial_balance_import](../deltatech_ai_trial_balance_import/index.md): folosește verificările la importul balanței din PDF (sume, coduri de cont, cod fiscal) și păstrează textul paginilor pentru „Verifică din nou”.
- [deltatech_partner_match](../deltatech_partner_match/index.md): sursa verificării codului fiscal, aceeași regulă ca la potrivirea partenerilor.
