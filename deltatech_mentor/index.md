# Mentor Interface (localizat la `deltatech_mentor/index.md`)

- **Nume Tehnic:** `deltatech_mentor`
- **Versiune:** `20.0.2.2.5`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_mentor`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_mentor`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite ținerea contabilității în WinMentor, în timp ce vânzările, achizițiile și stocurile se fac în Odoo. Pentru o perioadă aleasă, exportă din Odoo documentele de care are nevoie WinMentor, în formatul text al meniului său „Import date din alte aplicații", împachetate într-un singur fișier ZIP: parteneri, articole, facturi de furnizor și de client, documente de stoc și producție, plăți și încasări.

#### 2. Funcționalități Cheie

- **Parteneri și articole:** exportate cu codurile după care face potrivirea WinMentor: codul fiscal (CUI, cu RO pentru plătitorii de TVA) sau CNP pentru persoane fizice, și referința internă a produsului sau un cod per categorie de produs.
- **Achiziții:** facturi și note de credit de furnizor, separate în facturi interne și intracomunitare (acestea din urmă cu taxare inversă) și importuri din afara UE (cu codul de vamă), plus recepții de achiziție (bonuri fiscale de intrare).
- **Vânzări:** facturi, note de credit și bonuri de vânzare, un fișier per jurnal, cu seria facturii luată din jurnal.
- **Stoc și producție:** bonuri de consum și predări din producție între locația de stoc și cea de producție, avize de expediție și de intrare, plus lista gestiunilor.
- **Plăți și încasări:** opțional, plățile și încasările postate din perioadă, un fișier per jurnal.
- **Conturi contabile românești:** conturile Odoo sunt convertite în conturi WinMentor (cont sintetic fără zerouri finale, sufix analitic pe numărul ales de cifre).
- **O companie pe rând:** se exportă doar documentele companiei alese, iar jurnalele altei companii sunt refuzate.
- **Flux de utilizare:** *Facturare > Contabilitate > Mentor > Export Mentor* (sau *Contabilitate > Contabilitate > Mentor > Export Mentor* cu aplicația Contabilitate); se aleg perioada (luna precedentă implicit), **Locația de stoc**, **Locația de producție** și opțiunile: jurnale (toate dacă e gol), **Cod Vamă** pentru importuri, **Cod PF** fix pentru persoane fizice, **Export Payments**, **Only Category**, **All Products As Service**, **Use Internal Code** (ID-ul Odoo drept cod de articol), **Analytic Digits**, **Use Invoice Date** pentru facturile de furnizor (în loc de data contabilă) și **Compania**. Rezultatul listează câte documente din fiecare tip au fost exportate; se verifică cifrele și se descarcă ZIP-ul.
- **Import în WinMentor:** se despachetează arhiva și se importă fiecare fișier din *Intrări > Import date din alte aplicații*, începând cu `Partner.txt` și `Articole.txt`; pentru facturile de furnizor se alege seria NIR (*Carnet NIR*) și fișierul *Facturi Intrare*. WinMentor importă partenerii și articolele o singură dată; modificările ulterioare trebuie făcute în ambele sisteme.
- **Configurare în Odoo:** pe categoria de produs se completează **Simbol Tip Contabil**, **Gestiune Mentor**, **Way Production** (pentru categorii de producție), **Mentor UOM** (dacă WinMentor folosește altă unitate) și, opțional, **Mentor Use Article** (debifat = întreaga categorie ca un singur articol, cu **Cod Articol**); pe locațiile de stoc exportate ca gestiuni, **Simbol Mentor**; pe jurnalele de vânzare și de achiziție, **Serie Carnet Mentor**; partenerii au cod fiscal (sau CNP), produsele au referință internă potrivită cu codul articolului din WinMentor, iar conturile se completează pe categorii și parteneri. În WinMentor se mapează partenerii după CUI și articolele după cod și se setează configurarea contabilă a articolelor.
- **Erori și rezerve:** o linie de factură client fără produs oprește exportul cu numărul facturii, iar **Ignore Errors** o listează în rezultat și continuă; o factură de furnizor cu linie fără produs oprește mereu exportul. Partenerul fără cod fiscal se exportă cu `id_<ID partener>`, iar produsul fără referință internă cu `ID_<ID produs>`.
- Fluxul pas cu pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `product`
- [deltatech_contact](../deltatech_contact/index.md)
- `stock`
- `l10n_ro`

#### 4. Componente Cheie

*Readme-ul acoperă funcționalitățile, dar nu detaliază componentele tehnice; elementele de mai jos au fost confirmate în cod.*

**Modele**

- `export.mentor` (wizard, `wizard/export_mentor.py`): construiește fișierele text WinMentor (parteneri, articole, facturi, bonuri, avize, plăți, încasări, gestiuni) și arhiva ZIP.
- `product.category` (extindere): câmpurile de mapare WinMentor (tip contabil, gestiune, unitate, utilizare articol).
- `stock.location` (extindere): `Simbol Mentor` al gestiunii.
- `account.journal` (extindere): `Serie Carnet Mentor`.
- `res.partner` (`l10n_ro_vat_subjected`) și `stock.picking` (`l10n_ro_notice`): câmpuri auxiliare folosite la export.

**Vizualizări**

- `view_export_mentor_form` și `action_export_mentor` (`wizard/export_mentor_view.xml`): asistentul de export.
- `views/mentor_menu.xml`: meniul *Mentor*.
- `product_category_form_view`, `view_location_form`, `view_account_journal_form`: câmpurile WinMentor pe categorie, locație și jurnal.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește acțiuni programate.

#### 5. Conexiuni

- [deltatech_contact](../deltatech_contact/index.md): sursa datelor de contact (partenerii) folosite la export și maparea prin cod extern / CUI.
