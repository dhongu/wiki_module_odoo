# Romania - Beneficiarul real al partenerului (localizat la `l10n_ro_partner_ubo/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_ubo`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_partner_ubo
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_ubo`
- **Ultima Ingestie:** `2026-11-25`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține evidența beneficiarilor reali (UBO — Ultimate Beneficial Owner) ai partenerilor de afaceri, conform măsurilor de cunoaștere a clientelei impuse de Legea 129/2019 privind prevenirea și combaterea spălării banilor. Extinde motorul de screening din `l10n_ro_partner_screening` și îl aplică nu doar pe societate, ci pe persoanele fizice care o controlează — acolo unde riscul este de fapt ascuns.

#### 2. Funcționalități Cheie

- Tab dedicat "Beneficiari Reali" pe fișa partenerului persoană juridică, cu identificarea completă a fiecărei persoane fizice care deține sau controlează societatea
- Natura controlului conform art. 4 alin. (2): deținere directă (peste 25%), deținere indirectă, control prin alte mijloace sau conducere de rang înalt (art. 4 alin. (2) lit. a) pct. 2 din Legea 129/2019; folosită doar ca soluție subsidiară, cu tipul de control **Conducere de rang înalt**, justificată în câmpul Note, nu prin completarea unei cote fictive)
- Proveniența informației (declarația clientului, extras ONRC, RECOM, registru public al altui stat) și documentele justificative atașate
- CNP-ul și documentele sunt vizibile doar grupului "Ofițer de conformitate AML" (art. 23)
- Screening automat al fiecărui beneficiar real pe listele OFAC și UE Consolidated, limitat la intrările de tip persoană pentru a evita fals-pozitivele; rulează la salvare și după fiecare actualizare a listelor; confirmarea potrivirii rămâne a operatorului, prin butonul "Screening sancțiuni" de pe formularul beneficiarului real
- O potrivire la screening este semnalată ca „posibilă" și consemnată în chatter-ul partenerului; screeningul presupune liste de sancțiuni încărcate de `l10n_ro_partner_screening` (altfel verificarea nu rulează)
- Statusul de screening al partenerului capătă două trepte noi, cu prioritate asupra celorlalte semnale: "Beneficiar Real Sancționat" (primează asupra oricărui alt semnal, inclusiv asupra unei societăți altfel curate pe liste) și "Beneficiar Real Lipsă" (partener companie în relație de afaceri, client sau furnizor, fără niciun beneficiar real documentat, semnalat cu banner de avertizare pe fișă)
- Nivelul de risc AML se stabilește pe fișa fiecărui partener (implicit mediu) și determină periodicitatea revizuirii
- Detectare automată a structurilor de proprietate opace (niciun deținător nu depășește 25%)
- Revizuire periodică cu termen calculat pe nivelul de risc AML al partenerului — 12 luni (risc ridicat), 24 (mediu, implicit) sau 36 (redus) — vizibilă în meniul *Contabilitate → Beneficiari Reali*, filtrul "Revizuire expirată"; cronul săptămânal "RO UBO: Revizuirea periodică a beneficiarilor reali" (livrat dezactivat, se activează din *Setări → Tehnic → Acțiuni programate*) creează automat activități pentru persoana desemnată
- Evidența ultimei declarații proprii depuse la Registrul Comerțului (ONRC) și semnalarea automată a obligației anuale, rămasă în vigoare după Legea 315/2021 doar pentru societățile cu acționari sau sediu fiscal în jurisdicții necooperante (derivată din lista HG 1/2024 întreținută de modulul de screening)
- Configurare din *Contabilitate → Configurare → Setări → Partner Screening (RO)*: persoana desemnată AML (primește activitățile de revizuire) și data ultimei declarații depuse la ONRC; grupul "Ofițer de conformitate AML" se acordă din *Setări → Utilizatori → Contabilitate*

#### 3. Dependențe

- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.partner.ubo`: beneficiarul real — identitate, tip control, cotă deținută, sursa informației, termen de revizuire calculat din nivelul de risc al partenerului
- `l10n.ro.sanction` (extins): motorul de potrivire pe listele OFAC/UE Consolidated, aplicat aici limitat la intrările de tip persoană
- `res.partner` (extins): statusurile suplimentare "Beneficiar Real Sancționat" / "Beneficiar Real Lipsă", detectarea structurii de proprietate opace
- `res.company` / `res.config.settings` (extinse): persoana desemnată AML, data ultimei declarații ONRC

**Vizualizări**

- `l10n_ro_partner_ubo_view.xml`: formular și listă pentru beneficiarii reali, cu butonul de acțiune server "Screening sancțiuni"
- `res_partner_view.xml`: tabul "Beneficiari Reali" pe fișa partenerului și banner-ul de avertizare
- `res_config_settings_views.xml`: secțiunea de configurare Partner Screening (RO)

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ubo_review`: cron săptămânal (livrat inactiv) care revizuiește periodic beneficiarii reali expirați și creează activități pentru persoana desemnată AML
- `action_server_screen_ubo`: acțiune server legată la listă, rulează screening-ul de sancțiuni pe beneficiarii reali selectați (fără confirmare automată)

#### 5. Conexiuni

- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md): furnizează motorul de potrivire pe listele de sancțiuni (OFAC, UE Consolidated, HG 1/2024) pe care acest modul îl reutilizează pentru persoanele fizice
- [l10n_ro_aml_register](../l10n_ro_aml_register/index.md): depinde de acest modul; verificarea confirmată a unui beneficiar real (butonul **Screening sancțiuni**) se consemnează automat în registrul imutabil AML, iar grupul „Ofițer de conformitate AML" definit aici controlează ștergerea ciornelor din registru
