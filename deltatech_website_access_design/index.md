# Acces web designer pe website

- **Nume Tehnic:** `deltatech_website_access_design`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_access_design
- **Cale Locală:** odoo-addons/deltatech/deltatech_website_access_design
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Ascunde meniurile de back-office pentru parteneri, vânzări și facturi de utilizatorii care trebuie să lucreze doar pe website, de exemplu un web designer. Designerul editează site-ul cu dreptul standard *Website: Restricted Editor*, fără să fie administrator de website, și nu vede meniurile comerciale.

#### 2. Funcționalități Cheie

- Grup dedicat *Access Partners, Sale, Invoice*; la instalare, toți utilizatorii interni existenți intră în grup, deci nimeni nu pierde un meniu.
- La instalare, o singură dată, meniurile **Contacts**, **Sales**, **Invoicing > Customers** și **Invoicing > Vendors** sunt rezervate grupului, înlocuind grupurile anterioare; o actualizare nu le mai atinge, deci grupurile adăugate manual se păstrează.
- Configurarea unui designer: în *Settings > Users & Companies > Users*, **Website** = *Restricted Editor*, apoi scoaterea utilizatorului din grup (modul dezvoltator, fila **Users** a grupului).
- Se ascund doar meniurile; regulile de înregistrare și drepturile de acces nu se schimbă, deci înregistrările rămân accesibile prin alte meniuri, linkuri sau butoane inteligente.
- Limitări: utilizatorii interni creați după instalare nu sunt în grup și trebuie adăugați manual; la actualizarea Contacts, meniul Contacts redevine vizibil tuturor (se scoate din nou grupul *Internal User* din *Settings > Technical > Menu Items*); la dezinstalare meniurile primesc înapoi grupurile modulelor lor.

#### 3. Dependențe

- `website`
- `contacts`
- `sale`
- `account`

#### 4. Componente Cheie

**Modele**

- `res.groups` (înregistrare de date): grupul *Access Partners, Sale, Invoice*.

**Vizualizări**

- Fără vizualizări proprii; modulul modifică grupurile meniurilor existente.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: adaugă utilizatorii interni în grup și rezervă cele patru meniuri grupului.
- `uninstall_hook`: restabilește grupurile originale ale meniurilor.

#### 5. Conexiuni

- `website`: dreptul *Restricted Editor* pentru designer.
