# Romania - ANPC footer (localizat la `l10n_ro_footer_anpc/index.md`)

- **Nume Tehnic:** `l10n_ro_footer_anpc`
- **Versiune:** `19.0.0.0.5`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_footer_anpc
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_footer_anpc`
- **Ultima Ingestie:** `2026-11-02`

#### 1. Sumar

Acest modul afișează în footer-ul site-ului, pe rândul de copyright, pictograma ANPC „Soluționarea alternativă a litigiilor" (SAL), cu link către platforma `https://reclamatiisal.anpc.ro`. Ajută magazinele online din România să respecte obligația de informare a consumatorilor prevăzută de Ordinul ANPC nr. 449/2022, modificat prin Ordinul ANPC nr. 270/2026 (Monitorul Oficial nr. 420 din 19 mai 2026). Nu necesită configurare: după instalare, pictograma apare în subsolul tuturor paginilor.

#### 2. Funcționalități Cheie

- Afișează în footer, pe rândul de copyright, pictograma SAL oficială publicată de ANPC (pe `https://www.anpc.ro/sal`), într-o casetă de 250 x 50 pixeli, cu link către `https://reclamatiisal.anpc.ro/` (se deschide într-o filă nouă).
- Pictograma SOL (platforma europeană ODR) nu mai este afișată: platforma a fost închisă la 20 iulie 2025 (Regulamentul (UE) 2024/3228), iar Ordinul ANPC nr. 270/2026 a eliminat-o din obligația de afișare.
- Blocul ANPC urmează rândul de copyright și este aliniat la dreapta pe ecrane medii și mari (Bootstrap 5); imaginea are text alternativ.

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește și nu extinde modele.

**Vizualizări**

- `footer_anpc_data`: șablon QWeb moștenit din `web.frontend_layout`, care adaugă blocul `o_footer_anpc` (pictograma SAL cu link) în rândul de copyright al footer-ului.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni `ir.cron`, `base.automation` sau `ir.actions.server` definite în acest modul.

#### 5. Conexiuni

- `website`: modulul extinde subsolul site-ului furnizat de modulul standard `website`.
