from django.db import models

# Create your models here.
class Property(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, related_name='neighborhood')
    zipcode = models.ForeignKey('Zipcode', on_delete=models.CASCADE, related_name='zip_code')
    property_type = models.CharField(max_length=50, blank=True, null=True)
    sqf = models.IntegerField(blank=True, null=True)
    beds = models.IntegerField(blank=True, null=True)
    baths = models.IntegerField(blank=True, null=True)
    asking = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField(blank=True, null=True, default=True)

#ADVANCED METRICS
    # calculates npv of property
    def calculate_npv(self, interest_rate=.05, rent_growth=.02):
        npv = 0

    # calculates cap rate
    def calculate_caprate(self):
        cap_rate = 0

    # calculates cash-on-cash return
    def calculate_cashoncash(self):
        cash_on_cash = 0

    # returns an estimate of the property given the location, size, bedrooms, etc.
    def get_estimate():
        pass

# COMPONENT VALUES (values below are used to caluclate the above expressions)
    # returns iterable of property values for duration of 30-years
    def get_property_values(self, growth_rate=.02):
        value = self.asking
        property_values = []
        if self.Neighborhood.proj_price_appreciation:
            growth_rate = self.Neighborhood.proj_price_appreciation
        elif self.Zipcode.proj_price_appreciation:
            growth_rate = self.Zipcode.proj_price_appreciation
        for x in range(30):
            property_values.append(value)
            value *= (1+growth_rate)
        return property_values
    
    # returns iterable of rents for the duration of 30-years
    def get_gross_rent(self, growth_rate=.02, rent=0):
        property_values = self.get_property_values
        gross_rent = []

    # returns iterable of effective gross income for the 30-years (gross-vacancy)
    def get_egi(self, gross_rent, vacancy=.07):
        pass
    
    # returns iterable of each future year's operating expenses for the duration of 30-years
    def get_opex(self, taxRate=0, insurance=0, management=0, maintenance=0, capex=0, misc=0):
        if taxRate != 0:
            taxRate = taxRate
        else:
            try:
                taxRate = self.Neighborhood.tax_rate
            except:
                taxRate = self.Zipcode.tax_rate
        opex = []
        gross_rents = []

    # returns iterable of each future year's net operating income for the duration of 30-years
    def get_duration_noi(self):
        noi=0

    def get_operating_cf(self, noi):
        pass
    
#MORTGAGE CALCULATIONS
    # calculates mortgage payment of property
    def calculate_mortgage_payment(self, down_payment=.2, interest=.05, term=30):
        balance = self.asking - (self.asking*down_payment)
        payment = balance*(interest/(12))*(1+.05/12)^(12*term)/(1+interest/12)^(12*term) - 1
        return payment

    # returns iterable of principal amounts
    def calculate_principal(self, balance=0, interest=.05, term=30):
        principal = []

    # returns iterable of interest payments
    def calculate_interest(self, balance=0, interest=.05, term=30):
        interest = []

    def calculate_debt_balance(self, ibalance, interest, term, year=0):
        pass

# SALE CALCULATIONS
    def calculate_sale_proceeds(self, year=30, closing_costs=.02, misc_costs=0):
        pass
    
    def __str__(self):
        return self.address

class Neighborhood(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    price_sf = models.DecimalField(max_digits=10, decimal_places=2)
    rent_sf = models.DecimalField(max_digits=8, decimal_places=2)
    rent_over_value = models.DecimalField(max_digits=4, decimal_places=2)
    rent_per_bed = models.DecimalField(max_digits=8, decimal_places=2)
    proj_price_appreciation = models.DecimalField(max_digits=8, decimal_places=4)
    proj_rent_appreciation = models.DecimalField(max_digits=8, decimal_places=4)
    proj_airb_appreciation = models.DecimalField(max_digits=8, decimal_places=4)
    occupancy = models.DecimalField(max_digits=8, decimal_places=4)
    tax_rate = models.DecimalField(max_digits=8, decimal_places=4)
    def __str__(self):
        return self.name

class Zipcode(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    price_sf = models.DecimalField(max_digits=10, decimal_places=2)
    rent_sf = models.DecimalField(max_digits=8, decimal_places=2)
    rent_over_value = models.DecimalField(max_digits=4, decimal_places=2)
    rent_per_bed = models.DecimalField(max_digits=8, decimal_places=2)
    proj_price_appreciation = models.DecimalField(max_digits=8, decimal_places=4)
    proj_rent_appreciation = models.DecimalField(max_digits=8, decimal_places=4)
    proj_airb_appreciation = models.DecimalField(max_digits=8, decimal_places=4)
    occupancy = models.DecimalField(max_digits=8, decimal_places=4)
    tax_rate = models.DecimalField(max_digits=8, decimal_places=4)
    
    def __str__(self):
        return str(self.code)
