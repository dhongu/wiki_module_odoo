# Sale Margin (localizat la `deltatech_sale_margin/index.md`)

- **Nume Tehnic:** `deltatech_sale_margin`
- **Versiune:** `19.0.1.3.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_margin
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_margin`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde funcționalitatea standard de marjă din comenzile de vânzare, oferind un control mai strict asupra prețurilor. Permite ascunderea marjei și a prețului de achiziție de anumiți utilizatori, împiedicarea modificării prețurilor și gestionarea situațiilor în care prețul de vânzare scade sub prețul de achiziție. Reacția la o vânzare sub cost se alege **per companie**: blocarea vânzării (comportamentul implicit), doar avertisment, sau nicio verificare. Varianta „doar avertisment" este pentru companiile la care vânzarea sub cost face parte din activitatea normală — marfă perisabilă, lichidări de stoc, gesturi comerciale — unde o interdicție ar opri munca zilnică, iar nevoia reală este să se vadă când se întâmplă și cine decide. Astfel, companiile pot proteja informațiile comerciale sensibile și pot alege între a preveni și a semnala vânzările sub costul de achiziție. Modulul afișează și costul pe linia facturii către client și oferă un raport de analiză a profitului pe facturile postate, cu posibilitatea de a recalcula costul când e greșit.

#### 2. Funcționalități Cheie

- Grup tehnic de acces nou pentru a ascunde marja și prețul de achiziție în comanda de vânzare.
- Grup tehnic de acces nou pentru a împiedica modificarea prețului în comanda de vânzare.
- Grup tehnic de acces nou pentru a permite vânzarea la un preț sub prețul de achiziție.
- Avertizare sau eroare pe comanda de vânzare atunci când prețul de vânzare este sub prețul de achiziție.
- **Politică de reacție configurabilă per companie** (`Setări → Vânzări → Prețuri`): „Blochează vânzarea" (implicit, comportamentul istoric), „Doar avertisment" (nimic nu se blochează) sau „Fără verificare".
- **Marcaj pe linia comenzii** (`margin_below_limit`): rândul se colorează de îndată ce operatorul iese din câmpul de preț, adică acolo unde se ia decizia. Marcajul e vizibil oricui — spune *că* marja e sub limită, nu *cât* este costul, deci nu dezvăluie costul agenților care nu au dreptul să îl vadă; cifra rămâne pe câmpul de marjă restricționat pe grup.
- **Gardă de unitate la comparație**: costul e adus în unitatea liniei, iar comparația tace când unitatea liniei și unitatea de bază a produsului sunt din familii diferite. Odoo 19 a eliminat categoria de unități și convertește orice pereche folosind factorii absoluți, deci un cost pe „bucată" devine de 1.000 de ori mai mare exprimat pe kilogram — fără gardă, un produs configurat greșit ar raporta *fiecare* linie ca fiind sub cost, iar avertismentul ar fi ignorat ca zgomot.
- **Notă unică în chatter** la confirmarea unei comenzi sub cost, ca urmă a deciziei — nu un mesaj la fiecare modificare de preț.
- Setările de marjă sunt accesibile din interfață (`Setări → Vânzări`): pragul „Limită de marjă (%)" și verificarea doar la confirmare. Pragul acceptă valori negative (se tolerează o pierdere de până la X% fără alertă) și pozitive (se semnalează și marjele subțiri, deși pe plus).
- **Preț de cost pe factura client** (coloana „Preț cost", vizibilă doar grupului cu drept de cost): calculat din livrarea comenzii facturate (valoarea mișcării de stoc împărțită la cantitate, în unitatea liniei), din componentele livrate la kituri, din costul produsului la facturile fără comandă/livrare; la notele de credit, din returul de marfă (inversarea facturii preia costul liniei, iar reducerile de preț/discount au cost 0). Aceeași politică de companie se aplică și pe linia facturii.
- **Raport „Analiză profit"** (`Vânzări → Raportare`, pivot + listă) pe facturile client postate: valoare vânzare (fără TVA), valoare cost, profit, adaos (profit/cost) și marjă (profit/vânzare); regrupare după agent, categorie, client, factură, jurnal sau lună; export Excel; notele de credit scad și vânzarea, și costul. Vizibil grupului cu drept de cost și administratorilor de vânzări. Se pot adăuga și alte surse (ex. comenzi POS, prin [deltatech_sale_margin_pos](../deltatech_sale_margin_pos/index.md)).
- **Recalculare cost** (acțiunea „Actualizare preț achiziție" din lista raportului): „Preț din livrare" (implicit, cu cădere pe costul produsului), sau costul curent al produsului (fără conversie de unitate); „Pentru toate liniile" rescrie profitul și pentru perioadele deja raportate. O acțiune programată zilnică reîmprospătează costul liniilor facturate în ultimele 7 zile. Rulează doar administratorii de vânzări (și, cu `deltatech_sale_commission`, managerii de comisioane).
- Parametru de sistem `sale.check_price_website` pentru verificarea prețului la comenzile plasate de pe website.
- Parametru de sistem `sale.margin_limit_check_validate` — dacă este setat, verificarea se face la confirmarea comenzii (utilizatorii fără drept de a vinde sub marjă/prețul de achiziție pot crea totuși comenzi în starea ciornă).

#### 3. Dependențe

- `sale_margin`
- `sale_stock_margin`
- `account`
- `stock_account`
- `delivery`

#### 4. Componente Cheie

`readme/DESCRIPTION.md` descrie funcționalitățile la nivel de utilizator final (secțiunile 1 și 2). Se rețin totuși componentele pe care le referă alte module și configurarea:

**Modele**

- `res.company`: câmpul `sale_margin_check_mode` — politica de reacție la vânzarea sub cost (`block` / `warn` / `off`, implicit `block`).
- `sale.order.line`: câmpul calculat `margin_below_limit` (marcajul de linie, nestocat) și metoda `check_sale_price`, care reacționează conform politicii companiei.
- `sale.order`: `price_warning_message` (bannerul din capul comenzii) și `_post_margin_warning` (nota din chatter la confirmare).
- `uom.uom`: metoda `_dt_root_uom()` — rădăcina ierarhiei de unități, folosită pentru a stabili dacă două unități sunt din aceeași familie.
- `res.config.settings`: expune politica și parametrii `sale.margin_limit` / `sale.margin_limit_check_validate`.

- `account.move` / `account.move.line`: câmpul `purchase_price` pe linia facturii (calculat din livrare/retur/cost produs) și verificarea prețului sub cost pe factură.
- `sale.margin.report` (view SQL): raportul de profit pe facturile postate; permite scrierea `purchase_price` și surse suplimentare; metoda `cron_update_purchase_price`.
- `commission.update.purchase.price` (wizard): recalculează costul liniilor selectate sau al tuturor liniilor din raport.

**Vizualizări**

- `view_order_form`: bannerul de avertisment în capul comenzii de vânzare.
- `view_order_form_margin_flag`: colorarea liniei sub cost în lista liniilor comenzii.
- `res_config_settings_view_form`: politica și pragurile în `Setări → Vânzări → Prețuri`.
- `view_order_form_no_change_price`: preț și discount readonly pentru utilizatorii fără drept de modificare.
- `invoice_form` / `invoice_form_no_change_price`: coloana „Preț cost" pe factura client, restricționată pe grup, și preț readonly pentru grupul fără drept de modificare.
- `view_sale_margin_report_pivot` / `view_sale_margin_report_list` / `action_sale_margin_report`: raportul „Analiză profit" (meniu sub Vânzări → Raportare).
- `view_commission_update_purchase_price_form`: asistentul „Actualizare preț achiziție".

**Acțiuni Automate / Acțiuni Server**

- `cron_update_purchase_price` („Update Purchase Price Daily"): zilnic, reîmprospătează costul liniilor facturate în ultimele 7 zile.

#### 5. Conexiuni

- `sale_margin`: modul de bază Odoo extins de acest modul, care introduce calculul marjei pe comenzile de vânzare.
- `sale_stock_margin`: aduce `purchase_price` la valorizarea reală a livrării — costul pe care se face comparația; la marfa produsă, reflectă costul lotului.
- [deltatech_sale_margin_pos](../deltatech_sale_margin_pos/index.md): adaugă comenzile POS ca sursă în raportul de profit.
- [deltatech_sale_commission](../deltatech_sale_commission/index.md): folosește costul pe factură și raportul de profit pentru comisioane (funcționalitățile au fost mutate de acolo în acest modul); aplică aceeași politică de companie pe linia de factură, ca o vânzare permisă pe comandă să nu fie blocată la facturare.
- `inedit_sale_purchase_flow` (modul de proiect, în afara acestui wiki): pune politica pe „Doar avertisment" — cazul de utilizare care a motivat facilitatea.
