# Numerotare autofacturare SPV

- **Nume Tehnic:** `l10n_ro_message_spv_self_billing`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_message_spv_self_billing
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_message_spv_self_billing`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

La autofacturare (Codul fiscal, art. 319 alin. 18) clientul emite factura în numele furnizorului și o raportează în SPV. Numărul legal al unui asemenea document este cel alocat de client, nu unul din secvența proprie a furnizorului. Modulul preia acest număr din mesajul SPV, astfel încât documentele sosite cu întârziere și datate retroactiv să nu fie numerotate din secvența obișnuită de vânzări.

#### 2. Funcționalități Cheie

- Opțiune nouă pe jurnal (vânzări și achiziții): **Număr din mesajul SPV**, implicit dezactivată.
- La potrivirea unui draft cu mesajul SPV (*Găsește factura*), documentul dintr-un astfel de jurnal primește ca număr referința mesajului, nu numărul din secvența jurnalului.
- Documentele postate nu se renumerotează niciodată.
- Un număr deja folosit în jurnal este sărit și înregistrat în log, pentru că postarea ar eșua pe constrângerea de unicitate.
- Flux: se creează un jurnal dedicat (ex. *Autofacturare*), se bifează opțiunea, se înregistrează documentul ca draft, se potrivește cu mesajul SPV, apoi se postează. Ordinea contează: potrivirea întâi, postarea după, altfel documentul ajunge în SPV, unde clientul l-a raportat deja.

#### 3. Dependențe

- [l10n_ro_message_spv](../l10n_ro_message_spv/index.md)

#### 4. Componente Cheie

**Modele**

- `account.journal` (extins): câmpul *Număr din mesajul SPV*.
- `l10n.ro.message.spv` (extins): la potrivire numerotează draftul cu referința mesajului.

**Vizualizări**

- `view_account_journal_form`: moștenește formularul jurnalului (`account.view_account_journal_form`) cu opțiunea nouă.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [l10n_ro_message_spv](../l10n_ro_message_spv/index.md): sursa mesajelor SPV potrivite cu documentele.
