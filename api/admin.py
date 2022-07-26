from django.contrib import admin
from .models import Affiliates, Branches, Commerces, Company, DetLists, Lists, Terminals, Users, Profiles,Transactions

# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display =  ['identification', 'names', 'last_names', 'email']

admin.site.register(Company)
admin.site.register(Terminals)
admin.site.register(Profiles)
admin.site.register(Transactions)
admin.site.register(Affiliates)
admin.site.register(Branches)
admin.site.register(DetLists)
admin.site.register(Lists)
admin.site.register(Commerces)