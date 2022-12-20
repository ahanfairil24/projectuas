from django.contrib import admin

from . models import bathsulmasail

class bathsulmasailAdmin (admin.ModelAdmin):
    pass
admin.site.register(bathsulmasail, bathsulmasailAdmin)




# Register your models here.