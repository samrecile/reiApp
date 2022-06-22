from django.db import models

# Create your models here.
class Property(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    area = models.ForeignKey('Area', on_delete=models.CASCADE, related_name='neighborhood')
    property_type = models.CharField(max_length=50, blank=True, null=True)
    sqf = models.IntegerField(blank=True, null=True)
    beds = models.IntegerField(blank=True, null=True)
    baths = models.IntegerField(blank=True, null=True)
    asking = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    user = models.BooleanField(blank=True, null=True, default=False)
#ADVANCED METRICS
    # calculates npv of property
    def calculate_npv(self, interest_rate=.05, rent_growth=.02):
        npv = 0

    # calculates cap rate
    def calculate_caprate(self, value=0):
        noi = (self.duration_noi)[0]
        if value == 0:
            value = self.asking
        capRate = noi/value
        return capRate

    # calculates cash-on-cash return
    def calculate_cashoncash(self):
        cash_on_cash = 0

    # returns an estimate of the property given the location, size, bedrooms, etc.
    def get_estimate():
        pass

# COMPONENT VALUES (values below are used to caluclate the above expressions)
    # returns iterable of property values for duration of 30-years
    def future_values(self, growth_rate=.02):
        value = self.asking
        property_values = []
        growth_rate = self.area.proj_price_appreciation
        for x in range(30):
            property_values.append(value)
            value *= (1+growth_rate)
        return property_values
    
    # returns iterable of monthly gross rents for the duration of 30-years
    def gross_rent(self):
        property_values = future_values
        rent_sf = self.area.price_sf
        rent_ratio = self.area.rent_over_value
        rent_appreciation = self.area.proj_rent_appreciation
        gross_rents = []
        rent = 0
        for value in property_values:
            rent = ((value*rent_ratio)+(self.sqf*rent_sf))
            gross_rents.append(rent)
            rent*=(1+rent_appreciation)
        return gross_rents

    # returns iterable of monthyl effective gross income for the 30-years (gross-vacancy)
    def egi(self):
        egi = [grossValue*self.area.occupancy for grossValue in self.gross_rent]
        return egi
    
    # returns iterable of each future year's monthly operating expenses without taxes for the duration of 30-years
    def bt_opex(self, insurance=.1, management=.1, maintenance=.075, capex=.10, misc=.05):
        gross_rents = self.gross_rent
        bt_opex = []
        for rent in gross_rents:
            expense = rent*insurance
            expense += (rent*management)
            expense += (rent*maintenance)
            expense += (rent*capex)
            expense += (rent*misc)
            bt_opex.append(expense)
        return bt_opex

    # returns iterable of each future year's operating expenses with taxes for the duration of 30-years
    def at_opex(self, taxRate=.016):
        bt_opex = self.bt_opex
        gross_rents = self.gross_rent
        expense = 0
        at_opex = []
        for x in range(len(gross_rents)):
            taxes = (gross_rents[x] * taxRate)
            opex = bt_opex[x] + taxes
            at_opex.append(opex)
        return at_opex


    # returns iterable of each future year's net operating income for the duration of 30-years
    def duration_noi(self):
        noi=0

    def operating_cf(self):
        pass
    
#MORTGAGE CALCULATIONS
    # calculates mortgage payment of property
    def calculate_mortgage_payment(self, down_payment=.2, interest=.05, term=30):
        balance = self.asking - (self.asking*down_payment)
        payment = balance*(interest/(12))*(1+.05/12)^(12*term)/(1+interest/12)^(12*term) - 1
        return payment

    # returns how much equity has been built up
    def calculate_principal(self, balance=0, interest=.05, term=30):
        principal = []

# SALE CALCULATIONS
    def calculate_sale_proceeds(self, year=30, closing_costs=.02, misc_costs=0):
        pass
    
    def __str__(self):
        return self.address

class Area(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    price_sf = models.DecimalField(max_digits=10, decimal_places=2)
    rent_sf = models.DecimalField(max_digits=8, decimal_places=2)
    rent_over_value = models.DecimalField(max_digits=4, decimal_places=2)
    proj_price_appreciation = models.DecimalField(max_digits=8, decimal_places=4)
    proj_rent_appreciation = models.DecimalField(max_digits=8, decimal_places=4)
    proj_airb_appreciation = models.DecimalField(max_digits=8, decimal_places=4)
    occupancy = models.DecimalField(max_digits=8, decimal_places=4)
    tax_rate = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    def __str__(self):
        return self.name
