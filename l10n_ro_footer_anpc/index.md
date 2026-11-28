# Romania - ANPC footer (localizat la `l10n_ro_footer_anpc/index.md`)

- **Nume Tehnic:** `l10n_ro_footer_anpc`
- **Versiune:** `20.0.0.0.8`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_footer_anpc
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_footer_anpc`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul afișează în subsolul site-ului, pe rândul de copyright, pictograma ANPC „Soluționarea alternativă a litigiilor" (SAL), cu link către platforma `https://reclamatiisal.anpc.ro`, conform Ordinului ANPC nr. 449/2022, modificat prin Ordinul ANPC nr. 270/2026. Ajută magazinele online din România să respecte obligația legală de afișare, fără configurări.

#### 2. Funcționalități Cheie

- Pictograma ANPC SAL, cea publicată de ANPC, într-o casetă de 250 x 50 pixeli, în dreapta rândului de copyright pe desktop și centrată sub text pe telefon.
- Pictograma SOL (platforma europeană ODR) nu mai este afișată: platforma a fost închisă la 20 iulie 2025, iar Ordinul 270/2026 a eliminat obligația.
- Fără setări: după instalare, pictograma apare în subsolul tuturor paginilor.
- Funcționează pe **Odoo Online**: nu conține cod Python util și depinde doar de `website`; se instalează prin *Aplicații → Importați Modulul*, cu arhiva zip a modulului.
- Pașii de instalare și capturile sunt în fișa de consultant.

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, analiza componentelor a fost omisă; modulul nu are modele sau acțiuni automate, doar o vizualizare moștenită.

**Modele**

Niciunul (doar `__init__.py` gol, cerut de uneltele OCA).

**Vizualizări**

- `footer_anpc_data` (`views/footer_template.xml`): moștenește `web.frontend_layout` și adaugă pictograma ANPC SAL în subsol.

**Acțiuni Automate / Acțiuni Server**

Niciuna.

#### 5. Conexiuni

- `website`: modulul standard al cărui subsol este extins.
