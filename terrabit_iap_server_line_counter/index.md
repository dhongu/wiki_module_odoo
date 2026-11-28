# Terrabit IAP Server Line Counter (localizat la `terrabit_iap_server_line_counter/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_line_counter`
- **Versiune:** `20.0.2.0.2`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_iap_server_line_counter
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_line_counter`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Serviciu al serverului IAP Terrabit care numără liniile de cod sursă ale modulelor instalate pe instanța unui client. Operatorul Terrabit alege dintr-o listă modulele care contează (de regulă cele Terrabit sau de la terți, nu cele oficiale Odoo), iar rezultatul rămâne pe contul clientului, pentru evidență și facturare în funcție de volumul de cod livrat.

#### 2. Funcționalități Cheie

- Serviciu nou „Module Line Counter” (`line_counter`) în catalogul serviciilor serverului IAP.
- Buton de preluare a listei de module instalate de la client; la reîncărcare se păstrează bifele existente și se elimină modulele dezinstalate.
- Opțiunea „Hide Odoo S.A. Modules” (implicit activă) omite modulele oficiale Odoo; modulele OCA rămân vizibile.
- Modulele găsite direct în repo-ul principal al clientului (nu în submodul) sunt bifate automat pentru numărare; bifele manuale pe submodule se păstrează.
- Buton de numărare: clientul numără liniile doar pentru modulele bifate, iar pe cont se salvează liniile pe modul și totalul.
- Apelurile către client nu scriu tokenul contului în jurnal.
- Limitare cunoscută (P1, deschisă): apelurile nu folosesc validarea URL și restricția la redirecționări ale serviciului părinte.

#### 3. Dependențe

- `terrabit_iap_server`

#### 4. Componente Cheie

**Modele**

- `iap.server.account` (extins): lista modulelor clientului, totalul de linii și opțiunea de ascundere a modulelor oficiale; acțiunile de preluare și numărare.
- `iap.server.account.line.counter.module`: un modul al clientului, cu autor, bifa „Count”, indicatorul „Repo Module” și numărul de linii.
- `iap.server.service` (extins): adaugă codul de serviciu `line_counter`.

**Vizualizări**

- `view_iap_server_account_form_line_counter`: moștenește formularul contului IAP și adaugă lista modulelor, comutatorul de selecție și totalul.

**Acțiuni Automate / Acțiuni Server**

- Fără cron sau acțiuni server; serviciul se creează din `iap_server_service_data.xml`.

#### 5. Conexiuni

- `terrabit_iap_server`: serverul IAP pe care se înregistrează serviciul.
