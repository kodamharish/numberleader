from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(User)
admin.site.register([SubUser,IncomeStatement,BalanceSheet,CashFlow])


from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'company_id', 'user_name')
    list_display_links = ('user_id',)  # This makes user_id clickable to view details

admin.site.register(User, UserAdmin)


#username : admin
#password : 12345