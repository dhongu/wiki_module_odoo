# Reminder Zilnic de Activități

- **Nume Tehnic:** `deltatech_activity_reminder`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_activity_reminder
- **Cale Locală:** `odoo-addons/bitshop/deltatech_activity_reminder`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Trimite fiecărui utilizator, o dată pe zi și la ora aleasă de el, un singur email cu activitățile scadente astăzi și pe cele întârziate, ca nimic să nu rămână uitat în chatter-ul unui document. Managerii primesc în plus restanțele echipei lor, pe persoane.

#### 2. Funcționalități Cheie

- Un email pe zi, grupat pe tip de document (Contact, Comandă de vânzare, Tichet etc.), cu tipul și sumarul activității, documentul (link direct), scadența și numărul de zile de întârziere; butonul final deschide lista standard *Activitățile mele*, filtrată pe întârziate și de azi.
- Fiecare utilizator alege în *Preferințe*, tabul *Reminder activități*, ora (în fusul orar propriu) și zilele săptămânii (implicit luni–vineri); *Trimite-mi reminderul acum* trimite emailul imediat, ca previzualizare.
- Fără activități scadente sau întârziate (și fără restanțe de echipă) nu se trimite niciun email.
- Restanțe de echipă pentru manageri: administratorul completează *Echipă reminder* pe formularul utilizatorului (*Setări → Utilizatori și companii → Utilizatori*); sunt listate doar activitățile pe documente pe care managerul are voie să le citească.
- Setări de administrator (*Setări → Setări generale → Reminder activități*): tipuri de documente excluse, numărul maxim de linii pe secțiune (implicit 20) și butonul de activare pentru toți utilizatorii interni. După instalare reminderul este oprit pentru toți.
- Acțiune planificată orară; activitățile sunt citite cu drepturile fiecărui utilizator. Necesită servere de email de ieșire configurate. Pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- `mail`

#### 4. Componente Cheie

**Modele**

- `res.users` (extins): preferințele de reminder (activare, oră, zile, echipă, data ultimului reminder) și trimiterea emailului.
- `res.company` (extins): setările comune ale reminderului.
- `res.config.settings` (extins): tipurile de documente excluse, liniile pe secțiune, activarea pentru toți.

**Vizualizări**

- `view_users_form_activity_reminder`, `view_users_form_simple_modif_activity_reminder`: tabul *Reminder activități* pe formularul utilizatorului și în preferințe.
- `res_config_settings_view_form_activity_reminder`: blocul de setări generale.
- `activity_reminder_templates.xml`: șablonul emailului.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_activity_reminder` (*Activity Reminder: send daily emails*): rulează din oră în oră și trimite emailul fiecărui utilizator o dată pe zi, după ora aleasă.

#### 5. Conexiuni

- Fără conexiuni către alte module din wiki; modulul depinde doar de `mail` (Discuss).
