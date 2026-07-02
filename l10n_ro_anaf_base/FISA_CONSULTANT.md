# Fișă Modul: Infrastructură declarații ANAF

**Poziție plan:** C1
**Modul:** `l10n_ro_anaf_base`
**FR:** FR-53
**Capitol manual:** Cap 4.0
**Utilizator principal:** Responsabil fiscal, Administrator Odoo
**Prioritate:** 🔴 Ridicată

---

## 1. Scop business

Modulul oferă infrastructura comună pentru declarațiile fiscale ANAF din suita `l10n_ro_anaf_dxxx`: meniuri, configurări, date de identificare declarant și mecanisme comune pentru export.

## 2. Bază legală și context

Declarațiile fiscale se pregătesc în formatele publicate de ANAF. Modulul nu reprezintă o declarație individuală, ci baza tehnică folosită de modulele D300, D390, D394, D100, D120, D318, D398 și alte declarații.

## 3. Utilizatori și roluri

- Administrator funcțional: configurează compania și setările ANAF.
- Contabil șef: verifică datele declarantului înainte de export.
- Contabil fiscal: folosește modulele de declarații care depind de această bază.

## 4. Date implicate

- companie românească, CUI, adresă și date reprezentant;
- perioade fiscale;
- module de declarații instalate separat;
- configurări comune ANAF.

## 5. Configurare inițială

1. Instalați `l10n_ro_anaf_base`.
2. Verificați meniurile ANAF adăugate în contabilitate.
3. Completați datele companiei: CUI, adresă, reprezentant, telefon și e-mail.
4. Verificați că modulele de declarații folosesc aceeași companie și aceeași localizare RO.

## 6. Flux de utilizare

### Pasul 1 — Accesare

Meniu: `Contabilitate → Raportare → Declarații ANAF și Contabilitate → Configurare → Setări → Romanian ANAF Declarations`.

1. Deschideți meniul ANAF sau setările companiei.
2. Verificați datele declarantului.
3. Instalați modulul declarației necesare, de exemplu `l10n_ro_anaf_d300`.
4. Generați declarația din modulul specific.
5. Verificați că exportul preia datele comune din baza ANAF.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux |
|---|---|
| Module `l10n_ro_anaf_dxxx` | folosesc infrastructura comună de declarații |
| `account_reports` | sursa rapoartelor fiscale și a exporturilor |
| Certificat digital / submission local | flux separat pentru semnare și depunere, unde este disponibil |
| Date companie | CUI, adresă, reprezentant și metadate export |

Ce este automat: centralizarea setărilor comune pentru declarații ANAF.
Ce rămâne manual: verificarea certificatului, a datelor companiei și a modului de depunere.

## 8. Verificări pentru consultant

- [ ] Modulul se instalează fără erori.
- [ ] Meniurile ANAF sunt vizibile.
- [ ] Datele companiei sunt completate și corecte.
- [ ] Un modul de declarație dependent poate genera export folosind baza ANAF.

## 9. Mesaje frecvente

| Simptom | Cauză probabilă | Remediere |
|---------|-----------------|-----------|
| Lipsesc date declarant | Compania nu are CUI/adresă completă | Completați datele companiei |
| Modulul declarației nu apare | Declarația individuală nu este instalată | Instalați modulul `l10n_ro_anaf_dxxx` necesar |

## 9. Capturi recomandate

- [ ] Meniurile ANAF
- [ ] Configurarea companiei
- [ ] Setări comune folosite de declarații
- [ ] Exemplu de declarație care preia datele declarantului
