# Sale Return Cause (localizat la `deltatech_sale_return_cause/index.md`)

- **Nume Tehnic:** `deltatech_sale_return_cause`
- **Versiune:** `19.0.0.0.8`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_return_cause`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_return_cause`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul **Sale Return Cause** îmbunătățește gestiunea vânzărilor din Odoo, oferind o modalitate sistematică de a urmări și analiza motivele care stau în spatele retururilor de marfă. Permite companiilor să categorisească retururile, să monitorizeze valoarea returnată și să genereze rapoarte relevante pentru a identifica și remedia problemele frecvente din procesul de vânzare sau de livrare.

#### 2. Funcționalități Cheie

- **Urmărirea cauzei de retur:** se poate atribui ușor un motiv predefinit pentru fiecare retur, direct pe comanda de vânzare. Motivele includ probleme de calitate, erori de livrare, greșeli ale clientului și altele.
- **Calcul automat al valorii returnate:** modulul poate calcula automat valoarea totală returnată prin însumarea notelor de credit postate, asociate facturilor comenzii de vânzare.
- **Înregistrarea datei de retur:** se înregistrează automat data la care o cauză de retur este atribuită prima dată unei comenzi.
- **Actualizări zilnice automate:** o acțiune programată (cron) rulează zilnic pentru a reverifica și actualiza valorile returnate pentru comenzile din ultimul an, asigurând acuratețea datelor.
- **Raportare integrată:**
    - **Integrare în Analiza Vânzărilor:** cauzele de retur sunt integrate în raportul standard de Analiză a Vânzărilor.
    - **Vizualizări Pivot și Grafic:** analiza tendințelor de retur după cauză, dată sau alte dimensiuni de vânzare.
- **Configurare flexibilă:** se poate alege între calculul automat al valorilor returnate sau introducerea manuală, în funcție de nevoile de business.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.return.cause`: model nou care definește catalogul de cauze de retur predefinite (probleme de calitate, erori de livrare, greșeli ale clientului etc.).
- `sale.order` (extins): adaugă cauza de retur (câmpul nou `return_cause_id`, precum și câmpul vechi `return_cause` de tip selecție, păstrat pentru compatibilitate), valoarea returnată (`return_amount`) și data returului (`return_cause_date`) pe comanda de vânzare; include și logica de calcul automat al valorii returnate pe baza notelor de credit postate.
- `sale.report` (extins): adaugă cauza de retur (`return_cause_id`, `return_cause`, `return_cause_date`) în raportul standard de Analiză a Vânzărilor, inclusiv la nivel de select și group by SQL.

**Vizualizări**

- `sale_return_cause_view.xml`: vizualizările de listă și formular pentru catalogul de cauze de retur.
- `sale_order_view.xml`: extinderea formularului comenzii de vânzare cu câmpurile de retur.
- `sale_report_view.xml`: extinderea vizualizărilor pivot/grafic din Analiza Vânzărilor cu dimensiunea cauzei de retur.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_check_and_update_return_amount` (`ir_cron_data.xml`): acțiune programată (cron) zilnică ce reverifică și actualizează valorile returnate pentru comenzile din ultimul an care au o cauză de retur asociată, doar dacă e activat calculul automat.
- `param_auto_calculate_return_amount` (`ir_config_parameter_data.xml`): parametru de configurare (`deltatech_sale_return_cause.auto_calculate`) care comută între calculul automat și introducerea manuală a valorilor returnate.

#### 5. Conexiuni

- `sale`: modulul standard de vânzări Odoo, extins pentru a adăuga urmărirea cauzelor de retur pe comenzi și în Analiza Vânzărilor.
