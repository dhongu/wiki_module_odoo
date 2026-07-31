# Baza ANAF România (localizat la `l10n_ro_anaf_base/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_base`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_base
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_base`
- **Ultima Ingestie:** 2026-05-31
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul centralizează logica comună și infrastructura necesară pentru generarea și exportul declarațiilor fiscale către ANAF (Soft A - Adobe XDP și Soft J - XML). Oferă o bază solidă pentru toate modulele specifice de declarații ANAF, asigurând consistența și eliminând duplicarea codului.

## 2. Funcționalități Cheie

- **Mixin pentru Handlers (`L10nRoAnafReportHandlerMixin`):** Gestionează datele companiei și ale declarantului, validări înainte de export (VAT, adresă fiscală, județ, CAEN), validare XML față de scheme XSD ANAF, generare nume fișier și export XDP/XML.
- **Registru de Profile de Declarații (`anaf_declaration_profile`):** Mecanism centralizat pentru înregistrarea și selecția automată a versiunilor de formulare ANAF, cu suport pentru perioade istorice.
- **Extensii pe modele standard:** `res.company` și `res.config.settings` pentru configurarea persoanei responsabile, identificator declarant, tip export implicit și instalare module ANAF; `account.report` pentru înregistrarea tipului MIME pentru fișierele `.xdp`.
- **Date Demo și Utilitar de Pregătire:** Seturi de date de test și un script utilitar (`preparer.py`) pentru pregătirea rapidă a mediului de test.
- **Infrastructură Teste Automate:** Clasă de bază reutilizabilă (`AnafTestCommon`) pentru toate modulele ANAF, configurând automat mediul de test și eliminând duplicarea setup-ului.

## 3. Dependențe

- `account_reports`
- `l10n_ro`
- `accountant`

## 4. Componente Cheie

### Modele

- `anaf_declaration_profile`: Gestionează profilele de declarații ANAF, incluzând versiunea, valabilitatea și schemele XSD.
- `anaf_report_handler_mixin` (Mixin Python): Oferă logica comună pentru gestionarea datelor și validărilor necesare declarațiilor ANAF.
- `res.company`: Extins pentru a stoca informații despre persoana responsabilă și alte setări ANAF la nivel de companie.
- `res.config.settings`: Extins pentru a oferi o interfață de configurare a setărilor ANAF.
- `account.report`: Extins pentru a gestiona tipurile MIME pentru fișierele XDP.
- `account.chart.template`: Poate fi extins pentru a include setări specifice ANAF în template-urile planurilor de conturi.

### Vizualizări / Date

- `views/anaf_menu.xml`: Definește intrările de meniu relevante pentru declarațiile ANAF.
- `views/res_config_settings_views.xml`: Adaugă opțiuni de configurare în interfața de setări generale.
- `demo/demo_data.xml`: Conține date de test pentru demonstrații și dezvoltare.
- `security/ir.model.access.csv`: Definește drepturile de acces pentru entitățile ANAF.

### Acțiuni Automate / Acțiuni Server

*Nu au fost identificate explicit în `__manifest__.py` sau `readme/DESCRIPTION.md` ca acțiuni automate individuale, funcționalitățile fiind integrate în mixin-uri și profile.*