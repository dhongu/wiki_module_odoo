# POS ECR Base (localizat la `deltatech_pos_base/index.md`)

- **Nume Tehnic:** `deltatech_pos_base`
- **Versiune:** `19.0.1.2.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_pos_base
- **Cale Locală:** `odoo-addons/bitshop/deltatech_pos_base`
- **Ultima Ingestie:** `2026-11-18`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul este stratul de bază al suitei Terrabit de Point of Sale pentru casele de marcat fiscale (ECR) din România. Păstrează setările casei de marcat și codurile ECR ale metodelor de plată și ale taxelor și le încarcă în fiecare sesiune POS, astfel încât modulele de tipărire (`deltatech_pos`, `deltatech_ecr_connect`) să poată construi bonul fiscal. Singur, nu tipărește nimic.

#### 2. Funcționalități Cheie

- **Case de marcat și drivere:** funcționează cu Datecs, Optima, Incotex, Daisy și Succes, precum și cu alte modele care folosesc aceeași sintaxă de comenzi; testat extensiv cu driverele certificate FiscalWire și FiscalNet. Formatul comenzii (**ECR type**) se setează pe fiecare punct de vânzare.
- **Transportul comenzii către dispozitiv** (**ECR transport**):
  - *File (.prn/.inp download)*: fișier de comandă descărcat și preluat de driverul de pe casă (**File prefix** `order` și **File extension** `inp` implicit);
  - *Terrabit Connect (local agent)*: comanda se trimite agentului local (**Agent URL**, implicit `http://127.0.0.1:8765`), care o tipărește și returnează rezultatul sincron;
  - *DxPrint (local driver)*: bonul se trimite ca JSON driverului DxPrint (**Driver URL** implicit `http://127.0.0.1:8080`, plus utilizator și parolă dacă driverul are autentificare), care returnează imediat numerele bonului și ale raportului Z; rapoartele X/Z și operațiunile de numerar au cereri proprii;
  - pentru agent și DxPrint, dacă dispozitivul nu poate fi contactat, se revine la descărcarea fișierului.
- **Coduri ECR pe metodele de plată:** câmpul **Cod ECR** (un singur caracter, implicit `0`) identifică tipul de încasare (numerar, card, tichet) și se trimite cu fiecare bon.
- **Coduri ECR pe taxe:** câmp opțional **Cod ECR**, pentru două taxe cu aceeași cotă (de exemplu garanție SGR și vânzare cu taxare inversă, ambele 0%). Gol = categoria se deduce din procentul taxei; valoarea este poziția de TVA programată pe dispozitiv (pentru FiscalWire/datecs18, cifră de la 1 la 7, nu litera A–E).
- **Departament implicit:** trimis pe fiecare linie de vânzare; gol = departamentul se deduce din cota de TVA; se completează pentru dispozitive cu departamente fixe (FiscalNet / Tremol).
- **Nume lungi de produse:** **Trim long product name** și **Trim to** (implicit 30) scurtează numele la lungimea acceptată de imprimanta fiscală.
- **Casă de marcat simulată** pentru teste, demonstrații și suport, fără dispozitiv: *Simulated in Odoo (no agent)* sau *Simulated through the agent*, cu **Delay (ms)**; doar administratorul de sistem o poate activa sau dezactiva. Răspunsul simulat depinde de ultimele cenți ale totalului (`,91` fără hârtie, `,92` casă deconectată, `,93` răspuns întârziat, `,94` fără răspuns, `,95` bon anulat pe casă; cardul folosește `,01`–`,05`). Nimic tipărit în simulare nu este bon fiscal; simularea se oprește pe punctele de vânzare reale înainte de lansare.
- **Unde se configurează:** ecranele standard Odoo, fără meniu propriu: **Point of Sale → Configuration → Settings** (secțiunea ECR), **Point of Sale → Configuration → Payment Methods** și **Accounting → Configuration → Taxes**. După modificarea unui cod ECR se închide și se redeschide sesiunea POS. Pașii detaliați sunt în fișa consultant.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md`, `CONFIGURE.md` și `USAGE.md`; componentele de mai jos sunt cele declarate în manifest și verificate pe cod.

**Modele**

- `pos.payment.method` (extindere): câmpul `cod_ecr`, expus datelor încărcate în POS.
- `pos.config` (extindere): `ecr_type`, `ecr_trim`, `ecr_trim_to`, `file_prefix`, `file_ext`, `default_department`, `ecr_transport`, `ecr_connect_url`, câmpurile DxPrint (`ecr_dxprint_url`, `ecr_dxprint_user`, `ecr_dxprint_password`) și câmpurile de simulare (`ecr_simulation`, `ecr_simulator_next`, `ecr_simulator_sticky`, `ecr_simulator_delay_ms`).
- `account.tax` (extindere): câmpul `cod_ecr`, categoria dispozitivului pentru taxe cu aceeași cotă.
- `res.config.settings` (extindere): expune setările ECR în ecranul de setări al Point of Sale.
- `ir.http` (extindere): extinde datele de sesiune.

**Vizualizări**

- `pos_payment_method_view_form`: adaugă `cod_ecr` pe formularul metodei de plată POS.
- `account_tax_view_form`: adaugă `cod_ecr` pe formularul taxei.
- `res_config_settings_view_form`: secțiunea ECR din setările Point of Sale.

#### 5. Conexiuni

- [deltatech_pos](../deltatech_pos/index.md): modul care folosește această bază pentru tipărirea bonului fiscal.
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): transport către casa de marcat (agent local, panou *Virtual devices* pentru simulare).
