# Cargus Shipping (localizat la `deltatech_delivery_uc/index.md`)

- **Nume Tehnic:** `deltatech_delivery_uc`
- **Versiune:** `20.0.1.0.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_uc
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_uc`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul integrează în Odoo curierul Cargus. Expediați coletele prin Cargus și le urmăriți online: AWB-ul și eticheta se generează din livrare, tarifele se calculează pe comanda de vânzare cu tabelul de prețuri al contractului, iar starea coletului se citește din Cargus până la livrare. Sunt suportate și lockerele Cargus și livrările în alte țări deservite de același API.

#### 2. Funcționalități Cheie

- Generare AWB în format PDF, ZPL sau HTML; etichetă A4 sau 10x14; **Print AWB** și **Cancel AWB** (anulare la Cargus).
- Calcul de tarif pe comandă cu tabelul de prețuri Cargus, sau preț fix sub un prag.
- Colete multiple, dimensiuni, valoare declarată (asigurare), ramburs, livrare sâmbăta, deschiderea coletului.
- Oraș și județ prin identificatorii Cargus; liste de orașe, județe, lockere și puncte de ridicare, importate din API.
- Istoric de stare al coletului (fila **History**, buton **Refresh**) și lista de AWB-uri.
- Lockere și puncte de ridicare: import și administrare, curățarea automată a lockerelor cu coordonate invalide, trimiterea identificatorului de locker în AWB, hartă de selecție în checkout (necesită `deltatech_delivery_locker`).
- Expedieri în alte țări deservite de același API (inclusiv Polonia): țările cu catalog importat se aleg pe curier, iar AWB-ul poartă țara destinatarului.
- Cu `deltatech_delivery_cod`, import al extrasului Cargus pentru o perioadă (doar sumele deja plătite de Cargus).
- Neacoperit: oraș dat doar prin nume, fără identificator, și nota de restituire în AWB. Extensia PostgreSQL `unaccent` trebuie instalată; unele localități au în SIRUTA alt nume decât cel din Cargus (ex. Popești-Leordeni).
- Configurare: în metoda de livrare cu *Provider* = Cargus, fila **Cargus Configuration**: *Subscription Key*, utilizator, parolă; **Initialization** (importă tabelele de prețuri), **Get Pickup Locations** (cel puțin o locație de ridicare, necesară pentru fiecare AWB), țările din **Cargus Catalog Countries** și **Get city**; apoi tip și format etichetă, plătitor și metodele de plată tratate ca ramburs. Pașii cu capturi în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins, `models/delivery_uc.py`): tipul `uc` (Cargus), credențialele și opțiunile Cargus, `uc_rate_shipment`, `uc_send_shipping`, `uc_get_label`, `uc_cancel_shipment`, `uc_get_status_history`, `uc_get_awb_list`, importul de locații, orașe și lockere, `uc_cod_fetch_rows`.
- `delivery.carrier.service` (extins): valoarea `uc` la `delivery_type`, pentru serviciile Cargus.
- `stock.package.type` (extins): tipul de curier `uc` pentru ambalaje.
- `res.country`, `res.country.state`, `res.city` (extinse): câmpul `uc_id` (identificator Cargus).
- `res.country.street` (nou): străzile Cargus, legate de oraș.
- `res.config.settings` (extins): opțiuni de configurare Cargus.

**Vizualizări**

- `view_delivery_carrier_form_with_provider_uc`: fila de configurare Cargus pe formularul metodei de livrare.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server`. `data/delivery_uc_data.xml` definește serviciile Cargus (`service_1`, `service_4`, `service_34`, `service_35`, `service_36`).

#### 5. Conexiuni

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): selecția lockerului Cargus pe hartă în checkout.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): gestionarea și urmărirea stărilor de expediere.
- [deltatech_delivery_cod](../deltatech_delivery_cod/index.md): importul extrasului de ramburs Cargus.
