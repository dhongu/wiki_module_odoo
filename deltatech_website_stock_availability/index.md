# eCommerce Stock Availability (localizat la `deltatech_website_stock_availability/index.md`)

- **Nume Tehnic:** `deltatech_website_stock_availability`
- **Versiune:** `19.0.1.0.15`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_stock_availability
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_stock_availability`
- **Ultima Ingestie:** `2026-11-21`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

*Notă:* în Odoo Apps modulul apare sub numele *Website Stock Availability* (din 19.0.1.0.14); numele din manifest este „Website Stock Availability”, iar numele tehnic rămâne neschimbat.

#### 1. Sumar

Modulul permite afișarea stocului pe website sub un anumit prag, cu posibilitatea de a comanda produse chiar dacă stocul disponibil nu este suficient. Pe lângă disponibilitate, estimează numărul de zile până la livrare, luând în calcul timpul de livrare definit pe produs, zilele de siguranță și, pentru produsele care nu sunt pe stoc, timpul de livrare de la furnizor. Astfel, magazinul online comunică transparent atât disponibilitatea, cât și un termen realist de livrare.

#### 2. Funcționalități Cheie

- Afișarea stocului pe website sub un prag configurabil, cu posibilitatea de a comanda și când stocul nu ajunge.
- Calculul automat al zilelor estimate până la livrare, din termenul de livrare al produsului, zilele de siguranță și, pentru produsele fără stoc, termenul și stocul furnizorului aplicabil (din `deltatech_vendor_stock`).
  - Furnizorul se alege dintre liniile de furnizor ale companiei website-ului, pentru varianta afișată; sunt ignorate ofertele altor variante sau companii, ale furnizorilor arhivați și cele expirate, iar o ofertă curentă are prioritate față de una viitoare.
- Statusul stocului pe cardul de produs din magazin (livrare imediată sau ulterioară), configurat din editorul website-ului, în panoul *Products Design*: text, LED sau LED cu text, deasupra prețului, pe imagine sau lângă preț, cu portocaliu, gri sau roșu pentru produsele fără stoc.
- Stilul insignei de stoc de pe pagina produsului, ales din editor, panoul *Product Page* → *Stock Badge*: pastilă (standard), text cu punct, culorile temei, contur, bară de nivel sau doar starea.
- Insigne de livrare în coș, calculate pe stocul depozitului website-ului, exprimat în unitatea de măsură a liniei.
- Câmpuri adăugate pe produs: *Customer Safety Lead Time* (implicit 1 zi) și *Hide "Out of stock" message*; pe liniile de furnizor, *Lead Time* acceptă zecimale.
- Limitare cunoscută pe 19.0: pentru un termen de livrare al produsului peste 7 zile se poate afișa „Livrare în NaN săptămâni” (corectat doar pe 20.0). Detalii operaționale în fișa consultant.

#### 3. Dependențe

- `website`
- `website_sale_stock`
- `purchase`
- [deltatech_vendor_stock](../deltatech_vendor_stock/index.md)

#### 4. Componente Cheie

*Documentația pentru această secțiune este generată din `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului (modele, vizualizări, acțiuni) este omisă deoarece nu este menționată explicit în Readme.*

#### 5. Conexiuni

- [deltatech_vendor_stock](../deltatech_vendor_stock/index.md): furnizează stocul disponibil la furnizor (*Quantity Available*), folosit la estimarea termenului de livrare pentru produsele care nu sunt pe stoc.
