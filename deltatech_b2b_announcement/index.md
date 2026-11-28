# Anunțuri B2B

- **Nume Tehnic:** `deltatech_b2b_announcement`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_b2b_announcement
- **Cale Locală:** `odoo-addons/bitshop/deltatech_b2b_announcement`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Note datate pentru clienții companie ai portalului B2B: un cont bancar nou pentru plăți, o schimbare de preț la un furnizor, o gamă nouă de produse sau o regulă de livrare. Clienții le văd pe pagina de start a portalului, fără acces în backend.

#### 2. Funcționalități Cheie

- Anunțurile se administrează în *Website ▸ Configurare ▸ Anunțuri B2B*: titlu, dată, text și, la bazele cu mai multe website-uri, website-ul (gol: toate); arhivarea scoate anunțul din portal.
- Ultimele trei anunțuri apar pe pagina `/my` a contactelor unei companii B2B active, sub rezumatul contului din `deltatech_b2b_portal`, cele mai noi primele.
- Titlul și textul sunt traductibile.
- Temele le pot afișa și în alte locuri prin `_b2b_latest(website, limit)`.
- Pot scrie anunțuri doar editorii website-ului (*Website / Editor și Designer*); ceilalți angajați le pot citi. Pașii sunt în fișa consultantului.

#### 3. Dependențe

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.b2b.announcement`: anunțul (titlu, text, dată, website, activ).

**Vizualizări**

- `b2b_announcement_views.xml`: lista și formularul anunțurilor.
- `portal_templates.xml`: blocul *Anunțuri* de pe `/my`.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md): pagina `/my` pe care sunt afișate anunțurile.
- [deltatech_b2b_price_tier](../deltatech_b2b_price_tier/index.md) și [deltatech_b2b_website_restrict](../deltatech_b2b_website_restrict/index.md): alte extensii ale portalului B2B.
