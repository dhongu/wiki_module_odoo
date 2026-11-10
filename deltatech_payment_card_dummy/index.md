# Card Dummy Payment (localizat la `deltatech_payment_card_dummy/index.md`)

- **Nume Tehnic:** `deltatech_payment_card_dummy`
- **Versiune:** `19.0.0.0.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_card_dummy
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_card_dummy`
- **Ultima Ingestie:** `2026-11-01`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul Card Dummy Payment oferă un furnizor de plată cu cardul simulat (fictiv) pentru Odoo. Este destinat în principal testării fluxurilor de plată sau scenariilor în care plățile cu cardul sunt procesate printr-un terminal extern și trebuie înregistrate rapid în Odoo, fără o integrare bancară directă. Tranzacțiile sunt marcate instant ca finalizate, ceea ce permite verificarea rapidă a tranzițiilor de stare a comenzilor și facturilor, precum și a acțiunilor declanșate după plată (livrări automate, notificări pe e-mail), fără bani reali și fără configurări complexe de sandbox.

#### 2. Funcționalități Cheie

- Simulează plăți cu cardul în timpul procesului de checkout din eCommerce.
- Înregistrează plăți cu cardul pentru facturile din portal, fără a necesita date reale de card.
- Permite testarea fluxului complet comandă-spre-plată într-un mediu de dezvoltare sau staging.
- Poate fi folosit ca substitut (placeholder) pentru tranzacții manuale cu cardul gestionate prin terminale POS fizice.
- Flux de plată simulat care imită experiența unui furnizor de plată real: clientul confirmă plata, se creează o tranzacție simulată marcată imediat ca reușită, iar comanda sau factura își actualizează automat starea.
- Suport pentru capturarea manuală (manual capture) a tranzacțiilor autorizate.
- Configurare minimă: nu necesită chei API sau credențiale externe — funcționează imediat.
- Integrare completă cu modulele standard Odoo `payment` și `website_sale`.
- Configurare: din **Contabilitate** (sau **Facturare**) > **Configurare** > **Furnizori de plată** se deschide furnizorul „Card Dummy”, se setează **Starea** pe Mod test (dezvoltare) sau Activat (producție), se alege jurnalul de plată în care se înregistrează tranzacțiile și, dacă e nevoie, se publică furnizorul pe site.

#### 3. Dependențe

- `payment`
- `sale`
- `payment_custom`

#### 4. Componente Cheie

Readme-ul nu cere explicit detalierea componentelor; mai jos sunt cele verificate în cod.

**Modele**

- `payment.provider` (extins): adaugă codul de furnizor `card_dummy` („Card Dummy”), activează captura manuală (`support_manual_capture`: `full_only`) și setează metodele de plată implicite.
- `payment.transaction` (extins): pentru `card_dummy` omite validarea sumei și marchează tranzacția direct ca finalizată (`_set_done`).
- `sale.order`, `account.move` (extinse): moștenirile există, dar nu conțin logică activă (codul e comentat).

**Vizualizări**

- `inline_form` / `payment_details`: formularul inline afișat la checkout pentru furnizorul Card Dummy; conține doar câmpurile ascunse `provider_id` și `partner_id`, fără date de card.

**Acțiuni Automate / Acțiuni Server**

- Niciun `ir.cron` sau acțiune server. Există un controller public JSON-RPC `/payment/card_dummy/payment`, care procesează tranzacția simulată, plus `post_init_hook` / `uninstall_hook` care înregistrează, respectiv resetează furnizorul `card_dummy`. Furnizorul se creează implicit în stare de test și nepublicat.

#### 5. Conexiuni

- `website_sale`: checkout-ul eCommerce în care apare furnizorul simulat (nu e declarat în dependențe).
