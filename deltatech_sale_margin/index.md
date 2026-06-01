# Sale Margin (localizat la `deltatech_sale_margin/index.md`)

- **Nume Tehnic:** `deltatech_sale_margin`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_margin
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_margin`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Modulul extinde funcționalitatea standard de marjă din comenzile de vânzare, oferind un control mai strict asupra prețurilor. Permite ascunderea marjei și a prețului de achiziție de anumiți utilizatori, împiedicarea modificării prețurilor și gestionarea situațiilor în care prețul de vânzare scade sub prețul de achiziție. Astfel, companiile pot proteja informațiile comerciale sensibile și pot preveni vânzările sub costul de achiziție, fie prin avertizare, fie prin blocarea confirmării comenzii.

#### 2. Funcționalități Cheie

- Grup tehnic de acces nou pentru a ascunde marja și prețul de achiziție în comanda de vânzare.
- Grup tehnic de acces nou pentru a împiedica modificarea prețului în comanda de vânzare.
- Grup tehnic de acces nou pentru a permite vânzarea la un preț sub prețul de achiziție.
- Avertizare sau eroare pe comanda de vânzare atunci când prețul de vânzare este sub prețul de achiziție.
- Parametru de sistem `sale.check_price_website` pentru verificarea prețului la comenzile plasate de pe website.
- Parametru de sistem `sale.margin_limit_check_validate` — dacă este setat, verificarea se face la confirmarea comenzii (utilizatorii fără drept de a vinde sub marjă/prețul de achiziție pot crea totuși comenzi în starea ciornă).

#### 3. Dependențe

- `sale_margin`
- `account`
- `stock_account`
- `delivery`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, funcționalitățile sunt descrise la nivel de utilizator final (secțiunile 1 și 2). Documentul nu solicită explicit detalierea componentelor tehnice, prin urmare această secțiune nu este detaliată la nivel de modele, vizualizări sau acțiuni automate.

#### 5. Conexiuni

- `sale_margin`: modul de bază Odoo extins de acest modul, care introduce calculul marjei pe comenzile de vânzare.
