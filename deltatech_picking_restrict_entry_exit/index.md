# Picking Validation Restrict Entry Exit (localizat la `deltatech_picking_restrict_entry_exit/index.md`)

- **Nume Tehnic:** `deltatech_picking_restrict_entry_exit`
- **Versiune:** `19.0.0.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_picking_restrict_entry_exit
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_restrict_entry_exit`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul introduce un control de business care împiedică validarea recepțiilor și livrărilor de stoc (`stock.picking`) atunci când liniile de mișcare nu sunt legate de o comandă de achiziție, respectiv de vânzare, prevenind astfel mișcări de stoc fără document justificativ. În plus, blochează confirmarea sau salvarea unor cantități mai mari decât cele comandate, astfel încât depozitul să mute efectiv doar cantitățile aprobate în comenzi.

#### 2. Funcționalități Cheie

- Nu permite validarea (`button_validate`) unei recepții (intrare) dacă vreo linie de mișcare nu este asociată unei linii de comandă de achiziție, respectiv a unei livrări (ieșire) dacă nu este asociată unei linii de comandă de vânzare.
- Nu permite recepționarea/livrarea unei cantități mai mari decât cea comandată — verificare aplicată atât la validarea transferului, cât și la salvarea liniilor de mișcare (`write`).
- Restricția nu se aplică retururilor și back-order-urilor și nici transferurilor interne ale căror locații sursă/destinație aparțin aceluiași depozit.
- Există un grup implicit, „Picking create permission" (`group_picking_restrict_entry_exit`), care scutește utilizatorii membri de aceste restricții; la instalare, utilizatorii root și admin sunt adăugați automat în grup.
- Pentru a exonera un utilizator de restricție, acesta trebuie eliminat manual din grupul „Picking create permission" — atenție: orice modificare ulterioară asupra acelui utilizator îl poate readăuga automat în grup.

*Corecție față de `readme/DESCRIPTION.md`:* textul original menționează blocarea **creării** picking-ului fără origine; în codul actual (19.0) restricția din `create()` este dezactivată (comentată), iar controlul efectiv se aplică la **validare** (`button_validate`) și la **salvare** (`write`), nu la crearea înregistrării.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Conform fluxului de ingestie, Sumarul și Funcționalitățile Cheie au fost preluate din `readme/DESCRIPTION.md`. Pentru acuratețe (vezi corecția de mai sus), a fost necesară o verificare punctuală a codului, care a confirmat următoarele componente:

**Modele**

- `stock.picking` (extindere): suprascrie `button_validate` (blochează validarea transferurilor de intrare/ieșire fără linie de vânzare/achiziție aferentă sau cu cantitate mai mare decât cea comandată) și `write` (aplică aceleași verificări la salvarea liniilor de mișcare, inclusiv pentru linii noi adăugate manual).

**Securitate**

- `group_picking_restrict_entry_exit` ("Picking create permission"): grup `res.groups` ai cărui membri sunt scutiți de restricțiile de mai sus; conține implicit `base.user_root` și `base.user_admin`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale directe cu alte module documentate în wiki. Referințe punctuale, nefuncționale, există în testele modulului `deltatech_stock_picking_activity_report` (verificare defensivă `env.ref(..., raise_if_not_found=False)` pentru compatibilitate CI, fără dependență declarată în manifest) și în manifestul proiectului de client `proiecte/datus/terrabit_datus`.
