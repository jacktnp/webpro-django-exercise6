from django.contrib import admin
from django.contrib.auth.models import Permission

# Register your models here.
from record.models import Record

admin.site.register(Permission)

class RecordAdmin(admin.ModelAdmin):
    list_display = ['create_by', 'title', 'type','start_date', 'end_date', 'approve_status']
    list_per_page = 10

    list_filter = ['title', 'type','start_date', 'end_date', 'approve_status']
    search_fields = ['title', 'type','start_date', 'end_date', 'create_by']
    
    readonly_fields = ['create_by', 'title', 'type','start_date', 'end_date']

admin.site.register(Record, RecordAdmin)
