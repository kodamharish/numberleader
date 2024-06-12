from django.db import models

# Create your models here.
class UserIDSequence(models.Model):
    current_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.current_id)
    

class CompanyIDSequence(models.Model):
    current_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.current_id)

    

class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True, editable=False)
    user_name = models.CharField(max_length=50, unique=True, null=False)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=10)

    # Company Details
    company_id = models.CharField(max_length=10, unique=True, editable=False)
    company_name = models.CharField(max_length=100)
    website_url = models.URLField()
    introductory_video = models.CharField(max_length=200)

    # Founders Details
    founder_name = models.CharField(max_length=100)
    linkedIn_url = models.URLField()
    founder_introduction = models.CharField(max_length=100)
    founder_email = models.EmailField()
    phone_number = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.user_id:
            user_sequence, created = UserIDSequence.objects.get_or_create(pk=1)
            user_sequence.current_id += 1
            self.user_id = f'U{user_sequence.current_id:03d}'
            user_sequence.save()

        if not self.company_id:
            company_sequence, created = CompanyIDSequence.objects.get_or_create(pk=1)
            company_sequence.current_id += 1
            self.company_id = f'NL{company_sequence.current_id:03d}'
            company_sequence.save()

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_id




class SubUser(models.Model):
    sub_user_name=models.CharField(max_length=10,primary_key=True)
    sub_user_email=models.EmailField()
    sub_user_password=models.CharField(max_length=10)
    sub_user_fullname = models.CharField(max_length=50)
    sub_user_designation = models.CharField(max_length=50)
    sub_user_company_id = models.CharField(max_length=10)
    sub_user_phone_number = models.IntegerField()



#Income Statement
class IncomeStatement(models.Model):
    company_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=50)
    total_dividend =models.FloatField()
    total_revenue = models.FloatField()
    total_taxes = models.FloatField()
    total_cogs = models.FloatField()
    cogs_direct_labour= models.FloatField()
    cogs_material= models.FloatField()
    cogs_parts= models.FloatField()
    cogs_distribution= models.FloatField()
    cogs_other= models.FloatField()
    total_operating_expenses= models.FloatField()
    opexpense_rent= models.FloatField()
    opexpense_utilities= models.FloatField()
    opexpense_overhead= models.FloatField()
    opexpense_legal= models.FloatField()
    opexpense_depreciation= models.FloatField()
    opexpense_marketing_ads= models.FloatField()
    opexpense_interest= models.FloatField()
    opexpense_travel= models.FloatField()
    opexpense_wages= models.FloatField()
    opexpense_other= models.FloatField()
    opexpense_insurance= models.FloatField()
    modifiers_id  = models.CharField(max_length=50,null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return f"Cash Flow for Company ID: {self.company_id}"
    

class BalanceSheet(models.Model):
    company_id = models.CharField(max_length=10)
    total_current_assets = models.FloatField()
    cash = models.FloatField()
    accounts_receivables = models.FloatField()
    prepaid_expenses = models.FloatField()
    inventory = models.FloatField()
    other_current_assets = models.FloatField()
    cogs_direct_labour = models.FloatField()  # Shortened for clarity
    cogs_material = models.FloatField()       # Shortened for clarity
    cogs_parts = models.FloatField()          # Shortened for clarity
    cogs_distribution = models.FloatField()   # Shortened for clarity
    cogs_other = models.FloatField()          # Shortened for clarity
    total_non_current_assets = models.FloatField()
    property = models.FloatField()
    charity = models.FloatField()
    equipment = models.FloatField()
    leases = models.FloatField()
    other_non_current_assets = models.FloatField()
    total_current_liabilities = models.FloatField()
    accounts_payable = models.FloatField()
    accrued_expenses = models.FloatField()
    unearned_revenue = models.FloatField()
    other_current_liabilities = models.FloatField()
    total_non_current_liabilities = models.FloatField()
    long_term_debt = models.FloatField()
    other_non_current_liabilities = models.FloatField()
    shareholder_equity = models.FloatField()
    equity_investment_capital = models.FloatField()
    equity_retained_earnings = models.FloatField()
    creator_id = models.CharField(max_length=50,null=True)
    modifier_id = models.CharField(max_length=50,null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)


    def _str_(self):
        return f"Balance Sheet for Company ID: {self.company_id}"
    
    
class CashFlow(models.Model):
    company_id = models.CharField(max_length=10)
    net_financing = models.FloatField()
    cf_financing_inflow_drawing = models.FloatField()
    cf_financing_inflow_distribution = models.FloatField()
    cf_financing_inflow_other = models.FloatField()
    cf_financing_outflow_loan_payments = models.FloatField()
    cf_financing_outflow_other = models.FloatField()
    net_investments = models.FloatField()
    cf_investments_inflow_loans = models.FloatField()
    cf_investments_inflow_sell_property = models.FloatField()
    cf_investments_inflow_sell_equip = models.FloatField()
    cf_investments_inflow_other = models.FloatField()
    cf_investments_outflow_buy_property = models.FloatField()
    cf_investments_outflow_buy_equip = models.FloatField()
    cf_investments_outflow_other = models.FloatField()
    net_operations = models.FloatField()
    cf_operations_inflow_customers = models.FloatField()
    cf_operations_inflow_depreciation = models.FloatField()
    cf_operations_inflow_amortization = models.FloatField()
    cf_operations_inflow_other = models.FloatField()
    cf_operations_outflow_wages = models.FloatField()
    cf_operations_outflow_overhead = models.FloatField()
    cf_operations_outflow_interest = models.FloatField()
    cf_operations_outflow_taxes = models.FloatField()
    cf_operations_outflow_accounts_receivable = models.FloatField()
    cf_operations_outflow_inventory_increase = models.FloatField()
    cf_operations_outflow_other = models.FloatField()
    creator_id = models.CharField(max_length=50,null=True)
    modifier_id = models.IntegerField(max_length=50,null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return f"Cash Flow for Company ID: {self.company_id}"


