# Obținerea accesului la REGES-Online (sistem extern / API)

Acest document descrie pașii prin care un angajator obține credențialele necesare
pentru ca Odoo să se conecteze la **REGES-Online** (Registrul Electronic General al
Salariaților) și să transmită automat salariați și contracte.

> **Important.** Credențialele de „acces din sistem extern" sunt **per angajator (CUI)**
> și se obțin **doar din portalul REGES** de către **reprezentantul legal** al firmei.
> Odoo nu poate genera aceste credențiale — el doar le folosește.

---

## Medii

| Mediu | Portal angajator | API | Autentificare (OpenID) |
|-------|------------------|-----|------------------------|
| **Test (dev)** | `https://reges.dev.inspectiamuncii.org` | `https://api.dev.inspectiamuncii.org` | `https://sso.dev.inspectiamuncii.org/realms/API/...` |
| **Producție** | `https://reges.inspectiamuncii.ro` | `https://api.inspectiamuncii.ro` | `https://sso.inspectiamuncii.ro/realms/API/...` |

În Odoo nu introduceți manual aceste URL-uri: bifați doar **„Mediu de test (dev)"** și
URL-urile se aleg automat.

---

## Pas 1 — Acces în portalul angajatorului

1. Mergeți la portalul REGES (vezi tabelul de medii) și apăsați **„Conectare"**.
2. Autentificați-vă cu contul de **persoană fizică** al reprezentantului legal
   (sau al unei persoane împuternicite).
3. Din pagina principală alegeți **„Registrul pentru angajatori"**.
4. Selectați firma (CUI) pentru care lucrați — colțul din stânga sus arată
   *„Registru curent: <Firmă>, CUI: <CUI>"*.

## Pas 2 — Deblocarea registrului (dacă e cazul)

La prima utilizare, registrul firmei trebuie **deblocat în vederea scrierii**.
Acest pas se confirmă printr-un mesaj de tip:

> *„A fost deblocat accesul la registrul \<CUI\> în vederea scrierii!"*

Dacă registrul nu este deblocat, transmiterile din sistem extern vor fi respinse.

## Pas 3 — Generarea credențialelor de acces din sistem extern

1. În aplicația angajatorului, mergeți la **Setări → Angajator → Utile**.
2. La secțiunea **„Acces sistem extern"**, apăsați **„Obține credențialele"**.
3. Sistemul afișează un mesaj cu credențialele:
   - **user** = *ID angajator* (un UUID, ex. `8d954471-…`)
   - **parola** = șir generat (ex. `xrrUSud0nLKxKcTrg!&0`)

   > ⚠️ **Atenție:** fiecare apăsare pe „Obține credențialele" **regenerează parola**
   > (cea veche devine invalidă). Apăsați o singură dată și salvați parola imediat.

## Pas 4 — Informațiile API (opțional, pentru verificare)

Tot în **Setări → Angajator → Utile → „Informații necesare API"** găsiți:

- **ID utilizator** (UUID) — `Copiază ID utilizator`
- **ID angajator** (UUID) — `Copiază ID angajator` *(= username-ul de la Pas 3)*

---

## Pas 5 — Configurarea în Odoo

1. Mergeți la **Setări → REGES-Online**.
2. Bifați **„Mediu de test (dev)"** dacă lucrați pe mediul de test
   (debifat = producție).
3. Completați:
   - **Utilizator (ID angajator)** = user-ul de la Pas 3
   - **Parolă** = parola de la Pas 3
4. Apăsați **„Testează conexiunea"**.
   - La succes apare: *„Conexiune REGES reușită! Angajator: <Firmă>"*.
   - La eroare, mesajul indică problema (credențiale greșite, registru neblocat etc.).

După un test reușit, Odoo poate transmite salariați și contracte și poate citi
coada de rezultate (crons-urile REGES).

---

## Detalii tehnice (pentru integratori)

Conexiunea folosește **OpenID Connect (Keycloak), grant `password`**, cu un client
**confidential** comun tuturor angajatorilor:

```
POST {sso}/realms/API/protocol/openid-connect/token
  grant_type=password
  client_id=reges-api
  client_secret=<secretul clientului reges-api>
  username=<ID angajator>
  password=<parola generată în portal>
```

Token-ul JWT rezultat se trimite ca `Authorization: Bearer <token>` la apelurile API
(`/api/Profile`, `/api/Salariat`, `/api/Contract`, `/api/Status/PollMessage`, …).
Realm-ul este **`API`** (nu `reges`), iar gazda de autentificare este `sso.*`
(nu `auth.*`). Vezi `models/res_company.py` pentru implementare.

Referință oficială: <https://github.com/reges-ro/integrare>
(Swagger test: `https://api.dev.inspectiamuncii.org/swagger/`).
