# Sale Withdrawal (localizat la `deltatech_sale_withdrawal/index.md`)

- **Nume Tehnic:** `deltatech_sale_withdrawal`
- **Versiune:** `19.0.0.3.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_withdrawal
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_withdrawal`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează funcția de retragere din contract (dreptul de renunțare) cerută consumatorilor UE de Directiva (UE) 2023/2673, care a adăugat articolele 11a și 14a la Directiva Drepturilor Consumatorilor 2011/83/UE — aplicabilă din 19 iunie 2026 oricărui comerciant care vinde online către consumatori din UE, transpusă în România prin OUG 18/2026. Spre deosebire de o simplă cerere de anulare, retragerea este un act unilateral al consumatorului: produce efecte din momentul confirmării, iar comerciantul o confirmă de primire, nu o aprobă. Modulul expune pe portal un buton clar etichetat, accesibil și fără cont (inclusiv pentru comenzile ca invitat), cu un flux în doi pași — recapitulare, apoi confirmare separată — fără a cere un motiv, urmat de o confirmare automată pe suport durabil (e-mail plus PDF) cu data și ora exacte ale transmiterii.

#### 2. Funcționalități Cheie

- Buton de retragere clar etichetat, vizibil pe pagina comenzii din portal pe toată durata perioadei de retragere, sub un titlu propriu de secțiune („Right of withdrawal") cu ancoră proprie în navigarea rapidă (navspy) a portalului.
- Accesibil **fără cont**, deci acoperă și comenzile plasate ca invitat (guest checkout).
- Flux în doi pași: recapitulare a contractului, apoi buton separat de confirmare.
- **Fără motiv obligatoriu** — consumatorul nu trebuie să justifice retragerea.
- Confirmare automată de primire pe suport durabil (e-mail plus PDF), cu conținutul declarației și data **și ora** exactă a transmiterii.
- Retragere parțială, pe linie de comandă. Linia ia proporțional valorile liniei de comandă, fără și cu TVA; **totalul retragerii e cu TVA** — ce se rambursează consumatorului (art. 13) —, iar PDF-ul de confirmare arată suma cu TVA. Totalul cuprinde produsele; costul livrării la o retragere integrală se rambursează separat.
- Pe retragere, *Mod de execuție* se afișează cu eticheta modului; codul rămâne stocat, ca să fie citibil și după dezinstalarea modulului care l-a adus.
- Excepții legale (art. 16) declarate pe produs sau pe categorie de produs, afișate consumatorului ca neeligibile, nu ascunse.
- Registru de retrageri în Vânzări, cu termenul de rambursare din art. 13 și activitate programată pentru responsabil.
- Contract de execuție conectabil (pluggable), astfel încât urmărirea operațională (retur de stoc, notă de credit, sistem extern) se adaugă prin alte module, fără a atinge acest modul.
- Interfață tradusă integral în română (`i18n/ro.po`).
- **Configurare** în *Vânzări → Configurare → Setări → Withdrawal from Contract*: *Withdrawal Function* (expune butonul pe portal; perioada legală e de minimum 14 zile, o perioadă comercială mai lungă e permisă, una mai scurtă nu), *Withdrawal Period (days)* (implicit 14), *Refund Deadline* (zile pentru rambursare după informare, art. 13, implicit 14), *Withdrawal Execution* (modul implicit `Manual` e suficient legal: retragerea se înregistrează, consumatorul primește confirmarea și se programează o activitate; alte module adaugă alte moduri) și *Use Odoo's Native Withdrawal Button* (ascunde butonul modulului fără dezinstalare; registrul și înregistrările vechi rămân neatinse).
- **Excepții art. 16 pe produs**: câmpul *Withdrawal Exception* (la comandă, produse igienice sigilate, perisabile, suporturi desigilate, conținut digital deja livrat) se moștenește din categorie dacă nu e setat pe produs.
- Înainte de punerea în producție, e-mailul de confirmare a comenzii trebuie să conțină linkul de portal cu token de acces; fără el, un invitat nu poate ajunge la buton.
- Pe portal, după expirarea perioadei butonul rămâne pe pagină, dar dezactivat și cu explicație, ca existența lui să poată fi verificată ulterior; pagina urmează limba portalului. Consumatorul poate alege opțional un motiv și poate adăuga detalii.
- Dacă trimiterea confirmării eșuează, retragerea rămâne înregistrată, dar marcată ca neconfirmată, iar responsabilul comenzii primește o activitate; până la trimitere, perioada de retragere se extinde la douăsprezece luni, iar un cron orar reîncearcă.
- În registrul *Vânzări → Comenzi → Withdrawals*: filtre *Not Acknowledged* și *Refund Overdue*, grupare după stare sau lună de transmitere; comanda are un buton **Withdrawals**; formularul retragerii are **Resend Acknowledgement** și **Mark Refunded** (înregistrările rambursate apar estompate). Modulul nu creează înregistrări contabile: rambursarea se face prin fluxul obișnuit de facturare și plată (notă de credit, retur de plată).
- Ghidul pas-cu-pas, cu capturi de ecran, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale`
- `portal`

#### 4. Componente Cheie

**Modele**

- `deltatech.sale.withdrawal`: înregistrarea unei retrageri legate de o comandă de vânzare, cu stare (`submitted` / `acknowledged` / `refunded` / `disputed`), data și canalul de transmitere, termenul de rambursare calculat și modul de execuție folosit; nu are stare „aprobat" — retragerea produce efecte prin confirmarea consumatorului, nu prin aprobarea comerciantului.
- `deltatech.sale.withdrawal.line`: liniile de retragere (produs, cantitate retrasă, subtotal), cu validare că se retrage doar cantitatea încă disponibilă din linia comenzii.
- `sale.order` (extins): expune retragerile comenzii, numărul lor, termenul-limită de retragere calculat pe linii și disponibilitatea butonului pe portal.
- `sale.order.line` (extins): calculează termenul de retragere per linie (începe la livrare pentru bunuri, la data comenzii pentru servicii) și determină eligibilitatea/excepția art. 16; liniile de avans (down payment) sunt excluse explicit din verificarea de eligibilitate și din lista de linii oferite pe portal, pentru că nu au produs și unitate de măsură proprii — corecție introdusă în 19.0.0.2.1 după ce lipsa acestei excluderi bloca deschiderea oricărei comenzi cu avans, atât în back office cât și pe portal.
- `product.template` / `product.category` (extinse): câmp de excepție de retragere (art. 16), moștenit din categorie dacă nu e setat pe produs.
- `res.company` / `res.config.settings` (extinse): activarea funcției, perioada de retragere, termenul de rambursare, modul de execuție și opțiunea de a folosi butonul nativ Odoo (când va exista).

**Vizualizări**

- `view_deltatech_sale_withdrawal_list` / `_form` / `_search`: registrul de retrageri din back office, cu evidențierea în roșu a înregistrărilor nefinalizate cu confirmarea de primire.
- `action_deltatech_sale_withdrawal`: acțiunea din meniul **Vânzări → Comenzi → Withdrawals**.
- `views/sale_order_views.xml`, `views/product_views.xml`, `views/res_config_settings_views.xml`: integrarea pe formularul comenzii, pe produs și în setările Vânzărilor.
- `views/portal_templates.xml`: paginile portalului — recapitulare, confirmare și status al retragerii, accesibile prin link cu token, inclusiv pentru invitați. Secțiunea butonului de pe pagina comenzii are acum titlu propriu (`<h3>Right of withdrawal</h3>`), care generează automat o ancoră separată în navspy-ul portalului; butonul activ e stilizat `btn-primary` (anterior `btn-secondary`), pentru a-l scoate în evidență față de restul acțiunilor secundare ale comenzii.
- `report/withdrawal_report.xml`: raportul PDF anexat la confirmarea de primire.

**Migrare de la numele vechi**

- `hooks.py` → `pre_init_hook`: preia datele modulelor `bitshop_sale_withdrawal` / `bitshop_sale_withdrawal_stock`, cum se numeau înainte de redenumirea `bitshop_*` → `deltatech_*`. Modulele vechi erau deja instalate la Damira (și probabil la Romchim). Hook-ul redenumește pe loc tabelele (inclusiv cele many2many), coloanele `bitshop_withdrawal_*`, constrângerile, indecșii, secvențele, `ir_model` / `ir_model_fields`, xml id-urile și referințele la model din chatter, followeri, activități și atașamente. Fără el, retragerile înregistrate rămâneau în tabele orfane, iar Odoo le-ar fi șters la actualizarea modulelor vechi. Modulele vechi rămân în bază ca stub-uri care depind de cele noi, în repo-ul proiectului, așa că hook-ul rulează înainte de crearea tabelelor noi. Pe o instalare nouă nu face nimic.

**Acțiuni Automate / Acțiuni Server**

- `cron_withdrawal_ack_retry`: cron orar care reîncearcă trimiterea confirmării de primire pentru retragerile netrimise încă — cât timp confirmarea nu a plecat, obligația legală rămâne neîndeplinită, iar perioada de retragere se extinde la douăsprezece luni.

#### 5. Conexiuni

- [deltatech_sale_withdrawal_stock](../deltatech_sale_withdrawal_stock/index.md): extensie care depinde de acest modul și de `sale_stock`, adăugând anularea sau returul efectiv de stoc la execuția retragerii.
- [deltatech_rma](../deltatech_rma/index.md): returul comercial — act juridic diferit, model separat intenționat; puntea [deltatech_rma_withdrawal](../deltatech_rma_withdrawal/index.md) dă retragerii fișa cu cod de bare și recepția prin scanare.
- `mail`: (dependență tranzitivă, prin `sale` și `portal`) infrastructura de e-mail și șablon folosită pentru confirmarea de primire pe suport durabil.
