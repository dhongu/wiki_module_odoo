# Romania - VAT on Payment (localizat la `l10n_ro_vat_on_payment/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_on_payment`
- **Versiune:** `20.0.0.7.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_vat_on_payment
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_vat_on_payment`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Acest modul implementează suportul pentru **TVA la Încasare** (regim special de TVA conform legislației române), permițând verificarea automată a partenerilor înregistrați în sistemul ANAF ca plătitori de TVA la Încasare. Odoo standard nu are nicio integrare cu ANAF și nu poate seta automat poziția fiscală corectă pe baza acestui regim — modulul elimină nevoia verificării manuale a fiecărui furnizor pe site-ul ANAF, aducând statusul TVA la Încasare direct din sursa oficială (fișierul de istoric ANAF), verificat la data facturii și atât pentru furnizor, cât și pentru firma proprie.

#### 2. Funcționalități Cheie

- **Verificare ANAF**: descarcă și procesează fișierul de istoric ANAF (`istoric.txt`) cu toți contribuabilii înregistrați în regimul TVA la Încasare, stocând istoricul perioadelor de aplicare.
- **Câmp TVA la Încasare pe partener**: adaugă câmpul „Romania - VAT on Payment" pe fișa contabilă a partenerului, indicând dacă acesta aplică în prezent regimul.
- **Buton „Update VAT on Payment"** pe fișa partenerului — disponibil doar pentru companii (`is_company = True`) — caută în datele ANAF înregistrările asociate CUI-ului partenerului și le leagă de acesta.
- **Verificare automată**: la crearea sau modificarea unui partener român (cu TVA românesc), statusul TVA la Încasare este verificat și actualizat automat din datele ANAF.
- **Setare automată poziție fiscală pe facturi**: la selectarea partenerului pe o factură, modulul verifică dacă firma proprie sau furnizorul aplică TVA la Încasare la data facturii și setează automat poziția fiscală „Regim TVA la Încasare" (`l10n_ro_property_vat_on_payment_position_id`).
- **Configurare manuală necesară pentru taxe**: pentru facturare trebuie create manual taxele de TVA la Încasare și o poziție fiscală „Regim TVA la Incasare", cu maparea taxelor normale către cele de TVA la Încasare.
- **Joburi cron zilnice**: un job pentru descărcarea datelor ANAF și un job pentru actualizarea statusului TVA la Încasare al partenerilor români, astfel încât informațiile rămân mereu la zi.
- **Istoric ANAF pe partener**: fișa partenerului expune istoricul complet al perioadelor în care acesta a fost înregistrat în regimul TVA la Încasare.

#### 3. Dependențe

- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

Conform prioritizării Readme, analiza codului pentru această secțiune a fost omisă (există `readme/DESCRIPTION.md`, iar acesta nu solicită explicit detalierea componentelor tehnice).

#### 5. Conexiuni

- `account` (text `cod`, fără pagină wiki): modulul extinde `account.move`, `account.move.line` și liniile de repartizare a taxelor pentru a seta automat poziția fiscală de TVA la Încasare pe facturi.
