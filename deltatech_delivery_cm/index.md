# Courier Manager Shipping (localizat la `deltatech_delivery_cm/index.md`)

- **Nume Tehnic:** `deltatech_delivery_cm`
- **Versiune:** `20.0.1.2.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_cm
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_cm`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite expedierea coletelor prin Courier Manager și urmărirea lor online: generează AWB-ul, cotează tariful și citește starea expedierii direct din livrarea Odoo, fără introducere manuală în platforma curierului.

#### 2. Funcționalități Cheie

- Generare AWB în format PDF, anulare AWB și obținerea tarifelor pentru o expediere.
- Import listă de localități și istoric de stare al expedierii (tab-ul **History**, buton **Refresh**).
- Expediere cu mai multe colete, cu valoare declarată (asigurare), cu ramburs și cu nume de localitate fără id.
- **Configurare**: în *Inventory > Configuration > Delivery > Shipping Methods* se creează metoda cu **Provider** *Courier Manager*; în tab-ul **Courier Manager Configuration** se introduc **Endpoint** și **API Key**, apoi **Initialization** (importă serviciile) și **Get city** (adaugă localitățile lipsă); se aleg **Service**, **Cm Label Format** (eticheta e mereu PDF) și metodele de plată tratate ca ramburs.
- **Flux**: pe comanda de vânzare costul este cotat de curier (sau preț fix sub prag); pe livrare, **Carrier Details** deschide expedierea; la validare AWB-ul este rezervat și confirmat pentru ridicare, referința de urmărire se scrie pe livrare, iar eticheta se atașează (**Print AWB**, **Cancel AWB**).
- Lista AWB-urilor tuturor livrărilor: *Inventory > Operations > Delivery AWB > Delivery AWB List*.
- **Neacoperit**: AWB în format HTML, listă de lockere și de puncte de ridicare, expediere cu dimensiuni, notă de restituire, livrare sâmbăta, deschidere colet, restricționare la un punct de ridicare, trimiterea id-ului de locker în AWB.

#### 3. Dependențe

- `delivery`
- `stock_delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea „Componente Cheie" este omisă: `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, iar componentele tehnice nu sunt cerute explicit în Readme.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru transportatori și AWB pe care acest modul îl extinde pentru integrarea cu Courier Manager.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): gestionarea statusurilor de livrare, complementară urmăririi istoricului de statusuri al expedierilor Courier Manager.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): suport pentru livrarea la lockere; relevant ca parte a ecosistemului de livrare (lockerele nu sunt acoperite de acest modul).
