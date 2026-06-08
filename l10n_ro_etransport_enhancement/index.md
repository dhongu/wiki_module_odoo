# eTransport Enhancement (localizat la `l10n_ro_etransport_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_etransport_enhancement`
- **Versiune:** `19.0.0.1.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_etransport_enhancement
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_etransport_enhancement`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul `l10n_ro_etransport_enhancement` extinde funcționalitatea standard de e-Transport din Odoo pentru piața românească, adăugând îmbunătățiri și opțiuni suplimentare. Scopul său este să facă integrarea cu sistemul e-Transport (SPV) mai flexibilă și mai ușor de folosit, simplificând conformitatea fiscală pentru transporturile de mărfuri. Modulul reduce efortul administrativ al departamentelor de logistică și contabilitate, permițând trimiterea documentelor de transport către autorități direct din operațiunile de stoc.

#### 2. Funcționalități Cheie

- Funcționalitate îmbunătățită pentru trimiterea documentelor e-Transport direct din livrările de stoc (stock pickings).
- Suport pentru diferite tipuri de trimitere prin parametri de context.
- Gestionare îmbunătățită a urmăririi straturilor de valorizare a stocului (stock valuation layer) pentru documentele e-Transport.
- Integrare optimizată cu sistemul românesc de e-Transport (SPV).
- Opțiuni suplimentare disponibile în meniul de acțiuni al livrării, accesibile automat după instalare.

#### 3. Dependențe

- `l10n_ro_edi`
- `l10n_ro_edi_stock`

#### 4. Componente Cheie

Secțiune omisă conform fluxului de ingestie: fișierul `readme/DESCRIPTION.md` este prezent și nu solicită explicit analiza codului pentru această secțiune. Detaliile de implementare (extinderea metodelor de stock picking, mecanismele de urmărire a straturilor de valorizare, gestionarea contextului) sunt descrise la nivel conceptual în Readme, fără enumerarea componentelor tehnice individuale.

#### 5. Conexiuni

- `l10n_ro_edi`: modulul de bază pentru integrarea EDI/e-Transport în localizarea românească, pe care acest modul îl extinde.
- `l10n_ro_edi_stock`: integrarea EDI la nivel de stoc, baza pe care se adaugă îmbunătățirile pentru trimiterea documentelor e-Transport din livrări.
