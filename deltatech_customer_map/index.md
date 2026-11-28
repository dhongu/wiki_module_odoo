# Customer Map

- **Nume Tehnic:** `deltatech_customer_map`
- **Versiune:** `20.0.1.1.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_customer_map
- **Cale Locală:** `odoo-addons/bitshop/deltatech_customer_map`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Arată unde vinde compania pe o hartă 3D cu relief real: fiecare județ al României sau fiecare țară a Europei este colorată după vânzări, număr de clienți sau număr de facturi. Este gândită pentru directorii de vânzări care vor să vadă zonele neacoperite, pe care un tabel nu le arată.

#### 2. Funcționalități Cheie

- **Relief 3D real**; motorul 3D se încarcă doar la deschiderea hărții, iar fără WebGL 2 harta trece pe un desen 2.5D, fără eroare.
- **România și Europa**: 41 de județe plus București și 55 de țări europene; un clic pe România din harta Europei deschide harta județelor.
- **Trei indicatori, cinci perioade**: vânzări fără TVA în moneda companiei, clienți activi sau facturi, pe 3, 6, 12, 24 de luni sau tot istoricul.
- **Județe și orașe**: la trecerea mouse-ului se văd cifrele și rangul; clic deschide orașele, clienții de top și produsele de top.
- **Fiecare client plasat**: după județul din fișă, apoi după orașul înregistrat, apoi după numele orașului; clienții neplasabili și cei din afară sunt numărați separat.
- **Agenții își văd clienții**: cu rolul *Own customers* (impus pe server); cu *All customers* directorul vede toată compania și poate alege un agent.
- Vânzările sunt aceleași ca în Customer Portfolio (facturi postate minus note de credit, conturile de vânzări setate acolo, fără avansuri).
- Meniu: *Vânzări > Portofoliu clienți > Customer Map*. Pentru plasare completați Agent, Țară și Județ pe clienți; opțional `base_address_extended` și `l10n_ro_city`.
- Hărțile, terenul și motorul 3D sunt incluse în modul: nicio dată nu iese din Odoo.

#### 3. Dependențe

- [deltatech_customer_segment](../deltatech_customer_segment/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.customer.map`: model de serviciu care calculează la deschidere cifrele pe județe/țări, orașe, clienți și produse.

**Vizualizări**

- `action_customer_map`: acțiune client (harta 3D, componentă OWL).

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_customer_analysis](../deltatech_customer_analysis/index.md): tablou de acțiuni zilnice pe clienți, același meniu Customer Portfolio.
