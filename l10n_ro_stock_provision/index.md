# Romania - Ajustări pentru deprecierea stocurilor (39x) (localizat la `l10n_ro_stock_provision/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_provision`
- **Versiune:** `19.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_provision
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_stock_provision
- **Ultima Ingestie:** `2026-10-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul identifică automat stocurile fără rulaj (slow-moving) și generează note contabile de ajustare pentru depreciere, conform OMFP 1802/2014, pct. 143–148. Contabilul stabilește numărul de zile fără mișcare și procentul de depreciere, sistemul scanează stocurile și propune ajustările per produs, iar la confirmare se generează o singură notă: Dr 6814 = Cr 39x la constituire sau majorare și Dr 39x = Cr 7814 la diminuare sau reluare. Operațiunea mișcă doar conturi de clasa 3, 6 și 7 și nu afectează TVA.

#### 2. Funcționalități Cheie

- **Identificare automată slow-moving:** scanează stocurile interne cu cantitate și valoare pozitive, fără mișcare de intrare peste pragul configurat (implicit 180 de zile).
- **Calcul pe diferență:** provizionul propus (valoarea contabilă × procentul de depreciere) se compară cu cel existent (soldul contului 39x pentru produs), iar nota înregistrează doar diferența: constituire, majorare, diminuare, reluare sau fără ajustare.
- **Flux de aprobare:** Analiză → Confirmat → Note generate (plus Anulat); în lista **Contabilitate → Închidere → Provizioane Stocuri (39x)** se completează data analizei, jurnalul, zilele fără mișcare și procentul de depreciere, apoi **Calculează**. Fiecare linie are bifa „Aprobat" (implicit activă) și o observație internă; liniile debifate nu generează notă.
- **Generare note contabile:** după **Confirmă propunerile** (cel puțin o linie aprobată cu ajustare nenulă), **Generează Note Contabile** postează o singură notă în jurnalul ales; analiza cu notă postată nu se anulează direct, nota se stornează mai întâi.
- **Mapare conturi 39x per categorie de produs** (de exemplu 391 materii prime, 392 consumabile, 394 produse finite, 397 mărfuri), în secțiunea „Provizioane Stocuri RO (39x)" din categorie; categoriile fără cont 39x sunt ignorate de analiză.
- **Procent și prag per categorie:** procentul de depreciere și zilele slow-moving pot fi suprascrise pe categorie (`0` la zile înseamnă valoarea globală).
- **Setări generale:** în **Contabilitate → Configurare → Setări**, secțiunea „Provizioane Stocuri Slow-Moving": conturile 6814 și 7814 și zilele implicite fără mișcare.
- **Surse de date flexibile:** folosește `product.valuation.history` din `deltatech_stock_valuation` dacă e instalat, altfel stocul curent, cu data ultimei intrări din `l10n_ro_last_in_date` (dacă e instalat `l10n_ro_stock_aged_report`) sau din `in_date`.
- **Cron lunar opțional**, dezactivat implicit, care creează pe fiecare companie românească o analiză în starea Analiză, fără să posteze note.
- **Limitare:** un produs ieșit complet din stoc, dar cu sold 39x rămas, nu apare în analiză; soldul se reia printr-o notă contabilă directă.

#### 3. Dependențe

- `stock`
- `account`

Opțional (detectat la runtime, fără dependență în manifest): [l10n_ro_stock_aged_report](../l10n_ro_stock_aged_report/index.md) și [deltatech_stock_valuation](../deltatech_stock_valuation/index.md).

#### 4. Componente Cheie

**Modele**

- `l10n.ro.stock.provision`: analiza de provizioane, cu starea fluxului, propunerile și nota contabilă generată (are chatter și activități).
- `l10n.ro.stock.provision.line`: linia de propunere per produs, cu valoare contabilă, provizion existent și propus, ajustare, tip și bifa de aprobare.
- `res.company`, `res.config.settings`, `product.category` (extinse): conturile 6814/7814 și zilele implicite pe companie, contul 39x, procentul și pragul pe categorie.

**Vizualizări**

- `view_l10n_ro_stock_provision_form` / `view_l10n_ro_stock_provision_list`: analiza de provizioane (meniu `menu_l10n_ro_stock_provision`).
- `view_product_category_form_provision`: secțiunea „Provizioane Stocuri RO (39x)" din categoria de produs.
- `res_config_settings_view_form_stock_provision`: setările pentru provizioane slow-moving.

**Acțiuni Automate / Acțiuni Server**

- `cron_stock_provision_monthly` („Generare propuneri provizioane stocuri slow-moving (lunar)"): creează lunar analize în stare draft pentru verificare manuală; inactiv implicit.

#### 5. Conexiuni

- [l10n_ro_stock_aged_report](../l10n_ro_stock_aged_report/index.md): furnizează data ultimei intrări `l10n_ro_last_in_date`, când este instalat.
- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): istoricul valoric lunar `product.valuation.history`, mai precis decât stocul curent.
