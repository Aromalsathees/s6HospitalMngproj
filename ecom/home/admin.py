from django.contrib import admin
from . models import *
# Register your models here.


class prescribedTabular(admin.TabularInline):
    model=prescribed

class prescriptionAdmin(admin.ModelAdmin):
    inlines=[prescribedTabular]    



admin.site.register(prescription,prescriptionAdmin)


admin.site.register(ourservice)
admin.site.register(Bloodavailabilty)
admin.site.register(ourdocters)
admin.site.register(appo)
admin.site.register(docters_booking)
admin.site.register(articles)
admin.site.register(Medicine)
admin.site.register(deppp)
# admin.site.register(prescription)
admin.site.register(Patient)
# admin.site.register(prescribed)