# Romania - Instrumente de plată (cecuri, bilete la ordin) (localizat la `l10n_ro_payment_instruments/index.md`)

- **Nume Tehnic:** `l10n_ro_payment_instruments`
- **Versiune:** `19.0.1.2.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payment_instruments
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payment_instruments`
- **Ultima Ingestie:** 2026-10-09
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează instrumentele de plată specifice (cecuri, bilete la ordin, cambii) conform Legii 58/1934 (cambia și biletul la ordin) și Legii 59/1934 (cecul). Urmărește fiecare instrument printr-o mașină de stări de la emitere/primire până la onorare sau refuz, generează automat notele contabile aferente fiecărei etape, stinge facturile acoperite la înregistrare (și le redeschide la refuz) și oferă un scadențar cu alerte. Conturile contabile sunt auto-detectate din planul de conturi RO și pot fi suprascrise manual.

#### 2. Funcționalități Cheie

- Tipuri suportate: cec primit (5112), cec emis (conturi manuale), bilet la ordin de primit (413) / de plătit (403), cambie de primit (413) / de plătit (403).
- Mașină de stări: Ciornă → În portofoliu → Remis la bancă → Onorat, cu ramuri Refuzat → Protestat și Andosat (pentru BO/cambii primite).
- Note contabile automate per etapă:
  - cec primit: Dr 5112 = Cr 4111 la înregistrare; depunerea la bancă nu face notă; încasare Dr 5121 = Cr 5112; refuz Dr 4111 = Cr 5112;
  - BO/cambie primită: Dr 413 = Cr 4111 la înregistrare; depunere la bancă Dr 5113 = Cr 413; încasare Dr 5121 = Cr 5113 (sau Dr 5121 = Cr 413 fără depunere);
  - BO/cambie emisă: Dr 401 = Cr 403, plată Dr 403 = Cr 5121, refuz Dr 403 = Cr 401;
  - andosare: Dr 401 (furnizorul) = Cr 413 (clientul); factura furnizorului se reconciliază manual cu linia 401 din caseta „Debit nealocat".
- Facturi acoperite: se sting la înregistrarea instrumentului și se redeschid, cu scadența inițială, la refuz.
- Data operației: fiecare notă se datează cu câmpul „Data operației" de pe instrument (data primirii, a extrasului, a refuzului), nu cu data apăsării butonului; după fiecare pas câmpul revine la ziua curentă.
- Refuzul reface creanța/datoria și creează o activitate de avertizare; butonul Protest trece instrumentul în Protestat, fără notă.
- Blocaj opt-in la facturare (FR-39): dacă `res.company.l10n_ro_block_refused_instrument` e bifat (Setări → Contabilitate → Instrumente de plată (RO)), confirmarea unei facturi de client către un partener cu instrumente în stare Refuzat este blocată; nu se aplică notelor de credit și facturilor de furnizor și încetează la trecerea în Protestat.
- Scadențar (Contabilitate → Contabilitate → Instrumente de Plată, filtru implicit „În portofoliu") cu „Zile până la scadență" și coduri de culoare: roșu (depășit/refuzat/protestat), portocaliu (în 5 zile), verde (onorat/andosat), gri (anulat).
- Cron zilnic de alertă, dezactivat implicit, cu X zile înainte de scadență (parametru `l10n_ro_payment_instruments.alert_days_before_due`, implicit 5); activitatea se atribuie celui care a creat instrumentul, cu notificare pe email.
- Auto-detectare conturi 5112, 5113, 413, 403, 4111, 401, 5121 din planul RO (potrivire doar ca prefix de cod), cu suprascriere manuală per instrument; jurnalul implicit este primul de tip Operațiuni diverse, schimbabil pe instrument.
- Cu extrase bancare importate: la „Cont bancă" se poate alege contul reconciliabil de încasări/plăți în curs, ca încasarea să nu apară de două ori pe 5121.
- Un instrument cu note postate nu se poate anula până nu se stornează notele; „Resetează la Ciornă" apare doar pe instrumentele fără notă de înregistrare.
- Limitări: fără refuz/încasare parțială, fără scontare (5114, 667), fără calcul de termene de protest; valoarea nominală e în moneda companiei.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payment.instrument`: Instrumentul de plată cu mașina de stări, conturile asociate, data operației și generarea notelor contabile.
- `account.move` (extindere): adaugă blocajul opt-in de postare a facturilor de vânzare pentru partenerii cu instrumente refuzate, agregat în garda de postare din `l10n_ro_anaf_base`.
- `res.company` (extindere): câmpul boolean `l10n_ro_block_refused_instrument` care activează blocajul.
- `res.config.settings` (extindere): expune `l10n_ro_block_refused_instrument` în configurarea companiei.

**Vizualizări / Date**

- `views/l10n_ro_payment_instrument_views.xml`: Interfața de gestionare și scadențarul instrumentelor.
- `views/res_config_settings_views.xml`: Setarea de blocaj facturare pentru parteneri cu instrumente refuzate.
- `data/ir_cron.xml`: Cron-ul zilnic de alertă scadență.
- `security/ir.model.access.csv`: Drepturile de acces.

**Acțiuni Automate / Acțiuni Server**

- `cron_check_due_dates` („RO Payment Instruments: due date alert"): rulează zilnic (inactiv implicit) și creează activități de avertizare cu un număr configurabil de zile înainte de scadența instrumentelor în portofoliu sau remise.

#### 5. Conexiuni

- [l10n_ro_leasing](../l10n_ro_leasing/index.md)
