from django.urls import path
from .views import *


#from .import views
#path('',views.home,name='home'),


urlpatterns = [
    path('',home,name='home'),
    path('home',home,name='home'),
    path('about',about,name='about'),
    path('services',services,name='services'),
    path('products',products,name='products'),


    path('signin',signIn,name='signin'),
    path('logout',signOut,name='logout'),

    path('signup',signUp,name='signup'),
    path('dashboard',dashboard,name='dashboard'),
    path('income_statement',incomeStatement,name='income_statement'),
    path('balance_sheet',balanceSheet,name='balance_sheet'),
    path('cash_flow',cashFlow,name='cash_flow'),

    path('delete_income_statement/<int:id>',deleteIncomeStatement,name='delete_income_statement'),
    path('delete_balance_sheet/<int:id>',deleteBalanceSheet,name='delete_balance_sheet'),
    path('delete_cash_flow/<int:id>',deleteCashFlow,name='delete_cash_flow'),
    #subuser
    path('sub_user',subUser,name='sub_user'),
    path('update_sub_user/<str:username>',updateSubUser,name='update_sub_user'),
    path('delete_sub_user/<str:username>',deleteSubUser,name='delete_sub_user'),




    #tables
    path('income_statement_table',incomeStatementTable,name='income_statement_table'),
    path('balance_sheet_table',balanceSheetTable,name='balance_sheet_table'),
    path('cash_flow_table',cashFlowTable,name='cash_flow_table'),
    path('sub_user_table',subUserTable,name='sub_user_table')



    




]