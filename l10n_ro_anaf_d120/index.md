# Romania - ANAF D120 Declaration (localizat la `l10n_ro_anaf_d120/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d120`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d120
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d120`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Acest modul permite generarea Declarației 120 (Decont privind accizele) direct din Odoo Enterprise, oferind o soluție completă pentru companiile care produc, comercializează sau utilizează produse supuse accizelor. Declarația 120 este un document fiscal centralizator care raportează obligațiile de plată ale accizelor, fiind strâns corelat cu decontul de TVA, dar adăugând dimensiunea cantitativă specifică regimului accizelor.

#### 2. Funcționalități Cheie

- **Raportare cantitativă:** calculul automat al cantităților conform unităților de măsură fiscale (hl, hl alcool pur, kg, GJ, 1000 bucăți).
- **Integrare cu taxele Odoo:** maparea rândurilor din declarație pe baza tag-urilor fiscale din planul de conturi.
- **Automatizare transformări:** utilizarea unor coeficienți de conversie (ex: grade Plato la hl) pentru raportarea precisă în XML.
- **Export direct:** buton de export XML în raportul de taxe, eliminând operarea manuală a datelor.

#### 3. Dependențe

- `l10n_ro_excise`
- `[[l10n_ro_anaf_base]]`

#### 4. Componente Cheie

**Modele / Vizualizări**

*Modulul nu conține fișiere `data`; logica este implementată în handlerul de raport din `models/` care extinde infrastructura de raportare a accizelor și mixin-ul ANAF.*

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din raportul de taxe.*

#### 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_anaf_d100]]`
- `[[l10n_ro_anaf_d300]]`
