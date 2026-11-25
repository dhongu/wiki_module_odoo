# Romania - Registru de conformitate AML (localizat la `l10n_ro_aml_register/index.md`)

- **Nume Tehnic:** `l10n_ro_aml_register`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_aml_register
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_aml_register`
- **Ultima Ingestie:** `2026-11-25`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Registrul verificărilor de conformitate AML este jurnalul care dovedește, la un control
ONPCSB, că măsurile de cunoaștere a clientelei impuse de Legea 129/2019 au fost aplicate
efectiv. Este singurul artefact din zona AML care nu se poate reconstitui retroactiv: o listă
de parteneri verificați se poate reface oricând, dar dovada că o verificare a avut loc la o
anumită dată, de o anumită persoană, cu o anumită concluzie, se pierde definitiv dacă nu a
fost scrisă atunci — de aceea registrul este imutabil odată consemnat.

#### 2. Funcționalități Cheie

- Fiecare verificare primește o referință din secvență (`AML/2026/00001`), atribuită încă din ciornă.
- Odată consemnată (butonul **Consemnează**), o verificare nu mai poate fi modificată sau
  ștearsă din interfață — nici de ofițerul de conformitate; dacă situația s-a schimbat, se consemnează o
  verificare nouă. Concluzia motivată este obligatorie la consemnare — este partea citită la control.
- Verificările se consemnează manual (**Nou** în registru: partener, tip, rezultat, *Ce s-a verificat*,
  *Concluzie și motivare*). *Data verificării* este data declarată; momentul real al consemnării rămâne în chatter.
- Documentele justificative pot fi anexate și ulterior, fără a altera constatarea; chatter-ul
  rămâne activ prin `mail.thread`.
- Confirmarea unui screening de sancțiuni pe partener (butonul **Screening** de pe fișa partenerului) sau pe
  un beneficiar real (**Screening sancțiuni**) scrie automat o intrare deja consemnată în registru, cu listele
  interogate, numărul de potriviri și trimitere la înregistrarea verificată; dacă partenerul sau beneficiarul e
  marcat sancționat, rezultatul este *Escaladat către persoana desemnată* și riscul *Ridicat*.
  Screeningul automat care rulează la fiecare salvare și după fiecare import de liste **nu**
  scrie în registru, ca să nu-l umple de zgomot.
- Tipuri de verificare consemnate: cunoaștere inițială, revizuire periodică, screening
  sancțiuni, verificare beneficiar real, verificare ocazională legată de o operațiune,
  reevaluare de risc.
- Rezultate posibile: fără suspiciuni, escaladat către persoana desemnată, raportat ONPCSB,
  relație refuzată sau încetată — plus nivelul de risc constatat, documentul sursă și cine/când
  a verificat. În listă, rândurile portocalii sunt cele escaladate, iar cele roșii cele raportate
  ONPCSB sau cu relația refuzată/încetată.
- Pe fișa partenerului apare butonul **Verificări AML** cu numărul verificărilor consemnate (deschide istoricul
  partenerului, cronologic descrescător, inclusiv ciornele) și câmpul **Ultima verificare AML** din blocul
  *România — Screening Fiscal*, lângă celelalte semnale de screening.
- Registrul se deschide din *Facturare/Contabilitate → Configurare → Contabilitate → Registru Verificări AML*,
  filtrat implicit pe verificările consemnate; ștergerea ciornelor este permisă doar grupului **Ofițer de
  conformitate AML** (din `l10n_ro_partner_ubo`), iar verificările consemnate nu pot fi șterse
  de nimeni. Meniul cere rolul de Administrator la contabilitate; persoana desemnată are nevoie de ambele drepturi.
- Nu are configurare proprie. Câmpul **Persoană desemnată AML** din *Setări* aparține modulului de beneficiari
  reali: registrul nu îl folosește și nu trimite notificări când o verificare este escaladată.

#### 3. Dependențe

- [l10n_ro_partner_ubo](../l10n_ro_partner_ubo/index.md)

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md` (completat cu `USAGE.md` și `CONFIGURE.md`),
care nu solicită analiza codului pentru Componente Cheie; secțiunea de mai jos listează doar elementele evidente
din structura modulului.

**Modele**

- `l10n.ro.aml.review` (nou, cu `mail.thread`): verificarea AML din registru, cu referință din secvență, tip, rezultat, risc, concluzie și stare ciornă/consemnată.
- `res.partner` (extins): butonul **Verificări AML** și data ultimei verificări consemnate.
- `l10n.ro.partner.ubo` (extins): consemnarea automată în registru a verificării unui beneficiar real.

**Vizualizări**

- `view_l10n_ro_aml_review_list`, `view_l10n_ro_aml_review_form`, `view_l10n_ro_aml_review_search`: lista (colorată după gravitate), formularul și căutarea registrului.
- `view_partner_form_l10n_ro_aml_register`: butonul și câmpul AML pe fișa partenerului.
- `action_l10n_ro_aml_review`: acțiunea meniului registrului.

**Acțiuni Automate / Acțiuni Server**

- `seq_l10n_ro_aml_review`: secvența `AML/<an>/<număr>` a verificărilor (nu e cron; nu există acțiuni automate propriu-zise).

#### 5. Conexiuni

- [l10n_ro_partner_ubo](../l10n_ro_partner_ubo/index.md): sursa grupului de ofițer de conformitate AML și a modelului
  beneficiar real (`l10n.ro.partner.ubo`); verificarea confirmată a unui beneficiar real
  scrie automat în acest registru.
- `account`: meniul registrului este agățat sub *Contabilitate*, iar accesul de scriere/citire
  e condiționat de grupul `account.group_account_manager`.
