# Proiecte Kaizen (localizat la `deltatech_kaizen/index.md`)

- **Nume Tehnic:** `deltatech_kaizen`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_kaizen
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_kaizen`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Kaizen este o metodă de îmbunătățire continuă prin proiecte mici, care corectează pe rând câte o pierdere măsurabilă. Modulul înregistrează fiecare îmbunătățire ca proiect legat de o pierdere: de la nivelul de bază dinainte de intervenție, prin analiza cauzelor și acțiunile corective, până la economiile verificate după remediere.

#### 2. Funcționalități Cheie

- Pierderea de bază pe lună înainte de remediere, cu data ei, și opțional pierderea țintă.
- Analiza *5 Why* (până la cinci linii, una marcată drept cauză rădăcină) și diagrama *Ishikawa* pe cele șase categorii: Man, Machine, Method, Material, Measurement, Environment.
- Acțiuni corective cu responsabil, termen, marcaj de întârziere (roșu) și dată de finalizare (verde).
- Pierderea măsurată după remediere; *Monthly Savings* = pierdere de bază minus pierdere curentă, *Annual Savings (projection)* = economie lunară × 12, iar *Target Reached* se bifează când ținta este atinsă.
- Flux fix: Draft → Analysis → Actions → Verification → Done; la salvare proiectul primește referința `KZN/`.
- Închiderea (*Close project*) este permisă doar managerului Kaizen, din starea Verification, cu cauză rădăcină, toate acțiunile terminate, bază pozitivă și pierdere măsurată; *Cancel* este tot doar pentru manager.
- Meniuri **Kaizen → Projects**, **Ishikawa** (cauzele tuturor proiectelor, grupate pe categorii) și **Actions** (lista de urmărire pentru ședința săptămânală). Pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- `mail`

#### 4. Componente Cheie

**Modele**

- `kaizen.project`: proiectul de îmbunătățire (cu chatter și activități).
- `kaizen.why`: liniile analizei 5 Why.
- `kaizen.ishikawa.cause`: cauzele Ishikawa pe categorii.
- `kaizen.action`: acțiunile corective.

**Vizualizări**

- `views/kaizen_project_views.xml`: lista și formularul proiectului, cu filele de analiză, acțiuni și rezultate.
- `views/kaizen_menu.xml`: meniurile Kaizen.

**Acțiuni Automate / Acțiuni Server**

- `data/ir_sequence_data.xml`: secvența `KZN/` pentru proiecte (nu există cron).

#### 5. Conexiuni

- `mail`: istoric și activități pe proiect.
