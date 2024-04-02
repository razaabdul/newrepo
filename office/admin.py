from django.contrib import admin
from office.models import car,review

class caradmin(admin.ModelAdmin):
   # fields=['year','brand']     # you can chenge the field which you want to show first

    fieldsets=[
        ('TIMEINFORMATION',{'fields':['year']}),  # by using this you will get ablue bar in the tp of fields
        ('CAR INFORMATION',{'fields':['brand']})
    ]
admin.site.register(car,caradmin)
admin.site.register(review)


