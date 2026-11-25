# Vendor Bill UBL Review (localizat la `deltatech_vendor_bill_ubl_review/index.md`)

- **Nume Tehnic:** `deltatech_vendor_bill_ubl_review`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_vendor_bill_ubl_review
- **Cale Locală:** `odoo-addons/bitshop/deltatech_vendor_bill_ubl_review`
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Când o factură de furnizor este citită dintr-un XML UBL (încărcat manual sau primit din SPV), Odoo își completează liniile fără nicio confirmare: nimeni nu verifică dacă produsul găsit este cel corect, dacă prețul este cel obișnuit sau dacă TVA-ul din document corespunde taxei puse pe linie. Modulul adaugă un **pas de verificare pe factura ciornă**, înainte de postare, în care utilizatorul vede și corectează potrivirile, prețurile și TVA-ul.

#### 2. Funcționalități Cheie

- Butonul **Review UBL import** pe o factură sau o notă de credit de furnizor în ciornă, care are atașat un XML UBL. Factura primește insigna **UBL to review**, apoi **UBL reviewed**.
- **Un rând pe linie de XML**, cu produsul găsit și modul de potrivire: verde pentru cod furnizor, referință internă sau cod de bare, galben pentru potrivire doar după denumire, roșu când nu s-a găsit produs. Orice rând poate primi alt produs (devine verde, „Chosen by hand").
- **Verificarea prețului**: prețul din XML este comparat cu prețul furnizorului din lista de prețuri a furnizorului; abaterea peste toleranța companiei (implicit 5%) este evidențiată.
- **Verificarea TVA**: cota din XML este comparată cu taxa pe care o primește linia (taxa de achiziție a produsului prin poziția fiscală). Se raportează cotă diferită, linii cu taxare inversă sau intracomunitare (AE/K) a căror taxă nu este autolichidată, taxă de taxare inversă pe o linie nedeclarată astfel în XML și linii AE/K fără produs. Verificarea nu alege și nu modifică niciodată taxa.
- **Verificări de antet**: totalurile facturii diferite de cele din XML și altă factură a aceluiași furnizor cu aceeași referință (posibil duplicat, cu link către ea).
- **La confirmare**: liniile de produs ale facturii sunt rescrise din XML cu produsele, unitățile, prețurile și discounturile confirmate, cu taxele produsului prin poziția fiscală. Opțional se actualizează prețurile furnizorului (**Update vendor prices**) și se creează produsele lipsă (**Create missing products**, dezactivat implicit). Jurnalul verificării se postează în chatter.
- **Facturi legate de o comandă de achiziție**: liniile se păstrează (legătura cu comanda rămâne); verificarea actualizează totuși prețurile furnizorului și marchează factura ca verificată.
- **Blocare opțională la confirmare**: cu **Require UBL review before confirming** activ (implicit dezactivat), o factură creată din XML UBL nu poate fi postată înainte de verificare.
- **Configurare** (Facturare/Contabilitate → Configurare → Setări, secțiunea Vendor Bills): **Require UBL review before confirming** și **UBL review price tolerance (%)**, setări la nivel de companie. Potrivirea după cod furnizor cere *Vendor Product Code* pe liniile din lista de prețuri a furnizorului; altfel se folosesc codul de bare, referința internă sau denumirea.
- Importul standard (încărcare, descărcare SPV) rămâne neschimbat: verificarea lucrează pe factura creată de el.

#### 3. Dependențe

- [deltatech_account_ubl_import](../deltatech_account_ubl_import/index.md)

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): câmpurile `ubl_reviewed` și `ubl_review_state`, acțiunea `action_ubl_review` și blocarea postării (`_post`) când verificarea este obligatorie.
- `res.company` (extins): `ubl_review_required` și `ubl_review_price_tolerance`.
- `res.config.settings` (extins): expune cele două setări ale companiei.
- `vendor.bill.ubl.review.wizard` (tranzitoriu): asistentul de verificare; reutilizează parsarea și potrivirea din `account.ubl.import.mixin`; calculează avertismentele de total și de duplicat și aplică rezultatul pe factură.
- `vendor.bill.ubl.review.wizard.line` (tranzitoriu): un rând per linie de XML, cu tipul potrivirii, produsul ales, prețul furnizorului, abaterea și verificarea TVA.

**Vizualizări**

- `view_move_form_ubl_review`: butonul și insigna de verificare pe formularul facturii.
- `view_vendor_bill_ubl_review_wizard_form`: asistentul cu rândurile colorate, avertismentele și opțiunile.
- `res_config_settings_view_form_ubl_review`: setările din secțiunea Vendor Bills.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_account_ubl_import](../deltatech_account_ubl_import/index.md): modulul de bază (dependență) care oferă `account.ubl.import.mixin`, folosit pentru parsarea XML și potrivirea produselor.
