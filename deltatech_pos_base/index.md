# Deltatech POS Base (localizat la `deltatech_pos_base/index.md`)

- **Nume Tehnic:** `deltatech_pos_base`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_pos_base
- **Cale Locală:** `odoo-addons/bitshop/deltatech_pos_base`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul reprezintă stratul de integrare fundamental dintre sistemele Point of Sale (POS) și casele de marcat electronice (ECR) ale Odoo, oferind definițiile de bază și structurile de date necesare pentru tipărirea fiscală. Din punct de vedere business, este modulul esențial pentru companiile care trebuie să își conecteze POS-ul Odoo sau POS Backend la dispozitive fiscale externe, pentru a asigura conformitatea cu reglementările. El standardizează câmpurile și metodele folosite atât de modulele front-end, cât și de cele back-end de POS, astfel încât operațiunile cu ECR să fie consistente, iar dezvoltarea modulelor fiscale specifice unei piețe să fie simplificată pe o bază comună.

#### 2. Funcționalități Cheie

- Integrare robustă POS-ECR: oferă o fundație stabilă pentru comunicarea dintre Odoo și imprimantele fiscale sau casele de marcat conectate.
- Structură de date unificată: standardizează câmpurile și metodele utilizate de modulele POS de tip front-end și back-end pentru operațiuni ECR consistente.
- Conformitate fiscală simplificată: facilitează dezvoltarea și implementarea modulelor fiscale specifice fiecărei piețe pe o bază comună.
- Înregistrare fiabilă a tranzacțiilor: asigură capturarea și formatarea consecventă a datelor POS esențiale pentru fiscalizare.
- Operațiuni de retail scalabile: permite extinderea ușoară a rețelei de magazine folosind o bază POS comună pentru toate locațiile și tipurile de dispozitive fiscale.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de cod nu au fost analizate în detaliu deoarece `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie. Mai jos sunt listate elementele declarate în `__manifest__.py`.

**Vizualizări**

- `views/pos_payment_method_view.xml`: extinde configurarea metodelor de plată POS pentru integrarea cu dispozitivele fiscale (ECR).
- `views/res_config_settings_views.xml`: adaugă opțiunile de configurare POS-ECR în setările aplicației (Settings).

#### 5. Conexiuni

- [deltatech_pos](../deltatech_pos/index.md): modul soră care folosește această bază pentru funcționalitatea de Point of Sale Deltatech.
