# Export XML SAGA (bază)

- **Nume Tehnic:** `deltatech_saga_xml`
- **Versiune:** `20.0.1.0.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_saga_xml`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_saga_xml`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic care construiește fișierele XML de import SAGA pentru facturile de vânzare, pornind din date simple ale facturilor, fără să citească facturile din baza de date. Este folosit de serverul IAP Terrabit pentru bazele de date care nu pot rula Python (Odoo Online) și nu are meniuri proprii: alt modul apelează modelul `saga.xml`.

#### 2. Funcționalități Cheie

- Primește un dicționar de date (format versiunea 1) cu compania, opțiunile exportului și, pentru fiecare factură, antetul, clientul și liniile, cu faptele din baza de date deja rezolvate (coduri SAGA, conturi, cote de TVA, grupuri de taxe, curs). Fiecare valoare este verificată; o factură care nu e de client este omisă, cu mesaj.
- Scrie fișierele `CLI_<perioadă>.xml` (clienții), `f_<CUI>_IE_<jurnal>_<perioadă>.xml` (facturi în moneda companiei, bonurile cu sufixul `C`) și `f_<CUI>_IEV_<jurnal><monedă>_<perioadă>.xml` (facturi în valută și ale clienților străini).
- Aplică regulile exportului clasic SAGA pe valoare: tipul documentului (poziția fiscală, bon, factură de bon fiscal, taxare inversă internă), TVA la încasare, codul clientului (CUI sau cod completat cu zerouri), contul în notația SAGA (419 cu codul clientului), semnul notelor de credit, cursul (HUF la 100 de unități) și facturile cu linii mixte de taxare inversă și regulate.
- Export în doi pași: fiecare lot devine o parte stocabilă, iar părțile tuturor loturilor dau câte un fișier din fiecare fel, pentru perioade lungi.
- Opțiuni: cod client = CUI, lungimea codului, TVA la încasare pentru toate, formatul datei, tratarea facturilor mixte (omite, taxare inversă, regulat), un fișier per fel.
- Apeluri: `_saga_export_zip(data)` pentru un lot și o arhivă; `_saga_prepare` și `_saga_files` pentru mai multe loturi.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `saga.xml` (model abstract): validarea datelor, regulile formatului SAGA și generarea fișierelor XML și a arhivei.

**Vizualizări**

- Niciuna (modul tehnic, fără meniuri).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_saga](../deltatech_saga/index.md): interfața SAGA clasică, ale cărei reguli de export ale facturilor de vânzare sunt reproduse aici.
- [deltatech_saga_online](../deltatech_saga_online/index.md): exportul SAGA pentru Odoo Online, ale cărui fișiere sunt construite de serverul Terrabit cu acest modul.
