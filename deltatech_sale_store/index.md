# Deltatech Sale from Store (localizat la `deltatech_sale_store/index.md`)

- **Nume Tehnic:** `deltatech_sale_store`
- **Versiune:** `19.0.2.5.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_store
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_store`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul facilitează vânzarea directă din magazin prin emiterea de bonuri fiscale. Permite generarea unui fișier destinat programului de tipărit bonuri fiscale și definirea unui client generic pentru care bonurile fiscale se emit automat. Prin marcarea jurnalelor cu opțiunea „Bon fiscal", modulul stabilește ce jurnale de vânzări produc bonuri fiscale și restricționează utilizarea jurnalelor de tip cash, oferind astfel un flux ordonat pentru încasările din magazin.

#### 2. Funcționalități Cheie

- Generarea unui fișier pentru programul de tipărit Bonuri Fiscale.
- Definirea unui client generic pentru care se emit automat bonurile fiscale.
- Opțiunea „Bon fiscal" în jurnal: la un jurnal de vânzări, marcajul definește jurnalul (jurnalele) pentru bonuri fiscale; la un jurnal de tip cash, marcajul restricționează folosirea jurnalului în alte plăți/încasări.
- Pregătire necesară: trebuie definit un jurnal de vânzări pentru Bonuri Fiscale cu codul `BF`, marcat cu opțiunea „Jurnal bonuri fiscale". Opțiunea nu se bifează pe jurnalul obișnuit de facturi clienți (vânzări online/standard); informația „vândut pe bon fiscal" este purtată per document de câmpul **Vânzare din magazin** (`sale_store`), setat automat din comanda de vânzare.
- Jurnale: la jurnalul de bonuri fiscale se poate restricționa tipul de document permis (ex. doar *Chitanță*); la jurnalele cash folosite pentru încasarea bonurilor se setează **Cod ECR** (0 = numerar, 1 = tichet de masă, 2 = card). Setarea „Restricționează jurnalele pentru bonuri fiscale" (Vânzări → Setări) limitează plățile la jurnale bancare și cash marcate pentru bon fiscal.
- Client generic: comenzile pe partenerul generic (`deltatech_partner_generic`) sunt marcate automat „Vânzare fără factură", iar factura se creează ca chitanță (`out_receipt`) în jurnalul de bonuri fiscale; emiterea unei facturi obișnuite pe clientul generic este blocată.
- Transport bon fiscal din factură (parametri de sistem `account_invoice.*`): `ecr_transport` = `file` (implicit, descarcă un fișier `.inp`), `connect` (agent local Terrabit Connect) sau `fisco` (agent local Fisco.ro); plus `ecr_connect_url`, `ecr_fisco_url`, `ecr_type` (`datecs18` implicit, sau `daisy`) și `ecr_extension`. Transportul `fisco` și protocolul `daisy` nu sunt încă verificate pe echipament real; indicatorul de stare din systray funcționează doar pentru Terrabit Connect.
- Stornarea (retur magazin): o factură de tip storno se trimite la casa de marcat ca „dispoziție de plată" (retragere din sertar), doar dacă banii au fost returnați pe un jurnal cash; un retur non-cash nu trimite nimic la casă. Doar plățile `in_process`/`paid` sunt luate în calcul.
- Codul ECR al taxei (`cod_ecr`) este transmis la casa de marcat când există (necesită `deltatech_pos_base`); în lipsa lui se folosește codul derivat din procent.
- Grup nou de securitate „Înregistrează plăți doar la data curentă": utilizatorii din grup au data plății blocată pe azi în wizardul „Înregistrează plata" și în wizardul de plată al vânzării din magazin.
- Notificările email generate la vânzarea din magazin sunt puse în coadă, ca o eroare de trimitere să nu blocheze tipărirea bonului fiscal după commit.
- Câmpurile de audit fiscal (`fiscal_receipt_number`, `fiscal_doc_number`, `fiscal_z`, `fiscal_state`, `fiscal_error`) și `receipt_print` nu se mai copiază la duplicarea facturii.
- Export SAGA (coloana `TIP`): factură obișnuită = gol; factură cu „Vânzare din magazin" = `f`; chitanță (bon fără factură) = `B`, sau `C` dacă partenerul are CIF; storno-urile moștenesc marcajul comenzii (`f`).

#### 3. Dependențe

- `deltatech_ecr_fiscal`
- `account`
- `web`
- `sale`
- `stock`
- `sales_team`
- [deltatech_partner_generic](../deltatech_partner_generic/index.md)
- [deltatech_record_type](../deltatech_record_type/index.md)
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md)

#### 4. Componente Cheie

> Documentația pentru această secțiune este preluată din `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului (modele, vizualizări, acțiuni automate) este omisă deoarece Readme-ul nu o solicită explicit.

#### 5. Conexiuni

- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): furnizează conectarea la casa de marcat (ECR) folosită pentru tipărirea bonurilor fiscale generate de acest modul.
- [deltatech_saga](../deltatech_saga/index.md): fluxul de documente (factură/bon fiscal/storno) al acestui modul alimentează coloana `TIP` din exportul SAGA (`f`/`B`/`C`), conform `readme/CONFIGURE.md`.
- `deltatech_payment_report`: definește conturile contabile (`data/account_data.xml`) reutilizate de fluxul de plăți/încasări asociat bonurilor fiscale (referit în comentariile manifestului).
