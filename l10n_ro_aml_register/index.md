# Romania - Registru de conformitate AML (localizat la `l10n_ro_aml_register/index.md`)

- **Nume Tehnic:** `l10n_ro_aml_register`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_aml_register
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_aml_register`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Registrul verificărilor de conformitate AML este jurnalul care dovedește, la un control ONPCSB, că măsurile de cunoaștere a clientelei din **Legea 129/2019** au fost aplicate efectiv. Este singurul artefact din zona AML care nu se poate reconstitui retroactiv: o listă de parteneri verificați se poate reface oricând, dar dovada că verificarea a avut loc la o anumită dată, de o anumită persoană, cu o anumită concluzie, se pierde definitiv dacă nu a fost scrisă atunci.

#### 2. Funcționalități Cheie

- **Jurnal imutabil:** fiecare verificare primește o referință din secvență (`AML/2026/00001`) încă din ciornă. Odată consemnată (butonul **Consemnează**), nu mai poate fi modificată sau ștearsă din interfață, nici de ofițerul de conformitate; dacă situația s-a schimbat, se consemnează o verificare nouă. Documentele justificative pot fi anexate și ulterior.
- **Concluzie obligatorie:** consemnarea cere o concluzie motivată, partea urmărită la control; *Data verificării* este data declarată, iar momentul real al consemnării rămâne în chatter.
- **Consemnare automată:** confirmarea unui screening de sancțiuni pe partener și verificarea unui beneficiar real scriu automat în registru, cu trimitere la înregistrarea verificată. Screeningul automat (la salvare sau după importul listelor) nu scrie în registru, ca să nu-l umple de zgomot. Dacă partenerul sau beneficiarul este marcat sancționat, rezultatul este *Escaladat către persoana desemnată*, cu risc *Ridicat*.
- **Ce se consemnează:** tipul verificării (cunoaștere inițială, revizuire periodică, screening sancțiuni, verificare beneficiar real, verificare ocazională, reevaluare de risc), rezultatul (fără suspiciuni, escaladat, raportat ONPCSB, relație refuzată/încetată), nivelul de risc, documentul sursă, cine a verificat și când.
- **Meniu:** *Facturare/Contabilitate → Configurare → Contabilitate → Registru Verificări AML*, filtrat implicit pe verificările consemnate; rândurile sunt colorate după gravitate (portocaliu pentru escaladat, roșu pentru raportat ONPCSB sau relație refuzată/încetată).
- **Pe fișa partenerului:** butonul **Verificări AML** (numărul verificărilor consemnate, cu istoric cronologic descrescător) și câmpul **Ultima verificare AML** din blocul *România — Screening Fiscal*.
- **Drepturi:** fără configurare proprie; ștergerea ciornelor e permisă doar grupului **Ofițer de conformitate AML** (din `l10n_ro_partner_ubo`), iar meniul cere rolul de administrator la contabilitate. Registrul nu trimite notificări la escaladare.

#### 3. Dependențe

- [l10n_ro_partner_ubo](../l10n_ro_partner_ubo/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.aml.review`: verificarea AML (cu `mail.thread`), cu referință din secvență, stări ciornă/consemnată și blocarea modificărilor după consemnare.
- `res.partner` (extins): butonul și contorul de verificări AML, data ultimei verificări.
- `l10n.ro.partner.ubo` (extins): scrie automat în registru la verificarea unui beneficiar real.

**Vizualizări**

- `view_l10n_ro_aml_review_list` / `view_l10n_ro_aml_review_form` / `view_l10n_ro_aml_review_search`: lista (colorată după gravitate), formularul cu butonul Consemnează și filtrele registrului.
- `view_partner_form_l10n_ro_aml_register`: butonul și câmpul pe fișa partenerului.
- `action_l10n_ro_aml_review`: acțiunea de meniu a registrului.

**Acțiuni Automate / Acțiuni Server**

- `seq_l10n_ro_aml_review` (`ir.sequence`): secvența referințelor `AML/<an>/<număr>`.
- Nu există sarcini `ir.cron`.

#### 5. Conexiuni

- [l10n_ro_partner_ubo](../l10n_ro_partner_ubo/index.md): sursa grupului de ofițer de conformitate AML și a modelului beneficiar real (`l10n.ro.partner.ubo`); verificarea confirmată a unui beneficiar real scrie automat în acest registru.
- `account`: meniul registrului este sub *Contabilitate*, iar accesul e condiționat de grupul `account.group_account_manager`.
