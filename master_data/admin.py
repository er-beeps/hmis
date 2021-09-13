from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Province, District, LocalLevelType,
                LocalLevel, FiscalYear, NepaliMonth, Gender)
class DefaultAdmin(admin.ModelAdmin):
    pass
