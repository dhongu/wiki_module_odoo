# LibraPay Payment (localizat la `deltatech_payment_libra_pay/index.md`)

- **Nume Tehnic:** `deltatech_payment_libra_pay`
- **Versiune:** `19.0.1.0.16`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_libra_pay
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_libra_pay`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul integrează Odoo cu LibraPay, serviciul de plată online cu cardul oferit de Libra Internet Bank în România. Permite companiilor să accepte plăți cu cardul (Visa, Mastercard) atât pentru comenzile din magazinul online (eCommerce), cât și pentru facturile din portalul clienților, oferind o experiență de plată fiabilă și adaptată pieței românești. Fluxul folosește redirecționarea către pagina de plată găzduită de bancă, astfel încât datele cardului nu ajung niciodată pe serverul Odoo, iar statusul comenzilor și facturilor este actualizat automat pe baza confirmării primite de la bancă.

#### 2. Funcționalități Cheie

- Acceptarea plăților cu cardul prin metoda „Pay with card (LibraPay)” în procesul de checkout din eCommerce.
- Plata facturilor deschise direct din portalul clientului, cu **Pay Now**.
- Încasare imediată, într-un singur pas: cardul este debitat și comanda sau factura este marcată ca plătită.
- Actualizarea automată a statusului comenzilor de vânzare și al facturilor pe baza feedback-ului de la Libra Internet Bank.
- Notificări asincrone (IPN — Instant Payment Notifications), pentru a garanta înregistrarea plății chiar dacă clientul închide browserul înainte de redirecționare; adresa IPN se setează în portalul comerciantului LibraPay la `https://<domeniul-tău>/payment/libra_pay/ipn`.
- Mesaje semnate: cererile și răspunsurile sunt semnate cu cheia comerciantului; un răspuns cu semnătură greșită este respins înainte de orice procesare. Codul de răspuns `00` confirmă plata, orice alt cod pune tranzacția în „Error" cu mesajul băncii; suma și moneda fiecărui răspuns sunt verificate înainte de confirmare.
- Flux de redirecționare securizat: datele cardului sunt introduse pe infrastructura sigură a băncii. Odoo trimite către LibraPay, la fiecare plată, liniile comenzii/facturii (produs, cantitate, preț, TVA) și datele de contact de facturare și livrare ale clientului.
- Moduri de Test (sandbox) și Live (producție), cu adrese separate: starea **Test** pentru mediul de test LibraPay, **Enabled** pentru plăți reale; furnizorul se publică pe site.
- Configurare: Facturare → Configurare → Plăți online → Furnizori de plată → **Libra Pay**; fila **Credentials** (**Terminal**, **Libra Pay Key** — șir hexazecimal, **Merchant name**, **Merchant URL**, **Merchant**, **Merchant Email**), fila **Configuration** (jurnalul plăților). Cheia este stocată în clar pe furnizor, deci formularul trebuie deschis doar de utilizatori de încredere.
- Tranzacțiile (modul developer, Plăți online → Tranzacții de plată) apar ca **Confirmed**, **Pending** sau **Error**; **Provider Reference** este numărul comenzii trimis băncii (cifra 9 urmată de cifrele referinței Odoo), cel de căutat în portalul LibraPay. O plată refuzată rămâne în Error cu mesajul băncii, iar o nouă încercare creează o tranzacție nouă.
- Confirmarea creează o plată contabilă pe jurnalul furnizorului, „In Process" până la reconcilierea cu extrasul; comisionul băncii nu este calculat de modul, ci înregistrat la reconciliere. Rambursările se fac în portalul LibraPay.
- Pașii detaliați, cu capturi de ecran, sunt în [Fișa Consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `payment`
- `website_sale`

Dependențe Python externe: `phpserialize`.

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune nu este detaliată deoarece documentația se bazează pe `readme/DESCRIPTION.md`, care nu solicită explicit analiza componentelor tehnice (modele, vizualizări, acțiuni automate).

Pe scurt, din cod reiese că modulul definește un nou furnizor de plată (`payment.provider`, cod `libra_pay`, cu câmpurile de comerciant și `libra_pay_key`; câmpurile nefolosite de utilizator/parolă au fost eliminate) și o metodă de plată dedicate LibraPay, extinde `account.payment.method` (tip „multi", jurnale bancare), plus controllere pentru gestionarea redirecționării de retur și a notificărilor IPN (`/payment/libra_pay/ipn`). Hook-uri `post_init_hook` / `uninstall_hook` pentru configurarea furnizorului.

Note tehnice (corecții de compatibilitate cu API-ul de plăți din Odoo 19 și de securitate): `_extract_amount_data` este suprascris pentru LibraPay (rezolvă `KeyError: 'amount'` la fiecare retur/IPN); semnătura `P_SIGN` este verificată (cu `hmac.compare_digest`) în controllere înainte de orice procesare, iar o notificare cu semnătură invalidă este respinsă cu HTTP 400 fără a modifica starea tranzacției, deci o cerere falsificată nu poate perturba plata altui client; câmpurile din notificare sunt citite defensiv cu `.get()`; `_search_by_reference` nu mai generează eroare 500 când nu găsește nicio tranzacție (loghează un avertisment și lasă fluxul standard să redirecționeze către pagina de status a plății; dacă mai multe tranzacții au aceeași referință, se folosește ultima).

#### 5. Conexiuni

- `payment`: framework-ul standard Odoo de furnizori și tranzacții de plată, pe care se construiește acest acquirer.
- `website_sale`: magazinul online Odoo, unde LibraPay apare ca metodă de plată la checkout.
