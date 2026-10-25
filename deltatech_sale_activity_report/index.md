# Sale Order Last Modified (localizat la `deltatech_sale_activity_report/index.md`)

- **Nume Tehnic:** `deltatech_sale_activity_report`
- **Versiune:** `19.0.1.2.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_activity_report
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_activity_report`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Modulul adaugă un raport de activitate pentru comenzile de vânzare: de fiecare dată când un utilizator modifică ceva pe o comandă, se creează automat o înregistrare de activitate, astfel încât managerii de vânzări pot vedea, din meniul de rapoarte al aplicației Vânzări, cine a lucrat pe fiecare comandă și când. Înregistrările pot fi analizate și într-o vizualizare pivot, per utilizator, iar cele mai vechi de 2 luni sunt șterse automat prin mecanismul Data Recycle, astfel încât raportul rămâne relevant fără a acumula date istorice inutile.

#### 2. Funcționalități Cheie

- Ori de câte ori un utilizator modifică ceva pe o comandă de vânzare, se creează o înregistrare în raportul de activitate.
- Din meniul de rapoarte al aplicației Vânzări se pot vedea înregistrările de activitate, cu o vizualizare pivot pentru analiza activității per utilizator.
- Ștergerea automată a înregistrărilor de activitate mai vechi de 2 luni, prin mecanismul Data Recycle.
- Jurnalul urmează accesul la comenzile de vânzare: un vânzător vede doar jurnalul propriilor comenzi (sau al celor fără responsabil), vânzătorul cu „Toate documentele” și managerii văd tot, mereu în limita companiilor permise.
- Vânzătorii pot doar citi jurnalul; numai administratorul de vânzări poate modifica sau șterge înregistrări. Utilizatorii interni fără drepturi de vânzări nu au acces. Înregistrările continuă să fie scrise automat, de sistem, pentru orice utilizator.
- Programarea unei activități pe o comandă nu mai eșuează dacă `deltatech_website_sale_status` nu este instalat: stadiul comenzii se copiază în jurnal doar când câmpul există.
- Ștergerea din formular a unei linii nesalvate nu mai pierde jurnalul întregii scrieri.

#### 3. Dependențe

- `sale`
- `data_recycle`

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune este omisă deoarece `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit analiza componentelor tehnice.

#### 5. Conexiuni

- [deltatech_website_sale_status](../deltatech_website_sale_status/index.md): dependență opțională la rulare; dacă este instalat, stadiul comenzii este copiat în jurnal.
