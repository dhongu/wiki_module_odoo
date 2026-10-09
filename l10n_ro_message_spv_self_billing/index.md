# Self-Billing Message SPV (Autofacturare mesaje SPV)

- **Nume Tehnic:** `l10n_ro_message_spv_self_billing`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_message_spv_self_billing
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_message_spv_self_billing`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

La autofacturare (Codul fiscal, art. 319 alin. 18) clientul emite factura în numele furnizorului și o raportează în SPV. Numărul legal al unui astfel de document este cel alocat de client, nu unul din secvența proprie a furnizorului. Folosirea secvenței obișnuite de vânzări îl strică, pentru că documentele ajung la câteva zile după facturile deja emise și sunt datate retroactiv. Modulul adaugă pe jurnale o opțiune prin care ciorna este numerotată automat cu referința din mesajul SPV la care a fost asociată.

#### 2. Funcționalități Cheie

- Opțiune nouă pe jurnal, *Număr din mesajul SPV*, dezactivată implicit; vizibilă doar pe jurnalele de vânzări și de achiziții.
- La asocierea unei ciorne cu mesajul SPV (butonul *Find invoice*), dacă jurnalul are opțiunea bifată, ciorna primește ca număr referința mesajului, în locul numărului din secvența jurnalului.
- Documentele deja poștate nu sunt renumerotate niciodată.
- Dacă numărul există deja în același jurnal și companie, înlocuirea se omite și se scrie un avertisment în log (postarea ar eșua oricum pe constrângerea de unicitate); ciorna păstrează numărul din secvență.
- Configurare recomandată: un jurnal de vânzări dedicat (ex. *Autofacturare*) cu opțiunea bifată.
- Ordinea contează: întâi asocierea cu mesajul SPV, apoi postarea. Dacă documentul este postat înainte, el este trimis în SPV, unde clientul l-a raportat deja.

#### 3. Dependențe

- `l10n_ro_message_spv`

#### 4. Componente Cheie

**Modele**

- `account.journal` (extins): câmpul boolean `l10n_ro_spv_number_from_message` (*Number from SPV message*).
- `l10n.ro.message.spv` (extins): metoda `_l10n_ro_apply_number_from_message`, apelată din `get_data_from_invoice` înaintea metodei de bază, pentru ca numărul să fie pe factură înainte ca mesajul să își actualizeze starea.

**Vizualizări**

- `view_account_journal_form`: moștenește formularul jurnalului și adaugă opțiunea după `refund_sequence`, vizibilă doar pentru tipurile `sale` și `purchase`.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `l10n_ro_message_spv`: modulul de bază care preia mesajele din SPV și le asociază cu facturile.
- [l10n_ro_message_spv_purchase](../l10n_ro_message_spv_purchase/index.md): creează facturi de achiziție din mesajele SPV; poate fi folosit împreună cu jurnale de achiziții marcate pentru numerotare din mesaj.
