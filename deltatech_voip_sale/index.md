# Phone - Sales Orders (localizat la `deltatech_voip_sale/index.md`)

- **Nume Tehnic:** `deltatech_voip_sale`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_voip_sale
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_voip_sale`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Comenzile de vânzare la îndemână în timpul unui apel, în aplicația Telefon. Agentul vede imediat comenzile clientului care sună și poate începe o comandă nouă, iar pe comandă are la vedere telefoanele adreselor de facturare și de livrare.

#### 2. Funcționalități Cheie

- **Butonul Comenzi** în widgetul Telefon, înainte de *Mergi la*: la sunare, în timpul apelului, în rezumat, în istoric și în activități. Deschide comenzile clientului și pe cele livrate la una din adresele lui; o singură comandă se deschide direct, altfel se afișează lista (cele mai noi întâi), iar *Nou* începe o comandă pentru client.
- **Ambele telefoane pe comandă**: telefonul adresei de facturare și al celei de livrare, ca linkuri Telefon, sub adrese (cu opțiunea *Adresele clientului* activă în setările de facturare).
- Butonul se arată agenților de vânzări (*Vânzări / Utilizator: Numai documente proprii* și peste), pentru apeluri cu contact cunoscut; funcționează cu orice furnizor VoIP.

Fluxul detaliat este în fișa de consultant.

#### 3. Dependențe

- `voip_sale`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): telefoanele de facturare și livrare.
- `res.partner` (extins): comenzile clientului pentru butonul din widget.

**Vizualizări**

- `view_order_form_voip_phone`: telefoanele sub adresele comenzii.
- `static/src/orders_button.xml` și `orders_button.esm.js`: butonul Comenzi din widgetul Telefon.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_voip_daktela](../deltatech_voip_daktela/index.md): butonul funcționează și la apelurile Daktela.
- [deltatech_voip_missed_call](../deltatech_voip_missed_call/index.md): Comenzile se pot vedea înainte de apelul înapoi.
