# Product Website Visibility Score (localizat la `deltatech_product_visibility/index.md`)

- **Nume Tehnic:** `deltatech_product_visibility`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_visibility
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_visibility`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

`deltatech_product_visibility` acordă fiecărui produs un **scor de vizibilitate pe website între 0 și 100**, afișat ca un indicator colorat tip semafor, astfel încât echipa de vânzări sau marketing să vadă dintr-o privire cât de „găsibil" și complet este produsul în catalogul online — și exact ce trebuie corectat pentru a-l îmbunătăți. Scorul se calculează din conținutul care influențează cu adevărat vizibilitatea și conversia pe website (SEO, imagini, descrieri, categorie, preț și cod intern), iar starea de publicare este afișată separat, ca informație distinctă, nefiind parte din scor.

#### 2. Funcționalități Cheie

- Câmpuri calculate `website_visibility_score` (0–100) și `website_visibility_level`, stocate pe produs pentru a permite filtrare și grupare.
- Indicator colorat tip semafor pe formularul de produs, plus o pagină de defalcare care listează fiecare criteriu, punctajul aferent și dacă este îndeplinit sau nu.
- Coloane în lista de produse (bară de scor + etichetă de nivel), ascunse implicit, activabile din meniul de coloane opționale.
- Filtre de căutare „Vizibilitate: necesită atenție" și „Vizibilitate: invizibil", plus grupare după nivelul de vizibilitate, pentru triaj rapid al întregului catalog.
- Criterii și ponderi complet configurabile, fără nevoie de cod: fiecare criteriu are un cod fix (mapat în cod la o verificare concretă), o pondere editabilă, o secvență și un flag activ/inactiv.
- Scorul se recalculează automat la fiecare modificare a unui câmp sursă (câmp calculat stocat cu dependențe) — nu necesită job programat; după schimbarea ponderilor există o acțiune server „Recalculează scorurile de vizibilitate" pentru reevaluarea în masă a produselor existente.
- Criteriile implicite (pondere totală 100): SEO complet (25), imagine principală (18), descriere website amplă (15), categorie publică (12), galerie de imagini ≥ 2 (10), descriere eCommerce scurtă (10), preț de vânzare setat (5), cod produs/SKU (5). Nivelurile: Invizibil 0–39, Slab 40–69, Bun 70–89, Optim 90–100.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `deltatech.product.visibility.criterion`: criteriile de vizibilitate configurabile (cod fix, nume, pondere, secvență, activ), cu constrângere de unicitate pe cod și acțiunea `action_recompute_scores` care reevaluează scorul tuturor produselor.
- `product.template` (extindere): adaugă `website_visibility_score`, `website_visibility_level` (calculate, stocate) și `website_visibility_badge` / `website_visibility_detail` (HTML calculat, semafor și defalcare pe criterii), plus logica de evaluare a criteriilor (`_get_visibility_checks`) și de randare a indicatorului.

**Vizualizări**

- `product_template_only_form_visibility`: adaugă indicatorul colorat (semafor) pe formularul de produs, lângă codul intern.
- `product_template_form_visibility_detail`: pagină nouă „Vizibilitate website" în notebook-ul produsului, cu bara de progres a scorului, nivelul și defalcarea pe criterii.
- `product_template_tree_visibility`: coloane opționale (bară de scor, etichetă de nivel colorată) în lista de produse.
- `product_template_search_visibility`: filtre „Vizibilitate: necesită atenție" / „Vizibilitate: invizibil" și grupare după nivel în căutarea produselor.
- `visibility_criterion_view_list` / `visibility_criterion_view_form`: listă editabilă inline și formular pentru configurarea criteriilor și ponderilor, sub meniul **Sales → Configuration → Vizibilitate produs**.

**Acțiuni Automate / Acțiuni Server**

- `visibility_recompute_action`: acțiune server legată de modelul `deltatech.product.visibility.criterion` („Recalculează scorurile de vizibilitate") — reevaluează scorul de vizibilitate pentru toate produsele, utilă după modificarea ponderilor criteriilor.

#### 5. Conexiuni

- `website_sale`: modulul depinde direct de el pentru câmpurile de website ale produsului (SEO, descriere website, categorii publice, publicare) pe care se bazează scorul de vizibilitate.
