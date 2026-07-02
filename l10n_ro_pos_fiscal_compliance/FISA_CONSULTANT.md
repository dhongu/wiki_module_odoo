# Fișă Modul: Conformitate fiscală POS (AMEF)

**Modul:** `l10n_ro_pos_fiscal_compliance`
**FR:** FR-47
**Utilizator principal:** Operator POS / casier, Contabil retail
**Prioritate:** 🟡 Medie (zilnic în retail)

---

## 1. Scop business

Această fișă descrie utilizarea modulului `l10n_ro_pos_fiscal_compliance` pentru **conformitatea fiscală
a vânzării cu amănuntul prin POS** (aparate de marcat electronice fiscale — AMEF). Modulul completează
POS-ul Odoo cu evidența cerută în România: urmărirea seriei și numărului bonului fiscal pe fiecare
comandă, blocarea închiderii sesiunii dacă există comenzi plătite fără bon fiscal, raportul Z fiscal
reconciliat cu vânzările și încasările, și arhivarea jurnalului electronic AMEF.

## 2. Bază legală și context

OUG 28/1999 — obligația operatorilor economici care fac vânzări cu amănuntul către populație să
utilizeze aparate de marcat electronice fiscale și să emită bon fiscal. OPANAF 4156/2017 și actele
ulterioare reglementează fișierele AMEF (jurnal electronic, raport Z, bonuri fiscale) și conectarea
AMEF la ANAF.

> Modulul acoperă latura de conformitate (evidență, blocaj, raport Z, arhivă) peste POS-ul Odoo.
> Comunicarea efectivă cu aparatul fiscal se face printr-un driver (ex. `deltatech_pos`, opțional),
> care apelează metoda publică de înregistrare a răspunsului fiscal. Modulul **nu depinde** de un
> driver anume.

## 3. Utilizatori și roluri

Operator POS / casier (emite bonuri), Contabil retail (reconciliază raportul Z, arhivează jurnalul).

Roluri recomandate pentru testare:
- Administrator funcțional: instalează modulul, activează fiscalizarea pe punctul de lucru.
- Operator POS: înregistrează bonurile fiscale pe comenzi.
- Contabil/manager retail: generează și reconciliază raportul Z, arhivează jurnalul electronic.

## 4. Conturi și date implicate

Modulul **nu generează note contabile** — gestionează evidența fiscală a vânzărilor POS. Datele
implicate:
- **bon fiscal** pe `pos.order`: serie, număr, dată/oră fiscală, stare (de fiscalizat / emis / eroare);
- **punct de lucru** (`pos.config`): fiscalizare obligatorie + serie aparat fiscal (AMEF);
- **raport Z**: defalcare pe cote TVA și pe metode de plată, valori declarate vs. calculate;
- **jurnal electronic AMEF**: fișiere XML/raport pe perioadă și aparat.

Date minime pentru demo:
- companie românească cu localizarea contabilă și `point_of_sale` instalate;
- un punct de lucru POS cu fiscalizare activă și metode de plată;
- una sau mai multe comenzi POS plătite în sesiune.

## 5. Configurare inițială

1. Instalați modulul `l10n_ro_pos_fiscal_compliance`.
2. În **Point of Sale → Configurare → Setări**, selectați punctul de lucru și, la secțiunea
   **Conformitate fiscală RO (AMEF)**, bifați **Fiscalizare AMEF obligatorie** și completați **Seria
   aparatului fiscal**.
3. Verificați metodele de plată ale punctului de lucru (numerar, card, tichete).
4. Verificați că operatorul are grupul **Point of Sale / Utilizator**.

## 6. Flux de utilizare

### Pasul 1 — Activarea fiscalizării pe punctul de lucru

În **Point of Sale → Configurare → Setări**, la secțiunea **Conformitate fiscală RO (AMEF)**, activați
**Fiscalizare AMEF obligatorie** și completați seria aparatului fiscal. De acum, comenzile plătite din
acest punct de lucru trebuie să aibă bon fiscal emis înainte de închiderea sesiunii.

![Setări POS — fiscalizare AMEF obligatorie](screenshots/01_config_fiscal.png)

### Pasul 2 — Bonul fiscal pe comandă

Pe fiecare comandă POS (**Point of Sale → Comenzi → Comenzi**), fila **Fiscalizare AMEF** arată starea
și datele bonului. Driverul aparatului fiscal completează automat seria și numărul (prin metoda de
integrare); alternativ, le puteți introduce manual și apăsa **Înregistrează bon fiscal**, ceea ce trece
comanda în starea **Bon emis**. Dacă aparatul a întors eroare, comanda rămâne **Eroare fiscalizare** și
poate fi marcată drept eroare justificată.

![Comanda POS — fila Fiscalizare AMEF](screenshots/02_comanda_fiscal.png)

### Pasul 3 — Raportul Z fiscal

La finalul zilei, generați raportul Z din sesiune sau din **Point of Sale → Fiscalizare AMEF →
Rapoarte Z**. Apăsați **Calculează din sesiune**: se agregă vânzările pe cote TVA și încasările pe
metode de plată. Completați valorile declarate din raportul Z al aparatului și apăsați **Reconciliază**
— diferențele față de totalurile POS sunt evidențiate (stare „Reconciliat" sau „Diferențe").

![Raport Z fiscal — defalcare TVA + plăți, reconciliere](screenshots/03_raport_z.png)

### Pasul 4 — Arhivarea jurnalului electronic AMEF

Fișierele jurnalului electronic AMEF se încarcă și se arhivează pe perioadă/aparat în **Point of Sale →
Fiscalizare AMEF → Jurnale electronice AMEF**: completați aparatul, perioada, atașați fișierul și
apăsați **Arhivează**.

![Jurnal electronic AMEF arhivat](screenshots/04_jurnal_amef.png)

### Note de monografie și raportare

Modulul **nu produce note contabile** — nota contabilă agregată a sesiunii POS rămâne cea generată de
`point_of_sale` la închidere. Aportul modulului este: evidența seriei/numărului de bon fiscal,
**blocarea închiderii sesiunii** dacă există comenzi plătite nefiscalizate fără eroare justificată,
raportul Z reconciliat (pe cote TVA și metode de plată) și arhiva jurnalului electronic AMEF.
Returul fiscal referențiază bonul inițial (câmpurile „Bon inițial (retur)").

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `point_of_sale` | comenzi, sesiuni, metode de plată, nota de sesiune | dependență (manifest) |
| `account` | nota contabilă de sesiune (generată de POS) | dependență (manifest) |
| `l10n_ro` | plan de conturi și taxe RO | dependență (manifest) |
| `deltatech_pos` / `deltatech_pos_base` | driver fiscal AMEF (apelează `_l10n_ro_apply_fiscal_response`) | integrare opțională (nu dependență) |
| `l10n_ro_anaf_d394_pos` | agregarea bonurilor fiscale POS în declarația D394 (dacă e instalat) | integrare prin convenție (realizată de modulul D394 POS, nu de acesta) |

Ce este automat: marcarea stării de fiscalizare, blocarea închiderii sesiunii, calculul raportului Z și
reconcilierea cu vânzările/încasările POS.
Ce rămâne manual: configurarea fiscalizării pe punctul de lucru, completarea valorilor declarate din
raportul Z, justificarea erorilor de fiscalizare și încărcarea fișierului de jurnal electronic.

## 8. Verificări pentru consultant

- [ ] Modulul se instalează fără erori (cu `point_of_sale` prezent).
- [ ] În Setări POS apare secțiunea **Conformitate fiscală RO (AMEF)** cu cele două opțiuni.
- [ ] Pe comanda POS apare fila **Fiscalizare AMEF** cu starea bonului.
- [ ] O comandă plătită fără bon fiscal blochează închiderea sesiunii (cu mesaj clar).
- [ ] „Înregistrează bon fiscal" trece comanda în starea „Bon emis" și salvează seria/numărul.
- [ ] Raportul Z agregă corect pe cote TVA și pe metode de plată; reconcilierea semnalează diferențele.
- [ ] Jurnalul electronic AMEF poate fi arhivat cu fișier atașat.

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| „Nu se poate închide sesiunea …: … comenzi plătite nu au bon fiscal emis." | Comenzi plătite nefiscalizate într-o sesiune cu fiscalizare obligatorie | Emiteți bonul fiscal sau marcați eroarea ca justificată pe comenzile listate |
| „Completați numărul bonului fiscal pentru comanda …" | „Înregistrează bon fiscal" apăsat fără număr completat | Completați numărul (și seria) bonului fiscal |
| „Încărcați fișierul jurnalului electronic înainte de arhivare." | „Arhivează" apăsat fără fișier atașat | Atașați fișierul jurnalului electronic AMEF |

## 10. Capturi de ecran

Capturile (`readme/screenshots/`) sunt **generate automat** din `tests/test_screenshots.py`
(mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), în **limba română**,
pe planul de conturi RO (`setup_country("ro")`):

1. `01_config_fiscal.png` — setări POS, secțiunea „Conformitate fiscală RO (AMEF)".
2. `02_comanda_fiscal.png` — comanda POS, fila „Fiscalizare AMEF".
3. `03_raport_z.png` — raportul Z fiscal (defalcare TVA + metode de plată, reconciliere).
4. `04_jurnal_amef.png` — jurnalul electronic AMEF.

Regenerare:

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i l10n_ro_pos_fiscal_compliance,l10n_ro_doc_screenshots \
    --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

În manualul final, păstrați explicația orientată pe activitate: obligația bonului fiscal la vânzarea cu
amănuntul, ce înseamnă blocarea închiderii sesiunii, cum se citește raportul Z reconciliat și de ce se
arhivează jurnalul electronic. Subliniați că modulul nu modifică contabilitatea POS, ci adaugă
controlul fiscal cerut de lege; comunicarea cu aparatul fiscal fizic se face prin driverul de
fiscalizare instalat separat.
