# Romania - Stock Accounting Controls (localizat la `l10n_ro_stock_account_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_account_enhancement`
- **Versiune:** `20.0.0.0.6`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_account_enhancement
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_account_enhancement`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă controale suplimentare peste evaluarea stocului din localizarea românească, astfel încât valorile ajunse în contabilitate să nu fie zero și să aibă o sursă clară. Oprește mișcările de stoc cu preț de cost zero și, opțional, cere ca produsele stocabile de pe facturi să provină din comenzi de vânzare sau de achiziție.

#### 2. Funcționalități Cheie

- **Preț de cost nenul pe mișcările de stoc:** calculul prețului unitar al mișcărilor reale de stoc se oprește cu eroare dacă rezultă zero, de exemplu la validarea livrării unei mărfi fără cost cu modulul de marjă `sale_stock_margin` instalat, la închiderea sesiunii de punct de vânzare sau în raportul comenzii de producție. Fără `sale_stock_margin`, livrarea se validează. Prețul folosit la costul vânzării (COGS) de pe factură nu este verificat.
- **Facturi cu produse stocabile doar din comenzi:** la validarea unei facturi de vânzare sau de achiziție (inclusiv storno), fiecare linie cu produs stocabil trebuie să provină dintr-o linie de comandă de vânzare, respectiv de achiziție. Liniile cu servicii sau consumabile nu sunt verificate.
- **Activare din setări:** *Contabilitate → Configurare → Setări → România*, opțiunea *Verifică sursa liniei de produs stocabilă* (implicit dezactivată, valabilă pe toată baza de date).
- **Parametri de sistem:** `l10n_ro_stock_account.check_storable_line_source` (din spatele opțiunii) și `l10n_ro_stock_account.skip_price_unit_check` (pus pe `True`, dezactivează temporar verificarea prețului nenul, de ex. la un stoc inițial cu cost zero).
- Fluxul pas cu pas, cu capturi, se află în fișa consultantului.

#### 3. Dependențe

- [l10n_ro_stock_account](../l10n_ro_stock_account/index.md)
- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

Secțiune omisă: `readme/DESCRIPTION.md` este prezent și nu cere explicit analiza codului pentru componente (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server).

#### 5. Conexiuni

- [l10n_ro_stock_account](../l10n_ro_stock_account/index.md): evaluarea stocului în localizarea românească, pe care modulul o completează cu verificări.
- [l10n_ro_config](../l10n_ro_config/index.md): cadrul de setări unde apare opțiunea din secțiunea România.
