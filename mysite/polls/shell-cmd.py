from polls.models import R1Code,R2Code
r = R1Code.objects.get(r_1_code="01")
related_r2_codes = R2Code.objects.filter(r_1_code=r)
#for r2_code in related_r2_codes:
#    print(r2_code.r_2_code, r2_code.r_2_desc_en, r2_code.r_2_desc_tr)