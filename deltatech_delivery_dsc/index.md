# DSC Shipping (localizat la `deltatech_delivery_dsc/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dsc`
- **Versiune:** `19.0.2.0.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_dsc`
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_dsc`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Acest modul integrează Odoo cu serviciul de curierat Dragon Star Curier (DSC), permițând expedierea coletelor și urmărirea lor direct din livrările Odoo: tariful de transport, AWB-ul și eticheta sa, urmărirea, borderoul de sfârșit de zi și comanda de ridicare, fără reintroducerea datelor în aplicația web DSC. Funcționează cu noul API Dragon Star v1 (autentificare cu cheie API) și, până la retragerea sa de către Dragon Star, cu API-ul vechi (legacy).

#### 2. Funcționalități Cheie

- **Două versiuni de API:** transportatorii noi folosesc API v1 (cheie API); cei existenți rămân pe API-ul vechi (utilizator și parolă) până la comutare. Dragon Star păstrează API-ul vechi disponibil cel puțin până la 31 martie 2027. Câmpul *DSC API Version* de pe metoda de livrare alege varianta
- **Tarif pe comanda de vânzare:** costul transportului este cotat de Dragon Star (fără TVA) pentru punctul de lucru, sau se folosește un preț fix, cu un prag opțional peste care se interoghează Dragon Star. Cotarea funcționează doar dacă Dragon Star a activat-o pe contul clientului
- **AWB și etichetă:** AWB-ul se emite la validarea transferului; eticheta se atașează ca PDF (A4 sau A6) sau ZPL. Dacă eticheta nu poate fi obținută, AWB-ul rămâne pe livrare și eticheta se poate reobține ulterior (`dsc_get_label`); butonul *Print AWB* o tipărește
- **Opțiuni de expediere:** mai multe colete, valoare declarată, ramburs (cash on delivery, cu metodele de plată tratate drept ramburs configurabile), livrare sâmbăta, colet deschis la livrare, notificare prin SMS și cine plătește transportul (expeditor sau destinatar). Se completează din *Carrier Details* pe livrare
- **Puncte de lucru:** punctele de lucru (sucursalele) contului DSC se importă ca locații de ridicare (buton *Initialization*), iar fiecare AWB se emite pentru punctul de lucru din care pleacă coletul
- **Localități:** butonul *Get city* adaugă în agenda Odoo localitățile DSC care lipsesc
- **Borderou și comandă de ridicare:** un job programat zilnic la 18:00 (*DSC: Create borderou and pickup orders*) creează borderoul și trimite comenzile de ridicare pentru expedierile zilei, astfel încât AWB-urile rămân anulabile până atunci; numărul borderoului se salvează pe expedierile cuprinse
- **Anulare cu motiv clar:** un AWB se poate anula din Odoo (*Cancel AWB*) doar în 30 de minute de la creare și înainte de includerea în borderou; în caz contrar, Odoo spune care condiție nu este îndeplinită și unde se cere anularea. Momentul creării se păstrează ca `awb_date` în `shipment_info`; pentru AWB-urile create înainte de 19.0.1.4.0 fereastra de 30 de minute rămâne verificată de DSC
- **Urmărire:** istoricul stărilor se citește din Dragon Star și se scrie pe livrare, până la livrare; link-ul de urmărire deschide expedierea pe site-ul Dragon Star. Interogarea periodică este protejată: un AWB refuzat de curier nu blochează interogarea livrărilor următoare, iar starea se aplică printr-o singură scriere, doar dacă s-a schimbat
- **Configurare:** metodă de livrare cu *Provider* = Dragon Star Curier și produs de tip serviciu; cheia API se creează în aplicația DSC la *Settings > API access* (cu autentificare în doi pași), cu lista adreselor IP publice ale serverului Odoo; tipul etichetei (PDF/ZPL) și formatul paginii (A4/A6) se aleg în fila *DSC Configuration*. DSC nu are server de test, deci se folosește o cheie API separată pentru testare
- **Date trimise către Dragon Star:** la fiecare cotare și expediere se trimit numele destinatarului, persoana de contact, adresa, județul, localitatea, codul poștal, telefonul și e-mailul, numărul de colete și greutatea, suma ramburs, valoarea declarată, nota de livrare și punctul de lucru; comanda de ridicare poartă și adresa și telefonul de ridicare

Funcționalități neacoperite: dimensiunile coletului, returnarea coletului, nota de restituire, starea AWB-ului de retur, tipărirea borderoului în PDF, lockere și puncte de ridicare.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)

Dependență externă Python: `phonenumbers`.

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea de Componente Cheie a fost omisă deoarece există un fișier `readme/DESCRIPTION.md` care acoperă Sumarul și Funcționalitățile Cheie, iar acesta nu solicită explicit detalierea modelelor, vizualizărilor sau acțiunilor.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru gestiunea livrărilor pe care `deltatech_delivery_dsc` îl extinde cu integrarea curierului Dragon Star Curier; din el vine și aplicarea stării de livrare (`_apply_delivery_status`) folosită la urmărire.
