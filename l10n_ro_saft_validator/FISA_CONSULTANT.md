# Fișă Modul: Pre-Validator SAF-T D406 — Overview

**Modul:** `l10n_ro_saft_validator`
**FR:** FR-05 (SAF-T D406)
**Capitol manual:** Cap 5 / SAF-T
**Utilizator principal:** Contabil, Responsabil SAF-T
**Prioritate:** Medie

---

## 1. Scop business

Modulul rulează verificări **înainte** de generarea fișierului SAF-T D406, identificând datele
incomplete care ar duce la respingerea declarației de către ANAF (parteneri fără CUI, conturi
nemapate, active fără categorie SAF-T, tipuri de operație stoc fără cod etc.). Consultantul îl
prezintă ca pas de „pre-flight" care reduce erorile la validarea oficială DUK Integrator.

## 2. Bază legală și context

- **OPANAF 1783/2021** și actualizările — structura SAF-T D406 (fișierul standard de audit fiscal).
- Validarea oficială se face cu DUK Integrator; acest modul previne erorile uzuale înainte de export.

## 3. Cele trei spețe D406

D406 are patru tipuri de depunere indicate în câmpul `HeaderComment` din XML. Modulul tratează
cele trei spețe operaționale principale; vezi fișa dedicată pentru fluxul end-to-end:

| Tip | Cod ANAF | Conținut SAF-T | Fișa dedicată |
|-----|----------|----------------|----------------|
| Lunar / Trimestrial | **L** / **T** | GL + facturi + plăți + taxe + parteneri | [`FISA_CONSULTANT_LT.md`](FISA_CONSULTANT_LT.md) |
| Anual (Active) | **A** | Assets + AssetTransactions | [`FISA_CONSULTANT_A.md`](FISA_CONSULTANT_A.md) |
| La cerere (Stocuri) | **C** | PhysicalStocks + MovementOfGoods | [`FISA_CONSULTANT_C.md`](FISA_CONSULTANT_C.md) |

> Câmpul **Tip declarație** din wizard activează setul de verificări corespunzător. Verificarea de
> companie (CUI, adresă, județ) rulează pentru toate cele trei spețe.

## 4. Module Odoo implicate

| Modul | Rol |
|-------|-----|
| `l10n_ro_saft_validator` (acest modul) | pre-validare conform celor 3 spețe |
| `l10n_ro_saft` | export D406 — buton lunar (L/T) + buton **Asset Declaration** (A) |
| `l10n_ro_saft_stock` | export D406 — buton **Stocks** (C); câmp `l10n_ro_stock_movement_type` pe tip operație |
| `l10n_ro` | plan de conturi și structura fiscală RO |
| DUK Integrator (extern) | validare oficială ANAF înainte de depunere |

## 5. Verificări pe tip declarație

| Verificare | LT | A | C | Severitate |
|---|---|---|---|---|
| `company_incomplete` (date companie) | ✓ | ✓ | ✓ | error / warning |
| `partner_no_vat` (parteneri fără CUI) | ✓ |  |  | error / warning |
| `partner_no_country` / `partner_invalid_country` | ✓ |  |  | error / warning |
| `partner_no_city` (parteneri fără localitate) | ✓ |  |  | error |
| `partner_no_state` / `partner_invalid_state` (județ) | ✓ |  |  | warning |
| `partner_fiscal_type_mismatch` (țară și TVA se contrazic) | ✓ |  |  | error / warning |
| `move_line_no_partner` (note pe 40x/41x fără partener) | ✓ |  |  | error |
| `account_no_type` (conturi nemapate) | ✓ |  |  | error |
| `tax_no_saft_type` (taxe fără tip SAF-T) | ✓ |  |  | warning |
| `export_section_empty` (secțiuni care ar ieși goale) | ✓ |  |  | error |
| `payments_not_exported` (plăți fără extras bancar) | ✓ |  |  | warning |
| `product_no_default_code` (articole fără referință internă) | ✓ |  |  | error |
| `product_no_category` (articole fără categorie) | ✓ |  |  | error |
| `product_no_account` (articole fără cont de venit/cheltuială) | ✓ |  |  | warning |
| `asset_no_saft_category` (active fără categorie SAF-T) |  | ✓ |  | error |
| `picking_type_no_movement_type` (tip operație stoc fără cod SAF-T) |  |  | ✓ | error |
| `uom_no_unece_code` (UoM fără cod UNECE) |  |  | ✓ | warning |

> **Verificarea de companie s-a înăsprit** și se aplică tuturor celor trei spețe: pe lângă CUI,
> adresă și județ, sunt semnalate acum și lipsa telefonului, a contului bancar, a bazei de
> impozitare SAF-T și a unui contact cu nume din două cuvinte și telefon. Primele trei opresc
> exportul Enterprise înainte să genereze fișierul; al patrulea lasă declarația fără elementul
> obligatoriu `Contact` și o face respinsă de validatorul ANAF.

### De unde vin verificările

Cele mai multe nu sunt deduse din documentația D406, ci din confruntarea unui fișier generat de
Odoo cu validatorul oficial `D406Validator` din DUK Integrator: fiecare a fost mai întâi un fișier
respins, apoi o verificare. Două tipare merită reținute de consultant, pentru că nu se văd nicăieri
în interfața Odoo:

- **O secțiune emisă goală invalidează tot fișierul.** Exportul scrie necondiționat
  `SalesInvoices`, `PurchaseInvoices` și `Payments`, iar validatorul cere minimum un element în
  fiecare secțiune prezentă. O lună fără achiziții produce o declarație respinsă în întregime.
- **Plățile intră în declarație doar dintr-o linie de extras bancar.** O plată înregistrată prin
  „Înregistrează plata", fără extras, nu ajunge în fișier. Un client care nu importă extrase în
  Odoo generează sistematic un D406 nedepunabil.

## 6. Flux general

1. Deschideți **Contabilitate → Raportare → SAF-T Validator**.
2. Selectați **Tip declarație** (LT / A / C).
3. Apăsați **Validate** — wizardul afișează lista problemelor.
4. Corectați datele (vezi fișa dedicată).
5. Re-rulați până când lista e goală.
6. Generați D406 din raportul **General Ledger** (l10n_ro_saft / l10n_ro_saft_stock).

## 7. Capturi de ecran

Capturile per variantă sunt în fișele dedicate (`FISA_CONSULTANT_LT.md`, `_A.md`, `_C.md`).

**Wizard cu Tip declarație vizibil ①:**

![Validator SAF-T D406 — wizard cu tip declarație](screenshots/01_saft_validator_wizard.png)

| # | Fișier | Conținut |
|---|--------|----------|
| 1 | `screenshots/01_saft_validator_wizard.png` | Wizard validare ① — radio Tip declarație (LT/A/C) + sumar Errors/Warnings + lista problemelor |
