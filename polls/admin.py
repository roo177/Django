from django.contrib import admin

# Register your models here.
from .models import Question,Choice,R1Code,R2Code,R3Code,R4Code

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(R1Code)
admin.site.register(R2Code)
admin.site.register(R3Code)
admin.site.register(R4Code)
