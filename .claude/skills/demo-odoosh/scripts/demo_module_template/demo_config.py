# Generat de scripts/demo_branch.py. Fișierul trăiește doar pe branch-ul de demo
# și dispare odată cu branch-ul. NU copia valorile în alt loc.
ADMIN_PASSWORD = "__ADMIN_PASSWORD__"
# None = fără context RO; "own" = companie RO proprie + seed comercial;
# "fiscal" = compania demo standard `base.demo_company_ro` cu cazurile fiscale din
# l10n_ro_anaf_base (21%/11%, taxare inversă, IC bunuri/servicii, TVA la încasare) + seed comercial.
RO_MODE = __RO_MODE__
RO_COMPANY_NAME = __RO_COMPANY_NAME__
