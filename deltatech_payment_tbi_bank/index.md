# Banca TBI Bank Payment Acquirer (localizat la `deltatech_payment_tbi_bank/index.md`)

- **Nume Tehnic:** `deltatech_payment_tbi_bank`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_tbi_bank
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_tbi_bank`
- **Ultima Ingestie:** `2026-10-01`

#### 1. Sumar

Modulul adaugă în magazinul online metoda de plată „tbi Bank", prin care cumpărătorul poate solicita finanțare (plata în rate) direct la finalizarea comenzii sau la plata unei facturi. Datele cererii se pregătesc automat din comanda de vânzare sau din factură, se criptează și se trimit către banca TBI, iar decizia băncii (aprobat, refuzat, în așteptare) se reflectă automat în tranzacția din Odoo, fără intervenție manuală.

#### 2. Funcționalități Cheie

- Furnizor de plată nou `tbi Bank` (`code = tbi_bank`), cu metodă de plată dedicată.
- Cererea de finanțare (JSON cu datele comenzii, ale clientului și produsele) este criptată RSA (PKCS#1 v1.5) cu cheia publică TBI, împărțită în blocuri și codificată base64; browserul o trimite automat către endpoint-ul Finalize al băncii împreună cu `providerCode`.
- Endpoint-ul se alege automat după starea furnizorului: producție când furnizorul este activat, mediul UAT (de test) în caz contrar.
- Suportă atât comenzi de vânzare, cât și facturi: dacă tranzacția este legată de facturi, produsele și datele clientului se iau din factură; altfel din liniile comenzii; ca ultimă variantă, o singură linie.
- Procesarea răspunsului: datele primite de la bancă se decriptează cu cheia privată proprie, iar `status_id` se mapează pe starea tranzacției (`1` aprobat, `0` anulat/refuzat, `2` în așteptare).
- Mod opțional în două faze (autorizare, apoi captură manuală din Odoo): `tbi_bank_mode` = `1` (o fază) sau `2` (două faze, tranzacțiile aprobate rămân „Autorizate").
- Securitate: un răspuns cu `order_id` lipsă sau diferit de referința tranzacției este respins; răspunsurile pentru tranzacții deja finalizate sunt ignorate; un payload care nu poate fi decriptat lasă tranzacția în așteptare; datele sensibile nu se loghează.
- Configurare în Setări > Plăți > Furnizori > tbi Bank: `Store ID`, `Provider Code`, utilizator și parolă API, mod (o fază/două faze) și cheile PEM (publică TBI pentru criptare, privată proprie pentru decriptare).
- Limitări cunoscute: `order_total` se trimite rotunjit la număr întreg, conform exemplului PHP al băncii; codul categoriei produsului este implicit `"8"`; operațiile de captură/anulare urmează semantica iPay și pot necesita adaptare.

#### 3. Dependențe

- `payment`
- `website_sale`
- `phone_validation`
- Python extern: `cryptography`

#### 4. Componente Cheie

**Modele**

- `payment.provider` (extins): câmpuri tbi Bank (Store ID, Provider Code, utilizator, parolă, mod, chei PEM), alegerea URL-ului API (live/UAT), criptarea cererii și decriptarea răspunsului.
- `payment.transaction` (extins): construiește payload-ul cererii din comandă/factură, extrage referința și suma din răspuns, aplică statusul băncii asupra tranzacției, cereri de captură și anulare.
- `account.payment.method` (extins): înregistrează metoda de plată `tbi_bank`.

**Vizualizări**

- `tbi_bank_form` (`views/payment_templates.xml`): formularul de redirecționare automată către banca TBI.
- `acquirer_form_ipay` (`views/payment_views.xml`): formularul furnizorului de plată, cu câmpurile specifice tbi Bank.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni automate sau cron-uri. Controllerul `TBIPayController` (`controllers/main.py`) primește răspunsul băncii (return URL) și îl transmite spre procesare tranzacției. Modulul rulează `post_init_hook` și `uninstall_hook`.

#### 5. Conexiuni

- [deltatech_payment_bt_ipay](../deltatech_payment_bt_ipay/index.md): furnizor de plată iPay (Banca Transilvania), de la care provine adaptarea acestui modul.
