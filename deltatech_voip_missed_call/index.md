# Phone - Missed Calls to Call Back (localizat la `deltatech_voip_missed_call/index.md`)

- **Nume Tehnic:** `deltatech_voip_missed_call`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_voip_missed_call
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_voip_missed_call`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

O listă comună a clienților de sunat înapoi, în aplicația Telefon. Fiecare client care a sunat și nu a primit răspuns apare o singură dată, iar linia se închide singură în momentul în care cineva vorbește cu el. Astfel, apelurile pierdute, inclusiv cele din cozi fără agent, nu se mai pierd între operatori.

#### 2. Funcționalități Cheie

- **O linie per client**: la un apel primit pierdut sau respins, *Telefon > Apeluri pierdute* arată linia numărului, cu contactul, numărul de încercări și ultima încercare; apelurile următoare de la același număr, în orice format, se adaugă la aceeași linie.
- **Închidere automată**: un apel răspuns cu numărul respectiv (de ieșire sau primit), de orice utilizator, închide linia; un apel înapoi fără răspuns o lasă deschisă.
- **Comună operatorilor**: fiecare utilizator intern vede liniile companiilor sale, nu doar apelurile care l-au sunat.
- **Marchează ca rezolvat**: pentru clientul contactat altfel (mobil, email), cu evidența cine și când.
- **Note** pe linie, în listă sau în formular; rămân și după rezolvare.
- **Pe țări** (panou lateral, din prefixul numărului) și **pe operatori** (căutare, grupare, filtre salvate).
- **Apel înapoi dintr-un clic**: numărul este link Telefon.
- Funcționează cu orice furnizor VoIP (softphone Odoo sau integrări precum Daktela). La instalare se reiau apelurile pierdute și răspunse din ultimele 7 zile. Numerele se compară în format internațional față de țara companiei, deci aceasta trebuie setată.

Fluxul detaliat este în fișa de consultant.

#### 3. Dependențe

- `voip`

#### 4. Componente Cheie

**Modele**

- `voip.missed.call`: linia de apel de returnat (client, încercări, operatori, stare, rezolvat de, notă).
- `voip.call` (extins): leagă apelurile din istoric de linii și le închide.

**Vizualizări**

- `voip_missed_call_view_list`, `voip_missed_call_view_form`, `voip_missed_call_view_search`: lista, formularul și căutarea.
- `voip_missed_call_action`: acțiunea meniului *Apeluri pierdute*.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: reia apelurile din ultimele 7 zile la instalare.

#### 5. Conexiuni

- [deltatech_voip_daktela](../deltatech_voip_daktela/index.md): apelurile importate din Daktela închid sau deschid linii.
- [deltatech_voip_sale](../deltatech_voip_sale/index.md): același widget Telefon, cu comenzile clientului.
