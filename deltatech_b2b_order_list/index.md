# B2B Order Lists (localizat la `deltatech_b2b_order_list/index.md`)

- **Nume Tehnic:** `deltatech_b2b_order_list`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_b2b_order_list
- **Cale Locală:** `odoo-addons/bitshop/deltatech_b2b_order_list`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Liste de comandă salvate pentru clienții companie din portalul B2B. O fermă, un service sau un magazin comandă periodic aceleași produse („reparația combinei”, „consumabile lunare”). Cumpărătorul salvează o dată coșul ca listă cu nume și o comandă din nou cu un singur clic.

#### 2. Funcționalități Cheie

- **Salvarea coșului ca listă** din pagina de portal `/b2b/lists` (**Contul meu ▸ Liste de comandă**); dacă numele lipsește, se folosește „Listă din <data>”, iar numele e limitat la 80 de caractere. Un coș gol nu poate fi salvat.
- **Comandă din nou**: produsele listei ajung în coș la prețul de azi din lista de prețuri a clientului; un produs pe care site-ul nu îl mai vinde este omis. Utilizatorul este redirecționat în coș.
- **Ștergerea** unei liste din portal.
- Listele aparțin **companiei**: toți colegii le văd, nicio altă companie nu le vede (reguli de înregistrare; portalul nu citește listele ca superuser).
- Un contact doar cu drept de vizualizare sau un cont suspendat vede listele, dar nu le poate comanda.
- În back-office: *Vânzări ▸ Comenzi ▸ B2B Order Lists* (toate listele) și fila B2B din fișa clientului (listele companiei).

#### 3. Dependențe

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.b2b.order.list`: lista de comandă a unei companii (nume, companie, produse, număr de produse, activ); `_b2b_create_from_cart` creează lista din coșul curent.
- `deltatech.b2b.order.list.line`: linie de listă (produs, cod intern, cantitate).
- `res.partner` (extins): câmpul `b2b_order_list_ids` cu listele companiei.

**Vizualizări**

- `view_b2b_order_list_list` / `view_b2b_order_list_form` și acțiunea `action_b2b_order_lists`: administrarea listelor în back-office.
- `view_partner_form_b2b`: listele companiei în fila B2B a partenerului.
- `b2b_order_lists` și `portal_my_home_order_lists`: pagina `/b2b/lists` și intrarea din pagina de start a portalului.

**Controlere și securitate**

- Rute (extind `B2BPortal`): `/b2b/lists`, `/b2b/lists/save`, `/b2b/lists/<id>/order`, `/b2b/lists/<id>/delete`.
- Reguli `ir.rule` pe grupul portal: doar listele (și liniile) propriei companii comerciale. Drepturi de acces pentru `group_b2b_user` și `base.group_portal`.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md): portalul B2B pe care e construit modulul (verificări cont activ, drept de comandă, adăugare în coș).
- `agroamat_b2b`: sursa din care au fost preluate listele salvate (versiunea inițială, 2026-10-06).
