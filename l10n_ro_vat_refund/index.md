# Romania - Rambursare TVA (sold negativ D300) (localizat la `l10n_ro_vat_refund/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_refund`
- **Versiune:** `19.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_vat_refund
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_vat_refund
- **Ultima Ingestie:** `2026-10-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul urmărește cererile de rambursare a TVA rezultate din soldul negativ al decontului D300, conform Codului Fiscal art. 303: termen ANAF de 45 de zile, cu dobânzi de 0,02%/zi la depășire. Gestionează ciclul cererii printr-o mașină de stări (cerere → inspecție → rambursată/compensată) și generează notele contabile aferente. Depunerea documentației și comunicarea cu ANAF rămân pași manuali.

#### 2. Funcționalități Cheie

- **Alegerea opțiunii pe D300:** pe închiderea de TVA a perioadei, verificarea „TVA de recuperat — alegere opțiune" deschide un asistent pentru reportarea soldului sau cererea de rambursare; alegerea „rambursare" creează cererea și bifează rambursarea în D300 (`solicit_ramb = D`, cu primul cont bancar al companiei, schimbabil din verificarea „Opțiuni decont D300"). Asistentul se confirmă înainte de generarea fișierului D300.
- **Lista cererilor:** **Contabilitate → Raportare → Declarații ANAF → Rambursare TVA**, cu stare colorată (roșu pentru termen expirat sau cerere respinsă, verde pentru cele soluționate favorabil); numărul cererii vine dintr-o secvență dedicată.
- **Formularul cererii:** compania, luna D300, D300-ul aferent (opțional, recomandat), suma solicitată, jurnalul contabil (primul jurnal general, schimbabil) și zona de termene ANAF cu data depunerii, termenul de 45 de zile, data soluționării, zilele de depășire și dobânzile.
- **Mașină de stări:** Ciornă → Depusă la ANAF → În inspecție fiscală → Aprobată / Aprobată parțial / Respinsă → Virată de ANAF / Compensată, prin butoanele „Depune la ANAF", „În inspecție fiscală", „Aprobat integral", „Aprobat parțial", „Respins", „Înregistrează virat ANAF" și „Înregistrează compensare". Data depunerii se poate completa manual dacă cererea a fost depusă înainte de înregistrarea în Odoo.
- **Dobânzi de întârziere:** suma solicitată × 0,02% × zilele de depășire a termenului de 45 de zile, și în cazul aprobării parțiale (se calculează pe suma solicitată integral).
- **Note contabile:** la virament, încasarea în 5121 și stingerea TVA de recuperat 4424, cu linie suplimentară pentru dobânzi, în venituri 7588; la compensare, stingerea 4424, cu contrapartida (de exemplu 4423 sau 4481) completată manual pe notă. Conturile se caută automat în planul de conturi românesc.
- **Urmărirea termenelor:** o verificare programată creează activități de avertizare pe cererile aflate în stare Depusă sau În inspecție, cu termenul depășit.
- **Mai multe luni:** se creează câte o cerere pentru fiecare lună D300 cu sold negativ.

#### 3. Dependențe

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md)
- `mail`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.vat.refund`: cererea de rambursare TVA, cu stări, termen, dobânzi și notele contabile de virament și compensare (are chatter și activități).
- `l10n.ro.vat.refund.wizard` (wizard): alegerea între reportarea soldului negativ și rambursare.
- `account.return` (extins): legătura către cererea de rambursare (`l10n_ro_refund_id`) și opțiunea aleasă pentru soldul negativ (`l10n_ro_refund_option`).

**Vizualizări**

- `l10n_ro_vat_refund_form` / `l10n_ro_vat_refund_list`: formularul și lista cererilor.
- `l10n_ro_vat_refund_graph` / `l10n_ro_vat_refund_pivot` / `l10n_ro_vat_refund_search`: analiza și filtrarea cererilor.
- `l10n_ro_vat_refund_wizard_form`: asistentul de alegere a opțiunii.
- `check_template_vat_refund_option`: verificarea „TVA de recuperat — alegere opțiune" din fluxul `account.return` pentru D300.

**Acțiuni Automate / Acțiuni Server**

- `cron_l10n_ro_vat_refund_check_deadlines` („RO: Check VAT Refund Deadlines"): rulează săptămânal și creează activități de avertizare pentru cererile cu termenul de 45 de zile depășit.

#### 5. Conexiuni

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): sursa soldului negativ TVA care declanșează cererea de rambursare.
- `l10n_ro_reports`: tipul de declarație (`ro_tax_return_type`) pe care se atașează verificarea.
