from django.contrib import admin
from baristaapp.models import (
    Cafe, About, Work_Team, Menu, Reviews, 
    Contact, Reservation, PeopleNumber, SiteSettings
)



admin.site.register(Cafe)
admin.site.register(About)
admin.site.register(Work_Team)
admin.site.register(Menu)
admin.site.register(Reviews)
admin.site.register(Contact)
admin.site.register(Reservation)
admin.site.register(PeopleNumber)
admin.site.register(SiteSettings) 