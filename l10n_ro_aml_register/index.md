# Romania - Registru de conformitate AML (localizat la `l10n_ro_aml_register/index.md`)

- **Nume Tehnic:** `l10n_ro_aml_register`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_aml_register
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_aml_register`
- **Ultima Ingestie:** `2026-09-12`

#### 1. Sumar

Registrul verificărilor de conformitate AML este jurnalul care dovedește, la un control
ONPCSB, că măsurile de cunoaștere a clientelei impuse de Legea 129/2019 au fost aplicate
efectiv. Este singurul artefact din zona AML care nu se poate reconstitui retroactiv: o listă
de parteneri verificați se poate reface oricând, dar dovada că o verificare a avut loc la o
anumită dată, de o anumită persoană, cu o anumită concluzie, se pierde definitiv dacă nu a
fost scrisă atunci — de aceea registrul este imutabil odată consemnat.

#### 2. Funcționalități Cheie

- Fiecare verificare primește o referință din secvență (`AML/2026/00001`), fără întreruperi.
- Odată consemnată (butonul **Consemnează**), o verificare nu mai poate fi modificată sau
  ștearsă — nici de ofițerul de conformitate; dacă situația s-a schimbat, se consemnează o
  verificare nouă. Concluzia este obligatorie la consemnare — este partea citită la control.
- Documentele justificative pot fi anexate și ulterior, fără a altera constatarea; chatter-ul
  rămâne activ prin `mail.thread`.
- Confirmarea unui screening de sancțiuni pe partener (sau verificarea unui beneficiar real)
  scrie automat o intrare consemnată în registru, cu trimitere la înregistrarea verificată.
  Screeningul automat care rulează la fiecare salvare și după fiecare import de liste **nu**
  scrie în registru, ca să nu-l umple de zgomot.
- Tipuri de verificare consemnate: cunoaștere inițială, revizuire periodică, screening
  sancțiuni, verificare beneficiar real, verificare ocazională legată de o operațiune,
  reevaluare de risc.
- Rezultate posibile: fără suspiciuni, escaladat către persoana desemnată, raportat ONPCSB,
  relație refuzată sau încetată — plus nivelul de risc constatat, documentul sursă și cine/când
  a verificat.
- Pe fișa partenerului apare un buton cu numărul verificărilor consemnate și data ultimei
  verificări, lângă celelalte semnale de screening.
- Registru accesibil din *Contabilitate → Registru Verificări AML*, filtrat implicit pe
  verificările consemnate; ștergerea ciornelor este permisă doar grupului **Ofițer de
  conformitate AML** (din `l10n_ro_partner_ubo`), iar verificările consemnate nu pot fi șterse
  de nimeni.
- Nu are ecran de configurare propriu — se bazează pe setările din `l10n_ro_partner_ubo`
  (grupul de ofițer AML) și pe persoana desemnată AML din *Contabilitate → Configurare →
  Setări*.

#### 3. Dependențe

- [l10n_ro_partner_ubo](../l10n_ro_partner_ubo/index.md)

#### 5. Conexiuni

- [l10n_ro_partner_ubo](../l10n_ro_partner_ubo/index.md): sursa grupului de ofițer de conformitate AML și a modelului
  beneficiar real (`l10n.ro.partner.ubo`); verificarea confirmată a unui beneficiar real
  scrie automat în acest registru.
- `account`: meniul registrului este agățat sub *Contabilitate*, iar accesul de scriere/citire
  e condiționat de grupul `account.group_account_manager`.
