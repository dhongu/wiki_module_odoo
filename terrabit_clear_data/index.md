# Clear Data (localizat la `terrabit_clear_data/index.md`)

- **Nume Tehnic:** `terrabit_clear_data`
- **Versiune:** `20.0.1.0.15`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_clear_data
- **Cale Locală:** `odoo-addons/terrabit/terrabit_clear_data`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Asistent (*Setări > Tehnic > Clear Data*) care șterge datele tranzacționale ale unei baze de date (stoc, vânzări, achiziții, facturi, contabilitate, proiecte, producție, documente de service) și, opțional, datele de bază (liste de materiale, produse, parteneri), pentru o companie sau pentru toate. Este util la pregătirea unei baze de test sau la resetarea unei baze după încărcări de probă. Operația este ireversibilă și cere confirmare explicită.

#### 2. Funcționalități Cheie

- Opțiuni separate de ștergere: documente de stoc, vânzare, achiziție, facturi, documente contabile, proiecte, comenzi de producție, documente de service, mailuri; opțional LDM, produse (toate, finite, semifabricate) și parteneri.
- Confirmare obligatorie (bifa „Sunt sigur că vreau să șterg datele!”) și alegerea companiei (implicit compania curentă).
- Opțiuni pentru resetarea website-ului și încărcarea datelor demo.
- Scripturi proprii ale modulelor, fără ca acestea să depindă de `terrabit_clear_data`: `data/clear_data_transactional.sql` (rulat cu opțiunea de ștergere a datelor tranzacționale din module, bifată implicit) și `data/clear_data_master.sql` (date de bază din module), rulate în ordinea inversă a dependențelor.
- Scripturile primesc parametrii `%(company_ids)s` (compania aleasă sau toate) și `%(delete_shared)s` (datele fără companie pot fi șterse); un `%` literal se scrie `%%`. După rulare se curăță urmăritorii, mesajele, activitățile și atașamentele înregistrărilor șterse.
- Ștergerea se face în loturi, cu jurnalizarea progresului.
- La ștergerea unei companii se curăță în prealabil depozitele, regulile de stoc, site-urile și conturile contabile asociate.
- Acces rezervat administratorilor (`base.group_system`).

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `ir.data.clear`: asistentul de ștergere, cu opțiunile și logica de curățare.
- `res.company` (extins): `unlink` curăță depozitele, regulile de stoc, site-urile și conturile asociate companiei.

**Vizualizări**

- `view_clear_data_form`: formularul asistentului de ștergere.
- `action_clear_data`: acțiunea și meniul din Setări > Tehnic.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- Orice modul poate livra `data/clear_data_*.sql` pentru a fi inclus în curățare, fără dependență de acest modul.
