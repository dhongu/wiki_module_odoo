# Sale Margin & Profit (localizat la `deltatech_sale_margin/index.md`)

- **Nume Tehnic:** `deltatech_sale_margin`
- **Versiune:** `20.0.1.3.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_margin
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_margin`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde funcționalitatea standard de marjă din comenzile de vânzare, oferind un control mai strict asupra prețurilor. Permite ascunderea marjei și a prețului de achiziție de anumiți utilizatori, împiedicarea modificării prețurilor și gestionarea situațiilor în care prețul de vânzare scade sub prețul de achiziție. Reacția la o vânzare sub cost se alege **per companie**: blocarea vânzării (comportamentul implicit), doar avertisment, sau nicio verificare. Varianta „doar avertisment" este pentru companiile la care vânzarea sub cost face parte din activitatea normală — marfă perisabilă, lichidări de stoc, gesturi comerciale — unde o interdicție ar opri munca zilnică, iar nevoia reală este să se vadă când se întâmplă și cine decide. Astfel, companiile pot proteja informațiile comerciale sensibile și pot alege între a preveni și a semnala vânzările sub costul de achiziție.

#### 2. Funcționalități Cheie

- Grup tehnic de acces nou pentru a ascunde marja și prețul de achiziție în comanda de vânzare.
- Grup tehnic de acces nou pentru a împiedica modificarea prețului în comanda de vânzare.
- Grup tehnic de acces nou pentru a permite vânzarea la un preț sub prețul de achiziție.
- Avertizare sau eroare pe comanda de vânzare atunci când prețul de vânzare este sub prețul de achiziție.
- **Politică de reacție configurabilă per companie** (`Setări → Vânzări → Prețuri`): „Blochează vânzarea" (implicit, comportamentul istoric), „Doar avertisment" (nimic nu se blochează) sau „Fără verificare".
- **Marcaj pe linia comenzii** (`margin_below_limit`): rândul se colorează de îndată ce operatorul iese din câmpul de preț, adică acolo unde se ia decizia. Marcajul e vizibil oricui — spune *că* marja e sub limită, nu *cât* este costul, deci nu dezvăluie costul agenților care nu au dreptul să îl vadă; cifra rămâne pe câmpul de marjă restricționat pe grup.
- **Gardă de unitate la comparație**: costul e adus în unitatea liniei, iar comparația tace când unitatea liniei și unitatea de bază a produsului sunt din familii diferite. Odoo nu mai are categorii de unități și convertește orice pereche folosind factorii absoluți, deci un cost pe „bucată" devine de 1.000 de ori mai mare exprimat pe kilogram — fără gardă, un produs configurat greșit ar raporta *fiecare* linie ca fiind sub cost, iar avertismentul ar fi ignorat ca zgomot.
- **Notă unică în chatter** la confirmarea unei comenzi sub cost, ca urmă a deciziei — nu un mesaj la fiecare modificare de preț.
- **Cost pe linia facturii clientului** (coloana *Cost Price*): din livrarea comenzii facturate (valoarea mișcării de stoc către client împărțită la cantitate, în unitatea liniei), din componentele livrate la kituri, din costul produsului la facturile fără comandă sau livrare; la note de credit, din returul de marfă. Avertisment sau eroare și pe factură, când prețul e sub cost, după aceeași politică. Coloana e vizibilă doar grupului de cost.
- **Raport de profit** pe facturile clienților postate (`Vânzări > Raportare > Profit Analysis`): valoare vânzare, cost, profit, adaos (profit / cost) și marjă (profit / vânzare), cu grupare pe vânzător, categorie, client, factură, jurnal sau lună; alte surse se pot adăuga (comenzi POS, prin [deltatech_sale_margin_pos](../deltatech_sale_margin_pos/index.md)).
- **Actualizare preț de achiziție** (`Acțiuni > Update Purchase Price` pe raport, vizualizarea listă): din livrare (implicit) sau din costul curent al produsului; opțiunea *For all lines* rescrie și perioadele deja raportate. O acțiune programată reîmprospătează zilnic costul liniilor facturate în ultimele 7 zile.
- Linii excluse de la verificare: transport, servicii, recompense de loialitate, comenzi website.
- Setările de marjă sunt accesibile din interfață (`Setări → Vânzări`): pragul „Limită de marjă (%)" și verificarea doar la confirmare. Pragul acceptă valori negative (se tolerează o pierdere de până la X% fără alertă) și pozitive (se semnalează și marjele subțiri, deși pe plus).
- Parametru de sistem `sale.check_price_website` pentru verificarea prețului la comenzile plasate de pe website.
- Parametru de sistem `sale.margin_limit_check_validate` — dacă este setat, verificarea se face la confirmarea comenzii (utilizatorii fără drept de a vinde sub marjă/prețul de achiziție pot crea totuși comenzi în starea ciornă).

#### 3. Dependențe

- `sale_margin`
- `sale_stock_margin`
- `account`
- `stock_account`
- `delivery`

#### 4. Componente Cheie

`readme/DESCRIPTION.md` descrie funcționalitățile la nivel de utilizator final (secțiunile 1 și 2). Se rețin totuși componentele pe care le referă alte module și configurarea (fluxul pas cu pas este în fișa consultantului):

**Modele**

- `res.company`: câmpul `sale_margin_check_mode` — politica de reacție la vânzarea sub cost (`block` / `warn` / `off`, implicit `block`).
- `sale.order.line`: câmpul calculat `margin_below_limit` (marcajul de linie, nestocat) și metoda `check_sale_price`, care reacționează conform politicii companiei.
- `sale.order`: `price_warning_message` (bannerul din capul comenzii) și `_post_margin_warning` (nota din chatter la confirmare).
- `uom.uom`: metoda `_dt_root_uom()` — rădăcina ierarhiei de unități, folosită pentru a stabili dacă două unități sunt din aceeași familie.
- `account.move.line`: câmpul `purchase_price` (costul pe linia facturii) și `get_purchase_price`.
- `sale.margin.report`: raportul de profit pe facturi; `commission.update.purchase.price`: wizardul de actualizare a costului.
- `res.config.settings`: expune politica și parametrii `sale.margin_limit` / `sale.margin_limit_check_validate`.

**Vizualizări**

- `view_sale_margin_report_pivot` / `view_sale_margin_report_list`: raportul de profit.
- `invoice_form`: coloana *Cost Price* pe factură.
- `view_commission_update_purchase_price_form`: wizardul de actualizare a prețului de achiziție.
- `view_order_form`: bannerul de avertisment în capul comenzii de vânzare.
- `view_order_form_margin_flag`: colorarea liniei sub cost în lista liniilor comenzii.
- `res_config_settings_view_form`: politica și pragurile în `Setări → Vânzări → Prețuri`.
- `view_order_form_no_change_price`: preț și discount readonly pentru utilizatorii fără drept de modificare.

**Acțiuni Automate / Acțiuni Server**

- `cron_update_purchase_price`: zilnic, reîmprospătează costul liniilor facturate în ultimele 7 zile.

#### 5. Conexiuni

- `sale_margin`: modul de bază Odoo extins de acest modul, care introduce calculul marjei pe comenzile de vânzare.
- `sale_stock_margin`: aduce `purchase_price` la valorizarea reală a livrării — costul pe care se face comparația; la marfa produsă, reflectă costul lotului.
- [deltatech_sale_commission](../deltatech_sale_commission/index.md): aplică aceeași politică de companie pe linia de factură, ca o vânzare permisă pe comandă să nu fie blocată la facturare.
- [deltatech_sale_margin_pos](../deltatech_sale_margin_pos/index.md): adaugă comenzile POS ca sursă în raportul de profit.
- `inedit_sale_purchase_flow` (modul de proiect, în afara acestui wiki): pune politica pe „Doar avertisment" — cazul de utilizare care a motivat facilitatea.
