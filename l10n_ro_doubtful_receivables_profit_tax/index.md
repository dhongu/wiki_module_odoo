# Romania - Creanțe incerte în impozitul pe profit

- **Nume Tehnic:** `l10n_ro_doubtful_receivables_profit_tax`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_doubtful_receivables_profit_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_doubtful_receivables_profit_tax`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul-punte între creanțele incerte și impozitul pe profit; se instalează automat când ambele module sunt prezente. Fără el, diferența permanentă calculată pe fiecare dosar rămâne o cifră pe ecran, pe care contabilul o transcrie manual în registrul de evidență fiscală și în D101.

#### 2. Funcționalități Cheie

- Alimentează calculul D101: partea nedeductibilă a ajustărilor 491 din perioadă se adaugă la cheltuielile nedeductibile, cu rând propriu „(+) Ajustări nedeductibile pentru creanțe” și buton către dosare.
- Alimentează registrul de evidență fiscală (OMF 808/2026) cu câte un rând per creanță: valoare contabilă, valoare fiscală, diferență și temei legal propriu (art. 26 alin. (1) lit. c), cu mențiune distinctă când condițiile nu sunt îndeplinite).
- Semnalează dubla numărare dacă există o regulă `l10n.ro.tax.adjustment` pe contul 6814; nu o corectează singur, regula trebuie ștearsă.
- Nu are meniuri proprii: extinde ecranele Impozit pe profit și Registru de evidență fiscală (butoanele „Calculează din contabilitate”, „Generează din calculul D101”, „Tipărește registrul”).
- Rămân manuale: venitul neimpozabil la reluare, încadrarea pierderii din 654, ajustarea bazei TVA, evidența 8034.
- Pașii sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_doubtful_receivables](../l10n_ro_doubtful_receivables/index.md)
- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.profit.tax.compute` (extins): câmpul și calculul ajustărilor nedeductibile pentru creanțe, avertismentul de dublă numărare.
- `l10n.ro.tax.register` (extins): generarea rândurilor per creanță.

**Vizualizări**

- `view_profit_tax_compute_form_doubtful`: rândul și butonul către dosare în calculul D101.
- `view_tax_register_form_doubtful`: extinderea registrului de evidență fiscală.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_doubtful_receivables](../l10n_ro_doubtful_receivables/index.md): sursa dosarelor și a diferenței permanente.
- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md): calculul D101 și registrul fiscal alimentate.
