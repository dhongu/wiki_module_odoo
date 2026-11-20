# Portal Clienți B2B (B2B Customer Portal) (localizat la `deltatech_b2b_portal/index.md`)

- **Nume Tehnic:** `deltatech_b2b_portal`
- **Versiune:** `19.0.1.4.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_b2b_portal
- **Cale Locală:** `odoo-addons/bitshop/deltatech_b2b_portal`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un portal pentru clienții persoane juridice de pe website-ul Odoo: firmele cer un cont dintr-o pagină publică, un agent de vânzări îl aprobă dintr-un singur clic, iar apoi fiecare contact al firmei vede în portal ce contează pentru un cumpărător business: soldul, facturile restante, creditul disponibil și agentul de vânzări. Este baza familiei Terrabit B2B; comanda rapidă după cod, listele de comandă salvate și treptele de preț pe cantitate sunt module separate, construite peste el.

#### 2. Funcționalități Cheie

- Pagina publică **/b2b** cu formularul de cerere de cont: denumire firmă, CUI, nr. registrul comerțului, adresă, persoană de contact, cu câmp-capcană anti-spam și, opțional, acceptarea termenilor B2B. O cerere refuzată (câmp lipsă, e-mail sau CUI invalid, termeni neacceptați) reafișează formularul cu tot ce a introdus vizitatorul, iar câmpurile de corectat sunt marcate cu roșu. Pe un website românesc, un CNP introdus ca CUI este refuzat cu mesaj propriu (formularul e pentru firme), iar CUI-ul este pregătit pentru `l10n_ro_website_anaf_prefill` (completare automată din ANAF, dacă modulul e instalat).
- **E-mail opțional de confirmare** către cel care a trimis formularul (setarea *Confirmă cererile prin e-mail*, dezactivată implicit): text fix, fără nimic din formular în afară de CUI, deci formularul public nu poate fi folosit pentru a trimite cuiva un text propriu. **Limită de 5 cereri pe oră** de la aceeași adresă (IP); peste limită apare „Too many requests".
- **Cererea este chiar clientul**: formularul creează firma în starea *Solicitat* (cu contactul sub ea) și generează o activitate pentru agentul de vânzări; nu există un model separat de cereri care să dubleze datele.
- **Potrivire după CUI** (`RO 1234 5678` și `12345678` sunt aceeași firmă): la un client existent se adaugă doar contactul; datele introduse de un vizitator anonim nu suprascriu ce e deja înregistrat. Aceeași persoană care trimite de două ori nu duplică nimic; o cerere respinsă și arhivată care revine este dezarhivată.
- **Aprobare dintr-un clic**: contul devine activ, iar contactele care au cerut acces primesc invitația standard de portal. **Respingerea** cere motivul și poate arhiva firma (propus doar dacă nu are comenzi sau facturi).
- **Acordare acces portal** (buton pe o firmă cu cont deja activ): când un coleg al unui client existent trimite formularul, contactul este adăugat sub firmă și marcat „a cerut acces”; butonul trimite invitația standard de portal contactelor care au cerut și închide activitatea. Vizitatorul vede același mesaj ca la o cerere nouă (formularul nu dezvăluie cine e deja client).
- **Stare cont B2B** pe firmă (solicitat, activ, suspendat, respins) și **rol per contact**: poate comanda sau doar vizualizare (prețuri și documente). Rolul îl setează administratorul B2B.
- **Tablou de bord pe /my**: sold, restant, credit disponibil cu bară de utilizare (verde, galben de la 70%, roșu de la 90%), oferte în așteptare, facturi de plătit cu zile întârziere și cardul agentului de vânzări.
- **Blocarea comenzilor**: un contact „doar vizualizare" sau un cont suspendat nu poate finaliza coșul și nu poate semna sau plăti online o ofertă din portal; portalul explică motivul. Oferta deschisă din e-mail, fără autentificare, se semnează ca de obicei.
- **Meniuri** sub *Vânzări ▸ Comenzi*: *Cereri de cont B2B* (firmele în starea Solicitat, implicit) și *Clienți B2B* (conturi active și suspendate, cu sold, restanțe, credit disponibil); filtre pe contacte: *Clienți B2B*, *Cereri de cont B2B*, *B2B cu facturi restante*.
- **Activarea unui client existent**: *Acțiune ▸ Activare cont B2B* (administrator B2B) deschide wizardul standard de acces la portal; **Suspendă** oprește comenzile din portal fără a retrage accesul la documente, **Reactivează** le repornește fără invitație nouă.
- **Prețuri doar pentru clienți firmă** (setare pe website, dezactivată implicit): catalogul rămâne public și indexat, dar un vizitator sau o firmă fără cont B2B activ nu vede preț, stoc, filtru de preț, sortare după preț și nici butonul de adăugare în coș. Serverul exclude prețurile din pagină, din datele produsului și din sugestiile de căutare, iar un adaugă-în-coș trimis manual este refuzat; în locul prețului apare blocul standard *Contact Us*. Angajații și contactele firmelor cu cont activ (inclusiv cele „doar vizualizare”) văd prețurile normal. Setarea acoperă și feed-ul Google Merchant Center (produsele fără preț sunt omise) și ascunde panglica automată *Out of stock* pentru cine nu are voie să vadă stocul. Diferă de setarea standard *eCommerce Access ▸ Logged in users*, care închide tot magazinul.
- **Setări** (*Website ▸ Configurare ▸ Setări ▸ Portal B2B*): agentul de vânzări pentru cereri (implicit agentul website-ului), adresa termenilor B2B, confirmarea prin e-mail a cererilor și *Prețuri doar pentru clienți firmă*. Accesul în magazin doar pentru utilizatori autentificați se face cu setarea standard *eCommerce Access*.
- Drepturi de acces: **B2B Portal ▸ User** (aprobă, respinge, suspendă) și **B2B Portal ▸ Administrator** (activează clienți existenți, setează rolurile). Acțiunile de aprobare, suspendare și reactivare rulează cu drepturi de superutilizator, dar verifică mai întâi, pe utilizatorul care le apelează, rolul B2B User și dreptul de citire pe parteneri; un utilizator fără rol (inclusiv un client de portal care își reactivează singur firma suspendată) primește eroare de acces, inclusiv la apel RPC.
- **Metode ajutătoare pentru modulele construite peste acesta** (în controller): `_b2b_inactive_redirect()` trimite pe /b2b utilizatorul fără cont B2B activ, iar `_b2b_add_to_cart()` adaugă produse în coș, doar pe cele vândute pe website-ul curent. Sunt folosite de comanda rapidă și de listele de comandă salvate.
- Folosește mecanismele standard Odoo (agent de vânzări, limită de credit, listă de prețuri, termene de plată, invitație portal, acces eCommerce), fără duplicări. Limita de credit și facturile restante se impun prin `terrabit_partner_credit_limit` și `terrabit_partner_credit_limit_website`.
- Neinclus (planificat): aprobarea comenzilor plasate de colegi și completarea automată a datelor firmei dintr-un registru public.

#### 3. Dependențe

- `website_sale`
- `sale_management`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): câmpurile `b2b_state`, `b2b_role`, `b2b_access_requested`, `b2b_terms_accepted_date`, `b2b_note`, plus câmpuri calculate (`b2b_balance`, `b2b_overdue_count`, `b2b_overdue_amount`, `b2b_credit_available`); logica de creare/potrivire după CUI a cererilor, aprobare, respingere, suspendare, acordare acces portal (`action_b2b_grant_access`) și trimiterea confirmării (`_b2b_send_request_confirmation`); `_b2b_check_action_access()` verifică rolul B2B User și dreptul de citire ale apelantului înainte ca acțiunile să ruleze ca superutilizator.
- `website` (extins): `b2b_request_user_id`, `b2b_terms_url`, `b2b_request_confirmation` și `b2b_prices_companies_only`.
- `res.config.settings` (extins): expune cele patru setări ale website-ului.
- `product.template`, `product.product` (extinse): scot prețul din datele produsului pentru cine nu are voie să-l vadă.
- `product.feed` (extins): feed-ul Google Merchant Center fără preț când setarea e activă.
- `deltatech.b2b.reject.wizard`: wizard de respingere cu motiv obligatoriu și opțiunea de arhivare a firmei.

**Vizualizări**

- `view_partner_form_b2b`: fila B2B pe partener (stare, agent, listă de prețuri, termene, sold/restanțe/credit, butoane Aprobă / Respinge / Acordă acces portal / Suspendă / Reactivează).
- `view_partner_b2b_request_list` și `view_partner_b2b_customer_list`: listele *Cereri de cont B2B* și *Clienți B2B*.
- `view_res_partner_filter_b2b`: filtrele B2B din căutarea contactelor.
- `view_b2b_reject_wizard_form`: fereastra de respingere.
- `res_config_settings_view_form`: blocul *Portal B2B* din setările website-ului.
- `views/shop_templates.xml`: `products_item_b2b_price`, `filter_products_price_b2b`, `products_sort_b2b` (fără preț, filtru de preț și sortare după preț în /shop).
- `views/portal_templates.xml`: pagina /b2b și tabloul de bord din /my.

**Controllere**

- `/b2b` (public), `/b2b/request` (GET/POST): pagina și trimiterea formularului.
- Metode ajutătoare: `_b2b_inactive_redirect()`, `_b2b_add_to_cart(quantities)`.
- Suprascrieri: checkout, `portal_quote_accept`, `portal_order_transaction` (blocare pentru roluri fără drept de comandă) și `home` (/my) pentru tabloul de bord.

**Acțiuni Automate / Acțiuni Server**

- `action_server_b2b_activate`: *Activare cont B2B* pe client existent (formă sau listă).
- `mail_template_b2b_request_received`: șablonul e-mailului de confirmare a cererii (text fix, trimis doar dacă setarea e activă).
- `mail_activity_type_b2b_request`: tip de activitate „Cerere cont B2B", creat agentului la fiecare cerere și închis la aprobare/respingere.
- Nu există cron-uri.

#### 5. Conexiuni

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md): limita de credit și toleranțele ei; portalul afișează creditul disponibil din limita standard.
- [terrabit_partner_credit_limit_website](../terrabit_partner_credit_limit_website/index.md): impune limita și facturile restante la comanda din website.
- [deltatech_b2b_quick_order](../deltatech_b2b_quick_order/index.md): comanda rapidă după cod, construită peste portal (folosește metodele ajutătoare).
- [deltatech_b2b_order_list](../deltatech_b2b_order_list/index.md): liste de comandă salvate, construite peste portal (folosește metodele ajutătoare).
- [deltatech_b2b_price_tier](../deltatech_b2b_price_tier/index.md): trepte de preț pe cantitate, modul separat din familia B2B.
- [deltatech_b2b_website_restrict](../deltatech_b2b_website_restrict/index.md): website închis vizitatorilor: publice rămân doar pagina de prezentare B2B și formularul de cerere.
