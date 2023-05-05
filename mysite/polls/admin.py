from django.contrib import admin

# Register your models here.
from .models import Question,R1Code,R2Code

admin.site.register(Question)
admin.site.register(R1Code)
admin.site.register(R2Code)