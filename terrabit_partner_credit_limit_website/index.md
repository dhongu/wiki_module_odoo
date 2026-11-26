# Limită de Credit pe Partener — Website (localizat la `terrabit_partner_credit_limit_website/index.md`)

- **Nume Tehnic:** `terrabit_partner_credit_limit_website`
- **Versiune:** `19.0.0.0.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_partner_credit_limit_website
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_credit_limit_website`
- **Ultima Ingestie:** `2026-11-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde limita de credit pe partener către checkout-ul din website/e-commerce. Modulul nu blochează comanda: când un client autentificat depășește limita de credit (sau are facturi restante), pagina de plată îi ascunde metodele de plată „pe încredere” (transfer bancar, ramburs), iar clientul vede pe pagină soldul și eventualele facturi restante. Astfel politica de credit a companiei se aplică consecvent și pe canalul online, iar clientul e informat din timp, fără respingeri neașteptate de comenzi.

#### 2. Funcționalități Cheie

- Pe pagina de plată (`/shop/payment`), un client autentificat cu limită de credit vede o bară de progres cu valoarea comenzii raportată la limită și un rezumat cu **Limita de credit** și **Soldul** curent.
- Dacă clientul are facturi restante (peste zilele de grație din modulul de bază), apare o alertă roșie cu suma restantă și numerele facturilor, urmată de un mesaj cu telefonul departamentului de contabilitate.
- Când soldul plus valoarea comenzii depășește limita (sau există facturi restante), lista metodelor de plată se restrânge: dispar transferul bancar și plata la livrare (ramburs), rămân doar metodele online care confirmă plata imediat (de exemplu cardul). Un client în limită vede lista completă, nemodificată.
- Setarea **Restrict All Providers** (Website → Configurare → Setări, secțiunea de plăți): debifată (implicit) — la depășire se elimină doar transferul bancar și ramburs-ul; bifată — la depășire se elimină **toate** metodele de plată, iar clientul nu poate plăti până nu își reglează soldul.
- Comenzile cu termenul de plată **Plată imediată** sar complet peste verificare (comportament implicit al modulului de bază); la fel comenzile sau echipele de vânzări care au excepție de la limita de credit în modulul de bază.
- După ce comanda are orice tranzacție de plată înregistrată (chiar eșuată sau anulată), reîncărcarea paginii de plată nu mai aplică restricția, dacă modulul de bază nu e configurat altfel.
- Plata la livrare e restricționată doar dacă e instalat modulul opțional *Payment on Delivery*.
- Cerințe de configurare: limita de credit setată pe clienții controlați (modulul de bază), cel puțin un furnizor de plată online publicat pe website (altfel un client peste limită nu are cum plăti) plus furnizorul de transfer bancar, și un termen de plată altul decât *Plată imediată* pe comenzile verificate.

#### 3. Dependențe

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md)
- `website_sale`
- `payment_custom`

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe fișierele din `readme/`, care nu detaliază componentele tehnice individuale. Conform fluxului de ingestie, analiza codului pentru Modele, Vizualizări și Acțiuni Automate a fost omisă întrucât Readme-ul este prezent.

*Notă tehnică orientativă (neexhaustivă):* modulul extinde `payment.provider` (`_get_compatible_providers`) pentru a restricționa metodele de plată disponibile la checkout când limita de credit e depășită (parametrul de sistem `payment_provider_credit_limit.restrict_all_provider` controlează dacă se restricționează toți furnizorii sau doar transferul bancar `wire_transfer` și `on_delivery`), extinde `res.config.settings` cu setarea „Restrict All Providers”, și adaugă în șablonul `website_sale.payment` un bloc cu bara de progres a limitei de credit, soldul curent și eventualele facturi restante.

#### 5. Conexiuni

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md): modulul de bază (și dependență) care implementează logica de calcul și verificare a limitei de credit, extinsă aici pentru canalul website.
- `website_sale`: modulul standard de e-commerce ale cărui șabloane de checkout (`website_sale.payment`) și setări (`res.config.settings`) sunt extinse.
- `payment_custom`: furnizează modurile de plată personalizate (ex. transfer bancar) folosite în logica de restricționare a furnizorilor de plată.
