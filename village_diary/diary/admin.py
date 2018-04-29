from django.contrib import admin
from .models import Diary, dataEntryEmployee
# Register your models here.


class DiaryAdmin(admin.ModelAdmin):
    model = Diary
    list_display = ['villageName', 'villageCode', 'connectivity', 'allotted']
    list_filter = ['connectivity', 'allotted']
    search_fields = ['villageName', 'villageCode', 'gataNumber']


class dataEntryEmployeeAdmin(admin.ModelAdmin):
    model = dataEntryEmployee
    search_fields = ['employeeCodes']


admin.site.register(Diary, DiaryAdmin)
admin.site.register(dataEntryEmployee, dataEntryEmployeeAdmin)
