# Romania - Majorare colectivă a salariilor (localizat la `l10n_ro_hr_salary_increase/index.md`)

- **Nume Tehnic:** `l10n_ro_hr_salary_increase`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_hr_salary_increase
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_salary_increase`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Modulul majorează salariile mai multor angajați deodată, fără să deschideți fiecare contract. Alegeți angajații și metoda, verificați previzualizarea, iar modulul creează versiunile noi ale contractelor de la data de efect, actele adiționale și transmite modificarea în REGES.

#### 2. Funcționalități Cheie

- **Metode de majorare:** procent din salariul actual (rotunjit la leu), sumă fixă adăugată, salariu nou identic pentru toți cei aleși sau noul salariu minim (urcă doar contractele aflate sub minim; valoarea vine din parametrii salariali RO, nivelul S1 sau S2 al contractului, proporțional cu timpul de lucru la norma parțială și rotunjită în sus la leu).
- **Selecția angajaților:** toți angajații companiei, departamente (cu subdepartamente), funcții sau angajați aleși; asistentul se deschide și din lista de angajați (Acțiuni), cu cei selectați. Se iau doar angajații cu contract în vigoare la data de efect.
- **Previzualizare** cu salariul actual, salariul nou (editabil pe linie), diferența în lei și procente, totaluri și avertizări: contracte cu versiuni după data de efect (excluse implicit), salariu nou sub minim, fluturași deja validați după data de efect (nu se recalculează), contracte neactive în REGES.
- **Aplicare:** se creează versiunea nouă a contractului de la data de efect (cea veche rămâne neschimbată, deci lunile anterioare nu se modifică) și o notă în fișa angajatului cu salariul vechi, cel nou și motivul.
- **Acte adiționale:** opțional (bifa *Generează acte adiționale*), create în ciornă și tipărite într-un singur PDF; la majorarea la salariul minim bifa e oprită implicit, deoarece modificarea operează de drept (art. 164 din Codul muncii). Se avertizează la o dată de efect în trecut (art. 17 alin. (5) din Codul muncii).
- **Transmitere în REGES** (`ModificareContract`) pentru contractele active; rezultatul apare pe fiecare linie (*Trimis*, *Eroare* cu mesajul REGES sau *Netransmis*).
- **Flux:** Stat de plată → Angajați → Majorare colectivă a salariilor (RO), cu rolul *Administrator* din Stat de plată; pași: alegere angajați și metodă, previzualizare (cu reîmprospătare după schimbarea selecției), aplicare cu confirmare.
- **Configurare:** salariul minim din Stat de plată → Configurare → Parametri reguli (la o creștere prin hotărâre de guvern se adaugă valoarea nouă cu data de aplicare); conexiunea REGES din Setări → REGES-Online; pentru construcții se alege nivelul S2 pe contract.
- **Limită:** diferențele pentru luni deja calculate nu se recalculează automat.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- [l10n_ro_hr_documents](../l10n_ro_hr_documents/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.salary.increase`: asistentul (model tranzitoriu) cu selecția angajaților, metoda, data de efect, motivul, previzualizarea și aplicarea.
- `l10n.ro.salary.increase.line`: linia de previzualizare pe angajat (salariu actual/nou, diferență, avertizări, versiunea creată, actul adițional, rezultatul REGES).

**Vizualizări**

- `view_l10n_ro_salary_increase_form`: formularul asistentului de majorare colectivă.

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_salary_increase`: acțiunea de fereastră „Collective Salary Increase”, accesibilă din meniul Stat de plată → Angajați și din lista de angajați.

#### 5. Conexiuni

- [l10n_ro_reges](../l10n_ro_reges/index.md): transmiterea modificării de contract în REGES; starea contractului în REGES (`l10n_ro_reges_state`) este citită la aplicare.
