# Fișă Modul: Custodia Stocurilor (cont 8033)

**Modul:** `l10n_ro_stock_consignment`
**Utilizator principal:** Gestionar, Contabil stocuri
**Prioritate:** 🟡 Medie (mărfuri ale terților în gestiune)

---

## 1. Scop business

Modulul gestionează **bunurile primite în custodie** (fără transfer de proprietate) — mărfuri ale
terților ținute spre păstrare/custodie. Evidența se ține în afara bilanțului, pe contul **8033**,
iar stocul nu intră în valorizarea proprie. Rezolvă o nevoie frecventă: să ai mărfurile terțului în
gestiune fizic, dar separate contabil de stocul propriu.

## 2. Bază legală și context

OMFP 1802/2014 — contul în afara bilanțului **8033 „Valori materiale primite în păstrare sau
custodie"**, distinct de obiectele de inventar date în folosință (8035). Evidența extrabilanțieră a
bunurilor terților, fără impact pe bilanț sau pe contul de profit și pierdere.

## 3. Utilizatori și roluri

Gestionar (recepție/retur custodie), Contabil stocuri (verifică nota 8033 și raportul).

Roluri recomandate pentru testare:
- Utilizator Inventar: marchează transferul ca custodie, validează recepția.
- Contabil: verifică nota extrabilanțieră și raportul „Bunuri în custodie".

## 4. Conturi și date implicate

- **8033** — Valori materiale primite în păstrare sau custodie (debit la recepție).
- **803999** — Contrapartidă tehnică evidență extrabilanțieră (analitic al lui 8039, comun suitei; credit la recepție). Partida simplă nu are contrapartidă: linia există doar pentru că Odoo cere note echilibrate.
- Jurnalul **EXTR** (Evidență extrabilanțieră) pentru nota de custodie primită, dacă nu se configurează alt jurnal de custodie.
- Mărfurile primite **în consignație** (spre vânzare) se țin, după OMFP 1802/2014, în **8039**, nu în 8033: pentru ele, setați **Cont custodie** pe un analitic real al lui 8039 (de exemplu 803901).

Date minime pentru demo: companie RO (plan de conturi cu 8033; 803999 și jurnalul EXTR vin din `l10n_ro_off_balance`), un produs, un partener (terțul),
o locație de recepție.

## 5. Configurare inițială

1. Instalați `l10n_ro_stock_consignment`.
2. În **Contabilitate → Setări → Romania - Stock Custody**, verificați/setați **Contul de custodie**
   (implicit 8033), **Contul contrapartidă** (gol = 803999) și **Jurnalul de custodie** (gol = EXTR).
3. Dacă nu sunt setate, modulul le caută automat după cod în planul RO.

## 6. Flux de utilizare

### Pasul 1 — Marcarea și validarea recepției în custodie

Pe transferul de stoc (recepție), setați câmpul **Custodie** = „Primite în custodie", apoi
**Validează**. Modulul setează automat proprietarul (terțul) pe liniile de mișcare — consignație
nativă Odoo, deci bunurile **nu** intră în valorizarea proprie — și generează nota extrabilanțieră.

![Recepție validată, marcată custodie primită](screenshots/02_receptie_validata.png)

### Pasul 3 — Nota extrabilanțieră Dr 8033 = Cr 803999

Din transfer, deschideți nota de custodie generată automat: un articol pe conturi în afara bilanțului,
echilibrat, fără impact pe bilanț/CPP.

![Nota de custodie Dr 8033 = Cr 803999](screenshots/03_nota_8033.png)

### Pasul 4 — Raportul „Bunuri în custodie"

Accesați **Inventar → Raportare → Goods in Custody**. Pe ecran, fiecare rând e un stoc ținut pe seama
unui terț (quant cu proprietar setat). Verificați că apar doar bunurile în custodie (proprietar ≠
companie) și cantitățile corespund recepțiilor. Lista poate fi grupată pe proprietar.

![Raportul Bunuri în custodie](screenshots/04_raport_custodie.png)

### Pasul 5 — Stornarea la retur

La returul bunurilor către terț, apăsați **Reverse Custody Entry** pe transfer — se generează nota
de stornare (Dr 803999 = Cr 8033).

![Stornarea notei de custodie](screenshots/05_storno_custodie.png)

### Note de monografie și raportare

- Recepție custodie: **Dr 8033 = Cr 803999** (valoarea bunurilor, în afara bilanțului).
- Retur custodie: **Dr 803999 = Cr 8033** (stornare).
- „Custodie dată" (bunuri proprii la terți) este doar marcaj/evidență — tratamentul on-balance prin
  contul **357 „Mărfuri aflate la terți"** nu face parte din scope-ul acestui modul.

## 7. Legături cu alte module / declarații

| Modul | Rol |
|---|---|
| `stock` / `stock_account` (nativ) | Consignația (proprietar pe stoc), transferurile. |
| `l10n_ro` | Planul de conturi RO (8033). |
| `l10n_ro_off_balance` | Contrapartida tehnică 803999 și jurnalul EXTR, comune notelor extrabilanțiere. |

**Ce e automat:** proprietarul pe stoc, nota 8033/803999 la recepție, stornarea la retur, raportul.
**Ce rămâne manual:** marcarea transferului ca custodie; tratamentul 357 pentru „custodie dată".

## 8. Verificări pentru consultant

- [ ] Recepția marcată „custodie primită" setează proprietarul terț pe quant (stoc neevaluat propriu).
- [ ] Se generează nota **Dr 8033 = Cr 803999**, echilibrată și exclusiv pe conturi off-balance.
- [ ] Nota nu afectează bilanțul sau contul de profit și pierdere.
- [ ] Raportul „Bunuri în custodie" listează doar stocurile pe seama terților.
- [ ] **Reverse Custody Entry** generează stornarea (Dr 803999 = Cr 8033).

## 9. Mesaje de eroare frecvente

| Mesaj | Cauză | Remediere |
|---|---|---|
| „Configure the custody off-balance account (8033)…" | Contul nu este setat și nu există în plan | Setați contul în Contabilitate → Setări sau verificați planul RO |
| „No general journal available…" | Doar la custodia dată (357 = 371): nu există alt jurnal „Diverse” decât EXTR | Creați un jurnal general sau setați jurnalul de custodie |
| „This transfer has no custody entry to reverse." | Storno apăsat fără notă de custodie | Stornarea se aplică doar transferurilor cu notă de custodie |

## 10. Capturi de ecran

Se **generează automat** din `tests/test_screenshots.py` (mixin `ScreenshotCase`), în RO, pe planul RO.
La momentul redactării **nu există încă** — rulați `fisa-screenshots`. Lista planificată:

1. `02_receptie_validata.png` — recepție validată, marcată custodie primită (proprietar terț).
2. `03_nota_8033.png` — nota Dr 8033 = Cr 803999.
3. `04_raport_custodie.png` — raportul Bunuri în custodie.
4. `05_storno_custodie.png` — stornarea la retur (Dr 803999 = Cr 8033).

```bash
./odoo/odoo-bin -c odoo.conf -d test19 -u l10n_ro_stock_consignment \
  --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

- Subliniați separarea contabilă: bunurile în custodie NU sunt stoc propriu (off-balance 8033).
- Explicați diferența 8033 (primite în custodie) vs 357 (date la terți, on-balance, în afara scope).
- Menționați mecanismul de consignație nativ (proprietar pe quant) care exclude valorizarea proprie.
