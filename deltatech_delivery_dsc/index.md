# Dragon Star Curier Shipping (localizat la `deltatech_delivery_dsc/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dsc`
- **Versiune:** `20.0.2.0.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_dsc
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_dsc`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite expedierea coletelor prin Dragon Star Curier și urmărirea lor online: AWB-ul, tariful și starea expedierii se obțin direct din Odoo. Funcționează cu API-ul Dragon Star v1 (cheie API) și, până când Dragon Star îl retrage, cu API-ul vechi.

#### 2. Funcționalități Cheie

- Generare AWB în format PDF (sau ZPL), anulare AWB, tarife pentru o expediere (fără TVA), listă de localități și județe, listă de puncte de ridicare și mai multe puncte de lucru (pcId).
- Expediere cu mai multe colete, valoare declarată (asigurare), ramburs, nume de localitate fără id, livrare sâmbăta și pachet deschis; link de tracking și ultima stare a expedierii.
- **Borderou și ridicare**: acțiunea programată *DSC: Create borderou and pickup orders* rulează zilnic la 18:00 UTC, trimite expedierile zilei la Dragon Star pentru ridicare și creează borderoul; starea este apoi citită până la livrare.
- **Anulare**: **Cancel AWB** este permisă în 30 de minute, înainte de crearea borderoului; ulterior anularea se cere la Dragon Star.
- **Configurare**: în *Inventory > Configuration > Delivery > Delivery Methods* se creează metoda cu **Provider** *Dragon Star Curier*; în DSC se creează o cheie API (*Settings > API access*, cu autentificare în doi pași) și se declară IP-urile publice ale serverului; în tab-ul **DSC Configuration** se lasă **DSC API Version** pe *API v1 (API key)* și se lipește **DSC API Key** (API-ul vechi folosește **User** și **Password** și rămâne disponibil până cel puțin 31 martie 2027); **Initialization** importă punctele de lucru ca locații de ridicare, **Get city** adaugă localitățile lipsă; se aleg **Dsc Label Type** (PDF/ZPL), **DSC Page Format** (A4/A6) și metodele de plată tratate ca ramburs.
- Dragon Star nu are server de test (se folosește o cheie API separată); cotarea tarifelor funcționează doar dacă este activată de Dragon Star pe cont.
- **Neacoperit**: istoric complet de stare, starea AWB-ului de retur, tipărirea borderoului în PDF, dimensiuni (L, l, h), retur colet, notă de restituire.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)

Dependență externă Python: `phonenumbers`.

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea „Componente Cheie" este omisă: `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, iar componentele tehnice nu sunt cerute explicit în Readme.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru gestiunea livrărilor pe care `deltatech_delivery_dsc` îl extinde cu integrarea curierului Dragon Star Curier.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): modul înrudit din suita de livrare, folosit pentru urmărirea stării expedierilor.
