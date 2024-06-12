from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from numberleader import settings
from django.contrib.sites.shortcuts import get_current_site



# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def products(request):
    return render(request,'products.html')


def signUp(request):
    if request.method=='POST':
       user_name=request.POST['user_name']
       user_password=request.POST['user_password']
       user_email=request.POST['user_email']
       user_confirm_password=request.POST['user_confirm_password']

       company_name=request.POST['company_name']
       website_url=request.POST['website_url']
       introductory_video = request.POST['introductory_video']

       founder_name=request.POST['founder_name']
       linkedIn_url=request.POST['linkedIn_url']
       founder_introduction=request.POST['founder_introduction']
       founder_email=request.POST['founder_email']
       phone_number=request.POST['phone_number']
       
       if user_password == user_confirm_password:
           user=User.objects.create(user_name=user_name,user_email=user_email,user_password=user_password,
                         company_name=company_name,website_url=website_url,introductory_video=introductory_video,founder_name=founder_name,linkedIn_url=linkedIn_url,founder_introduction=founder_introduction,founder_email=founder_email,phone_number=phone_number)
           user.save()
           messages.success(request,'Data Submitted sucessfully')
           return redirect('signup')
       else:
           messages.error(request,'both password and confirm password  must be same')
           return redirect('signup')         
    else:
        return render(request,'signup.html')

def signIn(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.get(user_name=username,user_password=password)
        if user:
            request.session['current_user_id'] = user.user_id  # Store user id in session    
            return redirect('dashboard')
        else:
            messages.error(request,'invalid username or password')
            return redirect('signin')
    else:
        return render(request,'signin.html')
    
    
def signOut(request):
    request.session.flush()
    return redirect('home')


def dashboard(request):
    return render(request,'dashboard.html')



def subUser(request):
    if request.method=='POST':
        sub_user_name=request.POST['sub_user_name']
        sub_user_email=request.POST['sub_user_email']
        sub_user_password=request.POST['sub_user_password']
        sub_user_confirm_password=request.POST['sub_user_confirm_password']
        sub_user_fullname =request.POST['sub_user_fullname']
        sub_user_designation=request.POST['sub_user_designation']
        sub_user_company_id =request.POST['sub_user_company_id']
        sub_user_phone_number=request.POST['sub_user_phone_number']
        if sub_user_password == sub_user_confirm_password:
            sub_user= SubUser.objects.create(sub_user_name=sub_user_name,sub_user_email=sub_user_email,sub_user_password=sub_user_password,
                                 sub_user_fullname=sub_user_fullname,sub_user_designation=sub_user_designation,sub_user_company_id=sub_user_company_id,sub_user_phone_number=sub_user_phone_number)
            sub_user.save()
            # Get the current site domain
            current_site = get_current_site(request)
            domain = current_site.domain

            # Construct the signin URL
            signin_url = f'http://{domain}/signin'

            subject='Registration Details'
            txt='''Welcome to  Number Leader
                Below are your Login Details :
                Username :{}
                Email : {}
                Password : {}
                Full Name : {}
                Domain: {}
                    '''
            message=txt.format(sub_user_name,sub_user_email,sub_user_password,sub_user_fullname,signin_url)
            from_email=settings.EMAIL_HOST_USER
            to_list=[sub_user_email]
            print(message)
            send_mail(subject, message,from_email,to_list,fail_silently=True)
            messages.success(request,'Sub User Created Successfully')
            return redirect('dashboard') 

        else:
           messages.error(request,'both password and confirm password  must be same')
           return redirect('sub_user')     
    else:
        return render(request,'sub_user.html')



def incomeStatement(request):
     
     if request.method == 'POST':
        company_id = request.POST.get('company_id')
        product_name = request.POST.get('product_name')
        total_dividends = float(request.POST.get('total_dividends', 0))
        total_revenue = float(request.POST.get('total_revenue', 0))
        total_taxes = float(request.POST.get('total_taxes', 0))
        total_cogs = float(request.POST.get('total_cogs', 0))
        cogs_direct_labour = float(request.POST.get('cogs_direct_labour', 0))
        cogs_material = float(request.POST.get('cogs_material', 0))
        cogs_parts = float(request.POST.get('cogs_parts', 0))
        cogs_distribution = float(request.POST.get('cogs_distribution', 0))
        cogs_other = float(request.POST.get('cogs_other', 0))
        op_rent_expense = float(request.POST.get('op_rent_expense', 0))
        op_exp_rent = float(request.POST.get('op_exp_rent', 0))
        op_exp_utilities = float(request.POST.get('op_exp_utilities', 0))
        op_exp_overhead = float(request.POST.get('op_exp_overhead', 0))
        op_exp_legal = float(request.POST.get('op_exp_legal', 0))
        op_exp_depreciation = float(request.POST.get('op_exp_depreciation', 0))
        op_exp_marketing_ads = float(request.POST.get('op_exp_marketing_ads', 0))
        op_exp_insurance = float(request.POST.get('op_exp_insurance', 0))

        op_exp_interest = float(request.POST.get('op_exp_interest', 0))
        op_exp_travel = float(request.POST.get('op_exp_travel', 0))
        op_exp_wages = float(request.POST.get('op_exp_wages', 0))
        op_exp_other = float(request.POST.get('op_exp_other', 0))
        creator_id = request.POST.get('creator_id')
        modifier_id = request.POST.get('modifier_id')
        user_id = request.POST.get('user_id')
        user_id=User.objects.get(user_id=user_id)

        income_statement = IncomeStatement(
            company_id=company_id,
            product_name=product_name,
            total_dividend=total_dividends,
            total_revenue=total_revenue,
            total_taxes=total_taxes,
            total_cogs=total_cogs,
            cogs_direct_labour=cogs_direct_labour,
            cogs_material=cogs_material,
            cogs_parts=cogs_parts,
            cogs_distribution=cogs_distribution,
            cogs_other=cogs_other,
            total_operating_expenses=op_rent_expense,
            opexpense_rent=op_exp_rent,
            opexpense_utilities=op_exp_utilities,
            opexpense_overhead=op_exp_overhead,
            opexpense_legal=op_exp_legal,
            opexpense_depreciation=op_exp_depreciation,
            opexpense_marketing_ads=op_exp_marketing_ads,
            opexpense_interest=op_exp_interest,
            opexpense_travel=op_exp_travel,
            opexpense_wages=op_exp_wages,
            opexpense_other=op_exp_other,
            opexpense_insurance=op_exp_insurance,
            modifiers_id=modifier_id,
            user_id=user_id
        )
        income_statement.save()
        return redirect('income_statement')
     else:
        data={ }
        if 'username' in request.session:
            username = request.session['username']
            user_id = request.session['user_id']
            company_id = request.session['company_id']
            data = {
            'username': username,
            'user_id': user_id,
            'company_id': company_id
            }
        return render(request,'income_statement.html')




def balanceSheet(request):
     if request.method == 'POST':
        company_id = request.POST.get('company_id')
        total_current_assets = request.POST.get('total_current_assets')
        cash = request.POST.get('cash')
        accounts_receivables = request.POST.get('accounts_receivables')
        prepaid_expenses = request.POST.get('prepaid_expenses')
        inventory = request.POST.get('inventory')
        other_current_assets = request.POST.get('other_current_assets')
        cogs_direct_labour = request.POST.get('cost_of_goods_sold_direct_labour')
        cogs_material = request.POST.get('cost_of_goods_sold_material')
        cogs_parts = request.POST.get('cost_of_goods_sold_parts')
        cogs_distribution = request.POST.get('cost_of_goods_sold_distribution')
        cogs_other = request.POST.get('cost_of_goods_sold_other')
        total_non_current_assets = request.POST.get('total_non_current_assets')
        property = request.POST.get('property')
        charity = request.POST.get('charity')
        equipment = request.POST.get('equipment')
        leases = request.POST.get('leases')
        other_non_current_assets = request.POST.get('other_non_current_assets')
        total_current_liabilities = request.POST.get('total_current_liabilities')
        accounts_payable = request.POST.get('accounts_payable')
        accrued_expenses = request.POST.get('accrued_expenses')
        unearned_revenue = request.POST.get('unearned_revenue')
        other_current_liabilities = request.POST.get('other_current_liabilities')
        total_non_current_liabilities = request.POST.get('total_non_current_liabilities')
        long_term_debt = request.POST.get('long_term_debt')
        other_non_current_liabilities = request.POST.get('other_non_current_liabilities')
        shareholder_equity = request.POST.get('shareholder_equity')
        equity_investment_capital = request.POST.get('equity_investment_capital')
        equity_retained_earnings = request.POST.get('equity_retained_earnings')
        creator_id = request.POST.get('creator_id')
        modifier_id = request.POST.get('modifier_id')
        user_id = request.POST.get('user_id')
        user_id=User.objects.get(user_id=user_id)

        balance_sheet = BalanceSheet.objects.create(
            company_id=company_id,
            total_current_assets=total_current_assets,
            cash=cash,
            accounts_receivables=accounts_receivables,
            prepaid_expenses=prepaid_expenses,
            inventory=inventory,
            other_current_assets=other_current_assets,
            cogs_direct_labour=cogs_direct_labour,
            cogs_material=cogs_material,
            cogs_parts=cogs_parts,
            cogs_distribution=cogs_distribution,
            cogs_other=cogs_other,
            total_non_current_assets=total_non_current_assets,
            property=property,
            charity=charity,
            equipment=equipment,
            leases=leases,
            other_non_current_assets=other_non_current_assets,
            total_current_liabilities=total_current_liabilities,
            accounts_payable=accounts_payable,
            accrued_expenses=accrued_expenses,
            unearned_revenue=unearned_revenue,
            other_current_liabilities=other_current_liabilities,
            total_non_current_liabilities=total_non_current_liabilities,
            long_term_debt=long_term_debt,
            other_non_current_liabilities=other_non_current_liabilities,
            shareholder_equity=shareholder_equity,
            equity_investment_capital=equity_investment_capital,
            equity_retained_earnings=equity_retained_earnings,
            creator_id=creator_id,
            modifier_id=modifier_id,
            user_id=user_id
        )
        balance_sheet.save()
        return redirect('balance_sheet')
     else:
        data={ }
        if 'username' in request.session:
            username = request.session['username']
            user_id = request.session['user_id']
            company_id = request.session['company_id']
            data = {
            'username': username,
            'user_id': user_id,
            'company_id': company_id
            }
        return render(request,'balance_sheet.html')
        
        return render(request,'balance_sheet.html', context=data)


def cashFlow(request):
    if request.method == 'POST':
        company_id = request.POST['company_id']
        net_financing = float(request.POST['net_financing'])
        cf_financing_inflow_drawing = float(request.POST['cf_financing_inflow_drawing'])
        cf_financing_inflow_distribution = float(request.POST['cf_financing_inflow_distribution'])
        cf_financing_inflow_other = float(request.POST['cf_financing_inflow_other'])
        cf_financing_outflow_loan_payments = float(request.POST['cf_financing_outflow_loan_payments'])
        cf_financing_outflow_other = float(request.POST['cf_financing_outflow_other'])
        net_investments = float(request.POST['net_investments'])
        cf_investments_inflow_loans = float(request.POST['cf_investments_inflow_loans'])
        cf_investments_inflow_sell_property = float(request.POST['cf_investments_inflow_sell_property'])
        cf_investments_inflow_sell_equip = float(request.POST['cf_investments_inflow_sell_equip'])
        cf_investments_inflow_other = float(request.POST['cf_investments_inflow_other'])
        cf_investments_outflow_buy_property = float(request.POST['cf_investments_outflow_buy_property'])
        cf_investments_outflow_buy_equip = float(request.POST['cf_investments_outflow_buy_equip'])
        cf_investments_outflow_other = float(request.POST['cf_investments_outflow_other'])
        net_operations = float(request.POST['net_operations'])
        cf_operations_inflow_customers = float(request.POST['cf_operations_inflow_customers'])
        cf_operations_inflow_depreciation = float(request.POST['cf_operations_inflow_depreciation'])
        cf_operations_inflow_amortization = float(request.POST['cf_operations_inflow_amortization'])
        cf_operations_inflow_other = float(request.POST['cf_operations_inflow_other'])
        cf_operations_outflow_wages = float(request.POST['cf_operations_outflow_wages'])
        cf_operations_outflow_overhead = float(request.POST['cf_operations_outflow_overhead'])
        cf_operations_outflow_interest = float(request.POST['cf_operations_outflow_interest'])
        cf_operations_outflow_taxes = float(request.POST['cf_operations_outflow_taxes'])
        cf_operations_outflow_accounts_receivable = float(request.POST['cf_operations_outflow_accounts_receivable'])
        cf_operations_outflow_inventory_increase = float(request.POST['cf_operations_outflow_inventory_increase'])
        cf_operations_outflow_other = float(request.POST['cf_operations_outflow_other'])
        creator_id = request.POST['creator_id']
        modifier_id = request.POST['modifier_id']
        user_id = request.POST['user_id']
        user_id=User.objects.get(user_id=user_id)

        cash_flow = CashFlow(
            company_id=company_id,
            net_financing=net_financing,
            cf_financing_inflow_drawing=cf_financing_inflow_drawing,
            cf_financing_inflow_distribution=cf_financing_inflow_distribution,
            cf_financing_inflow_other=cf_financing_inflow_other,
            cf_financing_outflow_loan_payments=cf_financing_outflow_loan_payments,
            cf_financing_outflow_other=cf_financing_outflow_other,
            net_investments=net_investments,
            cf_investments_inflow_loans=cf_investments_inflow_loans,
            cf_investments_inflow_sell_property=cf_investments_inflow_sell_property,
            cf_investments_inflow_sell_equip=cf_investments_inflow_sell_equip,
            cf_investments_inflow_other=cf_investments_inflow_other,
            cf_investments_outflow_buy_property=cf_investments_outflow_buy_property,
            cf_investments_outflow_buy_equip=cf_investments_outflow_buy_equip,
            cf_investments_outflow_other=cf_investments_outflow_other,
            net_operations=net_operations,
            cf_operations_inflow_customers=cf_operations_inflow_customers,
            cf_operations_inflow_depreciation=cf_operations_inflow_depreciation,
            cf_operations_inflow_amortization=cf_operations_inflow_amortization,
            cf_operations_inflow_other=cf_operations_inflow_other,
            cf_operations_outflow_wages=cf_operations_outflow_wages,
            cf_operations_outflow_overhead=cf_operations_outflow_overhead,
            cf_operations_outflow_interest=cf_operations_outflow_interest,
            cf_operations_outflow_taxes=cf_operations_outflow_taxes,
            cf_operations_outflow_accounts_receivable=cf_operations_outflow_accounts_receivable,
            cf_operations_outflow_inventory_increase=cf_operations_outflow_inventory_increase,
            cf_operations_outflow_other=cf_operations_outflow_other,
            creator_id=creator_id,
            modifier_id=modifier_id,
            user_id=user_id
        )
        cash_flow.save()
        return redirect('cash_flow')
    else:
        data={ }
        if 'username' in request.session:
            username = request.session['username']
            user_id = request.session['user_id']
            company_id = request.session['company_id']
            data = {
            'username': username,
            'user_id': user_id,
            'company_id': company_id
            }
        
        return render(request,'cash_flow.html')




# Tables


def subUserTable(request):
    sub_user=SubUser.objects.all()
    context={
        'data':sub_user
    }
    return render(request, 'tables/sub_user.html', context)

def updateSubUser(request,username):
    subuser=SubUser.objects.get(sub_user_name=username)
    
    if subuser and request.method=='POST':
        sub_user_name=request.POST['sub_user_name']
        sub_user_email=request.POST['sub_user_email']
        sub_user_fullname =request.POST['sub_user_fullname']
        sub_user_designation=request.POST['sub_user_designation']
        sub_user_company_id =request.POST['sub_user_company_id']
        sub_user_phone_number=request.POST['sub_user_phone_number']
        subuser.sub_user_name = sub_user_name
        subuser.sub_user_email = sub_user_email
        subuser.sub_user_fullname = sub_user_fullname
        subuser.sub_user_designation = sub_user_designation
        subuser.sub_user_company_id = sub_user_company_id
        subuser.sub_user_phone_number = sub_user_phone_number
        subuser.save()
        return redirect('sub_user_table')
          
    else:
        context={
        'data':subuser
        }
        return render(request, 'update_sub_user.html', context)
    

def deleteSubUser(request,username):
    subuser=SubUser.objects.get(sub_user_name=username)
    subuser.delete()
    return redirect('sub_user_table')


def incomeStatementTable(request):
    income_statement=IncomeStatement.objects.all()
    context={
        'income_statement': income_statement
    }
    return render(request, 'tables/income_statement.html', context)

def deleteIncomeStatement(request,id):
    user=IncomeStatement.objects.get(id=id)
    user.delete()
    return redirect('income_statement_table')


def balanceSheetTable(request):
    balance_sheet=BalanceSheet.objects.all()
    context={
        'balance_sheet': balance_sheet
    }
    return render(request, 'tables/balance_sheet.html', context)


def deleteBalanceSheet(request,id):
    user=BalanceSheet.objects.get(id=id)
    user.delete()
    return redirect('balance_sheet_table')


def cashFlowTable(request):
    cash_flow=CashFlow.objects.all()
    context={
        'cash_flow': cash_flow
    }
    return render(request, 'tables/cash_flow.html', context)

def deleteCashFlow(request,id):
    user=CashFlow.objects.get(id=id)
    user.delete()
    return redirect('cash_flow_table')


    