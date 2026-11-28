# Trepte de Preț B2B

- **Nume Tehnic:** `deltatech_b2b_price_tier`
- **Versiune:** `20.0.1.1.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_b2b_price_tier
- **Cale Locală:** `odoo-addons/bitshop/deltatech_b2b_price_tier`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Afișează în pagina de produs, pentru clienții companie ai portalului B2B, prețul pe cantitate din lista lor de prețuri: „de la 10 bucăți plătiți mai puțin”. Tabelul arată exact ce taxează coșul, fără un preț paralel.

#### 2. Funcționalități Cheie

- Treptele sunt regulile obișnuite de listă de prețuri cu cantitate minimă din lista clientului.
- Se afișează doar contactelor unei companii cu cont B2B activ; vizitatorii și clienții retail văd pagina neschimbată.
- Dacă lista nu are reguli cu cantitate minimă pentru produs, se încearcă cantitățile uzuale (1, 5, 10, 25, 50); tabelul se ascunde când toate au același preț.
- Fiecare treaptă arată prețul unitar și economia față de o bucată.
- Condiții de configurare: activarea *Liste de prețuri* în *Vânzări ▸ Configurare ▸ Setări*, afișarea prețurilor fără taxe în website, iar pe clientul B2B contul *Activ* și lista de prețuri aleasă (tabul *B2B*).
- Limită cunoscută: prețurile sunt cele calculate de lista de prețuri, fără opțiunea website-ului de preț cu sau fără taxe. Pașii sunt în fișa consultantului.

#### 3. Dependențe

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md)

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): calculul treptelor de preț din lista de prețuri a clientului.

**Vizualizări**

- `product_templates.xml`: tabelul *Prețul tău pe cantitate* la finalul detaliilor de produs.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md): starea contului B2B și lista de prețuri a clientului.
- [deltatech_b2b_announcement](../deltatech_b2b_announcement/index.md) și [deltatech_b2b_website_restrict](../deltatech_b2b_website_restrict/index.md): alte extensii ale portalului B2B.
