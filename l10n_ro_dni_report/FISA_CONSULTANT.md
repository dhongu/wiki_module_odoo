# Fișă Modul: Raport livrări nefacturate (418)

**Modul:** `l10n_ro_dni_report` · **Versiune:** 19.0.1.0.0 · **Meniu:** Contabilitate → Raportare →
Livrări nefacturate (418)

## 1. Scop business

La închiderea lunii, soldul debitor al contului 418 („Clienți — facturi de întocmit”) trebuie
explicat: ce avize de livrare nu au fost încă facturate, către ce clienți și de cât timp. Raportul
le listează pe client, cu drill-down la document.

## 2. Bază legală și context

- **OMFP 1802/2014**, funcțiunea contului 418 (cont de activ): se debitează cu valoarea livrărilor de
  bunuri sau a serviciilor prestate pentru care nu s-au întocmit facturi, inclusiv TVA aferentă, și se
  creditează cu valoarea facturilor întocmite (411).
- **Avizul de însoțire a mărfii** (cod 14-3-6A) justifică livrarea până la emiterea facturii.
- **Codul fiscal, art. 319 alin. (16)**: factura se emite cel târziu până în ziua 15 a lunii
  următoare celei în care a avut loc livrarea (faptul generator). Un aviz din luna anterioară, încă
  nefacturat după data de 15, indică o factură emisă cu întârziere (la livrările intracomunitare se
  aplică alin. (15)).

## 3. Utilizatori și roluri

Contabilul care închide luna; responsabilul de facturare (urmărește avizele nefacturate).

## 4. Date implicate

Liniile contabile postate pe conturile 418 (din avizele de livrare ale `l10n_ro_stock_account` sau
din note manuale), cu partenerul și, unde există, mișcarea de stoc din spatele notei.

## 5. Configurare inițială

- Contul 418 din configurarea companiei (contul folosit la avizul de livrare, din
  `l10n_ro_stock_account`). Fără el, raportul ia toate conturile care încep cu 418.
- Liniile de pe 418 trebuie să aibă partenerul completat, ca gruparea pe client să fie corectă.

## 6. Flux de utilizare

### Pasul 1 — Deschiderea raportului

Accesați **Contabilitate → Raportare → Livrări nefacturate (418)** și alegeți perioada; soldul se
calculează cumulat la data de sfârșit.

**Găsiți pe ecran:** un rând pe client, cu *Livrat*, *Facturat*, *Rămas* și *Vechime (zile)*;
clienții fără sold nu apar.

### Pasul 2 — Detaliul pe document

Desfaceți clientul: fiecare înregistrare de pe 418 apare cu documentul ei — avizul (transferul)
pentru livrările din stoc, nota contabilă pentru înregistrările manuale.

## 7. Monografie și controale contabile

| Situație | Notă | Efect în raport |
|---|---|---|
| Livrare pe aviz | 418 = 707 (valoarea fără TVA; TVA-ul apare pe factură) | apare la *Livrat* |
| Factura emisă pe baza avizului | 4111 = 418 + 4427 | apare la *Facturat*, scade *Rămas* |
| Factură parțială | 4111 = 418, parțial | rămâne diferența |

Control: totalul coloanei *Rămas* = soldul debitor al conturilor 418 în balanța la aceeași dată. Dacă
pe 418 există și note manuale cu TVA inclus, coloana amestecă sume cu și fără TVA.

## 8. Scenarii de test pentru consultant

| ID | Scenariu | Rezultat așteptat |
|---|---|---|
| DNI-01 | Aviz de 1.000 lei, nefacturat | clientul apare cu Rămas 1.000 |
| DNI-02 | Avizul facturat integral | clientul dispare din raport |
| DNI-03 | Facturat 400 din 1.000 | Rămas 600 |
| DNI-04 | Aviz din luna anterioară | apare în luna curentă, cu vechimea corectă |

## 9. Legături cu alte module

| Modul | Rol |
|---|---|
| `l10n_ro_stock_account` | avizul de livrare (418 = 707) și legătura notei cu transferul |
| `l10n_ro_stock_picking_report` | tipărirea avizului de însoțire a mărfii |
| `l10n_ro_rni_report` | perechea pentru recepții nefacturate (408) |
